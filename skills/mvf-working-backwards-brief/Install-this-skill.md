# Install MyVeloFit Working Backwards Brief

`mvf-working-backwards-brief` is a portable file-based skill for turning a MyVeloFit project brief into a Working Backwards press release and FAQ package.

## What To Install

Install the full `mvf-working-backwards-brief/` folder, or unzip `mvf-working-backwards-brief.zip` and install the extracted `mvf-working-backwards-brief/` folder.

Preserve the folder name exactly and keep these contents together:
- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `references/`
- `assets/source-pdfs/`

`SKILL.md` must remain at the root of the installed folder.

## Generic Install Steps

1. Download the skill folder or the packaged `.zip`.
2. Copy `mvf-working-backwards-brief/` into your agent's skills directory.
3. Confirm that `SKILL.md` is at `.../mvf-working-backwards-brief/SKILL.md`.
4. Keep the bundled `references/` folder with it.
5. Keep the bundled `assets/source-pdfs/` folder with it if you want the packaged source material available for fidelity checks.
6. Restart or refresh the agent if the skill does not appear immediately.

If an older version already exists, replace it only after confirming that you want to overwrite it.

## Common Install Locations

### Codex

- `~/.codex/skills/mvf-working-backwards-brief/`

```bash
mkdir -p ~/.codex/skills && cp -R ./mvf-working-backwards-brief ~/.codex/skills/mvf-working-backwards-brief
```

### Claude-compatible local environments

- `/mnt/skills/user/mvf-working-backwards-brief/`

```bash
mkdir -p /mnt/skills/user && cp -R ./mvf-working-backwards-brief /mnt/skills/user/mvf-working-backwards-brief
```

### Other file-based agents

Install the folder into that agent's equivalent shared skills directory, preserving the same top-level folder name.

## macOS Finder Install

1. Unzip the package if needed.
2. In Finder, open the destination skills directory for your agent.
3. Drag `mvf-working-backwards-brief/` into that directory.
4. If the destination is hidden, use `Go > Go to Folder...` and enter the path directly.

## After Install

Confirm:
- the final installed path
- that `references/` was included
- that `assets/source-pdfs/` was included if you rely on packaged source material
- whether the agent needs a restart or refresh

## Update

Replace the existing installed folder with the latest packaged `mvf-working-backwards-brief/` folder.

## Uninstall

Delete the installed `mvf-working-backwards-brief/` folder from the agent's skills directory.
