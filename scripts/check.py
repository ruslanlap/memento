#!/usr/bin/env python3
"""Validate package metadata and local links, not agent behavior."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import yaml


ROOT = Path(__file__).resolve().parent.parent


def validate_skill(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("SKILL.md needs delimited YAML frontmatter")
    metadata = yaml.safe_load(match[1])
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    name = metadata.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise ValueError("invalid skill name")
    description = metadata.get("description")
    if not isinstance(description, str) or not 0 < len(description.strip()) <= 1024:
        raise ValueError("invalid skill description")
    return metadata


def main():
    metadata = validate_skill((ROOT / "SKILL.md").read_text(encoding="utf-8"))
    if metadata["name"] != "memento":
        raise ValueError("package name must be memento")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        targets = re.findall(r"\]\(([^\s)]+)\)", text) + re.findall(r'src="([^"]+)"', text)
        for target in targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            if not (path.parent / unquote(url.path)).exists():
                raise ValueError(f"{path.relative_to(ROOT)}: missing target {target}")
    print("Package metadata and local links valid; behavioral quality is evaluated separately.")


if __name__ == "__main__":
    main()
