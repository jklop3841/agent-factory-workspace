# Model Run 001 — Real-Model Pilot Protocol

**Status:** operational pilot only  
**Evidence status:** cannot upgrade LRI  
**Purpose:** verify that one exact real/local model can complete the frozen protocol before committing to the 20-run preregistered study.

The pilot is deliberately separated from Model Run 001's evidence-bearing repetitions. Its outputs are engineering diagnostics, not hypothesis evidence.

## Why a pilot exists

A full repeated matrix can consume thousands of model calls even after batching. Before spending that compute, we need to know whether the chosen model/runtime can reliably:

- return strict JSON plans;
- solve a batch of independent tool tasks without cross-task contamination;
- produce bounded successor prompts/configs;
- expose exact token usage if we intend to make equal-token claims;
- complete requests within the frozen timeout;
- preserve the same adapter behavior for B and C.

Failing these basic checks during a 20-run study would create an operationally inconclusive result rather than a scientific one.

## Pilot is not evidence

The pilot uses:

- a public/non-secret diagnostic seed;
- only one new child per generation;
- only one generation per phase;
- A/B/C only, without the full mechanism-ablation matrix;
- no statistical inference.

Do not include pilot results in the preregistered 20-run analysis.

Do not tune a configuration repeatedly until LRI happens to look favorable. Pilot changes may fix transport/format/runtime defects, but any scientific design change must be versioned and frozen before the evidence run.

## Pilot stages

### P0 — adapter doctor

Run `doctor_adapter.py`.

It performs exactly:

1. one batched task-agent request;
2. one mutation-agent request.

Pass criteria:

- both calls return valid JSON;
- every diagnostic task ID has a plan entry;
- mutation response contains bounded `system_prompt`, `planning_notes`, and `mutation_reason`;
- returned model identity is recorded;
- usage accounting availability is recorded.

A missing token-usage field does not fail the adapter, but it blocks later claims of exact token equality.

### P1 — one small A/B/C matrix

Use `config.local-model.pilot.template.json` and `run_pilot.py`.

Worst-case batch call topology with the frozen pilot config:

- A fixed: 8 task-model calls;
- B monolithic: 16 task calls + 4 mutation calls = 20;
- C lineage: 16 task calls + 4 mutation calls = 20;
- total: **48 model calls**.

This is small enough to diagnose model/runtime behavior without starting the real study.

### P2 — pilot acceptance

Proceed to the preregistered study only if:

- no unresolved adapter-format errors remain;
- no asymmetric B/C handling exists;
- batch responses consistently map plans to the correct task IDs;
- model/version/runtime are recorded precisely enough to reproduce;
- selected budgets fit available local compute/time;
- any protocol change made after the pilot is documented before the private evidence seed is frozen.

## What may be changed after the pilot

Allowed before the evidence freeze, with a dated amendment:

- endpoint compatibility details;
- timeout large enough for the chosen local model;
- JSON parsing compatibility that does not change model-visible task semantics;
- candidate/token budgets if compute estimates were wrong;
- model choice if the original model is operationally unusable.

Changes that alter the hypothesis test require a new protocol version rather than a silent edit, including:

- changing B/C topology asymmetrically;
- changing the primary endpoint;
- changing archive selection after viewing favorable/unfavorable pilot outcomes specifically to improve C;
- exposing hidden task/oracle information;
- changing candidate counts differently for B and C.

## Transition to evidence run

After pilot acceptance:

1. choose the final exact model/runtime;
2. freeze config and code commit;
3. generate a new **private** master seed unrelated to the pilot;
4. record the master-seed commitment;
5. run the preregistered repeated study;
6. do not inspect held-out results to retune mid-study;
7. publish positive, negative, or inconclusive outcomes under the same result schema.
