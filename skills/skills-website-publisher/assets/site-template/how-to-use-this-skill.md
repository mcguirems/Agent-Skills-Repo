# How To Use This Skill

Use `$TARGET_SKILL_NAME` in ChatGPT to publish a standalone documentation and download site for the target skill.

## Before you start

- Confirm the target skill folder is complete and ready to distribute.
- Confirm Netlify is connected or authenticated before publication.
- Remove credentials, private data, caches, and unrelated files from any downloadable package.

## Standard use

1. Open ChatGPT.
2. Type `$TARGET_SKILL_NAME /path/to/target-skill`.
3. Review the result and complete any stated manual follow-up.

## Other operating modes

### With a specific target skill

1. Provide the target skill directory or identify the skill by name.
2. Provide an icon if one should be used.
3. Let the skill build the static site, downloadable skill archive, and Netlify deployment.

### Without an icon

1. Tell ChatGPT to continue without a supplied icon.
2. The skill creates a simple original icon that matches the technical editorial style.
3. Review the icon in the generated site before publication.

## After the skill finishes

1. Open or download the result using the link ChatGPT provides.
2. Complete any required manual steps.
3. Review the output for accuracy.

## Limitations and troubleshooting

- The skill creates the documentation website; it does not create the underlying operational skill.
- If Netlify authentication is missing, connect or authenticate Netlify and resume publication.
- If more than one target skill matches the request, choose the intended source folder before continuing.
