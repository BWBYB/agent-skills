---
name: minimal-git-commit
description: Create atomic Git commits using Conventional Commits. Use when the user asks to generate or create a commit; use quick mode by default and full mode only when complete diff analysis is explicitly requested.
metadata:
  origin: personal
---

# Minimal Git Commit

## Goal

Create one or more atomic commits for the current agent task. Every generated commit message follows Conventional Commits. Keep ordinary submissions low-context; reserve complete diff analysis for an explicit full-mode request.

## Mode Selection

- Use **quick mode** by default.
- Use **full mode** only when the user says `full`, asks to scan or analyze the complete diff, or explicitly asks to check every change.
- Do not silently upgrade quick mode to full mode. If quick mode lacks enough information, ask for a change summary or ask the user to choose full mode.

## Quick Mode

Use the agent's explicit summary of the current task first. When needed, inspect only:

```bash
git status --short
git diff --stat
```

Do not read the complete diff or history. Do not guess about changes absent from the summary. Group the stated changes into atomic commits and generate their messages. If the user explicitly asks to commit, show the planned files/messages before mutating the index or creating commits when the file boundary is unclear.

## Full Mode

Read the complete relevant working-tree and staged diffs, inspect all changed files, and read [the Conventional Commits reference](references/conventional-commits.md). Check for omitted features, tests, docs, configuration, unrelated files, sensitive files, generated files, and independent logical changes. Confirm that generated files belong in version control: keep project-required outputs such as lockfiles or migrations, and exclude build artifacts and local outputs. Split independent features, bug fixes, refactors, and formatting-only changes into atomic commits; keep changes together when they are tightly coupled and cannot be independently tested or reverted. Run checks relevant to the changed files using existing project commands. Do not run the full test, lint, and type-check suite by default; reuse checks already run during the task and expand verification only when requested or needed by the changes. Do not inspect history unless explicitly requested.

Before `git add` or `git commit`, preserve user changes that are outside the current task. Execute those mutations only when the user explicitly asks to commit. Never push as part of this skill.

## Commit Rules

Use this shape:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

- Use `feat` for a new feature and `fix` for a bug fix.
- Prefer the project types `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, and `revert` when they accurately describe the change.
- Use a noun scope in parentheses only when it adds useful context.
- Mark breaking changes with `!` before the colon or an uppercase `BREAKING CHANGE:` footer.
- Keep the description concise, present-tense, imperative, and preferably under 72 characters.
- One commit represents one logical change. Split independent features, fixes, tests, docs, and refactors whenever possible.
- `fix` maps to SemVer PATCH, `feat` to MINOR, and any breaking change to MAJOR; do not change version files unless separately requested.

## Safety and Confirmation

- Never use `git add .` by default; add only files belonging to the current task.
- Never commit `.env`, credentials, tokens, private keys, or other secrets.
- In full mode, review staged content for secrets and confirm generated or build files are expected by the project before including them.
- Never modify Git configuration, skip hooks, force-push, or amend an existing commit unless the user explicitly requests that exact action.
- Do not mix pre-existing user changes with the agent's changes.
- Stop and ask when the task boundary, file ownership, logical split, or sensitive-file status is unclear.
- Creating a message is not permission to create a commit; require an explicit commit request before `git add` or `git commit`.

## Reference

Read [references/conventional-commits.md](references/conventional-commits.md) in full mode or when a type, footer, breaking change, revert, SemVer, or FAQ question needs detailed handling.
