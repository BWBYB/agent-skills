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
- Keep the seven headings in English, write body text in the project's main language, cap detailed history at 2-3 phases, and cap `Next` at 3 items.
- Evidence numbers come from command output; pause or block entries include a file/decision and first action for resuming.
- A reusable framework/toolchain/environment root cause is proposed first and written to `AGENTS.md` only after authorization; keep at most 12 entries and do not silently delete one.
- A consequential choice with real alternatives is appended to `docs/decisions.md`; routine choices are not logged or backfilled.
- A full audit creates an ordered Fix Plan from confirmed findings only, with files, acceptance checks, and prerequisites; inferred gaps stay out.
- Create `llms.txt` only after verifying its path is deployed or served by a route; otherwise report the uncertainty and stop.
- A new task overwrites the status panel; it does not append a previous-task table.
- A code-complete but unverified phase remains `◐` without strikethrough; only accepted phases become `●` with strikethrough.
- A status panel has one H1, `Progress`/`Current`/`Last Updated` as its only H2 sections, no HTML tags, and `Last Updated` as the final line.
