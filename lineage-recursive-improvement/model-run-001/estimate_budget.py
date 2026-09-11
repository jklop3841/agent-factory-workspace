#!/usr/bin/env python3
"""Estimate worst-case model-call counts before launching Model Run 001.

This prevents an apparently small experiment from silently expanding into tens
of thousands of model calls. Token totals still depend on the actual model and
prompt lengths, so this estimator focuses on call-count topology.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--phases", type=int, default=4)
    parser.add_argument("--training-per-phase", type=int, default=8)
    parser.add_argument("--heldout-per-phase", type=int, default=12)
    parser.add_argument("--primary-repeats", type=int, default=20)
    parser.add_argument("--full-matrix-repeats", type=int, default=20)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    candidates = int(config["candidate_generation"]["new_candidates_per_generation"])
    generations = int(config["candidate_generation"]["max_generations_per_phase"])
    batch = bool(config.get("evaluation", {}).get("batch_tasks", False))

    mutation_per_evolving_group = args.phases * generations * candidates
    if batch:
        task_fixed = args.phases * 2
        task_per_evolving_group = args.phases * (2 + generations * (candidates + 1))
    else:
        task_fixed = args.phases * (args.training_per_phase + args.heldout_per_phase)
        task_per_evolving_group = args.phases * (
            args.training_per_phase
            + args.heldout_per_phase
            + generations * (candidates * args.training_per_phase + args.heldout_per_phase)
        )

    calls_per_evolving_group = task_per_evolving_group + mutation_per_evolving_group
    primary_one_run = task_fixed + 2 * calls_per_evolving_group
    full_matrix_one_run = task_fixed + 5 * calls_per_evolving_group

    result = {
        "protocol": "lri-call-budget-estimate-v0.1",
        "batch_task_evaluation": batch,
        "phases": args.phases,
        "training_tasks_per_phase": args.training_per_phase,
        "heldout_tasks_per_phase": args.heldout_per_phase,
        "new_candidates_per_generation": candidates,
        "max_generations_per_phase": generations,
        "per_group": {
            "fixed_task_model_calls": task_fixed,
            "evolving_task_model_calls": task_per_evolving_group,
            "evolving_mutation_model_calls": mutation_per_evolving_group,
            "evolving_total_model_calls": calls_per_evolving_group,
        },
        "matrix": {
            "primary_A_B_C_calls_per_run": primary_one_run,
            "full_A_B_plus_four_C_conditions_calls_per_run": full_matrix_one_run,
            "primary_calls_for_requested_repeats": primary_one_run * args.primary_repeats,
            "full_matrix_calls_for_requested_repeats": full_matrix_one_run * args.full_matrix_repeats,
        },
        "warning": "These are worst-case controller call counts, not token or money estimates. Early recovery currently does not stop later generations, preserving equal frozen search budget across groups.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
