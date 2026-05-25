---
name: awesome-tech-writing-curator
description: Maintain the Awesome Technical Writing Skills README. Use when adding, editing, moving, de-duplicating, or validating README entries, sections, descriptions, anchors, or contribution-facing list content for this repository.
---

# Awesome Tech Writing Curator

Use this skill to keep `readme.md` accurate, narrowly scoped, and easy to
review.

## Load First

Read `references/repo-standards.md` before editing `readme.md`. It captures the
repo scope, section taxonomy, entry format, sort rules, and recurring gotchas.

## Curation Workflow

1. Read `readme.md` and `contributing.md`.
2. Classify each candidate resource into one current section:
   - `Agent & LLM Skills`: concrete agent skills, skill directories, or
     machine-readable skill definitions for docs workflows.
   - `AI Prompt Libraries`: reusable prompt packs for technical writing tasks.
   - `Best Practices`: guidance on creating, prompting, evaluating, or operating
     agent skills and AI-assisted writing workflows.
   - `Tools`: utilities for creating, validating, or managing skills.
3. Reject or flag resources that are outside scope:
   - Generic technical writing tutorials, courses, newsletters, or blog posts.
   - General writing tools or editors.
   - Documentation platforms without machine-readable writing skills, prompts,
     lint rules, or skill tooling.
   - Resources requiring login for basic inspection.
4. Verify the destination section is present in the contents list and has a
   matching heading.
5. Add or update entries in this exact format:

```markdown
- [Resource Name](URL): One to two factual sentences explaining what the resource is and why it is relevant to LLM-assisted technical writing workflows.
```

6. Keep entries within each section alphabetized by visible resource name,
   case-insensitive.
7. Keep descriptions factual and concise. Avoid marketing claims such as
   "powerful," "best," "ultimate," or "revolutionary."
8. Run the validator:

```bash
python3 skills/awesome-tech-writing-curator/scripts/validate_readme.py readme.md
```

9. Fix any reported issues and rerun the validator until it passes.

## Description Pattern

Use this shape for descriptions:

```markdown
- [Name](URL): A [specific type] from [source or project] for [specific docs or skill workflow], useful because [concrete relevance].
```

Good descriptions answer both:

- What is it?
- Why does it belong in this list?

## Gotchas

- The repo file is `readme.md`, lowercase.
- Do not add a new section for a single resource. New sections need at least
  two fitting resources and a clear distinction from existing sections.
- YouTube resources belong in `Best Practices` only when they are guidance for
  prompting, skill creation, or agent operation. Generic video tutorials do not
  belong.
- For GitHub directories, describe the collection, not just the repository.
- Preserve existing prose style: concise, plain, and contribution-oriented.
