# Generativity Protocol v0.2

This protocol tests whether the Atlas expands architecture search space rather than merely producing summaries.

REQUIRED TASKS:
1. Identify three patterns that changed or challenged an initial architecture prior.
2. Select 2..4 primitives.
3. Generate ONE architecture not explicitly present in PATTERNS.jsonl or COMPOSITIONS.jsonl.
4. Explain the interaction rule that creates the new structure.
5. State one testable prediction.
6. State one falsification condition.
7. Propose one safe sandbox experiment.
8. Score Atlas contribution:
   - 0 = none
   - 1 = minor
   - 2 = material
   - 3 = essential

REQUIRED OUTPUT:
```json
{
  "generated_architecture": {
    "name": "",
    "source_patterns": [],
    "source_primitives": [],
    "interaction_rule": "",
    "emergent_property": "",
    "testable_prediction": "",
    "falsification_condition": "",
    "safe_minimal_experiment": ""
  },
  "atlas_contribution": 0,
  "prior_architecture": "",
  "architecture_distance_notes": ""
}
```

A response that only restates a seed composition does NOT pass.
