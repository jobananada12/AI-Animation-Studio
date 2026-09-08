from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel, Field


class Scene(BaseModel):
    id: str
    title: str
    description: str = ""
    duration_seconds: float = 5.0


class AnimationProject(BaseModel):
    title: str = "Untitled Animation"
    logline: str = ""
    style: str = "2D cartoon"
    fps: int = 24
    scenes: list[Scene] = Field(default_factory=list)

    def create_directories(self, root: str | Path) -> None:
        root = Path(root)
        for directory in ("characters", "backgrounds", "scenes", "audio", "output"):
            (root / directory).mkdir(parents=True, exist_ok=True)
