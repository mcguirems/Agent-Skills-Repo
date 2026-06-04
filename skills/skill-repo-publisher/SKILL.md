---
name: skill-repo-publisher
description: Use when you are working from the 000-skills-repo workspace and need to import a skill from another local source directory into this repo as a transportable canonical skill, repair portability issues in the repo copy, generate the matching Flowershow page, create the installable zip, and then ask whether to publish to Git/Flowershow or stop.
---

# Skill Repo Publisher

Use this skill when you are already working inside `000-skills-repo` and want to import a source skill from another local directory into the Agent Skills Repo as a downloadable public skill.

Do not use this skill for routine edits to a skill that is already packaged correctly inside this repo unless the task also includes repackaging, re-zipping, or republishing.

## Goal

Create a transportable repo-managed skill package under `skills/<slug>/` plus a matching public Flowershow page under `docs/skills/<slug>.md`, while leaving the original source folder outside this repo unchanged.

## Start Condition

This skill should be run from the `000-skills-repo` workspace, not from the original source skill folder.

At the beginning of the run, ask for exactly one required input if it is not already provided:
- the full local path to the source skill directory that should be imported

If the source path is missing, stop and request it before doing any packaging work.

## Core Rules

- Treat the original skill folder as read-only source material.
- Make portability fixes only in the copied repo version.
- Package everything needed for installation inside the repo-managed skill folder.
- Generate a `.zip` that expands to one clean top-level `<slug>/` folder.
- Publish a public page with visible source and download links.
- Update only this repo's files for Git tracking and publishing.
- Do not silently publish to Git or Flowershow at the end.

## Required Workflow

Follow this order:

1. Confirm you are operating from `000-skills-repo`.
2. Ask for the source skill directory if it was not provided explicitly.
3. Inspect the source skill folder.
4. Choose the public title and normalized slug.
5. Copy the skill into `skills/<slug>/`.
6. Repair portability problems in the repo copy.
7. Ensure `SKILL.md` has YAML frontmatter with `name` and `description`.
8. Ensure install instructions are platform-neutral first and agent-specific second.
9. Remove unresolved placeholders, local-only paths, and external file dependencies.
10. Create or update:
   - `SKILL.md`
   - `README.md`
   - `Install-this-skill.md`
   - `references/` and other required support files
11. Build `<slug>.zip` inside the skill folder.
12. Create or update `docs/skills/<slug>.md`.
13. Add the skill to `docs/skills/index.md`.
14. Show the changed files and summarize what was prepared.
15. Ask one final question in this exact format:
   - `Packaging is complete. What should I do next?`
   - `1. Publish now`
   - `2. Stop now`
16. Explain the consequence of each option briefly:
   - `Publish now` means commit, push, and then tell the user to sync Flowershow if needed
   - `Stop now` means leave the repo changes prepared but uncommitted
17. If the answer is `1. Publish now`:
   - prepare the repo diff for commit
   - commit
   - push
   - tell the user to run or confirm the Flowershow sync if that step is not automated in the environment
18. If the answer is `2. Stop now`:
   - do not commit or push
   - leave the repo changes ready for review

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

Git publish is an explicit final branch, not an implicit default.

## Completion Criteria

The task is complete only when:
- the canonical repo copy is self-contained
- the zip artifact is rebuilt
- the public page includes the download and source links
- the landing page lists the skill
- the user has either:
  - chosen to stop with the repo changes prepared, or
  - chosen publish and the commit/push flow has completed
