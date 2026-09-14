# Skills Website Publisher

`skills-website-publisher` builds a standalone Netlify documentation website for an existing ChatGPT or Codex skill.

It packages a complete static site with overview, usage instructions, team instructions, a creation article, a validated skill download, and the technical editorial visual system bundled with this package.

## When to use it

Use this skill when you have a completed skill and want to publish a public documentation and download site for teammates or external users.

Good fits include:

- a reusable skill landing page
- a public download page for an installable skill archive
- a short team instruction page
- a case-study page explaining how the skill was created
- a Netlify-hosted static site for skill documentation

## When not to use it

Do not use this skill to create the underlying operational skill from scratch. Finish, test, and package the target skill first.

Do not use it when the target skill contains credentials, private customer data, local-only file references, or unreleased internal material that cannot be published.

## Included files

- `SKILL.md` - agent instructions for building and publishing the skill website.
- `Install-this-skill.md` - platform-neutral installation instructions.
- `agents/openai.yaml` - optional OpenAI agent metadata.
- `assets/icon.svg` - skill icon.
- `assets/site-template/` - reusable Markdown and CSS website templates.
- `references/site-spec.md` - required website structure, content mapping, visual system, and QA rules.
- `skills-website-publisher.zip` - installable archive built from this folder.

## Typical invocation

```text
$skills-website-publisher /path/to/target-skill
```

The skill will inspect the target skill, ask for or generate an icon, build the site into `dist/`, validate links and downloads, publish to Netlify, and report the production URL.
