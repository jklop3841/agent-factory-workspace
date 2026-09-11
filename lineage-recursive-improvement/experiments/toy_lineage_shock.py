"""Toy mechanism demo for Lineage Recursive Improvement (LRI).

This is NOT evidence that LRI improves real AI agents.
It demonstrates one narrow mechanism: preserving diverse lineages can retain
option value when an observable environment target changes repeatedly.

Run:
    python toy_lineage_shock.py

Zero third-party dependencies.
"""

from __future__ import annotations

import json
import random
import statistics

TARGETS = (2.0, 8.0, -5.0, 4.0)
EVALS_PER_GENERATION = 8
GENERATIONS_PER_PHASE = 15
SIGMA = 1.25
ARCHIVE_NICHES = 12
RECOVERY_THRESHOLD = 1.0
SEEDS = 500
LOWER = -10.0
UPPER = 10.0


def clip(value: float) -> float:
    return max(LOWER, min(UPPER, value))


def niche_index(value: float) -> int:
    fraction = (clip(value) - LOWER) / (UPPER - LOWER)
    return min(ARCHIVE_NICHES - 1, int(fraction * ARCHIVE_NICHES))


def niche_center(index: int) -> float:
    width = (UPPER - LOWER) / ARCHIVE_NICHES
    return LOWER + (index + 0.5) * width


def run_one(seed: int) -> dict[str, list[int]]:
    # Independent random streams prevent one group's draws from steering another.
    mono_rng = random.Random(seed * 2 + 1)
    lineage_rng = random.Random(seed * 2 + 2)

    fixed = 0.0
    monolithic = 0.0
    archive = [0.0]

    recovery = {"fixed": [], "monolithic": [], "lineage": []}

    for target in TARGETS:
        hits = {"fixed": None, "monolithic": None, "lineage": None}

        for generation in range(GENERATIONS_PER_PHASE):
            # Group B: same number of new candidate evaluations as Group C.
            mono_candidates = [
                clip(monolithic + mono_rng.gauss(0.0, SIGMA))
                for _ in range(EVALS_PER_GENERATION)
            ]
            monolithic = min(mono_candidates, key=lambda x: abs(x - target))

            # Group C: parents are sampled from preserved lineage representatives.
            lineage_candidates = [
                clip(lineage_rng.choice(archive) + lineage_rng.gauss(0.0, SIGMA))
                for _ in range(EVALS_PER_GENERATION)
            ]

            # Keep one representative per niche. Selection is based on niche position,
            # not the current target, so diversity is deliberately preserved.
            representatives: dict[int, float] = {}
            for candidate in archive + lineage_candidates:
                idx = niche_index(candidate)
                if (
                    idx not in representatives
                    or abs(candidate - niche_center(idx))
                    < abs(representatives[idx] - niche_center(idx))
                ):
                    representatives[idx] = candidate
            archive = list(representatives.values())

            lineage_best = min(archive, key=lambda x: abs(x - target))
            distances = {
                "fixed": abs(fixed - target),
                "monolithic": abs(monolithic - target),
                "lineage": abs(lineage_best - target),
            }

            for group, distance in distances.items():
                if hits[group] is None and distance <= RECOVERY_THRESHOLD:
                    hits[group] = generation + 1

        for group in recovery:
            recovery[group].append(
                hits[group] if hits[group] is not None else GENERATIONS_PER_PHASE + 1
            )

    return recovery


def main() -> None:
    samples = {
        "fixed": [[] for _ in TARGETS],
        "monolithic": [[] for _ in TARGETS],
        "lineage": [[] for _ in TARGETS],
    }

    for seed in range(SEEDS):
        result = run_one(seed)
        for group in samples:
            for phase, value in enumerate(result[group]):
                samples[group][phase].append(value)

    summary = {
        "experiment": "toy_lineage_shock",
        "interpretation": (
            "mechanism demonstration only; not evidence of real-agent superiority"
        ),
        "config": {
            "targets": TARGETS,
            "evaluations_per_generation": EVALS_PER_GENERATION,
            "generations_per_phase": GENERATIONS_PER_PHASE,
            "sigma": SIGMA,
            "archive_niches": ARCHIVE_NICHES,
            "recovery_threshold": RECOVERY_THRESHOLD,
            "seeds": SEEDS,
        },
        "mean_generations_to_recovery": {
            group: [round(statistics.mean(values), 3) for values in phases]
            for group, phases in samples.items()
        },
        "median_generations_to_recovery": {
            group: [statistics.median(values) for values in phases]
            for group, phases in samples.items()
        },
    }

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
