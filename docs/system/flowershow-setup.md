---
title: Flowershow Setup
description: How to publish this repository as a Flowershow site.
showToc: true
---

# Flowershow Setup

## Recommended Structure

The current documentation structure is:

```text
docs/
  index.md
  skills/
    index.md
    asana-small-task-writer.md
  system/
    index.md
    flowershow-setup.md
```

This is a good Flowershow structure for a documentation-style site:
- each section has its own landing page
- each publishable page lives under `docs/`
- skill runtime assets remain separate under `skills/`

## Recommended Publishing Model

Use this repository as the canonical working repo, but publish only the human-facing documentation layer in Flowershow.

That means:
- `skills/` remains the runtime/archive layer
- `docs/` becomes the website layer

## Flowershow Setup Steps

1. Create or sign in to your Flowershow account.
2. Connect the GitHub repository:
   - `mcguirems/Agent-Skills-Repo`
3. In the Flowershow site settings, use the repository as the content source.
4. If Flowershow lets you choose a content root, set it to `docs/`.
5. If Flowershow does not support a `docs/` content root for this workflow, use repo-root publishing and configure filtering so only the docs layer is published.
6. Enable auto-sync if you want Git pushes to refresh the site automatically.

## Site Configuration

Flowershow supports a root-level `config.json` for site settings, navigation, and content filtering.

Based on the current official docs, useful configuration areas include:
- navigation bar links
- sidebar behavior
- content filtering
- theme selection

Example navigation shape from official docs:

```json
{
  "nav": {
    "links": [
      {
        "href": "/skills",
        "name": "Skills"
      }
    ]
  }
}
```

Example content filtering shape from official docs:

```json
{
  "contentInclude": [
    "/docs"
  ]
}
```

Important note:
- Paths in `contentInclude` and `contentExclude` are relative to the Flowershow content root.
- If your content root is already `docs/`, you should not also include `/docs` again.

## Recommendation For This Repo

Preferred setup:
- content root = `docs/`

Fallback setup:
- content root = repository root
- use `contentInclude` / `contentExclude` in `config.json` to publish only the docs content

The preferred setup is cleaner because it avoids exposing planning and runtime folders in the published site navigation.

## Official References

I verified the following from official Flowershow documentation:
- Flowershow supports GitHub-connected publishing and auto-sync
- `config.json` is the root configuration file
- `contentInclude` and `contentExclude` control published content
- section landing pages can be created with markdown files inside folders

Official docs used:
- https://flowershow.app/docs/getting-started
- https://flowershow.app/docs/reference/config-file
- https://flowershow.app/docs/reference/content-filtering
- https://flowershow.app/docs/reference/navbar
- https://flowershow.app/docs/reference/sidebar
