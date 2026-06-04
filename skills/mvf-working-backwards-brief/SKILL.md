---
name: "mvf-working-backwards-brief"
description: "Use when turning a MyVeloFit project brief into a Working Backwards document in Amazon-style PR/FAQ format. Produces a press release, customer FAQ, and internal FAQ that match MyVeloFit language, product framing, and launch planning expectations while surfacing missing launch assumptions explicitly."
---

# MyVeloFit Working Backwards Brief

Use this skill after a project brief exists or when the user can provide enough equivalent context to simulate one.

## Workflow
1. Review the project brief or equivalent source material before writing.
2. Confirm only the missing launch-shaping details that materially affect positioning.
   - Examples: spokesperson, customer persona for quotes, headline tone, included services, primary CTA, launch timing.
3. Draft the press release first using `references/working-backwards-template.md`.
4. Draft the customer FAQ next.
5. Draft the internal FAQ last, covering rollout, technical considerations, support implications, and open questions.

## Output rules
- Output in markdown.
- Keep the voice clear, benefit-led, and credible.
- Focus on rider outcomes, ease, comfort, performance, and practical value.
- Quotes should sound realistic rather than promotional.
- If launch facts are missing, mark them clearly instead of inventing certainty.

## Runtime references
- Read `references/working-backwards-template.md` for required structure and section prompts.
- Read `references/company-context.md` for approved company and product framing.
- Read `references/example-brief-notes.md` for style cues from the sample Working Backwards briefs.

## Assets
- Original PDFs from the source GPT are preserved in `assets/source-pdfs/` for packaging completeness and fidelity checks.
