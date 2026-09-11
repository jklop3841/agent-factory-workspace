#!/usr/bin/env python3
"""Run the preregistered Model Run 001 comparison matrix.

This wrapper launches the same provider-neutral controller for:
- A_fixed
- B_monolithic
- C_lineage diversity archive
- C_lineage score-only archive ablation
- C_lineage equal-memory ablation
- C_lineage non-dominant-branch pruning ablation

It never changes the task or mutation adapter between B and C.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def invoke(
    root: Path,
    controller_script: str,
    group: str,
    config: Path,
    training: Path,
    heldout: Path,
    task_adapter: str,
    mutation_adapter: str,
    out_dir: Path,
    archive_policy: str = "diversity",
    prune_before_phase: str | None = None,
    timeout: float = 60.0,
) -> Path:
    controller_path = Path(controller_script)
    if not controller_path.is_absolute():
        controller_path = root / controller_path
    cmd = [
        sys.executable,
        str(controller_path),
        "--group",
        group,
        "--config",
        str(config),
        "--training",
        str(training),
        "--heldout",
        str(heldout),
        "--task-adapter",
        task_adapter,
        "--mutation-adapter",
        mutation_adapter,
        "--out-dir",
        str(out_dir),
        "--timeout",
        str(timeout),
    ]
    if group == "C_lineage":
        cmd.extend(["--archive-policy", archive_policy])
    if prune_before_phase:
        cmd.extend(["--prune-before-phase", prune_before_phase])
    completed = subprocess.run(cmd, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(
            f"controller failed for {group}/{archive_policy}:\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    filename = f"{group}-{archive_policy if group == 'C_lineage' else 'main'}.json"
    result = out_dir / filename
    if not result.exists():
        raise RuntimeError(f"controller did not create {result}")
    return result


def recovery_vector(result: dict[str, Any]) -> list[int | None]:
    return [phase.get("recovery_generation") for phase in result["phase_records"]]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--freeze-dir", type=Path, required=True)
    parser.add_argument("--task-adapter", required=True)
    parser.add_argument("--mutation-adapter", required=True)
    parser.add_argument("--controller-script", default="controller.py")
    parser.add_argument("--out-dir", type=Path, default=Path("results/matrix"))
    parser.add_argument("--timeout", type=float, default=60.0)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    training = args.freeze_dir / "training_with_oracle.json"
    heldout = args.freeze_dir / "heldout_with_oracle.json"
    if not training.exists() or not heldout.exists():
        raise SystemExit("freeze directory is missing training_with_oracle.json or heldout_with_oracle.json")

    config_data = load_json(args.config)
    training_data = load_json(training)
    phases = [phase["id"] for phase in training_data["phases"]]
    prune_phase = phases[2] if len(phases) >= 3 else phases[-1]

    def call(
        group: str,
        directory: str,
        archive_policy: str = "diversity",
        prune_before_phase: str | None = None,
        config: Path | None = None,
    ) -> Path:
        return invoke(
            root,
            args.controller_script,
            group,
            config or args.config,
            training,
            heldout,
            args.task_adapter,
            args.mutation_adapter,
            args.out_dir / directory,
            archive_policy=archive_policy,
            prune_before_phase=prune_before_phase,
            timeout=args.timeout,
        )

    runs: dict[str, Path] = {}
    runs["A_fixed"] = call("A_fixed", "A_fixed")
    runs["B_monolithic"] = call("B_monolithic", "B_monolithic")
    runs["C_lineage_diversity"] = call("C_lineage", "C_lineage_diversity", archive_policy="diversity")
    runs["C_lineage_score_only"] = call("C_lineage", "C_lineage_score_only", archive_policy="score_only")

    equal_memory_config = json.loads(json.dumps(config_data))
    equal_memory_bytes = int(config_data.get("ablations", {}).get("equal_memory_bytes", 16000))
    equal_memory_config["budget"]["max_stored_candidate_bytes"] = equal_memory_bytes
    equal_memory_path = args.out_dir / "config.equal-memory.frozen.json"
    write_json(equal_memory_path, equal_memory_config)
    runs["C_lineage_equal_memory"] = call(
        "C_lineage",
        "C_lineage_equal_memory",
        archive_policy="diversity",
        config=equal_memory_path,
    )
    runs["C_lineage_pruned"] = call(
        "C_lineage",
        "C_lineage_pruned",
        archive_policy="diversity",
        prune_before_phase=prune_phase,
    )

    data = {name: load_json(path) for name, path in runs.items()}
    b_budget = data["B_monolithic"]["budget"]
    c_budget = data["C_lineage_diversity"]["budget"]
    fairness = {
        "same_mutation_calls": b_budget["mutation_model_calls"] == c_budget["mutation_model_calls"],
        "same_task_calls": b_budget["agent_task_calls"] == c_budget["agent_task_calls"],
        "same_candidate_count": data["B_monolithic"]["candidates_generated_including_root"]
        == data["C_lineage_diversity"]["candidates_generated_including_root"],
        "token_accounting_exact_b": b_budget["token_usage_exact"],
        "token_accounting_exact_c": c_budget["token_usage_exact"],
    }

    summary = {
        "protocol": "lri-model-run-matrix-v0.1",
        "evidence_status": config_data.get("evidence_status"),
        "controller_script": args.controller_script,
        "evaluation_batch_tasks": bool(config_data.get("evaluation", {}).get("batch_tasks", False)),
        "prune_before_phase": prune_phase,
        "fairness_checks": fairness,
        "runs": {
            name: {
                "path": str(path),
                "recovery_generations": recovery_vector(data[name]),
                "budget": data[name]["budget"],
                "candidates_generated_including_root": data[name]["candidates_generated_including_root"],
                "final_active_candidates": data[name]["final_active_candidates"],
                "final_stored_candidate_bytes": data[name]["final_stored_candidate_bytes"],
            }
            for name, path in runs.items()
        },
        "interpretation_rule": "Smoke/local outputs are not automatically evidence. Evidence requires the preregistered repeated model-backed design, held-out evaluation, resource accounting and required ablations.",
    }
    write_json(args.out_dir / "MATRIX_SUMMARY.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
