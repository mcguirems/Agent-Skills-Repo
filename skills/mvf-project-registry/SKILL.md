---
name: mvf-project-registry
description: Use when reconciling MyVeloFit project numbers and names across the local `100 - Projects` directory, Google Drive `100 - Projects`, and Miro boards, including applying established canonical overrides, filtering scope, rebuilding the master CSV, and refreshing the team-facing Google Sheet registry.
---

# MVF Project Registry

Use this skill for the MyVeloFit project registry workflow in the `108 - Project Registry` workspace.

## Use This Skill When

- The user wants to rescan the MyVeloFit local `100 - Projects` directory.
- The user wants to refresh the Google Drive inventory for `Product / 100 - Projects`.
- The user wants to refresh the Miro board inventory for project-numbered boards.
- The user wants to rebuild the canonical registry CSV, workbook, or team-facing Google Sheet.
- The user wants to apply or update project-number overrides, naming overrides, or scope rules.

## Do Not Use This Skill When

- The user only wants a one-off spreadsheet formatting change unrelated to the registry workflow.
- The user wants to publish a skill to the skills repo. That is a separate workflow.
- The user wants destructive renames, moves, or deletions in the source local directory, Drive, or Miro. This workflow is review-first unless explicitly expanded.

## Required Working Directory

Run this from:

`108 - Project Registry`

This skill assumes the repo contains:

- `config/project_registry_config.json`
- `scripts/scan_local_projects.py`
- `scripts/reconcile_project_registry.py`
- `scripts/validate_registry.py`
- `scripts/build_registry_workbook.mjs`

## Tooling And Connector Assumptions

Document the live dependencies explicitly:

- Google Drive connector:
  - used for Drive folder inventory
  - used for Google Sheets import, move, and formatting updates
- Miro connector:
  - used for board inventory
- Workspace spreadsheet runtime:
  - used to build the local `.xlsx` workbook artifact before importing to Google Sheets

If a connector is unavailable, continue with local CSV generation and note the gap clearly instead of pretending the cross-system refresh succeeded.

## Canonical Workflow

1. Read `config/project_registry_config.json`.
2. Respect active scope rules and row overrides in config.
3. Refresh local inventory with `scripts/scan_local_projects.py` when the local source should be rescanned.
4. Refresh Drive inventory only from the shared folder `Product / 100 - Projects`.
5. Refresh Miro inventory only for project-numbered boards relevant to the registry.
6. Rebuild the master registry with `scripts/reconcile_project_registry.py`.
7. Run `scripts/validate_registry.py`.
8. Rebuild the workbook with `scripts/build_registry_workbook.mjs`.
9. If the user wants the team-facing Sheet refreshed:
   - import the workbook as a native Google Sheet
   - place it in `Product / 100 - Projects`
   - keep `master_registry` team-facing and minimal
   - keep `full_registry` for detailed automation data

## Team-Facing Sheet Contract

The visible `master_registry` tab should contain only:

- `Project_Number`
- `Letter_Suffix`
- `Project_Name`
- `google_url`

Formatting expectations:

- `Project_Number` and `Letter_Suffix` centered
- column A width `120`
- column B width `120`
- column C width `380`
- column D auto-fit

Top rows should contain:

- title
- date last updated
- share link

## Current Scope Rules

Default scope currently used in this project:

- location: `100 - Projects`
- require `project_key`
- exclude project numbers greater than `799`

Do not silently widen scope. If the user changes the rules, update config first.

## Current Decision Rules

Read the current config before acting. As of this workflow, examples include:

- `150` canonicalized as the top-level platform UX/UI project
- `150B` retained as a Miro-specific suffix board
- `154` canonicalized to Canyon Fit System - B2B Development
- `158` canonicalized to B2B Fit Reports
- `162` canonicalized to Morphology

Treat config as the source of truth, not this summary.

## Output Expectations

Local outputs:

- `output/registry/project_registry_master.csv`
- `output/registry/project_registry_master_workbook.xlsx`
- `output/reports/project_registry_error_report.md`

When reporting status back to the user:

- give the live Google Sheet link if refreshed
- state whether Drive and Miro were actually refreshed
- call out remaining true duplicate-key conflicts separately from formatting-only issues

## Validation Standard

At minimum:

- confirm no blank `project_key` rows remain in the master CSV when scope requires keys
- confirm no rows above scope remain in the master CSV
- run `scripts/validate_registry.py`
- if the Google Sheet was refreshed, verify the visible header rows and first data rows
