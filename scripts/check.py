#!/usr/bin/env python3
"""Zero-dependency repository check."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
EXAMPLE = ROOT / "examples" / "MEMENTO.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"error: {message}")


skill = SKILL.read_text(encoding="utf-8")
parts = skill.split("---", 2)
require(len(parts) == 3 and not parts[0].strip(), "SKILL.md needs YAML frontmatter")

metadata = {}
for line in parts[1].strip().splitlines():
    if ":" in line:
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

require(metadata.get("name") == "memento", "skill name must be memento")
require(bool(re.fullmatch(r"[a-z0-9-]{1,64}", metadata["name"])), "invalid skill name")
require(0 < len(metadata.get("description", "")) <= 1024, "invalid description")

headings = ("Case", "Tattoos", "Polaroids", "Loose Notes", "Crossed-out Notes", "Next Scene")
for heading in headings:
    require(f"## {heading}" in skill, f"SKILL.md is missing {heading}")

example = EXAMPLE.read_text(encoding="utf-8")
for heading in headings:
    require(f"## {heading}" in example, f"example is missing {heading}")

require("Evidence:" in example, "example needs reproducible evidence")
require("Invalidated by:" in example, "example needs a corrected false claim")
print("memento: valid")
