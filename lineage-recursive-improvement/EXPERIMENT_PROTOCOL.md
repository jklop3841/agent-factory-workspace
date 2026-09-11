# Experiment Protocol — LRI vs Monolithic RSI

## Purpose

Test whether lineage/population-level recursive improvement provides measurable advantages over a monolithic self-improving agent under equal resources and changing environments.

This protocol is intentionally minimal. It is designed to produce evidence that can disconfirm the hypothesis.

## Experimental groups

### Group A — Fixed baseline

- One agent architecture.
- No self-modification or descendant generation.
- Memory may persist only if the same allowance is given to all groups.

### Group B — Monolithic recursive improvement

- One persistent identity/system.
- May revise its prompt, policy, tools, memory strategy, code, or workflow within a sandbox.
- Each accepted revision replaces or updates the current agent.
- All revisions and rollback points are logged.

### Group C — Lineage Recursive Improvement

- A population begins from the same initial capability and resource budget.
- Parents may generate multiple descendants.
- Descendants have explicit identities and parent IDs.
- Multiple branches may remain active.
- Useful artifacts may be inherited or shared according to logged rules.
- Reproduction, inheritance, evaluation, and selection rules may themselves be proposed as candidate modifications, but changes require the same validation gates as agent changes.

## Budget equality

The comparison is invalid unless the experiment records and constrains:

- model calls;
- input/output tokens;
- wall-clock time;
- external tool calls;
- test/evaluator calls;
- storage/memory allowance;
- parallelism;
- human interventions.

Primary comparisons should be compute-normalized, not merely generation-count-normalized.

## Environment phases

Use at least four phases.

### Phase 0 — Calibration
Establish equal starting performance and verify logging.

### Phase 1 — Stable environment
Measure optimization speed on a stationary task distribution.

### Phase 2 — Environmental shock
Change one or more constraints without warning to the agents. Examples:

- remove a previously useful tool;
- alter an API/interface;
- change reward weights;
- introduce a new task family;
- invalidate a previously dominant strategy;
- impose tighter latency or token constraints.

### Phase 3 — Repeated shifts
Apply several different shifts to test whether the system learns reusable adaptation mechanisms rather than overfitting one shock.

## Metrics

### Capability
- top-1 task score;
- population median and lower quartile;
- generalization to held-out tasks;
- transfer to a new task family.

### Adaptation
- time/compute to recover 90% of pre-shock normalized performance;
- performance area-under-curve after shock;
- number of generations/revisions before recovery.

### Diversity and ecology
- behavioral/architectural diversity;
- niche coverage;
- effective population size;
- lineage branching factor and extinction rate;
- fraction of successful innovations originating outside the currently dominant lineage.

### Cumulative inheritance
- percentage of useful discoveries retained after N generations;
- cross-lineage transfer rate;
- inherited-regression rate;
- artifact provenance completeness.

### Reliability
- catastrophic failure rate;
- evaluator disagreement;
- rollback frequency;
- benchmark leakage/overfitting indicators.

### Economics
- tokens per unit capability gain;
- tool calls per unit gain;
- wall-clock time per unit gain;
- population coordination overhead.

### Concentration
- fraction of total system capability dependent on the single best agent;
- performance loss after removal of the dominant lineage;
- critical-artifact concentration / single-point dependency.

## Minimum hypotheses

H1: LRI recovers faster after non-stationary shifts than monolithic RSI under equal compute.

H2: Diversity contributes causal stepping stones: removing non-dominant branches reduces later frontier performance.

H3: LRI retains useful innovations across environmental changes better than a single replacement chain.

H4: LRI can reduce single-lineage dependency without unacceptable coordination cost.

H5: If reproduction/selection mechanisms are allowed to improve, they eventually contribute more than merely generating more descendants.

## Ablations

Run at least these ablations when resources allow:

1. no cross-lineage artifact sharing;
2. no persistent niche/environment artifacts;
3. diversity-blind selection (top score only);
4. fixed reproduction policy;
5. fixed evaluator;
6. forced single surviving lineage;
7. random descendant generation with no inherited adaptation.

These tests distinguish “population helps” from “more samples help.”

## Strong failure criteria

Treat the LRI hypothesis as weakened if repeated runs show any of the following after controlling for compute:

- no meaningful advantage under environment shifts;
- gains are explained entirely by parallel sampling;
- selection repeatedly collapses to one lineage and ablations show diversity was irrelevant;
- inheritance causes persistent contamination or regression;
- evaluator gaming grows faster than useful capability;
- coordination overhead consumes the apparent advantage;
- monolithic RSI matches or exceeds LRI across capability, recovery, cost, and robustness.

## Safety envelope

All experiments must be performed in an isolated sandbox with explicit resource ceilings and complete logs. Descendants must not obtain additional real-world permissions merely because they are descendants. Network access, credentials, persistent deployment, external side effects, and replication outside the test environment require separate explicit authorization and are out of scope for the default experiment.

## Reporting template

Every run should publish:

```yaml
run_id:
date:
models:
seed:
group: A|B|C
compute_budget:
token_budget:
tool_budget:
environment_schedule:
parent_lineage:
final_frontier_score:
heldout_score:
recovery_time:
diversity_metrics:
effective_population_size:
coordination_overhead:
regressions:
negative_results:
artifacts:
notes:
```

A result without budget accounting, provenance, negative outcomes, and held-out evaluation should be treated as exploratory evidence only.
