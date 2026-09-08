from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class OllamaConfig:
    base_url: str = "http://127.0.0.1:11434"
    model: str = "qwen2.5:7b"
    timeout: int = 300


class OllamaClient:
    """Small provider wrapper so the rest of the pipeline is model-agnostic."""

    def __init__(self, config: OllamaConfig | None = None) -> None:
        self.config = config or OllamaConfig()

    def generate(self, prompt: str, system: str | None = None) -> str:
        payload: dict[str, Any] = {
            "model": self.config.model,
            "prompt": prompt,
            "stream": False,
        }
        if system:
            payload["system"] = system

        response = requests.post(
            f"{self.config.base_url.rstrip('/')}/api/generate",
            json=payload,
            timeout=self.config.timeout,
        )
        response.raise_for_status()
        return str(response.json().get("response", "")).strip()
