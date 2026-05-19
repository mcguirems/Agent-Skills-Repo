# Install This Skill Template

Use this file as the standard per-skill installer prompt/document for skills in this repository.

It is modeled after the Proof install prompt pattern, but adapted for a Git-backed Codex skills archive where the primary install method is manual local installation from a downloaded repository into `~/.codex/skills/`.

---

## Purpose

Each shareable skill should include an `Install-this-skill.md` file that can be used in two ways:

1. as a human-readable install guide
2. as a prompt that can be pasted into an agent session to perform the install

This file should not replace `README.md`.

Recommended division:

- `SKILL.md` = canonical runtime instruction
- `README.md` = overview, use cases, included files, constraints
- `Install-this-skill.md` = install, update, uninstall, and agent prompt

---

## Template

Replace bracketed placeholders before publishing.

```md
# Install [Skill Name] for me

[Skill Name] is a Codex skill for [one-sentence purpose].

Install this skill for this agent from the local downloaded repository.
If you cannot install files or access the local filesystem in this chat, tell me to use Codex, Claude Code, OpenClaw, or another agent that can.

The source skill folder is:
`[LOCAL_REPO_PATH]/skills/[skill-folder-name]`

Install it to:
`~/.codex/skills/[skill-folder-name]`

Copy the full folder and preserve the folder name exactly.
Make sure `SKILL.md` remains at the root of the installed folder.
Keep any bundled `references/`, `scripts/`, or `assets/` folders with it.

For macOS Finder users:
- Use `Go > Go to Folder...` and enter `~/.codex/skills/`
- If needed, press `Command + Shift + .` in Finder to show hidden files

If there is already an installed version:
- replace it with this version only if I confirm, or
- tell me the current and proposed paths and ask whether to overwrite

For power users, the direct local install command is:

```bash
mkdir -p ~/.codex/skills && cp -R "[LOCAL_REPO_PATH]/skills/[skill-folder-name]" "~/.codex/skills/[skill-folder-name]"
```

After install, confirm:
- the final installed path
- whether supporting folders were included
- whether a restart or refresh may be needed

If this skill later behaves unexpectedly, inspect:
- `~/.codex/skills/[skill-folder-name]/SKILL.md`
- any bundled files in `references/`, `scripts/`, or `assets/`
- the source repo copy at `[LOCAL_REPO_PATH]/skills/[skill-folder-name]`

During setup, ask me exactly one question:
[Insert one optional configuration question only if the skill has a real mode or policy choice.]

Then finish the install and tell me:
- which configuration mode is active, if applicable
- the installed path
- whether the install completed successfully
```

---

## Authoring Rules

When creating a real `Install-this-skill.md`, follow these rules:

1. Start with `Install [Skill Name] for me.`
2. Explain what the skill does in 1 to 2 sentences.
3. Prefer manual local repo installation first.
4. Include the exact source folder and destination folder.
5. Include Finder guidance for macOS hidden folders when relevant.
6. Include one direct install command in a `Power Users` section when practical.
7. Preserve the entire skill directory, not only `SKILL.md`, unless the skill truly consists of only that file.
8. Include overwrite/update behavior.
9. Include uninstall or rollback guidance in the human-readable section if needed.
10. Ask exactly one setup question only when there is a meaningful configuration choice.
11. End with explicit completion reporting requirements.

---

## Recommended Human-Readable Sections

Below the prompt block, or in a separate section above it, include:

### Manual Install

1. Download or clone the repository.
2. Copy `skills/[skill-folder-name]/` to `~/.codex/skills/[skill-folder-name]/`.
3. Confirm that `SKILL.md` is at the root of the installed folder.
4. Keep all bundled support folders with it.
5. Restart or refresh Codex if the skill does not appear immediately.

### Find The Install Folder On macOS

1. In Finder, choose `Go > Go to Folder...`.
2. Enter `~/.codex/skills/`.
3. If the folder is not visible, press `Command + Shift + .` to show hidden files.
4. Press `Command + Shift + .` again to hide hidden files when finished.

### Power Users

Use a terminal command only if you prefer command-line installation.

```bash
mkdir -p ~/.codex/skills && cp -R "[LOCAL_REPO_PATH]/skills/[skill-folder-name]" "~/.codex/skills/[skill-folder-name]"
```

### Update

Replace the installed folder with the current repo version, preserving the same folder name.

### Uninstall

Delete `~/.codex/skills/[skill-folder-name]/`.

---

## Recommended Use In This Repo

For each skill in this repository, include:

```text
skills/
  [skill-folder-name]/
    SKILL.md
    README.md
    Install-this-skill.md
    references/
```

This aligns with:

- `skills-repo-summary-and-plan-v1.md`
  - repo as shareable Git archive
  - `skills/` as canonical runtime location
  - `docs/` as human-facing publishing layer

- `skills-repo-v2-plan.md`
  - approved canonical assets live in `skills/`
  - installation guidance is part of the reusable asset package
  - documentation should be clear for both internal use and future sharing

---

## Suggested Follow-On Standard

Later, the repo should also add:

- a root `INSTALLING-SKILLS.md` file for generic installation guidance
- a standard `README.md` template for all skills
- a consistent policy for whether installs default to overwrite or require confirmation
