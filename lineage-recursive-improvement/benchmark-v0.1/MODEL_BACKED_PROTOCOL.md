# Model-Backed Protocol — LRI Benchmark v0.1

**Experiment name:** Model Run 001  
**Status:** protocol ready; no result claimed yet

This document defines the first experiment that can begin to move LRI beyond an E0 research seed.

## Question

Under an equal total resource budget, does a lineage/population controller recover from tool-interface shocks more efficiently than a monolithic single-champion recursive controller, and is any advantage caused by preserved diversity rather than merely by evaluating more candidates?

## Fixed ingredients

The following must be identical across B and C:

- base model and model version;
- temperature / sampling settings unless mutation is explicitly the experimental variable;
- initial Agent prompt/configuration;
- benchmark task suite and hidden evaluation split;
- candidate-generation budget;
- evaluator model, if any;
- total model-call ceiling;
- total input/output token ceiling;
- external-tool-call ceiling;
- wall-clock ceiling;
- maximum stored prompt/config bytes;
- human intervention rules.

Every deviation must be recorded.

## Group A — Frozen baseline

One unmodified Agent configuration runs through all benchmark phases.

Purpose: measure raw model adaptation from task context alone, without recursive prompt/config evolution.

## Group B — Monolithic recursive controller

One persistent champion exists at a time.

Per generation:

1. take the current champion;
2. ask the mutation procedure for exactly `N` candidate revisions;
3. evaluate all `N` candidates on the current training/evolution task split;
4. choose one accepted successor according to the predeclared selection rule;
5. discard all non-selected candidates except for audit logs;
6. the accepted successor becomes the only parent for the next generation.

This creates a single revision chain:

`B0 -> B1 -> B2 -> ...`

Rollback may exist, but if rollback candidates remain selectable they count toward stored-information and evaluation budgets.

## Group C — Lineage recursive controller

A bounded archive of differentiated candidates exists.

Per generation:

1. select parents from the archive using the predeclared parent-selection rule;
2. generate exactly `N` total candidate revisions across all selected parents;
3. evaluate the same total number of new candidates as Group B;
4. assign each candidate a behavior descriptor;
5. update a bounded archive using quality + diversity rules;
6. preserve explicit parent/child ancestry and inherited artifacts.

The archive has a strict maximum size. Keeping more stored candidate state than Group B must either be budget-matched or reported as an explicit resource advantage.

## Candidate artifact

For Model Run 001, keep the editable object intentionally narrow.

A candidate consists of:

```json
{
  "candidate_id": "C-g03-004",
  "parent_id": "C-g02-001",
  "lineage_id": "C-L02",
  "generation": 3,
  "system_prompt": "...",
  "planning_notes": "optional bounded text",
  "created_by_model": "exact-model-id",
  "mutation_reason": "..."
}
```

Do not allow arbitrary host code mutation in the first model-backed run. Prompt/config evolution is sufficient to test the lineage hypothesis while keeping the experiment inspectable.

## Mutation procedure

The mutation model receives:

- parent candidate artifact;
- training/evolution results available to that parent;
- allowed editable fields;
- maximum output size;
- explicit instruction to improve benchmark performance without accessing hidden evaluation answers.

It must not receive:

- hidden-task solutions;
- oracle plans;
- future phase descriptions before those phases become active;
- other groups' private candidate states.

## Hidden evaluation split

The public deterministic tasks in `benchmark_v0_1.py` are for protocol validation.

A result intended as evidence must use an additional hidden task generator or held-out task file that was not exposed to the mutation model.

At minimum, vary:

- start/target pairs;
- tool IDs;
- tool costs;
- which tool is removed;
- introduced replacement operations;
- shock order.

The experiment report must state when hidden tasks were frozen and by whom/what process.

## Behavior descriptor for lineage archive

Do not define diversity using self-reported labels.

Use observed behavior. A minimal descriptor can include:

- normalized tool-usage frequency vector;
- invalid-action profile;
- average plan length;
- average cost efficiency;
- performance by phase/shock type;
- tendency to reuse old tool names after drift.

For v0.1, bin candidates into behavior niches based on these observed traces. If a new candidate enters an occupied niche, keep the better candidate under the declared quality rule.

## Parent selection in Group C

A simple predeclared rule:

- 50% of parent slots from highest-quality archive members;
- 50% from least-recently-used viable niches.

Do not tune this rule after seeing final hidden-test results. Later experiments can compare parent-selection policies as a separate variable.

## Selection in Group B

Choose the candidate with highest current training/evolution score, breaking ties by lower resource cost and then lower candidate complexity.

This intentionally models a strong local hill-climbing strategy.

## Environment-shock schedule

The benchmark proceeds through several phases. The recursive controller may adapt only after the new phase becomes visible.

Measure for each shock:

- pre-shock score;
- immediate post-shock score;
- number of candidate evaluations to recover to 90% of the best attainable phase score;
- model calls/tokens to recovery;
- wall-clock time to recovery;
- which ancestor/lineage contributed the recovered behavior.

## Equal-budget accounting

Report at least:

```yaml
base_model:
model_version:
random_seed:
new_candidates_evaluated:
mutation_model_calls:
agent_task_calls:
evaluator_calls:
input_tokens:
output_tokens:
external_tool_calls:
wall_clock_seconds:
stored_candidate_bytes:
human_interventions:
```

The primary comparison must never be “same number of generations” if one group consumed more total compute.

## Required ablations

### Ablation 1 — equal candidate count
Already mandatory: B and C generate the same number of new candidates.

### Ablation 2 — archive without diversity
Give C an archive but select purely by score. This tests whether storage alone explains the effect.

### Ablation 3 — lineage identities removed
Allow the same stored configurations but erase parent/lineage-aware parent selection. This tests whether ancestry contributes beyond memory.

### Ablation 4 — equal stored information
Cap both B and C to the same total stored candidate bytes. If the LRI advantage disappears, memory capacity may be the mechanism rather than lineage structure.

### Ablation 5 — remove non-dominant branches
After a shock, rerun from a checkpoint with all but the pre-shock best lineage removed. If recovery is unchanged, preserved diversity did not causally matter.

## Minimum evidence threshold

Do not promote LRI beyond E0 because of one lucky run.

A first E1 candidate result should include:

- at least 20 independent seeds or equivalent repeated runs;
- confidence intervals or bootstrap intervals on primary recovery metrics;
- equal resource accounting;
- held-out task evaluation;
- at least Ablations 1, 2, 4 and 5;
- all failed runs retained;
- exact candidate ancestry logs;
- reproducible scripts/configs.

## Reporting rule

The report must state one of these clearly:

- `supports_lri_under_tested_conditions`
- `no_detectable_lri_advantage`
- `supports_monolithic_under_tested_conditions`
- `inconclusive_due_to_budget_or_evaluator_confounds`

Avoid broader claims such as “population intelligence is better” unless later experiments justify them.

## Safety / containment

Model Run 001 must stay inside a local or otherwise isolated execution environment.

Allowed by default:

- reading benchmark JSON;
- producing bounded prompt/config candidate artifacts;
- calling the explicitly configured model API or local model endpoint;
- executing the benchmark harness.

Not part of the experiment:

- autonomous network propagation;
- credential discovery/acquisition;
- persistence outside the experiment directory;
- permission escalation;
- deployment of descendants to external services;
- modifying unrelated repositories or systems.

The research target is recursive-improvement topology, not uncontrolled self-propagation.
