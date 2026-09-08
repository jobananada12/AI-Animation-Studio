from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


class FilmDubUATTS:
    """Adapter for the TTS implementation already used by FilmDubUA.

    The FilmDubUA repository remains the source of the voice implementation.
    No credentials or tokens are copied into this project.
    """

    def __init__(self, filmdubua_root: str | None = None) -> None:
        root = Path(filmdubua_root or os.getenv("FILMDUBUA_ROOT", "")).expanduser()
        if not root:
            raise RuntimeError("Set FILMDUBUA_ROOT to the local FilmDubUA directory")
        self.root = root.resolve()
        self.tts_path = self.root / "core" / "tts.py"
        if not self.tts_path.exists():
            raise FileNotFoundError(f"FilmDubUA TTS module not found: {self.tts_path}")

        spec = importlib.util.spec_from_file_location("filmdubua_tts", self.tts_path)
        if spec is None or spec.loader is None:
            raise ImportError("Could not load FilmDubUA TTS module")
        module = importlib.util.module_from_spec(spec)
        sys.modules["filmdubua_tts"] = module
        spec.loader.exec_module(module)
        self._module = module

    def synthesize(
        self,
        text: str,
        output_wav: str,
        profile: str = "neutral",
        rate: int = 170,
        volume: float = 1.0,
    ) -> str:
        return self._module.synthesize_ukrainian(
            text=text,
            output_wav=output_wav,
            rate=rate,
            volume=volume,
            profile=profile,
        )
