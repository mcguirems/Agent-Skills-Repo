---
title: Asana Small Task Writer
status: active
---

# Asana Small Task Writer

SOURCE:
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/asana-small-task-writer)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/asana-small-task-writer/SKILL.md)

## Purpose

`asana-small-task-writer` converts a scoped product or UX change into one implementation-ready Asana small task.

## When To Use

Use this skill when the request is already small enough to define clearly without discovery work, complex user flows, or cross-team coordination.

Good fits include:
- UX and UI refinements
- behavior fixes
- navigation improvements
- accessibility and clarity improvements
- scoped polish work

## When Not To Use

Do not use this skill for:
- net-new feature definition
- information architecture work
- experiments
- multi-step user journeys
- cross-team initiatives
- work that still needs decomposition

## Output Structure

The skill writes tasks in this order:

1. `Description (Problem / Context)`
2. `Required Elements (Acceptance Criteria)`
3. `References / Constraints`
4. `Why This Is Needed (UX Rationale)`

If key information is missing, it adds a `Questions / Clarifications` section after the task.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `references/source-guide.md`
- `references/source-instructions.md`
- `references/example-1.md`
- `references/example-2.md`

## Canonical Runtime Location

- `skills/asana-small-task-writer/SKILL.md`

## Example Requests

- “Turn this into an Asana small task.”
- “Rewrite this draft task to match the small-task standard.”
- “Tighten the acceptance criteria and call out missing information.”
