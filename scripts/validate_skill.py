#!/usr/bin/env python3
"""Dependency-free static checker for this Skill package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

skill_path = ROOT / "SKILL.md"
if not skill_path.is_file():
    errors.append("Missing SKILL.md")
    skill_text = ""
else:
    skill_text = skill_path.read_text(encoding="utf-8")

if not skill_text.startswith("---\n"):
    errors.append("SKILL.md must start with YAML front matter ('---').")
else:
    parts = skill_text.split("---", 2)
    if len(parts) < 3:
        errors.append("Could not parse SKILL.md front matter.")
    else:
        front = parts[1]
        if not re.search(r"(?m)^name:\s*[a-z0-9-]+\s*$", front):
            errors.append("Front matter must contain a lowercase hyphenated name.")
        if not re.search(r"(?m)^description:\s*\S", front):
            errors.append("Front matter must contain a non-empty description.")

required_files = [
    "README.md", "agents/openai.yaml",
    "references/source-reading.md", "references/tensor-tracing.md",
    "references/training-inference.md", "references/model-adaptation.md",
    "references/output-templates.md", "evals/test-cases.md",
    "scripts/validate_skill.py",
]
for rel in required_files:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

for ref in re.findall(r"`(references/[^`]+\.md)`", skill_text):
    if not (ROOT / ref).is_file():
        errors.append(f"SKILL.md references missing file: {ref}")

if errors:
    print("FAIL")
    for item in errors:
        print(f" - {item}")
    sys.exit(1)

print("PASS: Skill package structure and front matter look valid.")
print(f"Checked: {ROOT}")
