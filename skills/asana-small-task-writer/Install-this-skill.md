# Install Asana Small Task Writer for me

Asana Small Task Writer is a Codex skill for turning a scoped product or UX request into one implementation-ready Asana small task.

Install this skill for this agent from the local downloaded repository.
If you cannot install files or access the local filesystem in this chat, tell me to use Codex, Claude Code, OpenClaw, or another agent that can.

The source skill folder is:
`[LOCAL_REPO_PATH]/skills/asana-small-task-writer`

Install it to:
`~/.codex/skills/asana-small-task-writer`

Copy the full folder and preserve the folder name exactly.
Make sure `SKILL.md` remains at the root of the installed folder.
Keep the bundled `references/` folder with it.

For macOS Finder users:
- Use `Go > Go to Folder...` and enter `~/.codex/skills/`
- If needed, press `Command + Shift + .` in Finder to show hidden files

If there is already an installed version:
- replace it with this version only if I confirm, or
- tell me the current and proposed paths and ask whether to overwrite

For power users, the direct local install command is:

```bash
mkdir -p ~/.codex/skills && cp -R "[LOCAL_REPO_PATH]/skills/asana-small-task-writer" "~/.codex/skills/asana-small-task-writer"
```

After install, confirm:
- the final installed path
- whether the `references/` folder was included
- whether a restart or refresh may be needed

During setup, ask me exactly one question:
Should this skill be used only when I explicitly ask, or may it be used automatically when a request is clearly a single scoped Asana task?
1. Only when I explicitly ask
2. Use automatically when clearly appropriate

Then finish the install and tell me:
- which mode is active
- the installed path
- whether the install completed successfully

## Manual Install

1. Download or clone the repository.
2. Copy `skills/asana-small-task-writer/` to `~/.codex/skills/asana-small-task-writer/`.
3. Confirm that `SKILL.md` is at the root of the installed folder.
4. Keep the `references/` folder with it.
5. Restart or refresh Codex if the skill does not appear immediately.

## Find The Install Folder On macOS

1. In Finder, choose `Go > Go to Folder...`.
2. Enter `~/.codex/skills/`.
3. If the folder is not visible, press `Command + Shift + .` to show hidden files.
4. Press `Command + Shift + .` again to hide hidden files when finished.

## Power Users

```bash
mkdir -p ~/.codex/skills && cp -R "[LOCAL_REPO_PATH]/skills/asana-small-task-writer" "~/.codex/skills/asana-small-task-writer"
```

## Update

Replace the installed folder with the current repo version, preserving the same folder name.

## Uninstall

Delete `~/.codex/skills/asana-small-task-writer/`.
