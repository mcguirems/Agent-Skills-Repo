# Conversion rules

Generate one black default and eight branded color variants: exactly nine SVG files.

| Filename | Color |
| --- | --- |
| `{icon}.svg` | `#000000` |
| `{icon}-2DC75C.svg` | `#2DC75C` |
| `{icon}-F3D127.svg` | `#F3D127` |
| `{icon}-F32727.svg` | `#F32727` |
| `{icon}-B0B0B0.svg` | `#B0B0B0` |
| `{icon}-F2470A.svg` | `#F2470A` |
| `{icon}-000069.svg` | `#000069` |
| `{icon}-555299.svg` | `#555299` |
| `{icon}-007AFF.svg` | `#007AFF` |

Use `{icon}.zip`, with exactly these nine SVGs at the archive root. Preserve the filename base; strip only the SVG extension and a recognized trailing suffix from the table. Do not invent names for pasted code.

## Rendering and normalization

Resolve simple class CSS, inline style, presentation attributes, and inherited styling before classifying. Treat the icon as outline when most drawable elements resolve to `fill: none`, or all drawables have strokes without specified fills. Otherwise classify as filled. Reject mixed filled/stroked artwork when these uniform rules would change its appearance.

Filled CSS: `.cls-1 { fill: #HEX; stroke-width: 0px; }`.
Outline CSS: `.cls-1 { fill: none; stroke: #HEX; }`.

Apply class `cls-1` to path, rect, circle, line, polyline, polygon, and ellipse. Put all output color in one style block under defs. Preserve non-color rendering properties, including stroke widths, caps, joins, dash settings, fill rules, and opacity. Resolve inherited stroke settings onto shapes before removing old CSS. Retain local group opacity so its compositing behavior is preserved.

Normalize root ID/data-name to `Layer_1`/`Layer 1`, use the SVG namespace, retain the original viewBox, and remove width/height sizing. Preserve root transforms and other rendering attributes rather than discarding them to satisfy a minimal attribute template. Remove inline color attributes and old class CSS after resolving them. Preserve every shape, its geometry attributes, and transforms. Existing geometry-related stroke widths remain on elements.

Write exactly one UTF-8 XML declaration as the first line; remove duplicate declarations before parsing. Pretty-print with one element per line and indented defs/style content.

## Supported subset

Support SVG/g containers, defs/style, title/desc, and the seven drawable element types above. Support simple class selectors and common presentation properties. Stop clearly for gradients, masks, clipping elements, use/text/image elements, nested SVG, unresolved classes, advanced CSS, DTD/entities, or missing viewBox. These need case-specific review; do not silently simplify them. If target files already exist, use a fresh output directory. Stage the complete result and verify it before moving files into place.
