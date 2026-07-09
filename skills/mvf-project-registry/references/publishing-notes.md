# Publishing Notes

## Source Skill Path

This local source skill lives at:

`local-skill/mvf-project-registry`

## Packaging Intent

This folder is intended to be the source directory for the skills repo publishing workflow after switching to the skills repo workspace.

## Connector Documentation Policy

Yes, document connector assumptions inside the skill when they are operationally important.

For this skill, explicitly mention:

- Google Drive connector
- Miro connector
- spreadsheet workbook build runtime

These are the plugins or connector families the installed skill relies on in practice:

- Google Drive / Google Sheets
- Miro
- workspace spreadsheet runtime

Do not hardcode plugin version numbers unless the version itself matters to the workflow.
