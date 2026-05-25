---
name: awesome-tech-writing-reviewer
description: Review proposed changes, issues, or pull requests for the Awesome Technical Writing Skills list. Use when evaluating whether resources belong in this repository, checking README entry quality, reviewing contribution scope, or giving maintainership feedback.
---

# Awesome Tech Writing Reviewer

Use this skill to review candidate additions and README changes against this
repo's scope and quality bar.

## Load First

Read `references/review-rubric.md` before reviewing. For changed README entries,
also read `../awesome-tech-writing-curator/references/repo-standards.md`.

## Review Workflow

1. Identify the review target:
   - Candidate URL or issue proposal.
   - README diff.
   - Pull request description.
   - Section proposal.
2. Read `readme.md` and `contributing.md` for current scope and conventions.
3. Check fit before wording:
   - Does the resource contain actual skill files, reusable prompts, rule
     configs, or skill tooling?
   - Is the resource specifically useful for LLM-assisted technical writing,
     docs-as-code, or developer documentation workflows?
   - Can a maintainer inspect it without logging in?
4. Check README quality:
   - Entry uses `- [Name](URL): Description`.
   - Section is appropriate.
   - Section entries are alphabetized.
   - Description is factual, concise, and not promotional.
   - No duplicate URL or duplicate resource under a different name.
5. Run the README validator when reviewing local changes:

```bash
python3 skills/awesome-tech-writing-curator/scripts/validate_readme.py readme.md
```

## Review Output

Lead with findings. Order by severity.

```markdown
## Findings

- **Must fix**: [Problem]. [Exact reason and suggested fix.]
- **Consider**: [Improvement]. [Why it would help.]

## Verdict

Accept | Request changes | Reject | Needs more information
```

Use `Must fix` for scope violations, broken format, wrong section, duplicate
entries, inaccessible resources, or alphabetization errors. Use `Consider` for
wording improvements and borderline fit.

## Reviewer Defaults

- Prefer a scoped rejection over weakening the list's niche.
- Ask for a new section only when the proposal supplies at least two resources
  that are clearly distinct from existing sections.
- If the resource is relevant but the description is weak, propose exact
  replacement text.
- If the resource is a broad repository, verify that the linked path lands on
  the relevant skill, prompt, config, or tool content.
