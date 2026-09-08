from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    name: str = "agent"

    @abstractmethod
    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Process a pipeline payload and return structured output."""
        raise NotImplementedError
