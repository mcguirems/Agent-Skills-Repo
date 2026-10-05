---
title: Weekly Activity Summary
description: "Last updated: October 5, 2026"
status: active
---

# Weekly Activity Summary

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/weekly-activity-summary/weekly-activity-summary.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/weekly-activity-summary)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/weekly-activity-summary/SKILL.md)

## Purpose

`weekly-activity-summary` creates Mike McGuire’s weekly MyVeloFit standup summary from available evidence across Asana, PostHog, Google Drive, Slack, ChatGPT work, and an optional low-priority Gmail check. It produces a numbered, 1Writer-compatible Markdown file and retrieves live Asana project status updates without inventing unavailable activity.

## When To Use

Use this skill when you need to:

- prepare Mike’s weekly work recap or standup notes
- combine activity and investigation evidence from multiple connected services
- distinguish implementation, review, handoff, open work, and verified launch
- include current recorded status updates for the default Asana project set
- revise an existing weekly summary while preserving approved wording

## When Not To Use

Do not use this skill for:

- a generic team-wide status report with a different subject
- analytics reporting that requires newly calculated PostHog metrics
- changing tasks, documents, messages, project statuses, or sharing permissions
- summaries that lack access to enough evidence and would require guessing
- creating a recurring automation unless the user explicitly requests scheduling

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/openai.yaml`
- `assets/icon.svg`
- `assets/summary-template.md`
- `references/sources.md`
- `weekly-activity-summary.zip`

## Requirements

Full coverage requires authenticated access to the relevant Asana, PostHog, Google Drive, Slack, and ChatGPT work sources. The package remains safe when sources are unavailable because its instructions require narrower coverage rather than invented evidence.

## Example Requests

- “Use `$weekly-activity-summary` to prepare last week’s standup notes.”
- “Create my weekly activity summary for September 28 through October 4.”
- “Update this week’s summary with the Asana project status posts.”
