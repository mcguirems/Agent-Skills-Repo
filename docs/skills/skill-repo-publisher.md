---
title: Skill Repo Publisher
status: active
---

# Skill Repo Publisher

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/skill-repo-publisher/skill-repo-publisher.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/skill-repo-publisher)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/skill-repo-publisher/SKILL.md)

## Purpose

`skill-repo-publisher` takes an existing source skill from another local folder, copies it into this repo as a transportable canonical package, and generates the public documentation and download assets needed for publication.

## When To Use

Use this skill when you need to:
- start from inside `000-skills-repo`
- import a skill from another local folder
- normalize it for portability inside this repo
- create or update the matching Flowershow page
- build a one-click downloadable `.zip`
- decide at the end between `1. Publish now` and `2. Stop now`

## When Not To Use

Do not use this skill for ordinary edits to a skill that is already packaged correctly in this repo unless the task also includes repackaging or republishing.

## Output

The skill is designed to produce:

1. a canonical repo copy under `skills/<slug>/`
2. a rebuilt `.zip` inside that skill folder
3. a public Flowershow page under `docs/skills/<slug>.md`
4. an updated entry on the public skills index
5. a final numbered choice after the file prep is complete:
   - `1. Publish now`
   - `2. Stop now`

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`

## Example Requests

- “From this repo, import a local skill folder and package it.”
- “Ask me for the source directory, then make this skill transportable and create the public Flowershow page.”
- “Import this source skill, rebuild the zip, add the page to the index, then ask whether to publish.”
