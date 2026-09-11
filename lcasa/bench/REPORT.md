# LCASA v0.2 Retrieval Benchmark

This is a **seed benchmark**, not a held-out generalization claim. The 10 tasks were already part of the v0.1 package and therefore should be treated as development-set evidence only.

- tasks: 10
- metric: macro recall@5 over expected structural coordinates
- lexical baseline: 0.10
- v0.2 hybrid retrieval: 0.45
- absolute gain: 0.35

Interpretation: the hybrid router is materially better than the deterministic lexical baseline on the seed set, but recall remains too low for the atlas to claim reliable semantic routing. This result justifies the v0.3 priority: learned embeddings, better graph fusion, and a genuinely held-out multi-model evaluation set.

## Failure signal

Tasks e04, e09, and e10 still have zero recall@5. Those misses are valuable: they show that hashing vectors and local graph boosts do not yet recover deeper paraphrased structures reliably. Do not hide these failures; keep them as regression targets.
