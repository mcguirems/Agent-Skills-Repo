# Install Asana Small Task Writer

`asana-small-task-writer` is a portable file-based skill for turning one scoped product or UX request into one implementation-ready Asana small task.

## What To Install

Install the full `asana-small-task-writer/` folder, or unzip `asana-small-task-writer.zip` and install the extracted `asana-small-task-writer/` folder.

Preserve the folder name exactly and keep these contents together:
- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `references/`

`SKILL.md` must remain at the root of the installed folder.

## Generic Install Steps

1. Download the skill folder or the packaged `.zip`.
2. Copy `asana-small-task-writer/` into your agent's skills directory.
3. Confirm that `SKILL.md` is at `.../asana-small-task-writer/SKILL.md`.
4. Keep the bundled `references/` folder with it.
5. Restart or refresh the agent if the skill does not appear immediately.

If an older version already exists, replace it only after confirming that you want to overwrite it.

## Common Install Locations

### Codex

- `~/.codex/skills/asana-small-task-writer/`

```bash
mkdir -p ~/.codex/skills && cp -R ./asana-small-task-writer ~/.codex/skills/asana-small-task-writer
```

### Claude-compatible local environments

- `/mnt/skills/user/asana-small-task-writer/`

```bash
mkdir -p /mnt/skills/user && cp -R ./asana-small-task-writer /mnt/skills/user/asana-small-task-writer
```

### Other file-based agents

Install the folder into that agent's equivalent shared skills directory, preserving the same top-level folder name.

## macOS Finder Install

1. Unzip the package if needed.
2. In Finder, open the destination skills directory for your agent.
3. Drag `asana-small-task-writer/` into that directory.
4. If the destination is hidden, use `Go > Go to Folder...` and enter the path directly.

## After Install

Confirm:
- the final installed path
- that `references/` was included
- whether the agent needs a restart or refresh

## Update

Replace the existing installed folder with the latest packaged `asana-small-task-writer/` folder.

## Uninstall

Delete the installed `asana-small-task-writer/` folder from the agent's skills directory.
