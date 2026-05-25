# Review Rubric

Use this reference when reviewing a candidate resource or pull request.

## Verdicts

- `Accept`: Resource fits scope, entry is well placed, description is factual,
  and validation passes.
- `Request changes`: Resource fits, but wording, section, sorting, or format
  needs revision.
- `Reject`: Resource is outside scope, inaccessible, duplicate, or too generic.
- `Needs more information`: The resource might fit, but the linked content does
  not expose enough detail to decide.

## Must-Fix Issues

- Resource does not contain skills, prompts, lint rules, skill tooling, or
  directly relevant best-practice guidance.
- Resource requires authentication for basic review.
- Entry is in the wrong section.
- Entry format does not match `- [Name](URL): Description`.
- Section entries are not alphabetized.
- Description uses marketing language or fails to explain relevance.
- URL is duplicated or points to a generic landing page when a deeper path is
  needed.

## Recommended Improvements

- Tighten long descriptions.
- Replace vague phrases like "a useful resource" with a concrete type.
- Mention the relevant workflow, such as docs authoring, review, prompt reuse,
  skill validation, release notes, or style enforcement.
- Link directly to a skill directory, prompt library, config file, or tool page
  when a repository root is too broad.

## Suggested Review Comments

Use exact replacement text when possible:

```markdown
Suggested entry:
- [Resource Name](URL): A [specific type] for [specific workflow]. It is relevant because [concrete reason].
```

For a rejection:

```markdown
This does not fit the current scope because the list focuses on machine-readable
skills, prompt libraries, linting configs, tools, and best-practice guidance for
AI-assisted technical writing workflows. This link appears to be [reason].
```
