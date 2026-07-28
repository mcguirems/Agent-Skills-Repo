---
title: Blog Extraction
status: active
---

# Blog Extraction

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/blog-extraction/blog-extraction.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/blog-extraction)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/blog-extraction/SKILL.md)

## Purpose

`blog-extraction` turns an article, blog post, or uploaded document into two markdown outputs: a clean full-text extraction and a concise coaching or reference summary.

## When To Use

Use this skill when you need a repeatable workflow for:

- extracting article content cleanly
- preserving metadata and structure
- generating a compact coaching or reference summary
- applying consistent filenames and quality checks across many articles

## When Not To Use

Do not use this skill for:

- one-line article summaries
- research synthesis across many sources at once
- workflows that need only raw scraping without editorial cleanup
- tasks where the user explicitly wants just one output file

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `blog-extraction.zip`
- `references/output-templates.md`
- `source/blog-extraction-SKILL_CLAUDE.md`
- `source/blog-extraction_CLAUDE.skill`

## Packaging Notes

The original source instructions were written for a Claude-style runtime with non-portable tool names and hardcoded output paths. The packaged version keeps the workflow intent while normalizing it for Codex and other portable skill installs.

## Canonical Runtime Location

- `skills/blog-extraction/SKILL.md`

## Example Requests

- “Extract this article into the two markdown files.”
- “Use the standard blog extraction format for this PDF.”
- “Create the clean extraction and coaching summary for this URL.”
