#!/usr/bin/env python3
"""Build a standalone interactive HTML explorer from a model config JSON."""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def validate(config):
    if not isinstance(config, dict):
        raise ValueError("Top-level JSON value must be an object.")
    if not isinstance(config.get("title"), str) or not config["title"].strip():
        raise ValueError("Config must have a non-empty 'title'.")
    modules = config.get("modules")
    edges = config.get("edges")
    if not isinstance(modules, list) or not isinstance(edges, list):
        raise ValueError("Config must contain 'modules' and 'edges' arrays.")
    ids = set()
    for m in modules:
        if not isinstance(m, dict) or not m.get("id") or not m.get("title"):
            raise ValueError("Every module must be an object with 'id' and 'title'.")
        if m["id"] in ids:
            raise ValueError(f"Duplicate module id: {m['id']}")
        ids.add(m["id"])
        for coord in ("x", "y"):
            if not isinstance(m.get(coord), (int, float)):
                raise ValueError(f"Module {m['id']} needs numeric {coord}.")
        for arr in ("inputs", "outputs", "steps", "sourceFiles", "upstream", "downstream", "caveats"):
            if arr in m and not isinstance(m[arr], list):
                raise ValueError(f"Module {m['id']}: '{arr}' must be an array.")
        if "status" not in m:
            raise ValueError(f"Module {m['id']} needs an evidence 'status'.")
    for e in edges:
        if not isinstance(e, dict) or e.get("from") not in ids or e.get("to") not in ids:
            raise ValueError(f"Edge has unknown endpoint: {e}")
        if e.get("type", "data") not in ("data", "training"):
            raise ValueError(f"Edge type must be 'data' or 'training': {e}")
    # Validate referenced upstream/downstream ids where provided.
    for m in modules:
        for key in ("upstream", "downstream"):
            for ref in m.get(key, []):
                if ref not in ids:
                    raise ValueError(f"Module {m['id']} references unknown {key} id {ref}.")
    return True

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, help="Path to model configuration JSON")
    parser.add_argument("--output", required=True, help="Output HTML path")
    parser.add_argument("--template", default=str(ROOT / "templates" / "paper_network_explorer.html"),
                        help="Path to HTML template")
    args = parser.parse_args()
    config_path = Path(args.config).resolve()
    output_path = Path(args.output).resolve()
    template_path = Path(args.template).resolve()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    validate(config)
    template = template_path.read_text(encoding="utf-8")
    marker = "__MODEL_CONFIG_JSON__"
    if template.count(marker) != 1:
        raise ValueError(f"Template must contain exactly one {marker} marker.")
    # Escape HTML-significant '<' so arbitrary labels cannot terminate the script tag.
    config_js = json.dumps(config, ensure_ascii=False, separators=(",", ":")).replace("<", r"\u003c")
    html = template.replace(marker, config_js)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Built: {output_path}")
    print(f"Modules: {len(config['modules'])}; edges: {len(config['edges'])}")
    print("Validation passed. Browser interactions still need visual testing.")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
