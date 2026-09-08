from __future__ import annotations

import json
from typing import Any

from core.llm import OllamaClient


SYSTEM_PROMPT = """You are a professional animation screenwriter and storyboard planner.
Turn a short story idea into a production-ready JSON plan.
Return JSON only. Do not use markdown fences.

Schema:
{
  \"title\": string,
  \"logline\": string,
  \"characters\": [{\"id\": string, \"name\": string, \"description\": string}],
  \"scenes\": [{\"id\": string, \"title\": string, \"description\": string,
    \"duration_seconds\": number, \"location\": string,
    \"characters\": [string], \"dialogue\": [{\"character\": string, \"line\": string}],
    \"action\": string, \"camera\": string}]
}
Keep the plan practical for animation production. Give every scene a clear visual action and camera direction.
"""


class ScriptWriterAgent:
    name = "scriptwriter"

    def __init__(self, client: OllamaClient | None = None) -> None:
        self.client = client or OllamaClient()

    def run(self, idea: str) -> dict[str, Any]:
        if not idea.strip():
            raise ValueError("Story idea cannot be empty")

        prompt = f"Create a professional animation plan from this idea:\n\n{idea.strip()}"
        raw = self.client.generate(prompt, system=SYSTEM_PROMPT)

        try:
            result = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Ollama returned invalid JSON: {raw[:500]}") from exc

        if not isinstance(result, dict) or "scenes" not in result:
            raise ValueError("Script Agent returned an incomplete project plan")
        return result
