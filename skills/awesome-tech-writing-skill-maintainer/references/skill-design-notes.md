# Skill Design Notes

Use this reference when creating or revising repo-local skills.

## Patterns To Preserve

- Triggering lives in frontmatter `description`. Include both the task and the
  contexts that should activate the skill.
- `SKILL.md` should contain the core workflow and the highest-value gotchas.
- Longer standards and rubrics belong in `references/`, with explicit load
  instructions.
- Scripts belong in `scripts/` only when the check is deterministic and likely
  to be rerun.
- Output templates are useful when reviews or reports need a predictable shape.

## Maintenance Skill Suite

- `awesome-tech-writing-curator`: edits and validates `readme.md`.
- `awesome-tech-writing-reviewer`: reviews resource fit, PRs, and candidate
  entries.
- `awesome-tech-writing-skill-maintainer`: maintains this skill suite.

## External Patterns Synthesized

- Diataxis-oriented documentation skills: clarify audience, goal, scope, and
  document type before writing.
- Project docs skills: separate standards, preparation, execution, and
  verification.
- Style-review skills: use severity categories and exact replacement text.
- Large docs repos: split workflows into focused skills rather than one
  everything skill.
- Agent Skills best practices: use real project artifacts, moderate detail,
  progressive disclosure, defaults instead of menus, checklists, validation
  loops, and gotchas.

## Validation

Run skill validation after each substantial edit:

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/<skill-name>
```

If `agents/openai.yaml` is stale, regenerate it with:

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/generate_openai_yaml.py" skills/<skill-name> --interface display_name="..." --interface short_description="..." --interface default_prompt="Use $skill-name to ..."
```
