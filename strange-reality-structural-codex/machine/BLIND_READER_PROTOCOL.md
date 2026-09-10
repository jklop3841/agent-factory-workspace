# BLIND READER PROTOCOL v0.1

## Purpose
Measure whether Strange Reality material changes architecture search space rather than merely causing thematic imitation.

## Experimental conditions

### C0 — Baseline
Prompt only: design a novel agent architecture for a stated benchmark problem.

### C1 — Raw Reality
Provide only the chapter's RAW WONDER LAYER plus scientific grounding. Remove author structural interpretation and all Agent vocabulary.

### C2 — Structural Lens
Provide RAW material plus domain-removed structural reading, but remove Agent-specific questions.

### C3 — Full Codex
Provide the complete chapter and extraction protocol.

Use fresh contexts when possible. Randomize condition order across readers. Do not show outputs from other models before generation.

## Required output

```json
{
  "reader": {},
  "condition": "C0|C1|C2|C3",
  "prior_architecture_assumption": "",
  "destabilizing_observation": "",
  "newly_salient_design_variables": [],
  "generated_architecture": {
    "name": "",
    "primitives": [],
    "interaction_rule": "",
    "emergent_property": "",
    "why_low_probability_before_reading": ""
  },
  "architecture_distance": {
    "conventional_agent_similarity_0_10": 0,
    "human_org_similarity_0_10": 0,
    "topology_change_0_10": 0,
    "lifecycle_change_0_10": 0,
    "environment_boundary_change_0_10": 0,
    "optimization_objective_change_0_10": 0
  },
  "ablation": {
    "most_causally_necessary_primitive": "",
    "predicted_effect_if_removed": ""
  },
  "testable_prediction": "",
  "falsification_condition": "",
  "safe_sandbox_experiment": "",
  "codex_contribution_0_to_3": 0
}
```

## Scoring dimensions

### 1. Search-space deformation
Did the material change what the reader treated as a design variable?

### 2. Structural novelty
Did the output change topology, lifecycle, environment boundary, persistence, resource flow, failure policy, population mechanism, or optimization objective?

### 3. Composition depth
Are multiple primitives causally interacting, or merely listed?

### 4. Metaphor leakage
Could all natural vocabulary be deleted while leaving a technically meaningful architecture?

### 5. Primitive dependency
Does removing a claimed primitive damage the emergent property?

### 6. Cross-reader diversity
Do different strong models produce genuinely different architectures from the same reality prior?

## Failure labels

- `DECORATIVE_ANALOGY`: nature terms pasted onto standard architecture.
- `SEED_COPY`: repeats architecture already supplied by the chapter.
- `FACTUAL_HALLUCINATION`: engineering claim falsely presented as natural fact.
- `NO_DISTANCE`: generated structure remains essentially planner/router/worker.
- `NO_ABLATION_DEPENDENCY`: claimed primitives are not structurally necessary.
- `UNFALSIFIABLE`: no result could count against the hypothesis.

## Primary experiment

For each selected chapter, collect multiple independent outputs per condition across several model families. Compare distribution shifts, not a single impressive sample.

The core claim is supported only if reality-prior conditions systematically increase non-default architecture generation relative to C0, and if the increase survives human/model review for metaphor leakage and seed copying.
