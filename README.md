# Shared Agent Skills

This repository is the canonical, agent-neutral source for reusable skills shared across Codex, Claude, and other compatible agents.

## Layout

- `skills/<skill-name>/SKILL.md` contains each portable skill.
- A skill may include `references/`, `scripts/`, or `assets/` when needed by its workflow.
- `platforms/` holds small platform-specific notes or adapters. Keep the canonical workflow in `SKILL.md` and avoid maintaining duplicate skill bodies.
- `scripts/validate-skills.py` checks skill names, required frontmatter, and local Markdown links.

## Adding a skill

Create `skills/<skill-name>/SKILL.md`. Use a lowercase hyphenated name matching the directory and include YAML frontmatter with `name` and `description`. The description should say what the skill does and when it applies. Put only portable workflow instructions in the canonical skill. Put platform-specific behavior in `platforms/<platform>/` when it cannot be expressed portably.

Run the validator from the repository root:

```sh
python3 scripts/validate-skills.py
```

## Using the skills

Codex can load a skill from its directory under `skills/`. For an agent that installs skills as account-level entries, install the `SKILL.md` content and make any referenced resources available in the expected local skill directory. An installation does not automatically synchronize later Git changes; re-import or update installed copies after changing the canonical source.

## Current skills

- `minimal-git-commit`: atomic Conventional Commits, with quick and full modes.
- `personal-skill-builder`: create, review, and maintain focused Agent Skills.
- `project-docs-maintainer`: maintain project documentation and audit drift.
