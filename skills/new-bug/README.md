# New Bug

## Purpose

`new-bug` finds or converts MyVeloFit Slack reports into standardized untriaged bug intake tasks in Asana project 021.

## When To Use

Use this skill when someone:
- invokes `$new-bug`
- provides a Slack message or thread link to log as a bug
- asks to find recent Slack discussions that could become bugs
- needs duplicate checking against existing project 021 tasks before intake

## When Not To Use

Do not use this skill to scope the fix, propose a solution, create a development task in project 101, or triage the bug after intake.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/openai.yaml`
- `assets/icon.png`
- `assets/icon.svg`
- `references/team-instructions.md`
- `references/how-to-use-this-skill.md`

## Transportability

This package is intended to be copied as a self-contained folder into another agent's skills directory.
Use the generated `new-bug.zip` distribution artifact when you want a one-file handoff for installation in another environment.

## Canonical Path

- `skills/new-bug/SKILL.md`
