from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Stage(str, Enum):
    SCRIPT = "script"
    STORYBOARD = "storyboard"
    ANIMATIC = "animatic"
    CHARACTERS = "characters"
    ANIMATION = "animation"
    LIP_SYNC = "lip_sync"
    COMPOSITING = "compositing"
    SOUND = "sound"
    RENDER = "render"


@dataclass
class PipelineResult:
    stage: Stage
    success: bool
    message: str


class AnimationPipeline:
    """Orchestrates production stages. Real AI workers will be plugged in later."""

    def __init__(self) -> None:
        self.stages = list(Stage)

    def plan(self) -> list[Stage]:
        return self.stages.copy()

    def run_stage(self, stage: Stage) -> PipelineResult:
        return PipelineResult(
            stage=stage,
            success=True,
            message=f"Stage '{stage.value}' is ready for an agent implementation.",
        )
