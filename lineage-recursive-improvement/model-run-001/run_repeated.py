#!/usr/bin/env python3
"""Run repeated preregistered Model Run 001 matrices.

The master seed is used only to derive per-run hidden task seeds. Generated
artifacts stay under the chosen output root, which should remain uncommitted
until the run is intentionally revealed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def derive_seed(master: str, index: int) -> str:
    return hashlib.sha256(f"{master}|{index}".encode("utf-8")).hexdigest()


def run_checked(cmd: list[str], cwd: Path) -> None:
    completed = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(
            f"command failed ({completed.returncode}): {' '.join(cmd)}\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--master-seed", required=True, help="Keep private until reveal for an evidence-bearing run.")
    parser.add_argument("--runs", type=int, default=20)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--task-adapter", required=True)
    parser.add_argument("--mutation-adapter", required=True)
    parser.add_argument("--out-root", type=Path, default=Path("results/repeated"))
    parser.add_argument("--training-per-phase", type=int, default=8)
    parser.add_argument("--heldout-per-phase", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    args.out_root.mkdir(parents=True, exist_ok=True)
    commitment = hashlib.sha256(args.master_seed.encode("utf-8")).hexdigest()
    index_rows = []

    for i in range(args.runs):
        run_name = f"run-{i:03d}"
        run_root = args.out_root / run_name
        freeze_dir = run_root / "hidden"
        matrix_dir = run_root / "matrix"
        seed = derive_seed(args.master_seed, i)

        run_checked(
            [
                sys.executable,
                "freeze_tasks.py",
                "--seed",
                seed,
                "--out",
                str(freeze_dir),
                "--training-per-phase",
                str(args.training_per_phase),
                "--heldout-per-phase",
                str(args.heldout_per_phase),
            ],
            root,
        )
        run_checked(
            [
                sys.executable,
                "run_matrix.py",
                "--config",
                str(args.config.resolve()),
                "--freeze-dir",
                str(freeze_dir.resolve()),
                "--task-adapter",
                args.task_adapter,
                "--mutation-adapter",
                args.mutation_adapter,
                "--out-dir",
                str(matrix_dir.resolve()),
                "--timeout",
                str(args.timeout),
            ],
            root,
        )
        freeze_manifest = json.loads((freeze_dir / "FREEZE_MANIFEST.json").read_text(encoding="utf-8"))
        index_rows.append(
            {
                "run": run_name,
                "seed_commitment_sha256": freeze_manifest["seed_commitment_sha256"],
                "shock_schedule_sha256": freeze_manifest["shock_schedule_sha256"],
                "training_bundle_sha256": freeze_manifest["training_bundle_sha256"],
                "heldout_bundle_sha256": freeze_manifest["heldout_bundle_sha256"],
                "matrix_summary": str(matrix_dir / "MATRIX_SUMMARY.json"),
            }
        )
        print(f"completed {run_name}", flush=True)

    manifest = {
        "protocol": "lri-model-run-001-repeated-v0.1",
        "run_count": args.runs,
        "master_seed_commitment_sha256": commitment,
        "master_seed_revealed": False,
        "config": str(args.config),
        "training_tasks_per_phase": args.training_per_phase,
        "heldout_tasks_per_phase": args.heldout_per_phase,
        "runs": index_rows,
        "note": "Reveal the master seed only after the frozen experiment is complete if independent task regeneration is desired.",
    }
    (args.out_root / "REPEATED_RUN_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
