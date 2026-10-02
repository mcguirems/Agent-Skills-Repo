---
name: svg-icon-converter
description: Normalize uploaded or pasted MyVeloFit SVG icons, preserve geometry, and export a ZIP containing a black default and eight brand color variants. Use for SVG conversion and recoloring requests.
---

# MVF SVG Icon Converter

## Workflow

1. Read the actual uploaded SVG from disk. Also check for pasted SVG code before reporting that no source was provided. Ask for another copy only if file reading fails and no valid pasted code exists.
2. Derive the icon name from the filename, stripping only `.svg` and one recognized trailing brand color suffix. For pasted code without a supplied name, ask “What should the icon name be?” Do not invent names.
3. Use [the conversion script](scripts/convert_svg.py): `python scripts/convert_svg.py INPUT_SVG OUTPUT_DIRECTORY`. Choose a writable directory with no existing target files. For pasted code, write it to a named temporary SVG before running the script.
4. Follow [the conversion rules](references/conversion-rules.md). Preserve geometry, transforms, viewBox, and geometry-related stroke styling. Do not rasterize or add/remove shapes.
5. Verify the ZIP exists, opens, and contains exactly nine SVGs with the required filenames. Verify each SVG has one XML declaration on the first line and the correct style color.
6. Return a downloadable ZIP. After its link, show only detected type, icon name, and ZIP filename.

Do not claim completion until the ZIP is created and verified. On failure, explain the specific error; do not return partial results. Ordinary filled and outline icons need no advance confirmation. If mixed artwork or unsupported CSS/elements prevent preservation, explain the limitation and ask about the particular change needed rather than silently changing the artwork. The script uses a conservative supported subset; it is not a general SVG renderer.

## Runtime

Require file reading/writing, XML processing, ZIP creation, and a writable host-supplied output directory. The bundled script uses Python 3 and its standard library.

### ChatGPT Work

Use the available Python/file-processing environment, read uploaded files from disk, run the script, and return the generated ZIP as a downloadable file. If the environment cannot execute scripts or create files, explain that limitation.

### Codex

Run the bundled script with the input path and an appropriate workspace output directory. Return the created ZIP using the host's downloadable-file mechanism.

## Resources

Read the [filled example](references/icon-example-filled.svg) and [outline example](references/icon-example-outline.svg) when checking expected rendering rules. For human guidance, see [usage](how-to-use-this-skill.md), [team instructions](team-instructions.md), and [installation](Install-this-skill.md).
