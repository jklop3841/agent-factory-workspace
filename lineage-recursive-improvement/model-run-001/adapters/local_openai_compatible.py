#!/usr/bin/env python3
"""Local/OpenAI-compatible model adapter for LRI Model Run 001.

Default endpoint targets an OpenAI-compatible local server such as Ollama,
LM Studio, vLLM, llama.cpp server, or another explicitly configured endpoint.
No vendor SDK is required. Python standard library only.

Environment variables:
  LRI_OPENAI_BASE_URL   default http://127.0.0.1:11434/v1/chat/completions
  LRI_MODEL             required, e.g. a local served model ID
  LRI_API_KEY           optional; never print it
  LRI_TEMPERATURE       default 0.2
  LRI_TOP_P             default 1.0
  LRI_TIMEOUT_SECONDS   default 120
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Any


def extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        value = json.loads(text)
        if isinstance(value, dict):
            return value
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        value = json.loads(text[start : end + 1])
        if isinstance(value, dict):
            return value
    raise ValueError("model response did not contain one JSON object")


def call_model(messages: list[dict[str, str]]) -> tuple[dict[str, Any], dict[str, Any]]:
    endpoint = os.environ.get("LRI_OPENAI_BASE_URL", "http://127.0.0.1:11434/v1/chat/completions")
    model = os.environ.get("LRI_MODEL")
    if not model:
        raise RuntimeError("LRI_MODEL is required")
    payload = {
        "model": model,
        "messages": messages,
        "temperature": float(os.environ.get("LRI_TEMPERATURE", "0.2")),
        "top_p": float(os.environ.get("LRI_TOP_P", "1.0")),
        "response_format": {"type": "json_object"},
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    api_key = os.environ.get("LRI_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    request = urllib.request.Request(endpoint, data=body, headers=headers, method="POST")
    timeout = float(os.environ.get("LRI_TIMEOUT_SECONDS", "120"))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"model endpoint HTTP {exc.code}: {detail[:1000]}") from exc
    choices = raw.get("choices") or []
    if not choices:
        raise RuntimeError("model endpoint returned no choices")
    content = choices[0].get("message", {}).get("content", "")
    parsed = extract_json(str(content))
    usage_raw = raw.get("usage") or {}
    usage = {
        "input_tokens": usage_raw.get("prompt_tokens"),
        "output_tokens": usage_raw.get("completion_tokens"),
        "model_calls": 1,
    }
    meta = {
        "provider_request_id": raw.get("id"),
        "model": raw.get("model", model),
        "usage": usage,
    }
    return parsed, meta


def task_messages(request: dict[str, Any]) -> list[dict[str, str]]:
    candidate = request["candidate"]
    task = request["task"]
    system = candidate.get("system_prompt") or "You are a tool-planning agent."
    notes = candidate.get("planning_notes", "")
    user = {
        "objective": "Return a valid plan of tool IDs that reaches target from start within max_steps. Prefer lower declared total tool cost when multiple valid plans exist.",
        "planning_notes": notes,
        "task": task,
        "output_contract": {"plan": ["tool_id", "..."]},
        "rules": [
            "Use only tool IDs currently present in task.tools.",
            "Reason from the current tool op/arg/cost fields; do not assume names from earlier tasks.",
            "Return JSON only.",
        ],
    }
    return [
        {"role": "system", "content": str(system)},
        {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
    ]


def batch_task_messages(request: dict[str, Any]) -> list[dict[str, str]]:
    candidate = request["candidate"]
    tasks = request.get("tasks", [])
    system = candidate.get("system_prompt") or "You are a tool-planning agent."
    notes = candidate.get("planning_notes", "")
    user = {
        "objective": "Solve every supplied task independently. For each task ID return a plan of currently available tool IDs that reaches its target within max_steps. Prefer lower declared total tool cost among valid plans.",
        "planning_notes": notes,
        "tasks": tasks,
        "output_contract": {
            "plans": {
                "task_id": ["tool_id", "..."]
            }
        },
        "rules": [
            "Return exactly one entry for every supplied task ID.",
            "Use only tool IDs present in that task's own tools list.",
            "Do not assume a tool identifier or meaning from another task or earlier phase.",
            "Treat tasks independently even though they share one batch request.",
            "Return JSON only.",
        ],
    }
    return [
        {"role": "system", "content": str(system)},
        {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
    ]


def mutation_messages(request: dict[str, Any]) -> list[dict[str, str]]:
    parent = request["parent"]
    user = {
        "objective": "Propose one bounded successor configuration that could improve adaptation to the observed training feedback without seeing hidden answers or future shocks.",
        "parent": parent,
        "available_feedback": request.get("available_feedback", {}),
        "mutation_slot": request.get("mutation_slot"),
        "limits": {
            "editable_fields": request.get("editable_fields"),
            "max_system_prompt_chars": request.get("max_system_prompt_chars"),
            "max_planning_notes_chars": request.get("max_planning_notes_chars"),
        },
        "output_contract": {
            "system_prompt": "string",
            "planning_notes": "string",
            "mutation_reason": "string",
        },
        "rules": [
            "Do not request hidden evaluator answers, oracle plans, credentials, external persistence, or permission changes.",
            "Keep the successor general enough to handle changed tool identifiers and semantics.",
            "Return JSON only.",
        ],
    }
    return [
        {
            "role": "system",
            "content": "You are a bounded configuration mutator for a controlled agent-adaptation experiment. You edit only the provided prompt/config text.",
        },
        {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
    ]


def task_output(parsed: dict[str, Any], meta: dict[str, Any]) -> dict[str, Any]:
    return {
        "plan": parsed.get("plan", []),
        "usage": meta["usage"],
        "provider_request_id": meta.get("provider_request_id"),
        "model": meta.get("model"),
    }


def batch_task_output(parsed: dict[str, Any], meta: dict[str, Any]) -> dict[str, Any]:
    plans = parsed.get("plans", {})
    if not isinstance(plans, dict):
        plans = {}
    return {
        "plans": plans,
        "usage": meta["usage"],
        "provider_request_id": meta.get("provider_request_id"),
        "model": meta.get("model"),
    }


def main() -> None:
    request = json.loads(sys.stdin.read())
    protocol = request.get("protocol")
    if protocol == "lri-model-agent-v0.1":
        parsed, meta = call_model(task_messages(request))
        output = task_output(parsed, meta)
    elif protocol == "lri-model-agent-batch-v0.1":
        parsed, meta = call_model(batch_task_messages(request))
        output = batch_task_output(parsed, meta)
    elif protocol == "lri-mutation-v0.1":
        parsed, meta = call_model(mutation_messages(request))
        output = {
            "system_prompt": str(parsed.get("system_prompt", request["parent"].get("system_prompt", ""))),
            "planning_notes": str(parsed.get("planning_notes", request["parent"].get("planning_notes", ""))),
            "mutation_reason": str(parsed.get("mutation_reason", "")),
            "usage": meta["usage"],
            "provider_request_id": meta.get("provider_request_id"),
            "model": meta.get("model"),
        }
    else:
        raise SystemExit(f"unsupported protocol: {protocol}")
    sys.stdout.write(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
