---
title: MVF Project Registry
status: active
---

# MVF Project Registry

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/mvf-project-registry/mvf-project-registry.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/mvf-project-registry)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/mvf-project-registry/SKILL.md)

## Purpose

`mvf-project-registry` packages the MyVeloFit registry reconciliation workflow for rebuilding the canonical project registry across local files, Google Drive, Miro, and the team-facing Google Sheet.

## When To Use

Use this skill when you need to refresh the registry workflow end to end, including rescanning local projects, refreshing Drive and Miro inventories, rebuilding the canonical outputs, and updating the shared sheet.

Good fits include:
- local inventory rescans
- Drive inventory refreshes
- Miro registry board refreshes
- canonical registry rebuilds
- team-facing Google Sheet refreshes
- override and scope-rule updates

## When Not To Use

Do not use this skill for:
- unrelated spreadsheet formatting work
- one-off reporting tasks outside the registry workflow
- destructive moves, renames, or deletions unless the workflow is explicitly expanded
- publishing another skill to this repo

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `mvf-project-registry.zip`
- `references/publishing-notes.md`

## Runtime Requirements

This skill is portable as an installable package, but it is designed to run inside the `108 - Project Registry` workspace and expects the project repository's local config and scripts to exist there.

Operational dependencies include:
- Google Drive or Google Sheets access
- Miro access
- a workbook build runtime for `.xlsx` generation

## Installation Notes

The packaged `.zip` is the preferred download for moving this skill into another agent environment because it preserves the required folder structure in one file.

## Canonical Runtime Location

- `skills/mvf-project-registry/SKILL.md`

## Example Requests

- “Refresh the MyVeloFit product registry from local files, Drive, and Miro.”
- “Rebuild the master registry and validate the current scope rules.”
- “Update the team-facing registry sheet after reconciling the current overrides.”
