# Skill Repo Publisher

## Purpose

`skill-repo-publisher` imports an existing skill from another local folder into this repo, normalizes it into a portable package, creates the public Flowershow page, and builds the installable `.zip`.

## When To Use

Use this skill when you are already working inside `000-skills-repo` and have a skill somewhere else on disk that you want to:
- copy it into this repo under `skills/<slug>/`
- repair portability issues in the repo copy
- create a public skill page under `docs/skills/`
- build a one-click downloadable `.zip`
- choose at the end between `1. Publish now` and `2. Stop now`

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`

## Transportability

This package is intended to be copied as a self-contained folder into another agent's skills directory.
Use the generated `skill-repo-publisher.zip` distribution artifact when you want a one-file handoff for installation in another environment.

## Canonical Path

- `skills/skill-repo-publisher/SKILL.md`
