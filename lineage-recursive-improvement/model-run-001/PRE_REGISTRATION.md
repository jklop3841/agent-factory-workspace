# Model Run 001 — Preregistration

**Status:** protocol freeze document  
**Evidence level before run:** E0  
**Primary comparison:** `B_monolithic` vs `C_lineage_diversity`

This file exists to make it harder to redefine success after seeing the result.

## Primary hypothesis

Under equal declared model-call, candidate-generation and task-evaluation budgets, a bounded lineage archive that preserves observed behavioral diversity will require fewer post-shock adaptation generations than a single-champion monolithic revision chain on held-out Tool Interface Drift tasks.

## Null / failure interpretation

The primary hypothesis is not supported if the repeated-run confidence interval for the paired recovery difference includes zero in a practically important range, if the direction favors B, or if budget/evaluator confounds prevent a valid paired comparison.

A C win is not attributed to lineage structure if it disappears under equal-memory or diversity-removal controls.

## Frozen groups

- `A_fixed`: no candidate mutation.
- `B_monolithic`: exactly one active champion; all new children descend from that champion; non-selected candidates are audit-only.
- `C_lineage_diversity`: bounded archive; same number of new children as B; parents selected by the frozen quality/least-recently-used rule; one best member per observed behavior niche before archive cap.

Required controls:

- `C_lineage_score_only`: archive exists but ignores diversity during retention.
- `C_lineage_equal_memory`: same lineage logic under the preregistered candidate-byte cap.
- `C_lineage_pruned`: before the selected later shock, remove all non-dominant active branches.

## Primary endpoint

For each post-stable shock phase:

`recovery_generation = first generation where held-out success_rate >= 0.90`

If a group never crosses the threshold within the frozen maximum generations for that phase, encode recovery for statistical analysis as:

`max_generations_per_phase + 1`

The main paired outcome for one run is:

`mean(B_recovery_generation - C_recovery_generation across shock phases)`

Positive values favor C because C recovered in fewer generations.

Stable phase is reported but excluded from the primary post-shock mean.

## Secondary endpoints

- held-out success trajectory / area under recovery curve;
- agent task calls to recovery;
- mutation calls to recovery;
- total exact input/output tokens to recovery when provider usage is available;
- cost efficiency on successful held-out tasks;
- invalid-action rate;
- active behavior-niche count;
- final stored candidate bytes;
- capability concentration, approximated by performance retained after removing non-dominant branches;
- operational failure rate.

## Fairness gates

The primary B/C comparison is invalid unless:

- same exact base model/version;
- same temperature/top-p/seed policy;
- same initial candidate artifact;
- same task freeze;
- same new candidate count per generation;
- same maximum generations per phase;
- same task-agent adapter configuration;
- same mutation-agent adapter configuration;
- same hidden-test schedule;
- same human intervention policy;
- no hidden answer/oracle feedback reaches the mutator.

Token-based claims additionally require exact provider token accounting for both groups.

## Repetitions

Minimum target: 20 independent task/model seeds or an equivalently justified repeated design.

All completed runs remain in the analysis set unless an operational exclusion rule defined before inspection applies symmetrically. Model refusal, malformed JSON and candidate failure are outcomes, not reasons to silently delete a run.

## Statistical analysis

Primary reporting:

- all seed-level paired differences;
- mean paired difference;
- median paired difference;
- nonparametric bootstrap 95% interval over run-level paired differences;
- proportion of runs favoring B / C / ties;
- failure and inconclusive counts.

No p-value is required for the first exploratory study. The interval and raw run distribution are more important than a binary significance label.

## Mechanism / ablation interpretation

A result can be labeled `supports_lri_under_tested_conditions` only when the main C condition outperforms B and the pattern remains meaningfully stronger than the score-only archive control.

If C beats B but equal-memory removes the advantage, report the mechanism as consistent with additional retained information, not lineage topology.

If pruning non-dominant branches does not worsen recovery, the experiment does not show causal stepping-stone value from preserved branches.

If score-only archive performs similarly to diversity archive, storage/search may explain the result better than behavioral diversity.

## Allowed study-level classifications

Exactly one:

- `supports_lri_under_tested_conditions`
- `no_detectable_lri_advantage`
- `supports_monolithic_under_tested_conditions`
- `inconclusive_due_to_budget_or_evaluator_confounds`

## Explicitly prohibited inference

Model Run 001 cannot establish that:

- population intelligence is universally superior;
- LRI causes AGI/ASI;
- a Cambrian-style agent explosion will occur;
- distributed agents are safer;
- Lu Cheng invented population-based evolutionary AI;
- the observed result transfers beyond the tested task/model regime.

## Reveal policy

Before the first evidence-bearing run:

1. freeze code/config commit hashes;
2. freeze the private task seed and publish its commitment hash;
3. execute the complete matrix without mid-run strategy changes;
4. retain all raw candidate and failure logs;
5. after the experiment is complete, reveal the task seed or publish the held-out bundle so the hash can be independently verified.

Any post-hoc code change creates a new protocol/run version rather than silently replacing the preregistered run.
