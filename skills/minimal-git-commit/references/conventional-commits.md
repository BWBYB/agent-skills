# Conventional Commits 1.0.0 Reference

Sources:

- https://www.conventionalcommits.org/en/v1.0.0/
- https://www.conventionalcommits.org/zh-hans/v1.0.0/
- https://semver.org/lang/zh-CN/

## Format

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Every commit has a type, followed by an optional scope, optional `!`, and the required colon plus space. The description follows immediately. Body and footers are optional and each begins after a blank line.

## Normative Rules

- `feat` MUST describe a new feature.
- `fix` MUST describe a bug fix.
- A scope MAY be used; it is a noun in parentheses describing a code area, for example `fix(parser):`.
- The body MAY contain free-form paragraphs.
- Each footer uses a token followed by `: ` or ` #` and a value. Footer tokens normally use hyphens instead of spaces.
- A breaking change MUST be marked with `!` in the prefix or an uppercase `BREAKING CHANGE:` footer.
- `!` goes immediately before the colon. Its footer may be omitted when the description explains the breaking change.
- Types other than `feat` and `fix` are allowed; the specification does not mandate a complete type list.
- Parsers should treat the structural elements case-insensitively, except `BREAKING CHANGE`, which is uppercase. `BREAKING-CHANGE` is synonymous when used as a footer token.

## Recommended Types For This Skill

```text
feat      new feature
fix       bug fix
docs      documentation
style     formatting without behavior change
refactor  restructuring without behavior change
perf      performance improvement
test      tests
build     build system or dependencies
ci        continuous integration
chore     maintenance
revert    revert a change
```

These are a project convention, not an exhaustive list required by the specification.

## Examples

```text
feat(lang): add Polish language
fix: prevent racing of requests
docs: correct spelling of CHANGELOG
feat(api)!: remove the legacy endpoint
```

```text
feat: change configuration inheritance

BREAKING CHANGE: the `extends` key now replaces the previous config behavior
```

Footers can use trailer-style references:

```text
fix: prevent racing of requests

Reviewed-by: Z
Refs: #123
```

## Atomic Commits

The specification FAQ recommends multiple commits when a change fits more than one type. Split independent features, fixes, tests, docs, and refactors whenever possible. Keep related changes together when they cannot be independently reverted or tested without breaking the feature.

## SemVer Mapping

```text
fix                         PATCH
feat                        MINOR
BREAKING CHANGE, any type   MAJOR
```

Other types have no implicit SemVer effect unless they include a breaking change. This skill does not change version files automatically.

## FAQ

### How should initial development commits be written?

Use the convention from the beginning, as if the product were already released. A structured history remains useful during initial development.

### Should types be uppercase or lowercase?

Either is allowed by the specification, but this skill consistently emits lowercase types.

### What if a commit fits multiple types?

Create multiple atomic commits whenever possible. If changes cannot be separated safely, use the dominant type and explain the related change in the body.

### Does this slow rapid development?

It discourages disorganized history, not rapid iteration. Quick mode keeps the normal workflow lightweight.

### Are projects limited to the recommended types?

No. Teams may define additional types. This skill uses the recommended list by default for consistency.

### How does this relate to SemVer?

`fix` normally produces PATCH, `feat` normally produces MINOR, and a breaking change produces MAJOR regardless of its type.

### How should extensions to the specification be versioned?

Use Semantic Versioning for the extension itself.

### What if the wrong type was used?

Before merge or release, correct the message with an interactive rebase or another project-approved history edit. After release, follow the project's release process. A completely invalid type may be skipped by tools built on the specification.

### Must every contributor use Conventional Commits?

Not necessarily. With a squash-based workflow, maintainers can normalize the merge commit message.

### How should reverts be handled?

The specification does not define one universal revert algorithm. A practical convention is `revert` plus a footer referencing the reverted commit:

```text
revert: remove temporary debug logging

Refs: abc1234
```
