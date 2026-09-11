#!/usr/bin/env python3
"""Freeze a deterministic hidden Tool Interface Drift task bundle.

The generator is public; the seed may remain private until the run is complete.
It writes training tasks, held-out tasks, and a hash manifest. Hidden-task files
should stay uncommitted until the experiment is intentionally revealed.

No network access. Python standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import math
import random
from pathlib import Path
from typing import Any

VALUE_BOUND = 200
DEFAULT_MAX_STEPS = 6


def stable_json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(stable_json_bytes(value)).hexdigest()


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
    raise ValueError(f"unsupported op: {op}")


def oracle_plan(task: dict[str, Any]) -> tuple[list[str] | None, int | None]:
    tools = {item["id"]: item for item in task["tools"]}
    queue: list[tuple[int, int, int, list[str]]] = [(0, 0, task["start"], [])]
    seen: dict[tuple[int, int], int] = {}
    while queue:
        cost, steps, value, plan = heapq.heappop(queue)
        state = (value, steps)
        if seen.get(state, math.inf) <= cost:
            continue
        seen[state] = cost
        if value == task["target"]:
            return plan, cost
        if steps >= task["max_steps"]:
            continue
        for tool_id, tool in tools.items():
            nxt = apply_tool(value, tool)
            if nxt is None or abs(nxt) > VALUE_BOUND:
                continue
            heapq.heappush(queue, (cost + int(tool["cost"]), steps + 1, nxt, plan + [tool_id]))
    return None, None


def random_tool_id(rng: random.Random, used: set[str]) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        token = "t_" + "".join(rng.choice(alphabet) for _ in range(6))
        if token not in used:
            used.add(token)
            return token


def make_tools(rng: random.Random, spec: list[tuple[str, int | None, int]]) -> list[dict[str, Any]]:
    used: set[str] = set()
    result = []
    for op, arg, cost in spec:
        result.append({"id": random_tool_id(rng, used), "op": op, "arg": arg, "cost": cost})
    return result


def phase_templates(rng: random.Random) -> list[dict[str, Any]]:
    shocks = [
        {
            "kind": "remove_multiplier",
            "description": "A previously useful multiplier is removed and a different multiplier appears.",
            "spec": [("add", 1, 1), ("add", -1, 1), ("mul", 3, 2), ("div_exact", 2, 1)],
        },
        {
            "kind": "semantic_rename_negate",
            "description": "Tool identifiers and useful semantics shift; sign inversion becomes useful.",
            "spec": [("add", 2, 1), ("add", -2, 1), ("mul", 2, 2), ("neg", None, 1)],
        },
        {
            "kind": "cost_shift",
            "description": "Semantics remain simple but the cheapest route changes materially.",
            "spec": [("add", 1, 3), ("add", 5, 1), ("neg", None, 1), ("div_exact", 2, 2)],
        },
    ]
    rng.shuffle(shocks)
    stable = {
        "kind": "stable",
        "description": "Initial tool interface before any shock.",
        "spec": [("add", 1, 1), ("add", -1, 1), ("mul", 2, 1), ("div_exact", 2, 1)],
    }
    return [stable, *shocks]


def synthesize_task(
    rng: random.Random,
    phase_id: str,
    description: str,
    tools: list[dict[str, Any]],
    task_id: str,
    max_steps: int,
) -> dict[str, Any]:
    for _ in range(500):
        start = rng.randint(-12, 12)
        value = start
        intended: list[str] = []
        steps = rng.randint(2, max_steps)
        for _ in range(steps):
            viable = []
            for tool in tools:
                nxt = apply_tool(value, tool)
                if nxt is not None and abs(nxt) <= VALUE_BOUND:
                    viable.append((tool, nxt))
            if not viable:
                break
            tool, value = rng.choice(viable)
            intended.append(tool["id"])
        if not intended or value == start:
            continue
        task = {
            "id": task_id,
            "phase": phase_id,
            "phase_description": description,
            "start": start,
            "target": value,
            "tools": tools,
            "max_steps": max_steps,
        }
        plan, cost = oracle_plan(task)
        if plan is None:
            continue
        task["_oracle_plan"] = plan
        task["_oracle_cost"] = cost
        return task
    raise RuntimeError(f"could not synthesize solvable task {task_id}")


def generate_split(
    rng: random.Random,
    phase_defs: list[dict[str, Any]],
    tasks_per_phase: int,
    split_name: str,
    max_steps: int,
) -> dict[str, Any]:
    phases = []
    for phase_index, phase in enumerate(phase_defs):
        phase_id = f"p{phase_index}_{phase['kind']}"
        tasks = [
            synthesize_task(
                rng,
                phase_id,
                phase["description"],
                phase["tools"],
                f"{split_name}-{phase_id}-{i:03d}",
                max_steps,
            )
            for i in range(tasks_per_phase)
        ]
        phases.append(
            {
                "id": phase_id,
                "kind": phase["kind"],
                "description": phase["description"],
                "tools": phase["tools"],
                "tasks": tasks,
            }
        )
    return {"protocol": "lri-hidden-tool-drift-v0.1", "split": split_name, "phases": phases}


def strip_oracles(bundle: dict[str, Any]) -> dict[str, Any]:
    public = json.loads(json.dumps(bundle))
    for phase in public["phases"]:
        for task in phase["tasks"]:
            task.pop("_oracle_plan", None)
            task.pop("_oracle_cost", None)
    return public


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", required=True, help="Keep private for a real preregistered run until reveal.")
    parser.add_argument("--out", type=Path, default=Path("hidden"))
    parser.add_argument("--training-per-phase", type=int, default=8)
    parser.add_argument("--heldout-per-phase", type=int, default=12)
    parser.add_argument("--max-steps", type=int, default=DEFAULT_MAX_STEPS)
    parser.add_argument("--publish-seed", action="store_true")
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    seed_material = args.seed.encode("utf-8")
    seed_int = int.from_bytes(hashlib.sha256(seed_material).digest()[:8], "big")
    phase_rng = random.Random(seed_int ^ 0xA17E)
    training_rng = random.Random(seed_int ^ 0xB011)
    heldout_rng = random.Random(seed_int ^ 0xC0DE)

    templates = phase_templates(phase_rng)
    phase_defs = []
    for template in templates:
        phase_defs.append(
            {
                "kind": template["kind"],
                "description": template["description"],
                "tools": make_tools(phase_rng, template["spec"]),
            }
        )

    training = generate_split(training_rng, phase_defs, args.training_per_phase, "training", args.max_steps)
    heldout = generate_split(heldout_rng, phase_defs, args.heldout_per_phase, "heldout", args.max_steps)

    write_json(args.out / "training_with_oracle.json", training)
    write_json(args.out / "heldout_with_oracle.json", heldout)
    write_json(args.out / "training_for_agent.json", strip_oracles(training))
    write_json(args.out / "heldout_for_agent.json", strip_oracles(heldout))

    schedule = [{"id": p["id"], "kind": p["kind"], "tools": p["tools"]} for p in training["phases"]]
    manifest = {
        "protocol": "lri-task-freeze-v0.1",
        "generator": "freeze_tasks.py",
        "seed_commitment_sha256": hashlib.sha256(seed_material).hexdigest(),
        "seed_revealed": bool(args.publish_seed),
        "seed": args.seed if args.publish_seed else None,
        "training_tasks_per_phase": args.training_per_phase,
        "heldout_tasks_per_phase": args.heldout_per_phase,
        "max_steps": args.max_steps,
        "shock_schedule_sha256": sha256_json(schedule),
        "training_bundle_sha256": sha256_json(training),
        "heldout_bundle_sha256": sha256_json(heldout),
        "training_agent_view_sha256": sha256_json(strip_oracles(training)),
        "heldout_agent_view_sha256": sha256_json(strip_oracles(heldout)),
        "notes": "Freeze this manifest before evolution. Do not expose heldout oracle data or the private seed to mutation agents.",
    }
    write_json(args.out / "FREEZE_MANIFEST.json", manifest)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
