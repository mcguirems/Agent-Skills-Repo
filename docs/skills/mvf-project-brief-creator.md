---
title: MyVeloFit Project Brief Creator
status: active
---

# MyVeloFit Project Brief Creator

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/mvf-project-brief-creator/mvf-project-brief-creator.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/mvf-project-brief-creator)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/mvf-project-brief-creator/SKILL.md)

## Purpose

`mvf-project-brief-creator` turns rough project inputs into a complete MyVeloFit project brief in the standard seven-section markdown structure.

## When To Use

Use this skill when you have early planning material and need a structured brief that clarifies rationale, scope, ownership, dependencies, milestones, and success metrics.

Good fits include:
- feature concepts
- app initiatives
- launch planning
- strategic updates
- scoped operational workstreams

## When Not To Use

Do not use this skill for:
- purely technical specs
- vague concepts with no defined project shape
- short implementation tasks
- lightweight ticket writing

## Output Structure

The skill follows the reference project-brief template and is designed to surface missing decisions explicitly with `[Update Required]` markers instead of fabricating specifics.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `mvf-project-brief-creator.zip`
- `references/project-brief-template.md`
- `references/company-context.md`
- `references/example-project-brief-notes.md`
- `agents/openai.yaml`
- `source/gpt-instructions.md`
- `assets/source-pdfs/`

## Installation Notes

The packaged `.zip` is the preferred download for moving this skill into another LLM or agent environment because it preserves the required folder structure in one file.

## Canonical Runtime Location

- `skills/mvf-project-brief-creator/SKILL.md`

## Example Requests

- “Turn these notes into a MyVeloFit project brief.”
- “Draft the seven-section project brief for this feature launch.”
- “Use this Asana export and identify any missing decisions in the brief.”
