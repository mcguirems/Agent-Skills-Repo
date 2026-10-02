---
title: MVF SVG Icon Converter
description: "Last updated: October 2, 2026"
status: active
---

# MVF SVG Icon Converter

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/svg-icon-converter/svg-icon-converter.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/svg-icon-converter)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/svg-icon-converter/SKILL.md)

## Purpose

`svg-icon-converter` normalizes an uploaded or pasted SVG, preserves its geometry, and exports a ZIP containing a black default plus eight MyVeloFit brand-color variants.

## When To Use

Use this skill when you need to:

- convert a filled or outline SVG to the MyVeloFit format
- remove inconsistent inline color styling
- create the complete nine-file brand-color set
- receive the finished variants in one validated ZIP

## When Not To Use

Do not use this skill for raster images or SVGs that rely on unsupported features such as gradients, masks, clipping elements, embedded images, text, or advanced CSS. Those files require case-specific review.

## Output

The skill produces exactly nine SVG files:

1. one black default using `#000000`
2. eight variants using the documented MyVeloFit brand colors

The bundled Python converter verifies filenames, XML declarations, colors, and ZIP contents before completion.

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/openai.yaml`
- `scripts/convert_svg.py`
- `references/conversion-rules.md`
- filled and outline SVG examples
- user and team instructions
- `svg-icon-converter.zip`

## Installation Notes

The ZIP is the preferred installation artifact. It expands into one top-level `svg-icon-converter/` folder and includes the converter script and all required public references.

## Example Requests

- “Use `$svg-icon-converter` to convert this SVG.”
- “Create all nine MVF color variants from this icon.”
- “Normalize this outline SVG without changing its geometry.”
