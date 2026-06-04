---
title: MyVeloFit Working Backwards Brief
status: active
---

# MyVeloFit Working Backwards Brief

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/mvf-working-backwards-brief/mvf-working-backwards-brief.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/mvf-working-backwards-brief)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/mvf-working-backwards-brief/SKILL.md)

## Purpose

`mvf-working-backwards-brief` converts a MyVeloFit project brief into an Amazon-style Working Backwards document with a press release, customer FAQ, and internal FAQ.

## When To Use

Use this skill when you already have enough launch context to describe the customer problem, the solution, the likely audience, and the practical rollout shape.

Good fits include:
- product launch briefs
- feature-positioning drafts
- internal launch narrative exercises
- B2C and B2B announcements that need realistic customer-facing framing

## When Not To Use

Do not use this skill for:
- purely technical specifications
- vague concepts without launch context
- short implementation tasks
- roadmap brainstorming without a defined customer problem

## Output Structure

The skill writes in this order:

1. `Press Release`
2. `Customer FAQ`
3. `Internal FAQ`

It is designed to surface missing launch assumptions explicitly instead of hiding uncertainty.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `mvf-working-backwards-brief.zip`
- `references/working-backwards-template.md`
- `references/company-context.md`
- `references/example-brief-notes.md`
- `assets/source-pdfs/`

## Installation Notes

The packaged `.zip` is the preferred download for moving this skill into another LLM or agent environment because it preserves the full folder structure in one file.

## Canonical Runtime Location

- `skills/mvf-working-backwards-brief/SKILL.md`

## Example Requests

- “Turn this project brief into a Working Backwards PR/FAQ.”
- “Draft the press release, customer FAQ, and internal FAQ for this MyVeloFit launch.”
- “Use this brief and call out any missing launch assumptions clearly.”
