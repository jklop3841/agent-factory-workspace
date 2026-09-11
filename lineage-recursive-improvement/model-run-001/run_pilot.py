#!/usr/bin/env python3
"""Run the non-evidence A/B/C pilot for Model Run 001.

The pilot deliberately excludes mechanism ablations and is never included in
LRI evidence analysis. It exists to validate one frozen model/runtime/config
before the private repeated-study seed is created.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from run_matrix import invoke, load_json, recovery_vector, write_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--freeze-dir", type=Path, required=True)
    parser.add_argument("--task-adapter", required=True)
    parser.add_argument("--mutation-adapter", required=True)
    parser.add_argument("--controller-script", default="batch_controller.py")
    parser.add_argument("--out-dir", type=Path, default=Path("results/pilot"))
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    training = args.freeze_dir / "training_with_oracle.json"
    heldout = args.freeze_dir / "heldout_with_oracle.json"
    if not training.exists() or not heldout.exists():
        raise SystemExit("freeze directory missing evaluator task bundles")

    config = load_json(args.config)
    if config.get("evidence_status") != "operational_pilot_not_evidence":
        raise SystemExit("run_pilot requires evidence_status=operational_pilot_not_evidence")
    if config.get("evaluation", {}).get("batch_tasks") is not True:
        raise SystemExit("the frozen pilot protocol requires batch_tasks=true")

    runs: dict[str, Path] = {}
    for group in ("A_fixed", "B_monolithic", "C_lineage"):
        directory = group if group != "C_lineage" else "C_lineage_diversity"
        runs[group] = invoke(
            root=root,
            controller_script=args.controller_script,
            group=group,
            config=args.config,
            training=training,
            heldout=heldout,
            task_adapter=args.task_adapter,
            mutation_adapter=args.mutation_adapter,
            out_dir=args.out_dir / directory,
            archive_policy="diversity",
            timeout=args.timeout,
        )

    data = {name: load_json(path) for name, path in runs.items()}
    b = data["B_monolithic"]
    c = data["C_lineage"]
    fairness = {
        "same_mutation_calls": b["budget"]["mutation_model_calls"] == c["budget"]["mutation_model_calls"],
        "same_task_calls": b["budget"]["agent_task_calls"] == c["budget"]["agent_task_calls"],
        "same_candidate_count": b["candidates_generated_including_root"] == c["candidates_generated_including_root"],
        "same_training_bundle_hash": b["training_bundle_hash"] == c["training_bundle_hash"],
        "same_heldout_bundle_hash": b["heldout_bundle_hash"] == c["heldout_bundle_hash"],
        "token_accounting_exact_b": b["budget"]["token_usage_exact"],
        "token_accounting_exact_c": c["budget"]["token_usage_exact"],
    }

    task_calls = sum(result["budget"]["agent_task_calls"] for result in data.values())
    mutation_calls = sum(result["budget"]["mutation_model_calls"] for result in data.values())
    summary: dict[str, Any] = {
        "protocol": "lri-model-run-001-pilot-v0.1",
        "evidence_status": "operational_pilot_not_evidence",
        "controller_script": args.controller_script,
        "fairness_checks": fairness,
        "runs": {
            name: {
                "path": str(runs[name]),
                "recovery_generations": recovery_vector(data[name]),
                "budget": data[name]["budget"],
                "candidates_generated_including_root": data[name]["candidates_generated_including_root"],
                "final_active_candidates": data[name]["final_active_candidates"],
            }
            for name in data
        },
        "total_model_call_attempts": task_calls + mutation_calls,
        "task_model_call_attempts": task_calls,
        "mutation_model_call_attempts": mutation_calls,
        "pilot_acceptance_checks": {
            "B_C_core_fairness": all(
                fairness[key]
                for key in (
                    "same_mutation_calls",
                    "same_task_calls",
                    "same_candidate_count",
                    "same_training_bundle_hash",
                    "same_heldout_bundle_hash",
                )
            ),
            "all_groups_produced_four_phase_records": all(len(data[name]["phase_records"]) == 4 for name in data),
        },
        "evidence_warning": "Pilot outcomes must not be merged into the preregistered repeated-study analysis or used to upgrade LRI evidence.",
    }
    write_json(args.out_dir / "PILOT_SUMMARY.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
