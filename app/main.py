from __future__ import annotations

import argparse
import json

from agents.scriptwriter import ScriptWriterAgent
from core.llm import OllamaClient, OllamaConfig


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Animation Studio")
    parser.add_argument("idea", help="Story idea to turn into a production plan")
    parser.add_argument("--model", default="qwen2.5:7b", help="Ollama model name")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    args = parser.parse_args()

    client = OllamaClient(OllamaConfig(base_url=args.ollama_url, model=args.model))
    project = ScriptWriterAgent(client).run(args.idea)
    print(json.dumps(project, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
