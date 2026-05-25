# Repo Standards

Use this reference when editing `readme.md` or evaluating list structure.

## Repository Scope

The list focuses on AI skills, prompt libraries, agent tools, linting rules, and
best practices that improve technical writing workflows. Strong resources are
LLM-native, docs-as-code friendly, or directly useful for developer
documentation.

## Current Sections

- `Agent & LLM Skills`: agent skill files, skill directories, or structured
  agent instructions for technical documentation work.
- `AI Prompt Libraries`: reusable prompt libraries for API docs, release notes,
  changelogs, user guides, onboarding content, or similar writing tasks.
- `Best Practices`: guidance for skill creation, prompting, agent operation,
  evaluation, or workflow design.
- `Tools`: validators, creators, or utilities that help authors create,
  improve, or check agent skills.

## Entry Rules

- Use `- [Resource Name](URL): Description`.
- Put a colon immediately after the link.
- Keep the description to one or two factual sentences.
- Explain what the resource is and why it matters to LLM-assisted technical
  writing.
- Sort entries alphabetically by visible resource name within each section.
- Avoid duplicate URLs and duplicate resources.

## Quality Bar

Accept resources that:

- Are publicly inspectable without login.
- Contain actual skill files, prompt libraries, rule configs, or skill tooling.
- Are relevant to technical writing, developer docs, docs-as-code, or AI-assisted
  documentation workflows.
- Look maintained enough to be useful.

Reject or ask for more information when a resource is:

- A generic technical writing blog post, course, or video.
- A general writing assistant or editor.
- A static site generator or documentation platform without relevant
  machine-readable writing workflows.
- Promotional, inaccessible, or too broad to inspect.

## Source Patterns Used For This Repo

- GitHub Copilot's Diataxis skill emphasizes audience, user goal, scope,
  document type, clarity, accuracy, and consistency.
- Gemini CLI's docs skill uses a phased workflow: standards, preparation,
  execution, and verification.
- Anaxite and Validated Patterns skills use selective reference loading and
  severity-based review output.
- Elastic, Medusa, and MongoDB organize docs work into focused skills for
  authoring, review, triage, release notes, redirects, previews, and validation.
- Agent Skills best practices recommend project-specific context, concise
  instructions, gotchas, templates, checklists, validation loops, and progressive
  disclosure.
- Anthropic's prompting and agent-operation talks reinforce clear goals,
  constraints, context, examples, and reduced step-by-step supervision.
