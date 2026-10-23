# Shared Agent Skills

This repository is the canonical, agent-neutral source for reusable skills shared across Codex, Claude, and other compatible agents.

The files under `skills/` are the source of truth. Installed copies in Codex, Claude, Qoder, or another agent account are local copies and do not update automatically after a Git change.

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

## Updating and contributing

Use this flow for changes:

1. Edit the canonical file under `skills/<skill-name>/`.
2. Run `python3 scripts/validate-skills.py` and `git diff --check`.
3. Create an atomic Conventional Commit.
4. Push the branch and open a Pull Request when collaboration or review is needed.
5. After the change is merged, manually re-import or copy the skill into each agent's local skill directory.

GitHub changes do not synchronize installed copies. This repository intentionally does not provide an automatic installer or sync script; platform-specific installation rules belong in `platforms/`.

## Using the skills

Codex can load a skill from its directory under `skills/`. For an agent that installs skills as account-level entries, install the `SKILL.md` content and make any referenced resources available in the expected local skill directory. Claude and other compatible agents may use different installation paths or discovery rules; verify those rules before importing. Qoder is treated as a potentially compatible platform here, but no platform-specific path or metadata is assumed until confirmed.

The repository remains platform-neutral: keep portable workflow instructions in `SKILL.md` and document genuine platform differences in `platforms/<platform>/` without duplicating the skill body.

## Current skills

- `minimal-git-commit`: atomic Conventional Commits, with quick and full modes.
- `personal-skill-builder`: create, review, and maintain focused Agent Skills.
- `project-docs-maintainer`: maintain project documentation and audit drift.

Behavior scenarios for manual review are kept in [`tests/skill-scenarios.md`](tests/skill-scenarios.md). They are intentionally lightweight and do not simulate model routing.
