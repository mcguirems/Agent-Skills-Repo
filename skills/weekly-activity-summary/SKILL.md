---
name: weekly-activity-summary
description: Create Mike McGuire’s MyVeloFit weekly work and investigation summary for standup meeting notes, combining Asana, PostHog notebooks and insights, Google Drive activity, relevant Slack action items, and available ChatGPT work. Use for /weekly-activity-summary, weekly work recaps, weekly standup updates, or revisions to this summary. Save a numbered Markdown file with live Asana project status updates and the established 1Writer-compatible format.
---

# Weekly Activity Summary

Create a concise, editable record of Mike’s work, investigations, decisions, and next steps. Use American spelling, direct language, and no emojis. Read [sources.md](references/sources.md) for source scope and discovery guidance. Follow [summary-template.md](assets/summary-template.md) for the exact output structure.

## Resolve the reporting period

- Use America/Toronto for date interpretation and source boundaries.
- Honor an explicit reporting range and standup date.
- For “last week,” use the previous Monday through Sunday. Default the standup date to the Monday following that period. Display both dates at the top.
- Use the standup date’s ISO week, padded to three digits, for the filename prefix. For example, the September 28–October 4, 2026 reporting period has an October 5 standup and filename `041-Weekly-Standup-Mike-Updates-05-Oct-2026.md`.
- Derive each prefix from the standup date; handle year changes instead of blindly incrementing the prior prefix. Honor a user-specified standup numbering scheme when provided.
- Do not ask for dates already established by the request or conversation.

## Collect evidence

1. Discover currently available connectors and follow their applicable skills. Perform read-only source collection. Do not modify tasks, analytics, documents, messages, or sharing.
2. Gather Asana tasks assigned to Mike, tasks created by Mike (including work assigned to others), and dated comments/review activity involving Mike. Include completed and incomplete work; distinguish creation, review, handoff, implementation, and launch. Read substantive task details before summarizing them.
3. Discover saved PostHog insights and notebooks created or modified during the period. Confirm the MyVeloFit project using a non-secret project list, then select it if required. Read notebook contents and metadata; do not rerun metrics just to write an activity summary.
4. Search Drive separately for created and modified files/folders during the period. Inspect relevant content or revisions when needed. Do not infer authorship, completion, or a particular edit from timestamps alone. Account for documents created during the period but modified later.
5. Search relevant public Slack messages authored by or mentioning Mike. Read meaningful action threads. Exclude greetings, social chatter, and duplicated Asana notifications. Follow connector permission rules for private messages.
6. Include relevant available prior ChatGPT work and user-supplied exports. Search broad recap windows without presupposing topics. Use Gmail only as a light, low-priority check; omit notification-only results.
7. Retain source, actor, activity date, artifact URL, outcome, and uncertainty internally. Do not put the evidence ledger or source coverage in the deliverable.

## Synthesize the work summary

- Group evidence by work topic; merge overlapping activity across sources.
- Attribute Mike’s contribution accurately. A task he created for another person is a handoff, not work he implemented.
- Use specific verbs such as defined, reviewed, investigated, documented, created, tested, and published. Avoid empty “continued” or “advanced” statements.
- Keep each work item to a short title and usually two to four bullets. Include useful artifact links in the relevant bullets.
- Record PostHog activity, insights explored, notebooks saved, and questions raised. Omit analytic counts, percentages, and impact claims unless verified for the correct cohort, dates, and denominator. Artifact dates and verified inventory counts may be used.
- Treat notebook narratives and AI exports as investigation records, not independent proof of causation, production fixes, survey launch, or schedules. Resolve contradictions using current evidence; omit unsupported claims.
- Distinguish proposed changes, open review, implementation, and verified launch. Preserve material blockers and uncertainty inside the relevant work bullets, without adding a separate notes section.
- Summarize Working on / Future from documented open actions and decisions. Do not invent ownership, deadlines, priority, or commitments.
- Preserve approved wording when editing the summary; make only requested changes unless correcting a factual problem.

## Retrieve Asana project statuses

- Fetch actual Asana project records and latest posted status updates. Use structured status types, update timestamps, summaries, and next steps. Do not derive a project status from task activity or copy AI-generated “On Track” claims without checking.
- Use the default project set in sources.md unless the user specifies another set.
- Present Project, Status, Latest update, and Summary in a Markdown table.
- Show the actual date of each status post, even when it predates the reporting period. Identify recorded milestones as recorded; do not treat old dates as reconfirmed schedules.
- If a project has no posted update, write “No recorded update” and an em dash for the date. Do not infer its health.
- If access fails, do not invent a status. Explain a material retrieval limitation briefly in chat if needed; do not add notes or disclaimers to the file.

## Format and save

- Start with `# Weekly Work Summary`, a blank line, the bold Reporting period label, another blank line, and the bold Standup label.
- Put a horizontal rule `***`, surrounded by blank lines, above each of the three H2 section headings. The first rule sits below the standup date. Do not add a rule above the document title or individual numbered work items.
- Use exactly these H2 headings: Work Completed or Advanced; Working on / Future; Project Status Updates — Asana.
- Number work items sequentially with bold titles. Leave a blank line after each title. Indent their bullet lists by four spaces so 1Writer recognizes the nested lists, including after item 10.
- Keep Working on / Future as an unindented H2 heading. Use regular, unindented `- ` bullets beneath it with a blank line after the heading. Never indent these bullets by four spaces: without a parent list they become a code block.
- Keep the project-status table unindented. Use a valid separator row and one line per project; escape any literal pipes inside cells.
- Do not append Source Coverage, methodological notes, general caveats, meta-commentary, or an offer to continue.
- Inspect the generated Markdown for accidental code blocks, collapsed numbering, heading/list spacing, table structure, correct dates and filename, and residual placeholders.
- Save the `.md` artifact through the runtime’s available file or artifact workflow. Use the Library workflow when available; otherwise save to the user’s requested destination or the current workspace. When editing, resolve and update the existing summary rather than creating a duplicate; create a new weekly file when appropriate.
- After saving, provide the exact local output path as a clickable link when the runtime supports local file links.
- Keep the final chat response short and provide the file link. Do not display the entire report again unless requested.
- Do not create a recurring automation solely because this skill generates weekly reports. Create one only when the user explicitly requests scheduling.
