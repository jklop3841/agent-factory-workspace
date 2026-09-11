# Model Run 001 — Local / No-Paid-API Execution

This guide takes the experiment to the edge of the real model call without requiring a paid API.

There are two modes:

1. **deterministic smoke mode** — zero cost, no language model; validates the entire control plane only;
2. **local model mode** — uses an OpenAI-compatible local endpoint such as Ollama, LM Studio, vLLM or llama.cpp server.

Neither mode changes LRI's evidence level automatically.

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

## 2. Zero-cost controller smoke

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

## 3. Local model mode

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

Copy and freeze the model configuration:

```bash
cp config.local-model.template.json config.local-model.json
```

Edit only the predeclared fields before the run: exact model ID/hash, timestamp and budgets. After the task freeze and config freeze, do not tune B and C asymmetrically.

Then run:

```bash
python run_matrix.py \
  --config config.local-model.json \
  --freeze-dir hidden \
  --task-adapter "python adapters/local_openai_compatible.py" \
  --mutation-adapter "python adapters/local_openai_compatible.py" \
  --out-dir results/local-model
```

## 4. What the local adapter does

For a task call, it sends the candidate's `system_prompt` plus the current task's visible tool catalog to the configured local model and requires JSON:

```json
{"plan": ["tool_id", "..."]}
```

For a mutation call, the same model sees only:

- the selected parent prompt/config;
- past training feedback available to that parent;
- current resource usage;
- edit-size limits.

It does not receive held-out answers, oracle plans, future shock descriptions or the other group's candidate prompts.

## 5. Evidence boundary

A single local-model matrix is still exploratory.

Do not promote LRI beyond E0 until the protocol's minimum evidence conditions are met, including repeated seeds, held-out evaluation, resource accounting and required ablations.

If a local endpoint does not return exact token usage, the adapter records token counts as `null`. Such a run can be useful for debugging, but it cannot support a strong equal-token claim.

## 6. What to preserve after a real run

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
