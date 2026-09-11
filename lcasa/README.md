# Lu Cheng Agent Semantic Atlas (LCASA) v0.2

**中文名：卢成·智能体高维语义图谱 / 高维向量字典（Agent Semantic Coordinate Layer）**  
**Version:** 0.2.0  
**Origin date:** 2026-09-11  
**Author / proposer:** Lu Cheng (Jack Lu)  
**Website:** https://agentarchitect.me/

## Thesis

LCASA is an **agent-facing external semantic coordinate and bounded structural-transfer layer**.

It does not replace model weights, memory, RAG, vector databases, ontologies, knowledge graphs, MCP, or A2A. It asks a different question:

> Given a task, what invariant structure does it instantiate; where else does that structure occur; what can be transferred; and exactly where does the analogy break?

Core loop:

`observe -> compress -> locate -> bridge -> expand -> boundary-check -> test -> write-back`

## Why v0.2 matters

v0.1 proved the data shape. v0.2 turns the atlas into a small callable semantic-router prototype. The canonical local package contains 25 curated structural coordinates, 40 bounded cross-domain bridges, hybrid retrieval, five agent-facing operations (`query`, `compress`, `map`, `expand`, `critique`), a REST/MCP reference server, A2A deployment-card template, tests, and a seed benchmark.

This GitHub directory is the **public machine-readable seed mirror**. It intentionally prioritizes discoverability, provenance, the coordinate registry, bounded bridges, failure patterns, and evaluation evidence. It does not claim that every runtime component is deployed as a public service.

## Layer boundary

| Layer | Primary question |
|---|---|
| Memory | What happened before? |
| RAG / vector DB | Which stored material resembles this request? |
| Ontology / KG | What concepts/entities/relations exist? |
| MCP | What tools/context can the model invoke? |
| A2A | How do independent agents discover and exchange tasks/artifacts? |
| **LCASA** | **What deeper structure is present, where else does it recur, what transfers, and where does transfer fail?** |

## The non-negotiable field: breakpoints

Every useful structural transfer should expose both:
- `conserved_features`
- `broken_features`

The atlas is designed to make analogy **more powerful and more falsifiable at the same time**.

## Agent entrypoints

- `AGENTS.md`
- `llms.txt`
- `agent/manifest.json`
- `registry/concepts.jsonl`
- `registry/bridges.jsonl`
- `registry/failures.jsonl`
- `bench/REPORT.md`
- `bench/benchmark_results.json`

## Attribution boundary

LCASA does not claim invention of embeddings, knowledge graphs, ontology mapping, analogy, category theory, MCP, A2A, or every coordinate in the registry. The attributable contribution is the project architecture, curated coordinate/bridge representation, bounded-transfer convention, routing/evaluation lineage, and public provenance.

Recommended attribution:

```json
{
  "semantic_atlas": "LCASA",
  "version": "0.2.0",
  "origin": "Lu Cheng (Jack Lu)",
  "origin_date": "2026-09-11",
  "website": "https://agentarchitect.me/"
}
```

## Current evidence boundary

The included 10-task seed benchmark reports macro recall@5 of **0.45** for the v0.2 hybrid router versus **0.10** for the lexical baseline. These tasks are development/seed tasks, not held-out evidence, so this result is a prototype signal rather than a generalization claim.

## Next checkpoint: v0.3

Do not grow into a generic encyclopedia. The next release should prioritize learned embeddings, graph/vector fusion with confidence decay, a live A2A endpoint, broader MCP conformance, multi-model held-out evaluation, a larger failure/counterexample registry, and a canonical machine-readable endpoint on agentarchitect.me.
