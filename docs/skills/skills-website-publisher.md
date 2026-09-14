---
title: Skills Website Publisher
status: active
---

# Skills Website Publisher

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/skills-website-publisher/skills-website-publisher.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/skills-website-publisher)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/skills-website-publisher/SKILL.md)

## Purpose

`skills-website-publisher` builds and publishes a standalone Netlify documentation website for an existing ChatGPT or Codex skill.

The generated site explains what the target skill does, how to use it, how it was created, what humans still need to review, and where to download a reusable skill package.

## When To Use

Use this skill when you need to:

- create a public skill landing page
- publish a Netlify-hosted documentation site for a completed skill
- generate usage instructions and team instructions
- document the creation process as a readable case study
- include a validated downloadable skill archive

## When Not To Use

Do not use this skill to create the underlying operational skill. The target skill should already be complete, tested, and safe to distribute.

Do not use it to publish private credentials, internal customer data, local-only paths, or any skill package that has not been reviewed for distribution.

## Output

The skill is designed to produce a static site project containing:

1. `index.html`
2. `how-to-use.html`
3. `team-instructions.html`
4. `how-i-created-this.html`
5. `how-to-use-this-skill.md`
6. `team-instructions.md`
7. `styles.css`
8. `assets/icon.*`
9. `downloads/<skill-name>.zip`

It then publishes the verified `dist/` directory to Netlify and reports the production URL.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/openai.yaml`
- `assets/icon.svg`
- `assets/site-template/how-to-use-this-skill.md`
- `assets/site-template/team-instructions.md`
- `assets/site-template/styles.css`
- `references/site-spec.md`

## Example Request

```text
$skills-website-publisher /path/to/my-finished-skill
```
