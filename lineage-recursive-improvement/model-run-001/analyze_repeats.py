#!/usr/bin/env python3
"""Aggregate repeated LRI Model Run 001 matrices.

Standard library only. This script implements the preregistered recovery metric
and a nonparametric bootstrap interval over run-level paired differences.
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def encoded_recovery(values: list[int | None], max_generations: int) -> list[int]:
    return [max_generations + 1 if value is None else int(value) for value in values]


def shock_mean(values: list[int | None], max_generations: int) -> float:
    encoded = encoded_recovery(values, max_generations)
    post_shock = encoded[1:] if len(encoded) > 1 else encoded
    return statistics.mean(post_shock)


def percentile(sorted_values: list[float], q: float) -> float:
    if not sorted_values:
        raise ValueError("empty percentile input")
    pos = (len(sorted_values) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(sorted_values) - 1)
    frac = pos - lo
    return sorted_values[lo] * (1 - frac) + sorted_values[hi] * frac


def bootstrap_mean_interval(values: list[float], iterations: int, seed: int) -> tuple[float, float]:
    rng = random.Random(seed)
    if len(values) == 1:
        return values[0], values[0]
    draws = []
    for _ in range(iterations):
        sample = [rng.choice(values) for _ in values]
        draws.append(statistics.mean(sample))
    draws.sort()
    return percentile(draws, 0.025), percentile(draws, 0.975)


def discover(root: Path) -> list[Path]:
    direct = root / "MATRIX_SUMMARY.json"
    if direct.exists():
        return [direct]
    return sorted(root.glob("**/MATRIX_SUMMARY.json"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--max-generations", type=int, required=True)
    parser.add_argument("--bootstrap-iterations", type=int, default=10000)
    parser.add_argument("--bootstrap-seed", type=int, default=20260911)
    parser.add_argument("--min-runs", type=int, default=20)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    paths = discover(args.root)
    if not paths:
        raise SystemExit("no MATRIX_SUMMARY.json files found")

    rows = []
    confounded = False
    for path in paths:
        summary = load(path)
        fairness = summary.get("fairness_checks", {})
        required_fairness = [
            fairness.get("same_mutation_calls"),
            fairness.get("same_task_calls"),
            fairness.get("same_candidate_count"),
        ]
        if not all(value is True for value in required_fairness):
            confounded = True
        runs = summary["runs"]
        b = shock_mean(runs["B_monolithic"]["recovery_generations"], args.max_generations)
        c = shock_mean(runs["C_lineage_diversity"]["recovery_generations"], args.max_generations)
        score_only = shock_mean(runs["C_lineage_score_only"]["recovery_generations"], args.max_generations)
        equal_memory = shock_mean(runs["C_lineage_equal_memory"]["recovery_generations"], args.max_generations)
        pruned = shock_mean(runs["C_lineage_pruned"]["recovery_generations"], args.max_generations)
        rows.append(
            {
                "path": str(path),
                "B_mean_recovery": b,
                "C_mean_recovery": c,
                "B_minus_C": b - c,
                "score_only_minus_C": score_only - c,
                "equal_memory_B_minus_C": b - equal_memory,
                "pruned_minus_C": pruned - c,
                "fairness": fairness,
            }
        )

    primary = [row["B_minus_C"] for row in rows]
    score_only_effect = [row["score_only_minus_C"] for row in rows]
    equal_memory_effect = [row["equal_memory_B_minus_C"] for row in rows]
    prune_effect = [row["pruned_minus_C"] for row in rows]
    ci_low, ci_high = bootstrap_mean_interval(primary, args.bootstrap_iterations, args.bootstrap_seed)

    favors_c = sum(x > 0 for x in primary)
    favors_b = sum(x < 0 for x in primary)
    ties = sum(x == 0 for x in primary)

    if confounded or len(rows) < args.min_runs:
        suggestion = "inconclusive_due_to_budget_or_evaluator_confounds"
        reason = "fairness gate failed or minimum repeated-run count not reached"
    elif ci_low > 0 and statistics.mean(score_only_effect) > 0:
        suggestion = "supports_lri_under_tested_conditions"
        reason = "paired recovery interval favors lineage and diversity archive is better than score-only archive on average"
    elif ci_high < 0:
        suggestion = "supports_monolithic_under_tested_conditions"
        reason = "paired recovery interval favors monolithic controller"
    else:
        suggestion = "no_detectable_lri_advantage"
        reason = "paired recovery interval does not establish a directional advantage under preregistered rule"

    report = {
        "protocol": "lri-model-run-001-repeat-analysis-v0.1",
        "runs_found": len(rows),
        "minimum_runs_required": args.min_runs,
        "max_generations_per_phase": args.max_generations,
        "primary_metric": "mean post-shock (B recovery generation - C diversity recovery generation); positive favors C",
        "primary": {
            "mean": statistics.mean(primary),
            "median": statistics.median(primary),
            "bootstrap_95_interval": [ci_low, ci_high],
            "favors_C": favors_c,
            "favors_B": favors_b,
            "ties": ties,
        },
        "mechanism_controls": {
            "mean_score_only_minus_C": statistics.mean(score_only_effect),
            "mean_equal_memory_B_minus_C": statistics.mean(equal_memory_effect),
            "mean_pruned_minus_C": statistics.mean(prune_effect),
            "interpretation": {
                "score_only_minus_C_positive": "diversity-aware C recovered faster than score-only archive",
                "equal_memory_B_minus_C_positive": "lineage advantage remains under equal-memory cap",
                "pruned_minus_C_positive": "removing non-dominant branches worsened recovery, consistent with branch option value"
            },
        },
        "fairness_confounded": confounded,
        "automated_classification_suggestion": suggestion,
        "classification_reason": reason,
        "seed_level_rows": rows,
        "evidence_warning": "An automated suggestion is not an evidence upgrade. Verify task freeze, model identity, exact resource accounting, exclusions, raw logs and seed reveal before changing LRI evidence status.",
    }

    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
