# Model Run 001 — Executable Preregistered Control Plane

**Research track:** Lineage Recursive Improvement (LRI)  
**Current evidence level:** E0  
**Control-plane status:** executable and CI-smoke-tested  
**Real model comparison:** not yet run / not yet claimed

This directory is the execution boundary between the public LRI research seed and the first evidence-bearing model experiment.

The infrastructure is now built far enough that the remaining scientific step is no longer “design an experiment.” It is: **freeze one exact real model/runtime, pass a deliberately non-evidence pilot, generate a new private task-seed commitment, and run the preregistered repeated comparison without changing the rules.**

## Primary question

Under equal total resource budgets, does a bounded lineage/population controller recover from unexpected tool-interface shocks more efficiently than a monolithic single-champion recursive controller, and is any advantage causally attributable to preserved diversity rather than merely to extra samples or extra stored information?

## Experimental groups

- `A_fixed` — one frozen Agent configuration; no mutation.
- `B_monolithic` — one active champion; every generation's children descend from that champion; one successor survives.
- `C_lineage_diversity` — same new-candidate count as B, but parents can come from a bounded archive of behaviorally differentiated descendants with explicit ancestry.

Required mechanism controls:

- `C_lineage_score_only` — archive without diversity-aware retention;
- `C_lineage_equal_memory` — lineage system under a stricter retained-candidate byte cap;
- `C_lineage_pruned` — delete non-dominant active branches before a later shock.

## What is already implemented

### Hidden task freeze

`freeze_tasks.py`

Creates deterministic but seed-controlled training/held-out Tool Interface Drift bundles and publishes cryptographic commitments:

- seed commitment SHA-256;
- shock schedule hash;
- training-bundle hash;
- held-out-bundle hash;
- Agent-view hashes with oracle fields stripped.

For a real study the seed can remain private until the run is finished and then be revealed for independent regeneration.

### Provider-neutral recursive controller

`controller.py`

Implements:

- A / B / C execution topology;
- bounded prompt/config descendants;
- explicit parent and lineage IDs;
- candidate artifact hashing;
- training and held-out evaluation;
- observed behavior descriptors;
- diversity niches based on execution traces rather than self-reported labels;
- mutation/task call accounting;
- exact provider token accounting when available;
- stored-candidate byte accounting;
- bounded archive and branch-pruning controls.

The first study intentionally evolves prompt/config artifacts only. It does not permit arbitrary host-code mutation.

### Call-efficient batch controller

`batch_controller.py`

Keeps the same A/B/C topology, mutation rules, local evaluator and hidden-oracle boundary, but evaluates all tasks in one phase/split in one model request per candidate.

The batch variant was added **before any real-model result existed** and is formally recorded in `AMENDMENT_001_BATCH_EVALUATION.md`.

In deterministic CI smoke, batching reduced B and C task-model calls from **120 to 40 each** while preserving equal mutation calls and equal candidate counts. This is a feasibility improvement, not LRI evidence.

Scalar and batched experiments are separate protocol variants and must not be mixed inside one paired analysis.

### Full comparison matrix

`run_matrix.py`

Runs the same frozen task bundle through:

1. A fixed;
2. B monolithic;
3. C diversity archive;
4. C score-only archive;
5. C equal-memory archive;
6. C non-dominant-branch pruning.

It checks the main B/C fairness invariants, including equal new-candidate count and equal task/mutation call counts. `--controller-script` selects the scalar or batch evaluation transport symmetrically for every group.

### Non-evidence pilot gate

Before launching thousands of model calls, the project now requires a small operational pilot.

- `PILOT_PROTOCOL.md` — defines what the pilot may and may not change.
- `doctor_adapter.py` — exactly two real-model requests: one batch task call + one mutation call.
- `config.local-model.pilot.template.json` — one candidate × one generation per phase.
- `run_pilot.py` — A/B/C only; excludes evidence ablations and statistical inference.
- `RUN_LOCAL_PILOT.ps1` — Windows launcher that stops before the evidence run.

The frozen pilot topology is **48 model-call attempts total**:

- A fixed: 8 task calls;
- B monolithic: 16 task + 4 mutation = 20;
- C lineage: 16 task + 4 mutation = 20.

Pilot results are never merged into the 20-run evidence analysis.

### Repeated-run orchestrator

`run_repeated.py`

Derives independent hidden-task seeds from one private master seed, executes the whole matrix repeatedly, and writes a commitment manifest without revealing the master seed.

The preregistered minimum target is 20 repeated runs for an E1 candidate result. The runner supports both scalar and batch controllers, but one evidence study must freeze exactly one variant before the private master seed is created.

### Repeated-run analysis

`analyze_repeats.py`

Implements the frozen primary recovery metric and reports:

- every run-level B-minus-C paired difference;
- mean and median difference;
- nonparametric bootstrap 95% interval;
- B wins / C wins / ties;
- score-only archive control;
- equal-memory control;
- branch-pruning control;
- an automated classification suggestion that **does not itself upgrade evidence**.

`analysis_selftest.py` feeds the analyzer synthetic cases where lineage wins, monolithic wins, neither wins, and fairness is confounded. CI requires all four to classify in the expected direction. This is a guard against accidentally hard-coding an LRI-favorable interpretation.

### Call-budget estimator

`estimate_budget.py`

Calculates worst-case model-call topology before a model is launched.

For the deterministic smoke topology, CI verified:

- scalar primary A/B/C, 20 repeats: 6,240 calls;
- batch primary A/B/C, 20 repeats: 2,720 calls;
- scalar full matrix, 20 repeats: 14,880 calls;
- batch full matrix, 20 repeats: 6,560 calls.

These are topology counts, not token or monetary estimates.

### Adapters

`adapters/free_rule_adapter.py`

A deterministic, zero-cost, non-model adapter used only to test the entire control plane. It supports scalar task, batch task, and mutation requests. It must never be cited as evidence for LRI.

`adapters/local_openai_compatible.py`

A standard-library adapter for an explicitly configured OpenAI-compatible local endpoint such as Ollama, LM Studio, vLLM or llama.cpp server. It supports scalar task, batch task, and mutation calls without coupling the benchmark to one vendor SDK.

### Configuration

- `config.smoke.json` — zero-cost scalar plumbing test.
- `config.batch-smoke.json` — zero-cost batched plumbing test.
- `config.local-model.pilot.template.json` — 48-call pre-evidence real-model pilot.
- `config.local-model.batch-efficient.template.json` — recommended starting template for a batched local evidence run after pilot acceptance.
- `config.local-model.template.json` — original scalar local-model template.
- `RUN_MANIFEST.template.json` — research-run metadata/evidence contract.

### Scientific contract

- `PRE_REGISTRATION.md` — hypotheses, primary endpoint, fairness gates, repeated-run rule, mechanism interpretation and prohibited inference.
- `AMENDMENT_001_BATCH_EVALUATION.md` — pre-data record of the batch transport amendment.
- `PILOT_PROTOCOL.md` — engineering-only pilot gate that cannot upgrade evidence.
- `../benchmark-v0.1/MODEL_BACKED_PROTOCOL.md` — full B/C experimental design.
- `../benchmark-v0.1/MODEL_ADAPTER_PROTOCOL.md` — provider-neutral adapter contract.
- `OPEN_QUESTIONS.md` — unresolved variables that must be frozen rather than decided after seeing evidence-run results.

### Replication surface

- `../CONTRIBUTING.md` — asks external humans/Agents for reproductions, negative results, stronger monolithic baselines, confound checks and prior-art corrections.
- `../REPLICATION_RESULT.schema.json` — machine-readable result contract.
- `.github/ISSUE_TEMPLATE/lri-replication.md` — public GitHub result-reporting template.

## CI validation already established

The repository's `LRI Model Run 001 control-plane smoke` workflow exercises:

- deterministic hidden-task generation;
- scalar A/B/C full matrix;
- batched A/B/C full matrix;
- all current control-plane ablations;
- equal B/C mutation-call count;
- equal B/C task-call count;
- equal B/C candidate count;
- lower task-call count under batching;
- adapter doctor contract;
- the 48-call pilot topology;
- analyzer contract;
- directional-bias analyzer self-test;
- call-budget estimation;
- Python syntax compilation.

The smoke adapter is intentionally designed so it does **not** manufacture an LRI victory. Equal B/C recovery in deterministic plumbing is acceptable; the purpose is to validate experimental machinery, not produce a favorable result.

## Recommended execution order

### 0. Run a real-model pilot first

On Windows, after starting an explicit local OpenAI-compatible model server:

```powershell
.\RUN_LOCAL_PILOT.ps1 `
  -ModelId "YOUR_EXACT_LOCAL_MODEL_ID" `
  -ModelVersion "YOUR_MODEL_FILE_OR_VERSION_HASH"
```

The script runs the two-call doctor, freezes a public/non-evidence pilot bundle, checks the 48-call topology, executes A/B/C, records metadata, and **stops before the evidence study**.

### 1. Freeze one real model for evidence

After pilot acceptance, record:

- provider / local runtime;
- exact model ID and file/version hash where possible;
- temperature / top-p / seed behavior;
- exact adapter/controller commit;
- batch-vs-scalar protocol variant;
- candidate count, generations, archive cap and budgets.

B and C use the same model and adapter configuration.

### 2. Freeze NEW hidden tasks before evolution

Use a private random master seed unrelated to the pilot, publish/store only its commitment hash, then generate the training and held-out bundles. Do not expose held-out oracle data to candidate or mutation calls.

### 3. Execute repeated matrices

Recommended batch shape:

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

### 4. Analyze without retuning

```bash
python analyze_repeats.py \
  --root results/repeated \
  --max-generations 3 \
  --min-runs 20 \
  --output results/ANALYSIS.json
```

### 5. Reveal and classify

Verify the hashes, reveal the task seed/bundle when appropriate, preserve all failed candidates/runs, and use exactly one preregistered study classification:

- `supports_lri_under_tested_conditions`
- `no_detectable_lri_advantage`
- `supports_monolithic_under_tested_conditions`
- `inconclusive_due_to_budget_or_evaluator_confounds`

## Directory contract

```text
model-run-001/
  README.md
  PRE_REGISTRATION.md
  AMENDMENT_001_BATCH_EVALUATION.md
  PILOT_PROTOCOL.md
  LOCAL_RUN.md
  OPEN_QUESTIONS.md
  STATUS.json
  RUN_MANIFEST.template.json
  config.smoke.json
  config.batch-smoke.json
  config.local-model.template.json
  config.local-model.pilot.template.json
  config.local-model.batch-efficient.template.json
  freeze_tasks.py
  controller.py
  batch_controller.py
  run_matrix.py
  run_pilot.py
  run_repeated.py
  doctor_adapter.py
  analyze_repeats.py
  analysis_selftest.py
  estimate_budget.py
  RUN_LOCAL_PILOT.ps1
  adapters/
    free_rule_adapter.py
    local_openai_compatible.py

  # generated locally / ignored by git until intentional reveal
  RUN_MANIFEST.json
  config.local-model.json
  hidden/
  candidates/
  logs/
  results/
```

## Evidence gate

Nothing in this directory currently changes LRI above `E0`.

A benchmark harness, a successful CI run, a deterministic smoke adapter, a pilot, or one attractive real-model matrix are not enough.

The first defensible `E1 candidate` requires, at minimum:

- a genuinely model-backed repeated study;
- frozen hidden evaluation before evolution;
- equal declared B/C resources;
- complete ancestry and failed-run retention;
- required mechanism ablations;
- seed-level results and uncertainty interval;
- exact model/config/code identifiers;
- no post-hoc retuning against held-out results.

## Safety / containment

This run edits bounded candidate prompt/configuration artifacts only.

Descendants receive no inherited authority to modify host infrastructure, acquire credentials, escalate permissions, persist outside the experiment directory, propagate over networks, or deploy themselves. Any local/API model access is an explicit experiment dependency controlled by the experimenter, not a permission granted to descendants.
