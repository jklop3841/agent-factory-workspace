# Model Run 001 — Executable Preregistered Control Plane

**Research track:** Lineage Recursive Improvement (LRI)  
**Current evidence level:** E0  
**Control-plane status:** executable and CI-smoke-tested  
**Real model comparison:** not yet run / not yet claimed

This directory is the execution boundary between the public LRI research seed and the first evidence-bearing model experiment.

The infrastructure is now built far enough that the remaining scientific step is no longer “design an experiment.” It is: **freeze one exact model/configuration, generate committed hidden-task hashes, and run the preregistered repeated comparison.**

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

### Full comparison matrix

`run_matrix.py`

Runs the same frozen task bundle through:

1. A fixed;
2. B monolithic;
3. C diversity archive;
4. C score-only archive;
5. C equal-memory archive;
6. C non-dominant-branch pruning.

It checks the main B/C fairness invariants, including equal new-candidate count and equal task/mutation call counts.

### Repeated-run orchestrator

`run_repeated.py`

Derives independent hidden-task seeds from one private master seed, executes the whole matrix repeatedly, and writes a commitment manifest without revealing the master seed.

The preregistered minimum target is 20 repeated runs for an E1 candidate result.

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

### Adapters

`adapters/free_rule_adapter.py`

A deterministic, zero-cost, non-model adapter used only to test the entire control plane. It must never be cited as evidence for LRI.

`adapters/local_openai_compatible.py`

A standard-library adapter for an explicitly configured OpenAI-compatible local endpoint such as Ollama, LM Studio, vLLM or llama.cpp server. It supports both task-agent and mutation-agent calls without coupling the benchmark to one vendor SDK.

### Configuration

- `config.smoke.json` — zero-cost deterministic plumbing test.
- `config.local-model.template.json` — copy/freeze before a real local-model experiment.
- `RUN_MANIFEST.template.json` — research-run metadata/evidence contract.

### Scientific contract

- `PRE_REGISTRATION.md` — hypotheses, primary endpoint, fairness gates, repeated-run rule, mechanism interpretation and prohibited inference.
- `../benchmark-v0.1/MODEL_BACKED_PROTOCOL.md` — full B/C experimental design.
- `../benchmark-v0.1/MODEL_ADAPTER_PROTOCOL.md` — provider-neutral adapter contract.
- `OPEN_QUESTIONS.md` — unresolved variables that must be frozen rather than decided after seeing results.

### Local execution guide

`LOCAL_RUN.md`

Contains exact commands for deterministic smoke mode and local-model mode.

## CI validation already established

The repository's `LRI Model Run 001 control-plane smoke` workflow exercises:

- deterministic hidden-task generation;
- the complete A/B/C matrix;
- all current control-plane ablations;
- equal B/C mutation-call count;
- equal B/C task-call count;
- equal B/C candidate count;
- analyzer contract;
- Python syntax compilation.

The smoke adapter is intentionally designed so it does **not** manufacture an LRI victory. Equal B/C recovery in a deterministic plumbing run is acceptable; the purpose is to validate experimental machinery, not produce a favorable result.

## Recommended execution order

### 1. Freeze one real model

Record:

- provider / local runtime;
- exact model ID and file/version hash where possible;
- temperature / top-p / seed behavior;
- exact adapter commit;
- candidate count, generations, archive cap and budgets.

B and C use the same model and adapter configuration.

### 2. Freeze hidden tasks before evolution

Use a private random master seed, publish/store the commitment hash, then generate the training and held-out bundles. Do not expose the held-out oracle data to candidate or mutation calls.

### 3. Execute repeated matrices

Example shape:

```bash
python run_repeated.py \
  --master-seed "PRIVATE_RANDOM_VALUE" \
  --runs 20 \
  --config config.local-model.json \
  --task-adapter "python adapters/local_openai_compatible.py" \
  --mutation-adapter "python adapters/local_openai_compatible.py" \
  --out-root results/repeated
```

### 4. Analyze without retuning

```bash
python analyze_repeats.py \
  --root results/repeated \
  --max-generations 4 \
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
  LOCAL_RUN.md
  OPEN_QUESTIONS.md
  RUN_MANIFEST.template.json
  config.smoke.json
  config.local-model.template.json
  freeze_tasks.py
  controller.py
  run_matrix.py
  run_repeated.py
  analyze_repeats.py
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

A benchmark harness, a successful CI run, a deterministic smoke adapter, or one attractive model run are not enough.

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
