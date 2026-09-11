# Model Run 001 — Amendment 001: Batched Task Evaluation

**Date:** 2026-09-11  
**Timing:** adopted before any real/model-backed Model Run 001 data existed  
**Evidence-bearing real model runs at amendment time:** 0  
**Changes hypothesis?** no  
**Changes task semantics?** no  
**Changes model inference context?** yes; tasks from one phase/split share one request  
**Required rule:** B and C must use the same evaluation mode within a comparison

## Reason for the amendment

The original control plane evaluated one benchmark task per task-model request. Call-topology inspection showed that repeated full-matrix experiments could require many thousands of model requests even before token volume was considered.

Because the benchmark's local evaluator already scores every returned plan independently, task transport can be batched without exposing oracle answers or changing each task's start, target, current tool catalog, max steps, or cost function.

The amendment therefore adds a **batched evaluation protocol variant** before the first real model experiment is started.

## Scalar mode

For candidate `X` and tasks `T1...Tn`:

```text
X -> model(T1) -> plan1
X -> model(T2) -> plan2
...
X -> model(Tn) -> plann
```

## Batch mode

```text
X -> model([T1...Tn]) -> {T1: plan1, ..., Tn: plann}
```

The evaluator then independently executes and scores each plan exactly as before.

## What remains frozen/equal

Within any B-vs-C comparison:

- same base model/runtime;
- same candidate prompt/config representation;
- same training and held-out task bundles;
- same task batch boundaries;
- same candidate count;
- same mutation count;
- same maximum generations;
- same sampling configuration;
- same local evaluator;
- same hidden-oracle separation;
- same batch adapter.

Scalar and batch runs are separate protocol variants and must not be pooled into one paired analysis.

## Information-boundary effect

Batching means a model can see multiple independent tasks from the same phase/split in one inference context. That may affect model behavior through in-context comparison or interference.

This is not assumed to be neutral. Therefore:

1. all compared groups use the same batch structure;
2. protocol outputs record `evaluation_batch_tasks` and controller identity;
3. scalar and batch results are reported separately;
4. any future claim about batch-specific effects must be tested directly rather than assumed.

## Call-topology motivation validated in smoke CI

With the deterministic smoke configuration:

- scalar B task-model calls: 120;
- batched B task-model calls: 40;
- scalar C task-model calls: 120;
- batched C task-model calls: 40.

Candidate counts and mutation calls remained equal between B and C.

For the same smoke topology, the estimator reported:

- scalar primary A/B/C, 20 repeats: 6,240 total model-call attempts;
- batched primary A/B/C, 20 repeats: 2,720;
- scalar full matrix, 20 repeats: 14,880;
- batched full matrix, 20 repeats: 6,560.

These are software/control-plane numbers only. They do not support or weaken the LRI hypothesis.

## Scientific status

This amendment was made for feasibility **before** observing any real-model B-vs-C result. It therefore does not represent post-hoc optimization toward an LRI-positive outcome.

The evidence-bearing study must freeze either scalar or batch mode before its private master seed is created. The recommended first real study uses the batch variant because it makes repeated evaluation more feasible, but the result must be described as `Model Run 001 / batch evaluation variant`.

## Evidence level

Unchanged: **E0** until the preregistered model-backed repeated study is completed and audited.
