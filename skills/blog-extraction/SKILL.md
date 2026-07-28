---
name: "blog-extraction"
description: "Use when the user wants a blog post, article, or uploaded document converted into two markdown outputs: a clean full-text extraction and a concise coaching or reference summary. Best fit for repeatable article-processing workflows that need consistent filenames, metadata capture, and quality checks."
---

# Blog Extraction

Use this skill to turn a URL or uploaded article document into two markdown files:

1. A clean full-text extraction with source metadata
2. A concise coaching or reference summary

## Workflow
1. Determine the source type.
   - Accept a URL or a local `.eml`, `.pdf`, `.md`, or `.txt` file.
   - If the source is a URL and includes tracking parameters, prefer the canonical page URL when possible.
2. Collect the content with tools available in the current runtime.
   - For web pages, use the available browsing or fetch tools for the current agent.
   - For local files, read or extract text with the available shell or file tools.
   - If content extraction is partial, note the limitation explicitly rather than inventing missing text.
3. Produce the full extraction markdown file.
   - Preserve the article title, structure, headings, lists, tables, quotes, and useful references.
   - Strip navigation, ads, cookie notices, comments, related links, and other non-article clutter.
   - Put source metadata at the top: URL or file origin, author if known, published date if known, and organization.
4. Produce the coaching or reference summary markdown file.
   - Keep only durable coaching points, reference insights, progressions, comparisons, and takeaways.
   - Convert comparisons or progressions into tables when that improves scanability.
   - End with one tight takeaway line that can stand alone.
5. Save both files using the required naming pattern.
   - Full extraction: `[Source] - [Article Title].md`
   - Summary: `COACHING SUMMARY - [Article Title].md`
6. Return both files together.
   - Present the summary first and the full extraction second when the runtime supports file presentation ordering.

## Output rules
- Always produce both files unless the user explicitly changes the workflow.
- Do not pad the summary with narrative filler.
- Preserve article meaning and sequence in the full extraction while cleaning non-content noise.
- Flag paywalls, missing metadata, partial fetches, or ambiguous authorship directly in the output.
- Prefer neutral, portable instructions over runtime-specific paths or tool names.

## Naming conventions by source

| Source | File 1 Prefix |
|---|---|
| GSMBC blog | `GSMBC - ` |
| BetterRide | `BetterRide - ` |
| Singletracks | `Singletracks - ` |
| RLC Hub | `RLC Hub - ` |
| Email (`.eml`) | `[Publication] - ` |
| PDF | `[Author-or-Org] - ` |
| Unknown source | `[Domain] - ` |

## Quality checks
- Full extraction includes source metadata at the top
- Full extraction removes navigation, ads, cookie banners, social prompts, and comments
- Summary contains only coaching or reference value
- Summary includes a one-line takeaway
- Both filenames follow the expected convention
- Any partial or uncertain extraction is clearly labeled

## Edge cases
- If the article is behind a paywall, extract only the accessible content and mark it as partial.
- If the article is very short, still produce both files in the same format.
- If the article is a gear or product review, include a `Coaching Application` or `Relevance for Riders` section in the summary.
- If the same article has already been processed in the current task context, confirm whether the user wants a refresh before duplicating work.

## Provenance
- The original Claude-authored source instructions are preserved in `source/blog-extraction-SKILL_CLAUDE.md` and `source/blog-extraction_CLAUDE.skill`.
