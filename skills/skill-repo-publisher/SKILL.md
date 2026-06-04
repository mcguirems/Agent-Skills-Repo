---
name: skill-repo-publisher
description: Use when you are inside an existing skill folder and need to package that skill into this repo as a transportable canonical skill, repair portability issues in the repo copy, generate the matching Flowershow page, create the installable zip, update the public index, and prepare the repo changes for Git publishing without modifying the original source folder.
---

# Skill Repo Publisher

Use this skill when the working context is an existing source skill that needs to be imported into the Agent Skills Repo and published as a downloadable public skill.

Do not use this skill for routine edits to a skill that is already packaged correctly inside this repo unless the task also includes repackaging, re-zipping, or republishing.

## Goal

Create a transportable repo-managed skill package under `skills/<slug>/` plus a matching public Flowershow page under `docs/skills/<slug>.md`, while leaving the original source folder outside this repo unchanged.

## Core Rules

- Treat the original skill folder as read-only source material.
- Make portability fixes only in the copied repo version.
- Package everything needed for installation inside the repo-managed skill folder.
- Generate a `.zip` that expands to one clean top-level `<slug>/` folder.
- Publish a public page with visible source and download links.
- Update only this repo's files for Git tracking and publishing.

## Required Workflow

Follow this order:

1. Inspect the source skill folder.
2. Choose the public title and normalized slug.
3. Copy the skill into `skills/<slug>/`.
4. Repair portability problems in the repo copy.
5. Ensure `SKILL.md` has YAML frontmatter with `name` and `description`.
6. Ensure install instructions are platform-neutral first and agent-specific second.
7. Remove unresolved placeholders, local-only paths, and external file dependencies.
8. Create or update:
   - `SKILL.md`
   - `README.md`
   - `Install-this-skill.md`
   - `references/` and other required support files
9. Build `<slug>.zip` inside the skill folder.
10. Create or update `docs/skills/<slug>.md`.
11. Add the skill to `docs/skills/index.md`.
12. Prepare the repo diff for commit and push.

## Transportability Standard

The packaged repo copy must be installable without access to the original source location.

Check for:
- absolute paths
- references to parent folders
- dependencies on files outside the packaged folder
- missing examples, references, templates, or assets
- unresolved placeholders

If any of those exist, fix them in the repo copy before publishing.

## Public Page Standard

Every published skill page must include a visible `SOURCE:` block near the top with:
- a direct `.zip` download link
- a GitHub folder link
- a direct raw `SKILL.md` link

The page should also describe:
- what the skill does
- when to use it
- when not to use it
- what files are included

## Zip Standard

The `.zip` must:
- live inside `skills/<slug>/`
- include one top-level `<slug>/` folder
- contain all required install files
- exclude junk files such as `.DS_Store`

## Git Boundary

Never add Git control to the original source folder.

Git actions apply only to:
- `skills/<slug>/`
- `docs/skills/<slug>.md`
- `docs/skills/index.md`
- other repo-managed publishing files that this repo owns

## Completion Criteria

The task is complete only when:
- the canonical repo copy is self-contained
- the zip artifact is rebuilt
- the public page includes the download and source links
- the landing page lists the skill
- the repo changes are ready to commit and publish
