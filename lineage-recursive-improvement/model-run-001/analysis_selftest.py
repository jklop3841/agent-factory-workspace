#!/usr/bin/env python3
"""Directional-bias self-test for analyze_repeats.py.

This script creates synthetic result fixtures where:
1. lineage clearly wins;
2. monolithic clearly wins;
3. neither has an advantage;
4. fairness is confounded.

The analysis code must classify all four in the expected direction. These are
software tests only, not empirical LRI results.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def run_entry(recovery: list[int | None]) -> dict[str, Any]:
    return {
        "recovery_generations": recovery,
        "budget": {
            "mutation_model_calls": 1,
            "agent_task_calls": 1,
            "input_tokens": 1,
            "output_tokens": 1,
            "token_usage_exact": True,
        },
        "candidates_generated_including_root": 2,
        "final_active_candidates": 1,
        "final_stored_candidate_bytes": 100,
    }


def matrix(kind: str) -> dict[str, Any]:
    fairness = {
        "same_mutation_calls": True,
        "same_task_calls": True,
        "same_candidate_count": True,
        "token_accounting_exact_b": True,
        "token_accounting_exact_c": True,
    }

    if kind == "lineage":
        b = [0, 3, 3, 3]
        c = [0, 1, 1, 1]
        score_only = [0, 3, 3, 3]
        equal_memory = [0, 1, 1, 1]
        pruned = [0, 3, 3, 3]
    elif kind == "monolithic":
        b = [0, 1, 1, 1]
        c = [0, 3, 3, 3]
        score_only = [0, 3, 3, 3]
        equal_memory = [0, 3, 3, 3]
        pruned = [0, 3, 3, 3]
    elif kind == "tie":
        b = c = score_only = equal_memory = pruned = [0, 2, 2, 2]
    elif kind == "confounded":
        b = [0, 3, 3, 3]
        c = [0, 1, 1, 1]
        score_only = [0, 3, 3, 3]
        equal_memory = [0, 1, 1, 1]
        pruned = [0, 3, 3, 3]
        fairness["same_candidate_count"] = False
    else:
        raise ValueError(kind)

    return {
        "protocol": "synthetic-analysis-selftest",
        "evidence_status": "software_fixture_not_evidence",
        "fairness_checks": fairness,
        "runs": {
            "A_fixed": run_entry([None, None, None, None]),
            "B_monolithic": run_entry(b),
            "C_lineage_diversity": run_entry(c),
            "C_lineage_score_only": run_entry(score_only),
            "C_lineage_equal_memory": run_entry(equal_memory),
            "C_lineage_pruned": run_entry(pruned),
        },
    }


def write_repeats(root: Path, kind: str, count: int = 20) -> None:
    for i in range(count):
        run_dir = root / f"run-{i:03d}" / "matrix"
        run_dir.mkdir(parents=True, exist_ok=True)
        (run_dir / "MATRIX_SUMMARY.json").write_text(
            json.dumps(matrix(kind), indent=2) + "\n", encoding="utf-8"
        )


def classify(root: Path) -> str:
    output = root / "analysis.json"
    command = [
        sys.executable,
        str(ROOT / "analyze_repeats.py"),
        "--root",
        str(root),
        "--max-generations",
        "3",
        "--min-runs",
        "20",
        "--bootstrap-iterations",
        "500",
        "--bootstrap-seed",
        "17",
        "--output",
        str(output),
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr or completed.stdout)
    result = json.loads(output.read_text(encoding="utf-8"))
    return result["automated_classification_suggestion"]


def main() -> None:
    expected = {
        "lineage": "supports_lri_under_tested_conditions",
        "monolithic": "supports_monolithic_under_tested_conditions",
        "tie": "no_detectable_lri_advantage",
        "confounded": "inconclusive_due_to_budget_or_evaluator_confounds",
    }
    observed = {}
    with tempfile.TemporaryDirectory(prefix="lri-analysis-selftest-") as temp:
        base = Path(temp)
        for kind, wanted in expected.items():
            root = base / kind
            write_repeats(root, kind)
            got = classify(root)
            observed[kind] = got
            if got != wanted:
                raise AssertionError(f"{kind}: expected {wanted}, got {got}")
    print(json.dumps({"expected": expected, "observed": observed, "status": "pass"}, indent=2))


if __name__ == "__main__":
    main()
