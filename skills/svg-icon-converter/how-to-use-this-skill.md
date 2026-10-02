# How to use this skill

Invoke `$svg-icon-converter` and upload an SVG: “Convert this icon.” For pasted SVG, include the intended icon filename. The skill produces exactly nine SVGs in a ZIP with the original icon name.

Ask for changes in ordinary language. Filled and outline icons convert directly. If preserving a complex icon is unsupported, the assistant explains the specific issue before altering the artwork.

In ChatGPT Work, use a host with Python/file-processing support and download the returned ZIP. In Codex, run `python scripts/convert_svg.py INPUT_SVG OUTPUT_DIRECTORY` from the skill folder with a writable, fresh output directory.
