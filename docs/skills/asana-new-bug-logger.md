---
title: Asana New Bug Logger
status: active
---

# Asana New Bug Logger

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/asana-new-bug-logger/asana-new-bug-logger.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/asana-new-bug-logger)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/asana-new-bug-logger/SKILL.md)

## Purpose

`asana-new-bug-logger` finds or converts MyVeloFit Slack reports into standardized untriaged bug intake tasks in Asana project 021.

## When To Use

Use this skill when the user invokes `$asana-new-bug-logger`, provides a Slack message or thread link to log, or asks to find recent Slack discussions that could become bugs.

Good fits include:
- logging a specific Slack report as a bug
- scanning recent reports in the bug-reporting Slack channel
- checking possible duplicate bugs in project 021
- creating an unassigned, undated intake task in `Incoming - New`

## When Not To Use

Do not use this skill for:
- scoping the fix
- proposing a solution
- writing acceptance criteria
- creating the later project 101 development task
- triaging, assigning, or moving the created bug

## Output Structure

The skill creates a plain-text Asana intake task with:

1. `Reported by`
2. `Title`
3. `Describe the issue, problem or inconsistency`
4. `Source`
5. `Supporting evidence`
6. `Intake notes`

It preserves the Slack permalink and records only facts supported by the Slack evidence.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `asana-new-bug-logger.zip`
- `agents/openai.yaml`
- `assets/icon.png`
- `assets/icon.svg`
- `references/team-instructions.md`
- `references/how-to-use-this-skill.md`

## Installation Notes

The packaged `.zip` is the preferred download for moving this skill into another LLM or agent environment because it preserves the full folder structure in one file.

## Canonical Runtime Location

- `skills/asana-new-bug-logger/SKILL.md`

## Example Requests

- `$asana-new-bug-logger [Slack link]`
- `$asana-new-bug-logger`
- “Create a bug from this Slack thread.”
