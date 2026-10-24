#!/usr/bin/env python3
"""Dependency-free structural checker for the V2 Skill package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
required = [
    "SKILL.md", "README.md", "agents/openai.yaml",
    "references/source-reading.md", "references/tensor-tracing.md",
    "references/training-inference.md", "references/paper-analysis.md",
    "references/experiment-analysis.md", "references/output-templates.md",
    "domains/object-detection.md", "domains/llm-transformer.md",
    "domains/diffusion-models.md", "domains/retrieval-rag.md",
    "domains/multimodal-learning.md",
    "references/model-config-schema.md",
    "templates/paper_network_explorer.html",
    "examples/model-config.example.json", "examples/paper_network_explorer-demo.html",
    "evals/general-tests.md", "evals/detection-tests.md",
    "evals/llm-tests.md", "evals/interactive-architecture-tests.md",
    "scripts/validate_skill.py", "scripts/build_explorer.py",
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md must start with YAML front matter.")
else:
    parts = skill.split("---", 2)
    if len(parts) < 3:
        errors.append("Could not parse front matter.")
    else:
        front = parts[1]
        if not re.search(r"(?m)^name:\s*[a-z0-9-]+\s*$", front):
            errors.append("Missing/invalid name field.")
        if not re.search(r"(?m)^description:\s*\S", front):
            errors.append("Missing description field.")

for ref in re.findall(r"`((?:references|domains|templates|scripts)/[^`]+\.(?:md|html|py))`", skill):
    if not (ROOT / ref).is_file():
        errors.append(f"SKILL.md references missing file: {ref}")

if errors:
    print("FAIL")
    for err in errors:
        print(" - " + err)
    sys.exit(1)

print("PASS: Skill package structure, front matter, and referenced files look valid.")
print(f"Checked: {ROOT}")

