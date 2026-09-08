# AI Animation Studio

AI-assisted animation production pipeline.

## Vision

Turn a story idea into a structured animation project through a professional-style pipeline:

`Idea → Script → Storyboard → Animatic → Characters → Animation → Lip Sync → Compositing → Sound → Final Render`

## Project status

🚧 Early development — foundation stage.

## Architecture

- `app/` — desktop/user interface
- `core/` — project model and pipeline orchestration
- `agents/` — specialized AI production agents
- `media/` — generated and source media
- `projects/` — animation projects
- `output/` — rendered results
- `tests/` — automated tests

## Planned agents

- Script Agent
- Storyboard Agent
- Character Agent
- Animation Agent
- Audio Agent
- Render Agent

## Local-first direction

The project is designed to support local AI models and tools where practical, including FFmpeg and local LLM/TTS/image-generation components.
