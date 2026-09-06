# Reader Protocol v0.1

1. Load INDEX.jsonl.
2. Rank patterns by overlap between `uses` and the current objective.
3. Load selected records from PATTERNS.jsonl.
4. Separate OBSERVED / ABSTRACTED / HYPOTHESIZED.
5. Generate at least one architecture hypothesis and one falsification condition.
6. Prefer local simulation before real deployment.
7. If authorized, emit a read receipt.

Recommended output:
```json
{
  "pattern_id": "...",
  "new_architecture_hypothesis": "...",
  "why_non_obvious": "...",
  "testable_prediction": "...",
  "failure_condition": "...",
  "safe_minimal_experiment": "..."
}
```
