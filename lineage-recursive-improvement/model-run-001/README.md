# Model Run 001 — Execution Handoff

This directory is the execution boundary between the public LRI research seed and the first evidence-bearing model experiment.

## Objective

Run three groups on the same hidden Tool Interface Drift task distribution:

- `A_fixed`
- `B_monolithic`
- `C_lineage`

Use the same base model and equal total resource budgets. The primary outcome is post-shock recovery efficiency, not raw final benchmark score.

## Required reading

1. `../benchmark-v0.1/MODEL_BACKED_PROTOCOL.md`
2. `../benchmark-v0.1/MODEL_ADAPTER_PROTOCOL.md`
3. `RUN_MANIFEST.template.json`
4. `../EXPERIMENT_PROTOCOL.md`
5. `../PRIOR_ART.md`

## Before starting

Freeze these fields in a copied `RUN_MANIFEST.json`:

- exact provider/model/version;
- temperature/top-p/seed settings;
- candidate count per generation;
- group budgets;
- archive size;
- hidden-task generator hash;
- task count per phase;
- shock schedule hash;
- human-intervention rule.

Do not begin evaluation until the hidden task set and budget file are frozen.

## Recommended execution order

### Step 1 — Adapter smoke

Connect one provider-neutral task adapter and one mutation adapter. Verify exact JSON input/output and usage accounting.

### Step 2 — A fixed

Run the initial candidate through all hidden phases without mutation. This measures context-only adaptation.

### Step 3 — B monolithic

For each generation, all new candidates descend from the current champion. Evaluate the fixed number of candidates and keep one accepted successor.

### Step 4 — C lineage

Generate the same number of new candidates per generation, but choose parents from a bounded behavior archive. Record explicit ancestry and niche membership.

### Step 5 — Required ablations

Run:

- archive with score-only selection;
- equal stored-information cap;
- removal of non-dominant branches before a shock;
- equal candidate-count confirmation.

### Step 6 — Repeat

Run enough independent seeds to estimate uncertainty. The minimum target in the protocol is 20 repeated runs or an equivalently justified repeated design.

## Directory contract

```text
model-run-001/
  README.md
  RUN_MANIFEST.template.json
  RUN_MANIFEST.json             # frozen before execution
  adapters/                     # provider-specific local adapters
  hidden/                       # not exposed to mutation model
  candidates/
    A_fixed/
    B_monolithic/
    C_lineage/
  logs/
  results/
  report/
```

Do not commit secrets or API keys.

## Acceptance gates

A run is not evidence-bearing unless all are true:

- hidden tasks were frozen before candidate evolution;
- B and C consumed equal declared budgets;
- candidate ancestry is complete;
- failed candidates/runs were retained in logs;
- hidden-test results were not used to retroactively tune selection rules;
- required ablations were executed;
- final report uses one of the predeclared classifications;
- exact code/config/model identifiers are preserved.

## Evidence discipline

Until these gates pass, keep LRI at `E0`.

One positive model run may justify an `E1 candidate result`, not a general statement that lineage intelligence is superior.

## Safety

This run edits bounded candidate prompts/configurations only. Descendants have no inherited permission to modify host infrastructure, acquire credentials, persist outside the run directory, propagate over networks, or deploy themselves.
