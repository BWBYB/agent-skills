#!/usr/bin/env python3
"""Validate shared skill directories and local Markdown links."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
errors: list[str] = []

if not SKILLS.is_dir():
    print(f"Missing skills directory: {SKILLS}", file=sys.stderr)
    sys.exit(1)

for skill_dir in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
    skill_file = skill_dir / "SKILL.md"
    if not NAME_RE.fullmatch(skill_dir.name) or len(skill_dir.name) > 64:
        errors.append(f"{skill_dir}: directory name must be lowercase hyphen-case (max 64 chars)")
    if not skill_file.is_file():
        errors.append(f"{skill_dir}: missing SKILL.md")
        continue

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{skill_file}: missing YAML frontmatter")
        continue
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{skill_file}: unterminated YAML frontmatter")
        continue

    frontmatter = text[4:end]
    name = re.search(r"(?m)^name:\s*['\"]?([^\s'\"]+)['\"]?\s*$", frontmatter)
    description = re.search(r"(?m)^description:\s*(\S.*)$", frontmatter)
    if not name:
        errors.append(f"{skill_file}: frontmatter requires name")
    elif name.group(1) != skill_dir.name:
        errors.append(f"{skill_file}: name does not match directory {skill_dir.name!r}")
    if not description:
        errors.append(f"{skill_file}: frontmatter requires a non-empty description")

    for target in LINK_RE.findall(text):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        local_target = target.split("#", 1)[0].split("?", 1)[0]
        if local_target and not (skill_dir / local_target).exists():
            errors.append(f"{skill_file}: missing local link target {local_target!r}")

if errors:
    print("Skill validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print("All shared skills passed validation.")
