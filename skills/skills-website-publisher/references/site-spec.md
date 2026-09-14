# Site specification

## Page structure

Use the same header and footer across all pages.

The overview page contains:

1. Sticky navigation with icon, skill name, Overview, How to use, Team instructions, and How I created this.
2. Hero with eyebrow, large title, short description, icon, primary download button, and secondary instructions button.
3. A two-card operating-mode section when the skill has distinct modes; otherwise use the closest meaningful two-part workflow.
4. Three capability cards.
5. A final human-in-the-loop or next-step card.
6. Compact footer attribution.

The instruction pages use `.article` for a readable single-column layout. Use `.code` for commands and `.note` for warnings or manual handoffs.

## Content mapping

- Render `how-to-use-this-skill.md` into `how-to-use.html` without changing its meaning.
- Render `team-instructions.md` into `team-instructions.html` without changing its meaning.
- Link both pages in primary navigation.
- Provide the Markdown files as downloads when useful.
- Keep overview copy short; put detailed explanation in the article pages.

## Styling

Copy `assets/site-template/styles.css` into the site root. Preserve all existing CSS declarations and class names. Add only the smallest necessary rules for new semantic elements, and place additions after the original stylesheet with a short comment.

Use the bundled color system:

- Ink: `#101321`
- Muted: `#62677b`
- Paper: `#f7f7fb`
- Panel: `#ffffff`
- Purple: `#59569f`
- Line: `#dfe1ec`
- Code: `#181a27`
- Accent: `#f2470a`

Use monospace body/interface type and system sans-serif display headings exactly as defined in the stylesheet. Keep the 1080px maximum content width, restrained borders, eight-pixel card radii, and 760px responsive breakpoint.

## Accessibility and quality

- Use semantic HTML and one `h1` per page.
- Provide meaningful page titles and descriptions.
- Use descriptive alt text unless an image is decorative.
- Preserve visible keyboard focus supplied by the browser; do not remove outlines.
- Keep sufficient contrast and do not encode meaning by color alone.
- Avoid JavaScript unless the target skill genuinely needs interactive behavior.
