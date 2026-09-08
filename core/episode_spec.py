from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EpisodeSpec:
    """Production targets for a narrated 30-minute YouTube episode."""

    target_minutes: int = 30
    words_per_minute: int = 140
    beat_min_seconds: int = 8
    beat_max_seconds: int = 15

    @property
    def target_words(self) -> int:
        return self.target_minutes * self.words_per_minute

    @property
    def approximate_visual_beats(self) -> tuple[int, int]:
        seconds = self.target_minutes * 60
        return seconds // self.beat_max_seconds, seconds // self.beat_min_seconds
