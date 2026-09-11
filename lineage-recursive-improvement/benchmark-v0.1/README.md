# LRI Benchmark v0.1 — Tool Interface Drift

**Status:** runnable benchmark harness  
**Evidence status for LRI:** still E0 until model-backed A/B/C runs exist  
**Dependencies:** Python standard library only

This benchmark is the first step after the scalar toy experiment. It gives a real command-line Agent a sequence of tool-use tasks and then changes the tool environment underneath it.

The benchmark is deliberately small. Its purpose is not to prove LRI. Its purpose is to create a common, reproducible surface on which fixed agents, monolithic recursive-improvement controllers, and lineage/population controllers can later be compared under the same task and budget rules.

## What changes across phases

The benchmark contains four phases:

1. **stable** — initial tool names and semantics;
2. **remove_double** — a useful tool disappears and a more expensive alternative appears;
3. **rename_and_negate** — tool names and semantics change substantially;
4. **cost_shift** — tools remain understandable but their economic structure changes.

Each task gives the Agent:

- current integer state;
- target integer;
- a current tool catalog;
- each tool's operation, argument and cost;
- maximum allowed tool calls.

The Agent must return a plan containing tool IDs.

## Run the built-in smoke baselines

From this directory:

```bash
python benchmark_v0_1.py --builtin oracle
python benchmark_v0_1.py --builtin legacy
```

Expected qualitative behavior:

- `oracle` succeeds on all phases and establishes the planning ceiling;
- `legacy` works on the original interface but fails after the first interface shock because it assumes the old tool names.

These are validation baselines, not RSI/LRI systems.

## Run the reference external Agent

```bash
python benchmark_v0_1.py \
  --agent-cmd "python example_agent.py" \
  --output reference-result.json
```

The reference Agent reads the current tool semantics and replans from scratch. It should achieve the oracle ceiling. This proves that the external command protocol is executable.

## External Agent protocol

For each benchmark task the harness launches the supplied local command and writes one JSON request to stdin:

```json
{
  "protocol": "lri-tool-drift-v0.1",
  "task": {
    "id": "remove_double-1",
    "phase": "remove_double",
    "phase_description": "...",
    "start": 2,
    "target": 11,
    "tools": [
      {"id": "inc", "op": "add", "arg": 1, "cost": 1}
    ],
    "max_steps": 6
  },
  "response_schema": {
    "plan": ["tool_id", "..."]
  }
}
```

The Agent writes exactly one JSON object to stdout:

```json
{"plan": ["inc", "inc", "triple", "dec"]}
```

The harness calculates success, invalid-action rate, actual execution cost and cost efficiency against a hidden optimal plan.

## Why this is useful for LRI

The benchmark itself does **not** perform recursive improvement. It separates the environment/evaluator from the improvement controller.

That separation lets future experiments compare:

- **A — fixed:** one frozen Agent configuration;
- **B — monolithic:** one persistent champion configuration that generates candidate revisions and replaces itself;
- **C — lineage:** multiple descendant configurations with explicit ancestry and a diversity archive.

All three can be evaluated through the same command protocol.

The model-backed experiment contract is in `MODEL_BACKED_PROTOCOL.md`.

## What v0.1 measures

The harness reports, per phase:

- task success rate;
- invalid-action rate;
- mean cost efficiency among successful tasks;
- per-task execution details.

For an actual recursive-improvement study, the controller must additionally log:

- candidate generation cost;
- model tokens/calls;
- evaluation calls;
- wall-clock time;
- lineage/revision ancestry;
- recovery after each shock;
- behavior diversity;
- archive/storage overhead;
- capability concentration.

## What v0.1 does not prove

A high score only means an Agent can solve this small tool-drift environment.

It does not prove:

- LRI is better than monolithic RSI;
- multi-Agent populations are safer;
- preserving diversity is always worth its cost;
- the benchmark predicts AGI or ASI dynamics;
- a model can improve its own architecture.

LRI should remain at E0 until a controlled model-backed comparison is run and published.

## Design constraints

- zero new Python dependencies;
- local command execution only;
- no benchmark-provided network access;
- no credential management;
- no autonomous persistence or external deployment;
- deterministic task suite in v0.1;
- evaluator keeps optimal plans private from the Agent.

## Next build

The next evidence-bearing step is **Model Run 001**:

> same base model, same total model-call/token/tool budget, same hidden task phases; compare a single-champion recursive controller against a lineage archive that preserves differentiated descendants.

The important result is not merely who gets the highest final score. The central measurement is **recovery after environment shock per unit total resource**, and whether any lineage advantage disappears when candidate count and stored information are equalized.
