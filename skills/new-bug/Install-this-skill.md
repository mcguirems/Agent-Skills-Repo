# Install New Bug

`new-bug` is a portable file-based skill for finding Slack bug reports and creating standardized Asana project 021 intake tasks.

## What To Install

Install the full `new-bug/` folder, or unzip `new-bug.zip` and install the extracted `new-bug/` folder.

Preserve the folder name exactly and keep these contents together:
- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/`
- `assets/`
- `references/`

`SKILL.md` must remain at the root of the installed folder.

## Generic Install Steps

1. Download the skill folder or the packaged `.zip`.
2. Copy `new-bug/` into your agent's skills directory.
3. Confirm that `SKILL.md` is at `.../new-bug/SKILL.md`.
4. Keep the bundled `agents/`, `assets/`, and `references/` folders with it.
5. Restart or refresh the agent if the skill does not appear immediately.

If an older version already exists, replace it only after confirming that you want to overwrite it.

## Common Install Locations

### Codex

- `~/.codex/skills/new-bug/`

```bash
mkdir -p ~/.codex/skills && cp -R ./new-bug ~/.codex/skills/new-bug
```

### Claude-compatible local environments

- `/mnt/skills/user/new-bug/`

```bash
mkdir -p /mnt/skills/user && cp -R ./new-bug /mnt/skills/user/new-bug
```

### Other file-based agents

Install the folder into that agent's equivalent shared skills directory, preserving the same top-level folder name.

## macOS Finder Install

1. Unzip the package if needed.
2. In Finder, open the destination skills directory for your agent.
3. Drag `new-bug/` into that directory.
4. If the destination is hidden, use `Go > Go to Folder...` and enter the path directly.

## After Install

Confirm:
- the final installed path
- that `agents/`, `assets/`, and `references/` were included
- whether the agent needs a restart or refresh

## Update

Replace the existing installed folder with the latest packaged `new-bug/` folder.

## Uninstall

Delete the installed `new-bug/` folder from the agent's skills directory.
