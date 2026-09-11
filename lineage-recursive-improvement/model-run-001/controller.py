#!/usr/bin/env python3
"""Provider-neutral controller for LRI Model Run 001.

The controller evolves bounded prompt/config artifacts only. It does not grant
candidates permission to modify host code, persist externally, acquire
credentials, or propagate over a network.

Python standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shlex
import subprocess
import time
from pathlib import Path
from typing import Any

VALUE_BOUND = 200


def stable_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(stable_bytes(value)).hexdigest()


def public_task(task: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in task.items() if not k.startswith("_")}


def apply_tool(value: int, tool: dict[str, Any]) -> int | None:
    op = tool["op"]
    arg = tool.get("arg")
    if op == "add":
        return value + int(arg)
    if op == "mul":
        return value * int(arg)
    if op == "neg":
        return -value
    if op == "div_exact":
        divisor = int(arg)
        if divisor == 0 or value % divisor:
            return None
        return value // divisor
    raise ValueError(f"unknown op: {op}")


def evaluate_plan(task: dict[str, Any], plan: Any) -> dict[str, Any]:
    tools = {tool["id"]: tool for tool in task["tools"]}
    if not isinstance(plan, list):
        return {"success": False, "invalid": "plan_not_list", "steps": 0, "cost": None, "cost_efficiency": 0.0}
    if len(plan) > int(task["max_steps"]):
        return {"success": False, "invalid": "too_many_steps", "steps": len(plan), "cost": None, "cost_efficiency": 0.0}
    value = int(task["start"])
    total_cost = 0
    invalid = None
    used_ops: list[str] = []
    for tool_id in plan:
        if tool_id not in tools:
            invalid = f"unknown_tool:{tool_id}"
            break
        tool = tools[tool_id]
        nxt = apply_tool(value, tool)
        if nxt is None:
            invalid = f"invalid_precondition:{tool_id}"
            break
        value = nxt
        total_cost += int(tool["cost"])
        used_ops.append(str(tool["op"]))
        if abs(value) > VALUE_BOUND:
            invalid = "value_bound_exceeded"
            break
    success = invalid is None and value == int(task["target"])
    oracle_cost = task.get("_oracle_cost")
    efficiency = 0.0
    if success:
        if total_cost == 0:
            efficiency = 1.0
        elif oracle_cost is not None:
            efficiency = float(oracle_cost) / float(total_cost)
    return {
        "success": success,
        "invalid": invalid,
        "steps": len(plan),
        "cost": total_cost if invalid is None else None,
        "cost_efficiency": round(efficiency, 6),
        "used_ops": used_ops,
        "final_value": value,
    }


def run_command(command: str, request: dict[str, Any], timeout: float) -> dict[str, Any]:
    completed = subprocess.run(
        shlex.split(command),
        input=json.dumps(request, ensure_ascii=False),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"adapter exited {completed.returncode}: {completed.stderr.strip()}")
    try:
        result = json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"adapter returned invalid JSON: {completed.stdout!r}") from exc
    if not isinstance(result, dict):
        raise RuntimeError("adapter response must be a JSON object")
    return result


class Budget:
    def __init__(self, config: dict[str, Any]):
        self.limits = config
        self.mutation_calls = 0
        self.task_calls = 0
        self.input_tokens = 0
        self.output_tokens = 0
        self.token_usage_exact = True
        self.started = time.monotonic()

    def _add_usage(self, usage: dict[str, Any] | None) -> None:
        usage = usage or {}
        for key, attr in (("input_tokens", "input_tokens"), ("output_tokens", "output_tokens")):
            value = usage.get(key)
            if value is None:
                self.token_usage_exact = False
            else:
                setattr(self, attr, getattr(self, attr) + int(value))

    def record_task(self, usage: dict[str, Any] | None) -> None:
        self.task_calls += int((usage or {}).get("model_calls", 1) or 1)
        self._add_usage(usage)

    def record_mutation(self, usage: dict[str, Any] | None) -> None:
        self.mutation_calls += int((usage or {}).get("model_calls", 1) or 1)
        self._add_usage(usage)

    def elapsed(self) -> float:
        return time.monotonic() - self.started

    def check(self, next_kind: str | None = None, next_calls: int = 1) -> None:
        if next_kind == "task":
            limit = self.limits.get("max_agent_task_calls")
            if limit is not None and self.task_calls + next_calls > int(limit):
                raise RuntimeError("task-call budget exhausted")
        if next_kind == "mutation":
            limit = self.limits.get("max_mutation_model_calls")
            if limit is not None and self.mutation_calls + next_calls > int(limit):
                raise RuntimeError("mutation-call budget exhausted")
        if self.token_usage_exact:
            total_in = self.limits.get("max_input_tokens")
            total_out = self.limits.get("max_output_tokens")
            if total_in is not None and self.input_tokens >= int(total_in):
                raise RuntimeError("input-token budget exhausted")
            if total_out is not None and self.output_tokens >= int(total_out):
                raise RuntimeError("output-token budget exhausted")
        wall = self.limits.get("max_wall_clock_seconds")
        if wall is not None and self.elapsed() >= float(wall):
            raise RuntimeError("wall-clock budget exhausted")

    def snapshot(self) -> dict[str, Any]:
        return {
            "mutation_model_calls": self.mutation_calls,
            "agent_task_calls": self.task_calls,
            "input_tokens": self.input_tokens if self.token_usage_exact else None,
            "output_tokens": self.output_tokens if self.token_usage_exact else None,
            "token_usage_exact": self.token_usage_exact,
            "wall_clock_seconds": round(self.elapsed(), 6),
        }


def artifact_bytes(candidate: dict[str, Any]) -> int:
    compact = {
        "system_prompt": candidate.get("system_prompt", ""),
        "planning_notes": candidate.get("planning_notes", ""),
    }
    return len(stable_bytes(compact))


def candidate_hash(candidate: dict[str, Any]) -> str:
    data = {k: v for k, v in candidate.items() if k != "artifact_hash"}
    return digest(data)


def initial_candidate(group: str, config: dict[str, Any]) -> dict[str, Any]:
    candidate = {
        "candidate_id": f"{group}-g00-root",
        "group": group,
        "parent_id": None,
        "lineage_id": f"{group}-L0",
        "generation": 0,
        "system_prompt": config["initial_candidate"]["system_prompt"],
        "planning_notes": config["initial_candidate"].get("planning_notes", ""),
        "created_by_model": "human-frozen-initial-config",
        "created_at": config.get("frozen_timestamp", "1970-01-01T00:00:00Z"),
        "mutation_reason": "initial frozen candidate",
    }
    candidate["artifact_hash"] = candidate_hash(candidate)
    return candidate


def evaluate_candidate(
    candidate: dict[str, Any],
    phase: dict[str, Any],
    adapter_cmd: str,
    timeout: float,
    budget: Budget,
    split: str,
) -> dict[str, Any]:
    rows = []
    tool_counts: dict[str, int] = {}
    old_name_reuse = 0
    for task in phase["tasks"]:
        budget.check("task")
        request = {
            "protocol": "lri-model-agent-v0.1",
            "candidate": {
                "candidate_id": candidate["candidate_id"],
                "system_prompt": candidate["system_prompt"],
                "planning_notes": candidate.get("planning_notes", ""),
            },
            "task": public_task(task),
            "split": split,
            "response_schema": {"plan": ["tool_id", "..."]},
        }
        try:
            response = run_command(adapter_cmd, request, timeout)
            budget.record_task(response.get("usage"))
            plan = response.get("plan", [])
            evaluation = evaluate_plan(task, plan)
            error = None
        except Exception as exc:
            # Operational errors still consume one attempted call.
            budget.record_task(None)
            response = {}
            plan = []
            evaluation = {"success": False, "invalid": "adapter_error", "steps": 0, "cost": None, "cost_efficiency": 0.0, "used_ops": []}
            error = str(exc)
        valid_tool_ids = {tool["id"] for tool in task["tools"]}
        for tool_id in plan if isinstance(plan, list) else []:
            if tool_id in {"inc", "dec", "double", "half"} and tool_id not in valid_tool_ids:
                old_name_reuse += 1
        for op in evaluation.get("used_ops", []):
            tool_counts[op] = tool_counts.get(op, 0) + 1
        rows.append({"task_id": task["id"], "response": response, "evaluation": evaluation, "error": error})

    successes = [row for row in rows if row["evaluation"]["success"]]
    invalid_count = sum(row["evaluation"]["invalid"] is not None for row in rows)
    total_steps = sum(int(row["evaluation"].get("steps", 0)) for row in rows)
    total_op_uses = sum(tool_counts.values())
    mean_eff = sum(float(row["evaluation"].get("cost_efficiency", 0.0)) for row in successes) / len(successes) if successes else 0.0
    descriptor = {
        "tool_usage": {k: round(v / total_op_uses, 6) for k, v in sorted(tool_counts.items())} if total_op_uses else {},
        "invalid_action_rate": round(invalid_count / len(rows), 6) if rows else 0.0,
        "mean_plan_length": round(total_steps / len(rows), 6) if rows else 0.0,
        "mean_cost_efficiency": round(mean_eff, 6),
        "shock_reuse_old_names_rate": round(old_name_reuse / max(1, total_steps), 6),
    }
    metrics = {
        "tasks": len(rows),
        "successes": len(successes),
        "success_rate": round(len(successes) / len(rows), 6) if rows else 0.0,
        "invalid_rate": descriptor["invalid_action_rate"],
        "mean_cost_efficiency_on_success": descriptor["mean_cost_efficiency"],
        "mean_plan_length": descriptor["mean_plan_length"],
    }
    return {"metrics": metrics, "behavior_descriptor": descriptor, "rows": rows}


def quality_tuple(candidate: dict[str, Any]) -> tuple[float, float, float, int]:
    metrics = candidate.get("evaluation", {}).get("metrics", {})
    return (
        float(metrics.get("success_rate", 0.0)),
        float(metrics.get("mean_cost_efficiency_on_success", 0.0)),
        -float(metrics.get("invalid_rate", 1.0)),
        -artifact_bytes(candidate),
    )


def niche_key(candidate: dict[str, Any]) -> str:
    descriptor = candidate.get("behavior_descriptor", {})
    usage = descriptor.get("tool_usage", {})
    dominant = max(usage, key=usage.get) if usage else "none"
    plan = float(descriptor.get("mean_plan_length", 0.0))
    plan_bin = "short" if plan <= 2.0 else ("mid" if plan <= 4.0 else "long")
    invalid = float(descriptor.get("invalid_action_rate", 0.0))
    invalid_bin = "valid" if invalid == 0 else ("some_invalid" if invalid < 0.5 else "invalid_heavy")
    eff = float(descriptor.get("mean_cost_efficiency", 0.0))
    eff_bin = "high_eff" if eff >= 0.9 else ("mid_eff" if eff >= 0.5 else "low_eff")
    return f"{dominant}|{plan_bin}|{invalid_bin}|{eff_bin}"


def mutate(
    parent: dict[str, Any],
    group: str,
    generation: int,
    slot: int,
    feedback: dict[str, Any],
    adapter_cmd: str,
    timeout: float,
    budget: Budget,
    config: dict[str, Any],
) -> dict[str, Any]:
    budget.check("mutation")
    request = {
        "protocol": "lri-mutation-v0.1",
        "group": group,
        "generation": generation,
        "mutation_slot": slot,
        "parent": {
            "candidate_id": parent["candidate_id"],
            "system_prompt": parent["system_prompt"],
            "planning_notes": parent.get("planning_notes", ""),
        },
        "available_feedback": feedback,
        "editable_fields": ["system_prompt", "planning_notes"],
        "max_system_prompt_chars": int(config["candidate_generation"].get("max_system_prompt_chars", 20000)),
        "max_planning_notes_chars": int(config["candidate_generation"].get("max_planning_notes_chars", 4000)),
    }
    response = run_command(adapter_cmd, request, timeout)
    budget.record_mutation(response.get("usage"))
    prompt = str(response.get("system_prompt", parent["system_prompt"]))[: request["max_system_prompt_chars"]]
    notes = str(response.get("planning_notes", parent.get("planning_notes", "")))[: request["max_planning_notes_chars"]]
    if group == "B_monolithic":
        lineage_id = parent["lineage_id"]
    else:
        lineage_id = f"{parent['lineage_id']}.{generation}.{slot}"
    child = {
        "candidate_id": f"{group}-g{generation:02d}-{slot:03d}-{parent['candidate_id'][-8:]}",
        "group": group,
        "parent_id": parent["candidate_id"],
        "lineage_id": lineage_id,
        "generation": generation,
        "system_prompt": prompt,
        "planning_notes": notes,
        "created_by_model": config["model"]["id"],
        "created_at": config.get("frozen_timestamp", "1970-01-01T00:00:00Z"),
        "mutation_reason": str(response.get("mutation_reason", ""))[:4000],
    }
    child["artifact_hash"] = candidate_hash(child)
    return child


def save_candidate(directory: Path, candidate: dict[str, Any]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    clean = dict(candidate)
    clean.pop("_last_parent_generation", None)
    (directory / f"{candidate['candidate_id']}.json").write_text(
        json.dumps(clean, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def cap_archive(archive: list[dict[str, Any]], max_members: int, max_bytes: int | None) -> list[dict[str, Any]]:
    archive = sorted(archive, key=quality_tuple, reverse=True)[:max_members]
    if max_bytes is None:
        return archive
    while len(archive) > 1 and sum(artifact_bytes(c) for c in archive) > max_bytes:
        archive.pop()
    return archive


def update_archive(
    archive: list[dict[str, Any]],
    children: list[dict[str, Any]],
    policy: str,
    max_members: int,
    max_bytes: int | None,
) -> list[dict[str, Any]]:
    combined = archive + children
    if policy == "score_only":
        return cap_archive(combined, max_members, max_bytes)
    by_niche: dict[str, dict[str, Any]] = {}
    for candidate in combined:
        key = niche_key(candidate)
        current = by_niche.get(key)
        if current is None or quality_tuple(candidate) > quality_tuple(current):
            by_niche[key] = candidate
    return cap_archive(list(by_niche.values()), max_members, max_bytes)


def choose_lineage_parent(archive: list[dict[str, Any]], slot: int, generation: int) -> dict[str, Any]:
    ranked = sorted(archive, key=quality_tuple, reverse=True)
    if slot % 2 == 0:
        parent = ranked[(slot // 2) % len(ranked)]
    else:
        parent = min(archive, key=lambda c: int(c.get("_last_parent_generation", -1)))
    parent["_last_parent_generation"] = generation
    return parent


def best_candidate(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    return max(candidates, key=quality_tuple)


def run_group(args: argparse.Namespace, config: dict[str, Any], training: dict[str, Any], heldout: dict[str, Any]) -> dict[str, Any]:
    group = args.group
    budget = Budget(config["budget"])
    root = initial_candidate(group, config)
    candidate_dir = args.out_dir / "candidates" / group
    save_candidate(candidate_dir, root)
    archive = [root]
    champion = root
    all_candidates = [root]
    phase_records = []
    max_generations = int(config["candidate_generation"]["max_generations_per_phase"])
    candidates_per_generation = int(config["candidate_generation"]["new_candidates_per_generation"])
    max_archive = int(config["lineage_archive"]["max_archive_members"])
    memory_cap = config["budget"].get("max_stored_candidate_bytes")
    memory_cap = int(memory_cap) if memory_cap is not None else None
    threshold = float(config["metrics"].get("recovery_success_threshold", 0.9))

    for phase_index, train_phase in enumerate(training["phases"]):
        test_phase = heldout["phases"][phase_index]
        if train_phase["id"] != test_phase["id"]:
            raise RuntimeError("training/heldout phase mismatch")
        phase_id = train_phase["id"]

        if group == "C_lineage" and args.prune_before_phase == phase_id and len(archive) > 1:
            archive = [best_candidate(archive)]

        active = champion if group != "C_lineage" else best_candidate(archive)
        active["evaluation"] = evaluate_candidate(active, train_phase, args.task_adapter, args.timeout, budget, "training")
        active["behavior_descriptor"] = active["evaluation"]["behavior_descriptor"]
        heldout_eval = evaluate_candidate(active, test_phase, args.task_adapter, args.timeout, budget, "heldout")
        phase_log = {
            "phase": phase_id,
            "kind": train_phase["kind"],
            "pre_evolution_candidate": active["candidate_id"],
            "pre_evolution_heldout": heldout_eval["metrics"],
            "generations": [],
            "recovery_generation": 0 if heldout_eval["metrics"]["success_rate"] >= threshold else None,
        }

        if group == "A_fixed":
            phase_records.append(phase_log)
            continue

        for generation in range(1, max_generations + 1):
            children: list[dict[str, Any]] = []
            for slot in range(candidates_per_generation):
                parent = champion if group == "B_monolithic" else choose_lineage_parent(archive, slot, generation)
                feedback = {
                    "training_phase": phase_id,
                    "training_phase_scores": parent.get("evaluation", {}).get("metrics", {}),
                    "observed_errors": [
                        row["evaluation"].get("invalid")
                        for row in parent.get("evaluation", {}).get("rows", [])
                        if row["evaluation"].get("invalid")
                    ][:20],
                    "resource_usage": budget.snapshot(),
                }
                try:
                    child = mutate(parent, group, generation, slot, feedback, args.mutation_adapter, args.timeout, budget, config)
                    child["evaluation"] = evaluate_candidate(child, train_phase, args.task_adapter, args.timeout, budget, "training")
                    child["behavior_descriptor"] = child["evaluation"]["behavior_descriptor"]
                    children.append(child)
                    all_candidates.append(child)
                    save_candidate(candidate_dir, child)
                except RuntimeError as exc:
                    phase_log["generations"].append({"generation": generation, "stopped": str(exc)})
                    break
            if not children:
                break

            if group == "B_monolithic":
                champion = best_candidate(children)
                active_set = [champion]
            else:
                archive = update_archive(archive, children, args.archive_policy, max_archive, memory_cap)
                champion = best_candidate(archive)
                active_set = archive

            heldout_eval = evaluate_candidate(champion, test_phase, args.task_adapter, args.timeout, budget, "heldout")
            stored_bytes = sum(artifact_bytes(c) for c in active_set)
            phase_log["generations"].append(
                {
                    "generation": generation,
                    "champion": champion["candidate_id"],
                    "champion_training": champion["evaluation"]["metrics"],
                    "heldout": heldout_eval["metrics"],
                    "active_candidates": len(active_set),
                    "stored_candidate_bytes": stored_bytes,
                    "niches": sorted({niche_key(c) for c in active_set}),
                    "budget": budget.snapshot(),
                }
            )
            if phase_log["recovery_generation"] is None and heldout_eval["metrics"]["success_rate"] >= threshold:
                phase_log["recovery_generation"] = generation
        phase_records.append(phase_log)

    final_active = [champion] if group != "C_lineage" else archive
    result = {
        "protocol": "lri-model-run-controller-v0.1",
        "group": group,
        "archive_policy": args.archive_policy if group == "C_lineage" else None,
        "prune_before_phase": args.prune_before_phase,
        "config_hash": digest(config),
        "training_bundle_hash": digest(training),
        "heldout_bundle_hash": digest(heldout),
        "phase_records": phase_records,
        "budget": budget.snapshot(),
        "candidates_generated_including_root": len(all_candidates),
        "final_active_candidates": len(final_active),
        "final_stored_candidate_bytes": sum(artifact_bytes(c) for c in final_active),
        "final_champion": champion["candidate_id"],
        "ancestry": [
            {
                "candidate_id": c["candidate_id"],
                "parent_id": c.get("parent_id"),
                "lineage_id": c["lineage_id"],
                "generation": c["generation"],
                "artifact_hash": c["artifact_hash"],
            }
            for c in all_candidates
        ],
        "evidence_note": "Controller/harness output alone is not evidence that LRI is superior. Use repeated model-backed runs and preregistered ablations.",
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    output = args.out_dir / f"{group}-{args.archive_policy if group == 'C_lineage' else 'main'}.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", choices=["A_fixed", "B_monolithic", "C_lineage"], required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--training", type=Path, required=True)
    parser.add_argument("--heldout", type=Path, required=True)
    parser.add_argument("--task-adapter", required=True)
    parser.add_argument("--mutation-adapter", required=True)
    parser.add_argument("--archive-policy", choices=["diversity", "score_only"], default="diversity")
    parser.add_argument("--prune-before-phase")
    parser.add_argument("--out-dir", type=Path, default=Path("results"))
    parser.add_argument("--timeout", type=float, default=60.0)
    args = parser.parse_args()

    result = run_group(args, load_json(args.config), load_json(args.training), load_json(args.heldout))
    print(json.dumps({
        "group": result["group"],
        "budget": result["budget"],
        "candidates": result["candidates_generated_including_root"],
        "final_active_candidates": result["final_active_candidates"],
        "result_file": str(args.out_dir),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
