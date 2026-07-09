# MVF Project Registry

## Purpose

`mvf-project-registry` packages the MyVeloFit project registry reconciliation workflow for rebuilding the canonical registry across local files, Google Drive, Miro, and the team-facing Google Sheet.

## When To Use

Use this skill when you need to rescan the MyVeloFit `100 - Projects` source set, reconcile numbering and naming decisions, rebuild the master registry outputs, or refresh the shared registry sheet.

Good fits include:
- local project inventory refreshes
- Drive inventory refreshes
- Miro board inventory refreshes
- canonical registry rebuilds
- team-facing sheet refreshes
- config-driven override updates

## When Not To Use

Do not use this skill for one-off spreadsheet cleanup, unrelated reporting work, or destructive renames and moves across source systems unless the workflow is explicitly expanded to handle that.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `references/publishing-notes.md`

## Required Environment

This skill is meant to be run from the `108 - Project Registry` workspace where the referenced config and scripts already exist.

Operational dependencies are documented in `SKILL.md` and `references/publishing-notes.md`, including:
- Google Drive connector
- Miro connector
- spreadsheet workbook build runtime

## Transportability

This package is self-contained for skill installation, but it orchestrates a workflow that depends on the target `108 - Project Registry` project repository and its local scripts.

Use the packaged `mvf-project-registry.zip` artifact when you want a single-file handoff that preserves the expected folder structure.

## Canonical Path

- `skills/mvf-project-registry/SKILL.md`
