# Skill Behavior Scenarios

Use these short scenarios for manual or agent review after changing a skill. They describe expected routing and safety behavior; they are not an automated model evaluation.

## minimal-git-commit

- "Commit this change" -> use quick mode and create an atomic Conventional Commit.
- "Scan the complete diff before committing" -> use full mode.
- "Write a commit message, but do not commit" -> generate the message without mutating Git.
- Do not default to `git push`, `git add .`, `amend`, or force operations.

## personal-skill-builder

- "Change the trigger conditions of an existing skill" -> use this skill.
- "Update a project's README" -> do not use this skill unless the request is about designing or maintaining the skill itself.
- Read a local design guide only when the user explicitly requests its conventions or the task depends on them.

## project-docs-maintainer

- "Update the README" -> use the documentation maintenance path.
- "Stop at this version for now" -> use `Milestone Snapshot` and refresh the project status.
- "The work is blocked by a dependency" -> use `Milestone Snapshot` and record the blocker.
- "Try changing this one line first" -> do not update `status.md` for the intermediate step alone.
- A primarily code-focused task still refreshes status when it reaches completion, pause, block, or handoff.
- Before creating `docs/status.md`, add `/docs/status.md` to the project-root `.gitignore`.
- If `docs/status.md` is tracked, remove it from the index with `git rm --cached` and preserve the local file; never stage or commit it.
- Status-panel completion requires `git ls-files docs/status.md` to be empty, the local file to exist, and no Markdown links to it from README or `llms.txt`.
- Each worktree uses only its own ignored panel; cross-machine handoffs carry a concise progress summary in the handoff message.
- Keep `In Progress` to 1-3 completion conditions; group completed work by phase and append the short commit hash when available.
