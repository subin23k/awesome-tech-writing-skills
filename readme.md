# Awesome Technical Writing Skills

> A curated list of AI skills, prompt libraries, and agent tools to enhance
> and automate technical writing workflows. Focused on LLM-native,
> docs-as-code, and developer documentation use cases.

## Contents

- [Agent & LLM Skills](#agent--llm-skills)
- [AI Prompt Libraries](#ai-prompt-libraries)
- [Best Practices](#best-practices)
- [Tools](#tools)
- [Contributing](#contributing)

## Agent & LLM Skills

- [Anaxite Agent Skills](https://github.com/anaxite/agent-skills/tree/main/skills): A collection of modular agent skills for AI-assisted workflows. Several skills are applicable to technical documentation tasks, including content structuring and summarization.
- [Elastic Docs Skills](https://github.com/elastic/elastic-docs-skills/tree/main/skills): Official documentation skills from Elastic, showcasing how the company structures AI-assisted writing skills for large-scale technical documentation.
- [Medusa Claude Skills](https://github.com/medusajs/medusa/tree/develop/.claude/skills): Claude Code skills from the Medusa open-source commerce platform, including a dedicated technical writer skill that automates authoring of MDX documentation files while enforcing Medusa's style guide and Vale compliance standards.
- [MongoDB Docs Claude Skills](https://github.com/mongodb/docs/tree/main/.claude/skills): Claude Code skills from MongoDB's official documentation repository, covering the full docs contribution lifecycle: Jira triage, PR creation, release notes authoring, redirect handling, and staging preview.
- [Validated Patterns Docs – RuleSync Skills](https://github.com/validatedpatterns/docs/tree/main/.rulesync/skills): A set of rulesync skills from the Red Hat Validated Patterns project, demonstrating how documentation writing standards can be enforced programmatically in a docs-as-code environment.

## AI Prompt Libraries

- [Prompt Library for Writers](https://snehap16.github.io/awesome-tech-writing/ai-prompt-library.html): A prompt library for technical writers covering API docs, release notes, and user guide authoring with AI assistants.

## Best Practices

- [Agent Skills – Best Practices for Skill Creation](https://agentskills.io/skill-creation/best-practices): A guide from the Agent Skills open standard on building effective skills, covering how to ground them in real expertise, manage context usage, calibrate instruction specificity, and apply structural patterns like gotchas sections, output templates, and validation loops.

## Tools

- [Claude Skill Creator](https://claude.com/plugins/skill-creator): Anthropic's official toolkit for developing, testing, and iterating on Claude Code skills. Provides four modes: Create, Eval, Improve, and Benchmark, covering the full skill development lifecycle from initial concept to production-ready output. The underlying [SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) is also a useful reference for understanding how a well-structured skill is built.
- [Skill Validator](https://github.com/agent-ecosystem/skill-validator): A validation tool for agent skill files. Useful when authoring new skills to ensure they conform to expected structure and standards before publishing or submitting a PR.

## Contributing

Contributions welcome! Please read the
[contribution guidelines](contributing.md) first.

### 🚀 What We're Looking For

If you know of or have built any of the following, please submit a PR:

- Agent skill files targeting docs workflows.
- Prompt packs for API documentation, release notes, or changelog generation.
- Rules/linting configs that enforce writing standards in a docs-as-code pipeline.

This is an underserved niche, and your contribution could set the standard
for how the community approaches AI-assisted technical writing at scale.
