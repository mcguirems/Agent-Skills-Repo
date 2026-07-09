# Install MVF Project Registry

`mvf-project-registry` is a portable file-based skill for running the MyVeloFit registry reconciliation workflow from the `108 - Project Registry` workspace.

## What To Install

Install the full `mvf-project-registry/` folder, or unzip `mvf-project-registry.zip` and install the extracted `mvf-project-registry/` folder.

Preserve the folder name exactly and keep these contents together:
- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `references/publishing-notes.md`
- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `references/publishing-notes.md`
`SKILL.md` must remain at the root of the installed folder.

## Generic Install Steps

1. Download the skill folder or the packaged `.zip`.
2. Copy `mvf-project-registry/` into your agent's skills directory.
3. Confirm that `SKILL.md` is at `.../mvf-project-registry/SKILL.md`.
4. Keep the bundled `references/` folder with it.
5. Restart or refresh the agent if the skill does not appear immediately.

If an older version already exists, replace it only after confirming that you want to overwrite it.

## Common Install Locations

### Codex

- `~/.codex/skills/mvf-project-registry/`

```bash
mkdir -p ~/.codex/skills && cp -R ./mvf-project-registry ~/.codex/skills/mvf-project-registry
```

### Claude-compatible local environments

- `/mnt/skills/user/mvf-project-registry/`

```bash
mkdir -p /mnt/skills/user && cp -R ./mvf-project-registry /mnt/skills/user/mvf-project-registry
```

### Other file-based agents

Install the folder into that agent's equivalent shared skills directory, preserving the same top-level folder name.

## Required Runtime Context

After install, this skill still expects:
- the `108 - Project Registry` workspace
- the local config and scripts referenced in `SKILL.md`
- Google Drive access for Drive and Sheets refreshes
- Miro access for board inventory refreshes
- a workbook build runtime for `.xlsx` generation

## After Install

Confirm:
- the final installed path
- that `references/` was included
- that the target workspace contains the referenced scripts and config
- that the required connectors are available in the target agent
- whether the agent needs a restart or refresh

## Update

Replace the existing installed folder with the latest packaged `mvf-project-registry/` folder.

## Uninstall

Delete the installed `mvf-project-registry/` folder from the agent's skills directory.
