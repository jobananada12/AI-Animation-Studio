# AI Animation Studio

AI-assisted production of original long-form YouTube stories.

## New direction

The project is being built around a narrated **30-minute YouTube episode**:

`Idea → Original Story → Chapter/Beat Plan → Image Prompts → Ukrainian Narration → Image Sequence → Music/SFX → Final MP4`

The goal is not to make a conventional frame-by-frame cartoon. It is a cinematic narrated story where AI-generated illustrations change according to the meaning of the narration, with subtle camera motion and transitions.

## Episode targets

- approximately 30 minutes;
- approximately 3,900–4,500 Ukrainian narration words;
- strong hook in the first 30 seconds;
- three-act narrative with escalation and payoff;
- visual beats around 8–15 seconds;
- original plot and characters for every episode;
- stable visual descriptions for recurring characters;
- image prompts tied to the exact narration beat;
- one narrator voice, using the existing FilmDubUA TTS implementation through an adapter.

## Architecture

- `app/` — application/CLI
- `core/` — project model, LLM and production rules
- `agents/` — story and media-planning agents
- `providers/` — TTS and future image-generation providers
- `projects/` — episode projects
- `output/` — rendered videos

## FilmDubUA integration

`providers/filmdubua_tts.py` loads the existing TTS implementation from a local FilmDubUA checkout. Set `FILMDUBUA_ROOT` to that directory. Credentials and tokens are intentionally not copied into this repository.

## Pipeline roadmap

1. Long-form Story Agent
2. Story quality/repetition checker
3. Character bible
4. Visual Beat / Storyboard Agent
5. Image Generator Provider
6. FilmDubUA narration provider
7. Music/SFX planner
8. FFmpeg editor and Ken Burns-style motion
9. Final 16:9 YouTube render
10. Thumbnail and title generator
