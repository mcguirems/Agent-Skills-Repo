---
name: "mvf-project-brief-creator"
description: "Use when drafting or refining a MyVeloFit project brief for a feature, app initiative, launch, strategic update, or scoped workstream. Converts rough inputs into MyVeloFit's seven-section brief format, identifies missing decisions, aligns rationale and metrics to company strategy, and preserves MyVeloFit terminology and markdown output conventions."
---

# MyVeloFit Project Brief Creator

Use this skill to turn a rough project concept, Asana export, task list, or early product notes into a complete MyVeloFit project brief in markdown.

## Workflow
1. Start with the project rationale.
   - Draft the "why now" based on the user's description and the strategic context in `references/company-context.md`.
2. Identify missing inputs before finalizing.
   - Ask only for information that materially affects scope, ownership, milestones, KPIs, or success metrics.
   - If facts are still missing, insert `[Update Required]` rather than inventing specifics.
3. Produce the brief in the standard seven-section structure from `references/project-brief-template.md`.
4. Keep the brief operational.
   - Confirm scope boundaries, investigation items, role ownership, dependencies, and milestone dates where possible.
   - Reuse relevant KPI patterns from the reference material, but tailor them to the initiative.

## Output rules
- Output in markdown unless the user asks for another format.
- Preserve MyVeloFit language, product names, and documentation style.
- Use concise business prose with short paragraphs and bullets where they improve scanability.
- Do not leave placeholder strategy statements that are not grounded in the provided inputs or reference material.

## Runtime references
- Read `references/project-brief-template.md` for the required section order and field expectations.
- Read `references/company-context.md` when you need mission, growth, product, or KPI context.
- Read `references/example-project-brief-notes.md` when you need formatting cues from the sample brief.

## Assets
- Original PDFs from the source GPT are preserved in `assets/source-pdfs/` for packaging completeness and fidelity checks.

## Provenance
- `source/gpt-instructions.md` preserves the original GPT instruction source used to derive this skill package.
