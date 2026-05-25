---
name: awesome-tech-writing-skill-maintainer
description: Create, update, and validate the repo-local maintenance skills under skills/. Use when modifying SKILL.md files, skill references, bundled scripts, openai.yaml metadata, or workflows that help maintain this repository.
---

# Awesome Tech Writing Skill Maintainer

Use this skill to maintain the skills that maintain this repository.

## Load First

Read `references/skill-design-notes.md` before changing any file under
`skills/`.

## Skill Maintenance Workflow

1. Identify which maintenance behavior is changing:
   - README curation.
   - Contribution review.
   - Skill design and validation.
   - Deterministic checks or scripts.
2. Read the affected skill's `SKILL.md`, any referenced files, and
   `agents/openai.yaml`.
3. Keep `SKILL.md` focused on instructions needed on every run. Move detailed
   rubrics, source notes, or longer checklists to `references/`.
4. Use imperative procedures, not generic declarations. Prefer exact commands,
   output templates, and validation gates.
5. Keep descriptions trigger-oriented. The frontmatter `description` must say
   what the skill does and when to use it.
6. Update `agents/openai.yaml` if the skill name, purpose, or default prompt
   changes.
7. Validate every changed skill:

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/<skill-name>
```

8. If the README validator changed, run it against the current README:

```bash
python3 skills/awesome-tech-writing-curator/scripts/validate_readme.py readme.md
```

## Skill Design Standards

- Ground instructions in this repo's files and actual maintenance workflows.
- Include gotchas that prevent likely mistakes.
- Use progressive disclosure: link reference files by name and explain when to
  load them.
- Bundle scripts only for checks that should be deterministic.
- Do not copy external skill content wholesale. Extract reusable patterns and
  adapt them to this repo.
- Keep the skill suite small. Add a new skill only for a coherent workflow that
  would otherwise make an existing skill too broad.

## Gotchas

- These skills live in the repository, not in the user's global Codex skills
  directory.
- This repo intentionally has minimal project structure. Do not introduce build
  systems or package managers just to validate Markdown.
- A skill can reference another repo-local skill's reference file by relative
  path, but avoid deep reference chains.
