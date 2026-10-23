---
name: personal-skill-builder
description: Create, review, refine, or update an Agent Skill when designing or maintaining its scope, trigger conditions, instructions, or supporting resources. Use for new skills and changes to existing skills; do not use for ordinary prompts, project documentation, or general agent configuration.
---

# Personal Skill Builder

Create small, discoverable skills that improve agent decisions for a specific, repeatable workflow.

## Scope

Use this skill for a new skill or a focused change to an existing skill. Preserve the user's requested location, invocation policy, and authorization boundaries. Do not create a skill merely to hold generic advice that the agent already knows.

## Workflow

1. Define the task boundary before writing files:
   - What repeatable outcome does the skill provide?
   - Which requests should activate it, and which similar requests should not?
   - What inputs, tools, side effects, and completion checks matter?
2. Inspect an existing skill before changing it. Keep useful resources and policies; do not reinitialize an existing directory.
3. Choose the smallest structure:
   - `SKILL.md` is required.
   - Add `references/` only for substantial, conditional material that changes decisions.
   - Add `scripts/` only for repeated or deterministic work where execution improves reliability.
   - Add `assets/` only for files used in generated output.
4. Write `SKILL.md`:
   - Frontmatter `name` must be lowercase hyphen-case, match the directory, and be at most 64 characters.
   - `description` must say both what the skill does and when it applies; include a boundary when it prevents misrouting.
   - Keep the body focused on outcomes, non-obvious rules, execution order, confirmation points, and completion checks.
   - Put conditional detail in a linked resource and state exactly when to read it.
5. Validate the result with the available skill validator when the environment provides one (locate `quick_validate.py` under the installed `skill-creator` skill):

   ```bash
   python3 <skill-creator>/scripts/quick_validate.py /path/to/skill
   ```

   If no validator is available, perform the equivalent frontmatter, naming, resource-link, placeholder, and script checks manually. Run added scripts when practical.

## Design Rules

- Treat the description as a routing condition, not a feature catalogue.
- Keep shared instructions short enough for routine loading; do not copy an entire external specification into the entrypoint.
- Prefer explicit scope and observable completion criteria over broad prohibitions or vague quality adjectives.
- Do not add README files, examples, templates, or resource directories without a concrete workflow that uses them.
- Preserve existing supported frontmatter and `agents/openai.yaml` fields when updating a skill.
- Keep automatic discovery enabled unless the user explicitly requests explicit-only invocation.

## References

Read the [Agent Skills specification](https://agentskills.io/specification) when portability, frontmatter fields, naming limits, or loading behavior is uncertain. Treat any user-provided or machine-local design guide as an optional preference source: read it only when the user explicitly requests those conventions or the task depends on them, and do not copy its full contents into the skill. Consult an installed `skill-creator` skill for initializer, UI metadata, or validation details instead of depending on a machine-specific absolute path.
