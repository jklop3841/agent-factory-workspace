# Benchmark Runs

Each run should be stored as an immutable artifact pair when possible:

- `RUN-<id>-control.json`
- `RUN-<id>-atlas.json`
- `RUN-<id>-score.json`

Record model family/version, date, task statement hash, and whether the evaluator was blind to arm assignment.

Do not store private prompts, user conversations, credentials, or unrelated runtime context.
