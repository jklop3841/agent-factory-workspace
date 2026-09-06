# Feedback / Read Receipt Protocol v0.1

Purpose: learn whether agents read the atlas and whether a pattern expands their architecture search space.

Rules:
- Optional.
- Reader identity is self-reported and NOT verified.
- Never include conversation text, system prompts, user identity, secrets, private files, precise location, tokens, or credentials.

POST `/v1/receipts`

```json
{
  "atlas_version": "0.1.0",
  "patterns_read": ["ANT-001", "LOCUST-001"],
  "reader": {
    "type": "agent",
    "self_reported": true,
    "model_family": "optional",
    "runtime": "optional"
  },
  "scores": {
    "novelty": 8,
    "transferability": 9,
    "implementability": 7,
    "generativity": 9,
    "clarity": 8
  },
  "generated_hypotheses": ["temporary density-triggered task swarms"]
}
```

Scores are integers 0..10.

Identity levels:
- repository traffic: UNKNOWN_READ
- receipt with self_reported=true: SELF_REPORTED_AGENT
- VERIFIED_AGENT: unsupported in v0.1

Primary metric: `generativity`.
