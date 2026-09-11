# Model Run 001 — Local / No-Paid-API Execution

This guide takes the experiment to the edge of the real model call without requiring a paid API.

There are three useful modes:

1. **deterministic scalar smoke** — zero cost, no language model; validates the original one-task-per-adapter-call path;
2. **deterministic batch smoke** — zero cost; validates the call-efficient one-phase-batch transport;
3. **local model mode** — uses an OpenAI-compatible local endpoint such as Ollama, LM Studio, vLLM or llama.cpp server.

None of these modes changes LRI's evidence level automatically.

## 1. Freeze a task set

From `lineage-recursive-improvement/model-run-001/`:

```bash
python freeze_tasks.py --seed CI-DEMO-SEED --out hidden --training-per-phase 4 --heldout-per-phase 6
```

For a real preregistered run, replace `CI-DEMO-SEED` with a private random seed and do **not** commit the generated `hidden/` directory. The freeze manifest records hashes without requiring the seed to be public.

Files created:

```text
hidden/
  training_with_oracle.json
  training_for_agent.json
  heldout_with_oracle.json
  heldout_for_agent.json
  FREEZE_MANIFEST.json
```

The controller receives the oracle-bearing copies only as evaluator data. Every task sent to an Agent has `_oracle_*` fields stripped.

## 2. Zero-cost scalar controller smoke

```bash
python run_matrix.py \
  --config config.smoke.json \
  --freeze-dir hidden \
  --task-adapter "python adapters/free_rule_adapter.py" \
  --mutation-adapter "python adapters/free_rule_adapter.py" \
  --out-dir results/smoke
```

This runs:

- A fixed;
- B monolithic;
- C lineage with diversity archive;
- C score-only archive ablation;
- C equal-memory ablation;
- C non-dominant-branch pruning ablation.

`free_rule_adapter.py` is deliberately not a model. Its results are plumbing tests, not evidence.

## 3. Zero-cost batched smoke

The batch controller asks the task model to solve every training task in a phase in one request, and every held-out task in another request. Local evaluation still scores each task separately.

```bash
python run_matrix.py \
  --config config.batch-smoke.json \
  --freeze-dir hidden \
  --controller-script batch_controller.py \
  --task-adapter "python adapters/free_rule_adapter.py" \
  --mutation-adapter "python adapters/free_rule_adapter.py" \
  --out-dir results/batch-smoke
```

Batching is a transport/cost optimization only. B and C must use the same mode.

## 4. Estimate call topology before launching a model

Always estimate worst-case model calls before a local or paid run:

```bash
python estimate_budget.py \
  --config config.local-model.batch-efficient.template.json \
  --training-per-phase 8 \
  --heldout-per-phase 12 \
  --primary-repeats 20 \
  --full-matrix-repeats 20
```

The estimator counts task-model and mutation-model calls from the frozen experimental topology. It does **not** estimate money because local speed, tokenization and provider pricing vary.

Why this matters: the original scalar design can turn a modest-looking repeated experiment into many thousands of model calls. Batch evaluation materially reduces task-call count while keeping every task independently scored by the local evaluator.

## 5. Local model mode — recommended batched path

Start an OpenAI-compatible model server locally. The adapter defaults to:

```text
http://127.0.0.1:11434/v1/chat/completions
```

Example environment variables:

### Linux / macOS

```bash
export LRI_MODEL="YOUR_EXACT_LOCAL_MODEL_ID"
export LRI_OPENAI_BASE_URL="http://127.0.0.1:11434/v1/chat/completions"
export LRI_TEMPERATURE="0.2"
export LRI_TOP_P="1.0"
```

### PowerShell

```powershell
$env:LRI_MODEL="YOUR_EXACT_LOCAL_MODEL_ID"
$env:LRI_OPENAI_BASE_URL="http://127.0.0.1:11434/v1/chat/completions"
$env:LRI_TEMPERATURE="0.2"
$env:LRI_TOP_P="1.0"
```

Copy and freeze the call-efficient model configuration:

```bash
cp config.local-model.batch-efficient.template.json config.local-model.json
```

Edit only the predeclared fields before the run: exact model ID/hash, timestamp and budgets. After task/config freeze, do not tune B and C asymmetrically.

Then run one exploratory matrix:

```bash
python run_matrix.py \
  --config config.local-model.json \
  --freeze-dir hidden \
  --controller-script batch_controller.py \
  --task-adapter "python adapters/local_openai_compatible.py" \
  --mutation-adapter "python adapters/local_openai_compatible.py" \
  --out-dir results/local-model-batch
```

For the preregistered repeated study:

```bash
python run_repeated.py \
  --master-seed "PRIVATE_RANDOM_VALUE" \
  --runs 20 \
  --config config.local-model.json \
  --controller-script batch_controller.py \
  --task-adapter "python adapters/local_openai_compatible.py" \
  --mutation-adapter "python adapters/local_openai_compatible.py" \
  --out-root results/repeated
```

Then analyze:

```bash
python analyze_repeats.py \
  --root results/repeated \
  --max-generations 3 \
  --min-runs 20 \
  --output results/ANALYSIS.json
```

## 6. What batching changes — and does not change

Scalar task evaluation:

```text
candidate -> task 1 model call
candidate -> task 2 model call
candidate -> task 3 model call
...
```

Batched task evaluation:

```text
candidate -> [all tasks in this phase/split] -> one model call -> task_id -> plan map
```

The benchmark still locally evaluates every plan against its own start/target/tool catalog/oracle cost. The model never sees oracle plans.

Batching can introduce a different inference context because several tasks share one request. Therefore scalar and batch experiments are different protocol variants and should not be mixed inside one B/C comparison. Record the controller/config in every run manifest.

## 7. What the local adapter sees

For a task batch, the candidate's `system_prompt` and planning notes are supplied with the visible tasks and their current tool catalogs. The model must return:

```json
{
  "plans": {
    "task-id-1": ["tool_id", "..."],
    "task-id-2": ["tool_id", "..."]
  }
}
```

For a mutation call, the same model sees only:

- the selected parent prompt/config;
- past training feedback available to that parent;
- current resource usage;
- edit-size limits.

It does not receive held-out answers, oracle plans, future shock descriptions or the other group's candidate prompts.

## 8. Evidence boundary

A single local-model matrix is still exploratory.

Do not promote LRI beyond E0 until the protocol's minimum evidence conditions are met, including repeated seeds, held-out evaluation, resource accounting and required ablations.

If a local endpoint does not return exact token usage, the adapter records token counts as `null`. Such a run can be useful for debugging, but it cannot support a strong equal-token claim.

The software analysis path is also tested against synthetic fixtures where lineage wins, monolithic wins, neither wins, and fairness is confounded. Passing those tests shows the classifier is not hard-coded to return an LRI-favorable label; it still does not constitute empirical evidence.

## 9. What to preserve after a real run

Keep:

- frozen config;
- `FREEZE_MANIFEST.json`;
- exact generator/controller/adapter commit hashes;
- all candidates including failures;
- ancestry;
- budget snapshots;
- raw phase-level evaluation;
- operational errors/interventions;
- matrix summary;
- eventual seed reveal or third-party custody statement.

Do not commit API keys or local service credentials.
