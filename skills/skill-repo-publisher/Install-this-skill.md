# Install Skill Repo Publisher

`skill-repo-publisher` is a portable file-based skill for importing and publishing other skills into this repo.

## What To Install

Install the full `skill-repo-publisher/` folder.

Preserve the folder name exactly and keep these contents together:
- `SKILL.md`
- `README.md`
- `Install-this-skill.md`

`SKILL.md` must remain at the root of the installed folder.

## Generic Install Steps

1. Download the skill folder.
2. Copy `skill-repo-publisher/` into your agent's skills directory.
3. Confirm that `SKILL.md` is at `.../skill-repo-publisher/SKILL.md`.
4. Restart or refresh the agent if the skill does not appear immediately.

## Recommended Use

Run this skill from inside the `000-skills-repo` workspace.
At the start of the run, provide the full local path to the source skill directory that should be imported.
After packaging is complete, the skill should ask:
1. `Publish now`
2. `Stop now`

## Common Install Locations

### Codex

- `~/.codex/skills/skill-repo-publisher/`

```bash
mkdir -p ~/.codex/skills && cp -R ./skill-repo-publisher ~/.codex/skills/skill-repo-publisher
```

### Claude-compatible local environments

- `/mnt/skills/user/skill-repo-publisher/`

```bash
mkdir -p /mnt/skills/user && cp -R ./skill-repo-publisher /mnt/skills/user/skill-repo-publisher
```

### Other file-based agents

Install the folder into that agent's equivalent shared skills directory, preserving the same top-level folder name.

## Update

Replace the existing installed folder with the latest packaged `skill-repo-publisher/` folder.

## Uninstall

Delete the installed `skill-repo-publisher/` folder from the agent's skills directory.
