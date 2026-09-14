---
name: skills-website-publisher
description: Build and publish a standalone Netlify documentation website for an existing ChatGPT skill. Use when the user wants a downloadable skill website, a public skill landing page, team instructions, or a site explaining how a skill works and was created. Reuse the bundled technical editorial CSS and page structure exactly unless the user requests a visual change.
---

# Skills Website Publisher

Create a complete static documentation site for one existing skill and publish it to Netlify.

## Required inputs

Identify the target skill from the user's message or skill directory. If more than one skill could be meant, ask which one. Read its complete `SKILL.md`, `agents/openai.yaml`, and only the supporting resources needed to explain its behavior accurately.

Ask whether the user has an icon. If they do, use it. If they do not, offer to create one; if they want the work to continue without choosing, create a simple original icon consistent with the site's technical style. Never reuse another skill's branded icon.

## Required outputs

Create a maintainable static site project containing:

- `index.html` — summary, value proposition, operating modes, capabilities, and download CTA.
- `how-to-use.html` — rendered from `how-to-use-this-skill.md`.
- `team-instructions.html` — rendered from `team-instructions.md`.
- `how-i-created-this.html` — detailed article describing the decisions, workflow, safeguards, testing, and reusable lessons behind the skill.
- `how-to-use-this-skill.md` — complete end-user instructions for the skill.
- `team-instructions.md` — concise instructions suitable for sharing with a team.
- `styles.css` — copy [the bundled stylesheet](assets/site-template/styles.css) unchanged unless the user requests a visual edit.
- `assets/icon.*` — the supplied or newly created icon.
- `downloads/<skill-name>.zip` — a validated, reusable copy of the target skill when the user is authorized to distribute it. Exclude credentials, private data, caches, and unrelated files.

Use the Markdown documents as the source of truth for the corresponding website pages. Do not maintain conflicting HTML-only copy.

## Content rules

Derive claims from the target skill. Do not invent capabilities, permissions, integrations, or test results.

Keep `how-to-use-this-skill.md` practical and complete. Include prerequisites, invocation examples, operating modes, expected results, manual follow-up, limitations, and troubleshooting when relevant.

Keep `team-instructions.md` brief and shareable. Include what the skill does, how to start it, the most common usage modes, what happens next, and any required human review.

Write “How I created this” as a detailed but readable case study. Explain the problem, requirements, workflow design, duplicate or safety controls, human handoffs, testing, iteration, packaging, and publication. Never expose secrets, private messages, customer data, or internal credentials.

## Visual system

Read [site-spec.md](references/site-spec.md) before building. Copy the bundled stylesheet exactly. Follow the existing page hierarchy and component classes so the result visually matches the reference site. Customize content, metadata, icon, download filename, and accessible alt text.

## Build and verification

Build into a `dist/` directory. Verify:

1. Every navigation link and CTA resolves.
2. Both required Markdown files exist and their content appears on the matching pages.
3. The skill download opens and the archive validates.
4. The icon and favicon load.
5. Pages work at desktop and mobile widths without horizontal overflow.
6. Page titles, descriptions, headings, and link labels match the target skill.
7. No credential, environment file, private data, dependency directory, or build cache is included.

## Netlify publication

Publish the verified `dist/` directory to Netlify using the user's connected or authenticated Netlify account. If the user identifies an existing Netlify site, deploy to that site. Otherwise create a new site with an available, readable name based on the skill.

Do not ask the user to paste access tokens into chat. If Netlify authentication is unavailable, preserve the completed site and ask the user to connect or authenticate Netlify, then resume publication.

After deployment, open the production URL and verify the home page plus each navigation route. Report the public Netlify URL and the local project location. Mention any remaining manual step.
