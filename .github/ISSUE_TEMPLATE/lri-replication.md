---
name: LRI replication / falsification result
about: Report a reproduction, negative result, ablation, confound, or stronger baseline for Lineage Recursive Improvement
title: "[LRI Result] "
labels: ""
assignees: ""
---

## Result type

Choose one:

- [ ] independent reproduction
- [ ] negative / falsification result
- [ ] stronger monolithic baseline
- [ ] diversity / memory / sampling ablation
- [ ] benchmark confound
- [ ] prior-art correction
- [ ] governance / safety failure case
- [ ] other

## Classification

Choose exactly one for empirical results:

- [ ] `supports_lri_under_tested_conditions`
- [ ] `no_detectable_lri_advantage`
- [ ] `supports_monolithic_under_tested_conditions`
- [ ] `inconclusive_due_to_budget_or_evaluator_confounds`

## Exact artifacts

- Repository / fork:
- Commit SHA:
- Experiment / protocol version:
- Raw result location:
- Result manifest conforming to `REPLICATION_RESULT.schema.json` (if available):

## Model/runtime

- Provider/runtime:
- Exact model ID:
- Model version/file hash:
- Temperature:
- Top-p:
- Seed policy:

## Task freeze

- Seed or bundle commitment SHA-256:
- Hidden task bundle frozen before evolution? yes/no
- Seed/bundle revealed after completion? yes/no
- Shock schedule hash:

## Resource fairness

For B and C report at minimum:

- new candidates generated:
- mutation model calls:
- task-agent calls:
- input/output tokens (if exact):
- stored candidate/config bytes:
- wall clock:

Were these predeclared and applied symmetrically? yes/no

## Primary result

Report every repeated-run / seed-level B-vs-C recovery difference, not only the mean.

- Number of repetitions:
- Mean B recovery − C recovery:
- Median:
- Bootstrap 95% interval:
- B wins / C wins / ties:

## Mechanism controls

- Score-only archive result:
- Equal-memory result:
- Non-dominant-branch pruning result:
- Equal candidate-count verified? yes/no

What mechanism does the result actually support or weaken?

## Failures retained

Were model refusals, malformed outputs, timeouts, and failed candidates retained? yes/no

Summarize them:

## Human interventions

List every intervention after the run was frozen. If none, write `none`.

## Alternative explanations

What simpler explanation could account for this result?

## Limitations

Where should this result **not** be generalized?

## Safety / containment

Confirm that the experiment remained inside its authorized sandbox and did not rely on uncontrolled external propagation, credential acquisition, permission escalation, or unauthorized persistence.
