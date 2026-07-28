---
name: blog-extraction
description: Extract and summarise any blog post, article, or web page into two structured markdown files: a clean full-text extraction and a concise coaching/reference summary. Use this skill whenever the user provides a URL and asks to extract, parse, save, or create files from a blog or article — including phrases like "do the 2 files for this", "extract this blog", "same format as before", "create the markdown files", or "save this article". Also use when the user uploads an .eml, .pdf, or .md file containing article content and asks for the same treatment. Always produce both files — never just one.
---

# Blog Extraction Skill

Produces two markdown files from any blog post, article, or uploaded document:

1. **Full extraction** — clean article text, nav/ads stripped, source metadata at top
2. **Coaching/reference summary** — concise, structured coaching points only

---

## Step 1: Get the Content

**From a URL:**
- Use `web_fetch` to retrieve the page
- If the URL is too long, strip tracking parameters (everything after `?`) and try again
- If fetch fails, use `web_search` to find the article, then fetch the result URL

**From an uploaded file:**
- `.eml` — use `bash_tool` to `cat` the file and extract body text
- `.pdf` — use `pdftotext` via `bash_tool`
- `.md` or `.txt` — read directly from `/mnt/user-data/uploads/`

---

## Step 2: Create File 1 — Full Article Extraction

**Filename format:** `[Source] - [Article Title].md`

Examples:
- `GSMBC - How to Corner - Stability and Balance.md`
- `BetterRide - Mountain Bike Bump Jump.md`
- `Singletracks - 3 Ways to Eliminate Rear Wheel Slip.md`

**File structure:**
````
# [Article Title]

**Source:** [full URL]
**Author:** [author name if available]
**Published:** [date if available]
**Organisation:** [org/publication name]

---

[Clean article body — all section headings, paragraphs, lists preserved]
[Remove: navigation, ads, related articles, comments, social links, cookie notices]

---

*Source: [Publication] — [domain]*
````

**Content rules:**
- Preserve all section headings as ##
- Preserve lists, tables, quotes, and drill progressions exactly
- Keep research references if present
- Remove everything that is not article content

---

## Step 3: Create File 2 — Coaching/Reference Summary

**Filename format:** `COACHING SUMMARY - [Article Title].md`

Examples:
- `COACHING SUMMARY - How to Corner - Stability and Balance.md`
- `COACHING SUMMARY - Bump Jump.md`

**File structure:**
````
# Coaching Summary: [Article Title]

**Source:** [Publication] / [Author if known] — [Date]
**Topic:** [One-line description of what the article covers]

---

## Core Concept
[The single most important idea. One short paragraph or a pull quote.]

---

## [Section headings as needed]
[Coaching points only — no filler, no repetition]
[Use tables for comparisons, progressions, or before/after]
[Use prose for concepts that do not lend themselves to tables]

---

## One-Line Coaching Takeaway
> [A single sentence that captures the key lesson]

---

*Source: [Publication] — [domain]*
````

**Summary rules:**
- Coaching points only — no narrative, no filler
- Convert drill progressions to numbered tables where possible
- Convert comparisons to tables (expert vs beginner, tall vs low, etc.)
- Flag connections to other vault content when obvious
- Keep the takeaway line tight — it should stand alone

---

## Step 4: Save and Present Both Files

Save both files to `/mnt/user-data/outputs/` and call `present_files` with both paths — summary first, full article second.

---

## Naming Conventions by Source

| Source | File 1 Prefix |
|---|---|
| GSMBC blog | `GSMBC - ` |
| BetterRide | `BetterRide - ` |
| Singletracks | `Singletracks - ` |
| RLC Hub | `RLC Hub - ` |
| Email (.eml) | `[Publication] - ` |
| PDF | `[Author/Org] - ` |
| Unknown source | `[Domain] - ` |

---

## Quality Checks Before Saving

- All nav, ads, social links, and cookie notices removed from File 1
- Source metadata (URL, author, date, org) at top of File 1
- File 2 has no filler sentences — every line is a coaching point
- File 2 has a one-line takeaway
- Both filenames follow naming convention
- `present_files` called with summary first

---

## Edge Cases

**Article behind a paywall:** Fetch what is available, note content may be partial.

**Very short article under 500 words:** Still produce both files — the summary will be brief but the format stays consistent.

**Gear or product review:** File 2 should include a Coaching Application or Relevance for Riders section rather than pure technique points.

**Already extracted in this session:** Flag to the user rather than duplicating.
