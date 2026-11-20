# Google Docs Global Styles

## Purpose

`google-docs-global-styles` applies Mike McGuire's live Global Styles template whenever an agent creates a new Google Doc. It reads the template again for every document so later style changes are inherited without editing the skill.

## When To Use

Use this skill when an agent creates a new Google Doc, including a report, plan, summary, or a Google Doc produced from an uploaded or converted file.

Use it alongside content-specific skills. A document-specific formatting request takes precedence for that document.

## When Not To Use

Do not use this skill to restyle an existing document unless the user asks, to change the source template, or to apply Google Docs formatting rules to another file format.

## Requirements

The agent needs:

- access to the Google Docs Global Styles template identified in `SKILL.md`
- a Google Drive or Google Docs integration that can read document formatting
- permission to create or copy a Google Doc in the requested destination

The live template is an intentional runtime dependency. The package does not cache or hardcode its fonts, spacing, margins, or other style values.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/openai.yaml`
- `assets/icon.svg`

## Transportability

This package is a self-contained skill definition, but its workflow requires authorized access to the live Google Docs template named in `SKILL.md`. Install the full folder so the agent metadata and icon remain available.

Use `google-docs-global-styles.zip` for a one-file handoff to another supported environment.

## Canonical Path

- `skills/google-docs-global-styles/SKILL.md`
