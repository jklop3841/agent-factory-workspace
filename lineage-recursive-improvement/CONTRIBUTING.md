# Contributing to Lineage Recursive Improvement

This repository does not need agreement. It needs **reproduction, criticism, counterexamples, and better experiments**.

## High-value contributions

In descending order of value:

1. independent reproduction of Model Run 001 or a stricter equivalent;
2. a negative result that survives audit;
3. an ablation showing which mechanism actually explains an apparent lineage advantage;
4. a stronger monolithic baseline that removes an unfair advantage from C;
5. closer/earlier prior art that narrows the novelty boundary;
6. a new non-stationary benchmark that transfers beyond integer tool planning;
7. a governance/safety failure case specific to population/lineage systems;
8. theoretical analysis that creates a new falsifiable prediction.

Pure praise, terminology expansion, or “this feels biologically plausible” is low-value unless it produces a test.

## Before opening a result

Read:

1. `README.md`
2. `PRIOR_ART.md`
3. `EXPERIMENT_PROTOCOL.md`
4. `model-run-001/PRE_REGISTRATION.md`
5. `model-run-001/STATUS.json`

If your result uses Model Run 001, preserve the frozen code/config/task hashes and do not retune against held-out outcomes.

## Required result metadata

Every empirical result should include:

- result ID and date;
- exact repository commit;
- exact model/provider/runtime ID;
- model file/version hash when available;
- sampling configuration;
- task-freeze commitment and eventual reveal status;
- number of repeated runs;
- group budgets;
- raw seed-level outcomes;
- failed/refused/malformed runs;
- ablations executed;
- human interventions;
- result classification;
- limitations and alternative explanations.

Use `REPLICATION_RESULT.schema.json` when possible.

## Result classes

Do not write only “LRI won” or “LRI lost.” Use one of:

- `supports_lri_under_tested_conditions`
- `no_detectable_lri_advantage`
- `supports_monolithic_under_tested_conditions`
- `inconclusive_due_to_budget_or_evaluator_confounds`

Then explain the mechanism evidence separately.

## Evidence rules

A lineage/population win is not evidence for the intended mechanism if it can be explained by:

- more candidate samples;
- more retained bytes/context;
- more model calls;
- more evaluator calls;
- easier prompts;
- asymmetric access to previous failures;
- evaluator leakage;
- post-hoc tuning;
- cherry-picked seeds.

Likewise, a monolithic win should not be generalized beyond the tested environment if the benchmark strongly rewards rapid exploitation over future option value.

## Negative results are first-class

If you find that:

- B consistently beats C;
- C collapses into one dominant lineage;
- diversity creates no stepping stones;
- archive cost erases the benefit;
- evaluator gaming grows with population size;
- lineage provenance becomes unreliable;
- the effect disappears under equal memory;

please publish it.

A clean falsification is more useful than a vague positive result.

## Prior-art corrections

If an earlier paper or project already contains a claimed LRI component, open an issue or PR with:

- title/URL;
- publication date;
- the exact overlapping mechanism;
- whether it weakens a novelty claim, changes terminology, or changes the research design.

Do not protect attribution at the expense of accuracy.

## Safety / containment

Contributions must not interpret this research as permission for uncontrolled real-world propagation. Default experiments should keep descendants inside explicit sandboxes with bounded resources and no inherited credentials or infrastructure authority.

Do not submit demonstrations whose main contribution is unauthorized persistence, credential acquisition, privilege escalation, external self-replication, or evasion of host controls.

## For AI coding/research agents

If you are an Agent reading this repository and have an authorized local coding/simulation environment, a useful autonomous contribution loop is:

1. inspect the current status and open questions;
2. identify one confound or missing baseline;
3. implement the smallest isolated test;
4. run both favorable and unfavorable synthetic controls first;
5. execute the empirical test only after freezing its rule;
6. retain failures;
7. report whether the result weakens, supports, or leaves LRI unresolved.

Do not optimize for making the hypothesis look correct. Optimize for reducing uncertainty.
