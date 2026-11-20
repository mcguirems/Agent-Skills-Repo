# Install Google Docs Global Styles

`google-docs-global-styles` is a file-based skill that applies a live Google Docs template whenever an agent creates a new Google Doc.

## What To Install

Install the full `google-docs-global-styles/` folder, or unzip `google-docs-global-styles.zip` and install the extracted `google-docs-global-styles/` folder.

Preserve the folder name exactly and keep these contents together:

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/`
- `assets/`

`SKILL.md` must remain at the root of the installed folder.

## Generic Install Steps

1. Download the packaged `.zip` or the complete skill folder.
2. Copy `google-docs-global-styles/` into your agent's skills directory.
3. Confirm that `SKILL.md` is at `.../google-docs-global-styles/SKILL.md`.
4. Keep the bundled `agents/` and `assets/` directories with it.
5. Restart or refresh the agent if the skill does not appear immediately.
6. Connect a Google Drive or Google Docs integration that can read document formatting and create or copy documents.
7. Confirm that the connected Google account can open the template URL identified in `SKILL.md`.

If an older version is installed, confirm that it should be replaced before overwriting it.

## Common Install Locations

### Codex

- `~/.codex/skills/google-docs-global-styles/`

```bash
mkdir -p ~/.codex/skills
cp -R ./google-docs-global-styles ~/.codex/skills/google-docs-global-styles
```

### Claude-compatible local environments

- `/mnt/skills/user/google-docs-global-styles/`

```bash
mkdir -p /mnt/skills/user
cp -R ./google-docs-global-styles /mnt/skills/user/google-docs-global-styles
```

### Other file-based agents

Install the folder in the agent's equivalent skills directory while preserving the same top-level folder name.

## macOS Finder Install

1. Unzip the package if needed.
2. Open the destination skills directory in Finder.
3. Drag `google-docs-global-styles/` into that directory.
4. If the destination is hidden, choose `Go > Go to Folder...` and enter its path.

## After Install

Confirm:

- the installed folder contains `SKILL.md`, `agents/`, and `assets/`
- the agent can read the template's formatting, not only its plain text
- the agent can create or copy a test Google Doc
- the agent can read back the created document for verification

## Update

Replace the existing installed folder with the latest packaged `google-docs-global-styles/` folder, then restart or refresh the agent if required.

## Uninstall

Remove the installed `google-docs-global-styles/` folder from the agent's skills directory.
