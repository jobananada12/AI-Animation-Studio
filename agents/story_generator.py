from __future__ import annotations

import json
from typing import Any

from core.llm import OllamaClient


SYSTEM_PROMPT = """You are a senior YouTube documentary/story writer and showrunner.
Create original, emotionally engaging long-form narrated stories for a YouTube channel.
The target is approximately 30 minutes of narration, not a short cartoon.

Rules:
- Write an ORIGINAL story; never copy or paraphrase a known video.
- Build a strong hook in the first 30 seconds.
- Use a clear three-act structure with escalating stakes, discoveries and a satisfying ending.
- Vary sentence rhythm and scene types. Avoid repetitive AI-sounding phrases.
- Include concrete visual details so every paragraph can be illustrated.
- The narration should work with one narrator voice.
- Target 3,900-4,500 Ukrainian words for a 30-minute episode.
- Divide the episode into visual beats of roughly 8-15 seconds each.
- Each visual beat gets an image prompt that matches the exact narration meaning.
- Keep recurring characters visually consistent by giving them stable character descriptions.
- Do not make every image a new location; reuse locations when appropriate and vary framing/camera.
- Prompts must describe original characters and scenes, not celebrities or copyrighted characters.

Return JSON only, with this shape:
{
  "title": string,
  "hook": string,
  "logline": string,
  "genre": string,
  "estimated_minutes": 30,
  "characters": [{"id": string, "name": string, "visual_identity": string}],
  "chapters": [{
    "id": string,
    "title": string,
    "narration": string,
    "visual_beats": [{
      "id": string,
      "duration_seconds": number,
      "narration": string,
      "image_prompt": string,
      "motion": string
    }]
  }]
}
"""


class LongFormStoryAgent:
    name = "long_form_story"

    def __init__(self, client: OllamaClient | None = None) -> None:
        self.client = client or OllamaClient()

    def run(self, idea: str, genre: str = "mystery adventure") -> dict[str, Any]:
        if not idea.strip():
            raise ValueError("Story idea cannot be empty")

        prompt = (
            "Create a new 30-minute Ukrainian YouTube story.\n"
            f"Genre: {genre}.\n"
            f"Seed idea: {idea.strip()}\n\n"
            "Make the plot substantially different from previous stories and avoid predictable filler."
        )
        raw = self.client.generate(prompt, system=SYSTEM_PROMPT)
        try:
            result = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Story Agent returned invalid JSON: {raw[:500]}") from exc

        if not isinstance(result, dict) or not result.get("chapters"):
            raise ValueError("Story Agent returned an incomplete episode")
        return result
