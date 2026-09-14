---
name: asana-new-bug-logger
description: Find or convert a MyVeloFit Slack message or thread reporting a product, UX, UI, website, mobile, or B2B bug into a standardized untriaged task in Asana project 021. Use when someone invokes asana-new-bug-logger, provides a Slack link to log, or asks to find recent Slack discussions that could become bugs. Do not use to scope the fix, propose a solution, create the later development task, or add work to project 101.
---

# Asana New Bug Logger

Create a faithful intake record from the Slack evidence. Keep intake separate from Mike's later triage and the Asana Small Task Writer workflow.

## Choose the mode

### Slack link supplied

Read that exact message or thread and create the requested bug from it. Do not search for alternatives.

### No Slack link supplied

1. Identify the invoking Slack user when possible.
2. Search all messages and threads from all users during the last 14 days in `#bugs-ui-ux-problem-reports` (`C082WEB869Y`). Inspect likely bug reports and their thread context.
3. If that channel yields no unlogged candidate, search only the active user's public Slack messages from the last 14 days across other channels. Do not search other people's activity outside `#bugs-ui-ux-problem-reports`.
4. Compare every candidate against all tasks in project 021 before presenting it.
5. Present up to five unlogged candidates with a short title, reporter, date, channel, one-line reason, and Slack permalink. Rank the clearest candidate first.
6. List discussions explicitly confirmed as fixed or resolved in a separate `Resolved — no task required` section. Do not treat them as creation candidates unless the user requests historical logging.
7. Ask the user which candidate to convert. Do not create a task until they select one, unless they explicitly requested a uniquely identifiable candidate such as “the most recent bug.”

Search public Slack content by default. Before searching the active user's private channels, DMs, or group DMs, request and receive explicit permission. Do not search other people's private activity. Do not expose unrelated conversation content; include only the minimum context needed to identify a possible bug.

Treat a discussion as a candidate only when it describes observable incorrect behavior, an inconsistency, an error, or a broken customer flow. Do not propose general complaints, questions, feature ideas, or unclear comments as bugs. If Slack indexing, permissions, pagination, or inaccessible files may have limited the scan, state that limitation with the results.

## Prevent duplicates

Search all project 021 tasks, including incomplete, completed, obsolete, and not-required items. Compare the Slack candidate against:

- The exact Slack permalink or source message.
- The affected screen, feature, or workflow.
- The observed and expected behavior.
- Similar task titles and descriptions.

Treat an exact source-link match as a duplicate. Treat a strong behavior-and-context match as a likely duplicate even when the wording differs. Exclude confirmed duplicates from the candidate list and provide the existing Asana task link when useful. If the match is uncertain, show the possible existing task beside the Slack candidate and ask the user whether it is new. Repeat the duplicate check immediately before creation. Never create a new task when a confirmed duplicate exists; return the existing task instead.

An explicit request for a distinct variant is not a duplicate when it changes a material dimension such as customer type, account tier, platform, or affected workflow. Create the variant only when the user clearly requests it, explain the distinction in the description, and link both the original Asana task and Slack source.

## Workflow

1. Read the selected Slack parent message and its complete thread. Read linked or attached evidence needed to understand the report.
2. Extract only supported facts: reporter, observed behavior, expected or questionable behavior, platform, browser, affected area, priority, support link, and attachments.
3. Distinguish direct statements from reasonable visual inferences. Do not invent reproduction steps, scope, root cause, acceptance criteria, or a solution.
4. If the discussion is not actually a bug report or lacks enough information to identify the problem, ask one focused question instead of creating a task.
5. Check the selected report against all tasks in project 021 using the duplicate rules above.
6. When the user supplies a Slack link and explicitly asks to add or submit a non-duplicate bug, create the task immediately. Without a Slack link, follow the discovery mode above.
7. Verify the created task. Do not modify, triage, complete, or move it afterward.
8. Publish a confirmation in the ChatGPT conversation. Use the heading `New bug created from Slack report:` followed by the new Asana task title and clickable link. Do not use duplicate language for a newly created task. Follow it with this note:

   `Screenshots must be added by you. You can download them from Slack, then open the bug using the link above and add them under “+ Attachments.”`

If no task was created because the report already exists, instead say `No new bug was created. This Slack report is already logged:` and provide the existing Asana task link or links. Do not show the screenshot-upload reminder when no new task was created.

## Asana destination

- Always use this destination. Do not ask about or offer another project.
- Project: `021 - Product Bugs and Changes` (`1208572728438762`)
- Canonical destination: `https://app.asana.com/1/1204834634202873/project/1208572728438762/list/1208573259956841`
- Section: `Incoming - New` (`1209016259831229`)
- Assignee: none
- Due date: none
- Leave `Initiative`, `PM Reviewed`, `Asana Instruction`, and `Status` unset.

## Task content

Write a concise, specific title describing the mismatch. Use this description order:

```text
Reported by:
<Slack author's real name>

Title:
<task title>

Describe the issue, problem or inconsistency:
<what was observed>

<expected behavior or why the behavior is questionable, only when supported>

Source:
<Slack permalink>

Supporting evidence:
<file names or links; say when a file remains attached to the Slack source>

Intake notes:
<material missing facts, inferences, or known resolution state; omit when unnecessary>
```

Preserve the Slack permalink so later triage can inspect the full discussion and its files. Never say a Slack file is attached to Asana unless the attachment operation actually succeeded.

## Custom fields

Set a field only from direct evidence or a clear visual inference. When browser is absent, use `Not sure`; when area is unclear, use `Not Categorized`. Leave platform and priority unset when unknown. Resolve the Slack reporter to an Asana user before setting the people field; retain the name in the description even if resolution fails.

| Field | Field GID | Options |
| --- | --- | --- |
| Priority | `1208572732701992` | High `1208572732701993`; Medium `1208572732701994`; Low `1208572732701995`; Ignore `1209016260291330` |
| Browser | `1208572732701997` | Not sure `1208572732701998`; Chrome `1208572732701999`; Safari `1208572732702000`; IE `1208572732702001`; Firefox `1208572732702002`; Other Browser `1208595368754099` |
| Platform | `1208595368754118` | Mobile iOS `1208595368754119`; Mobile Android `1208595368754120`; Tablet `1208595368754121`; Desktop `1208595368754122` |
| Reported By | `1208594588928797` | Asana user GID array |
| Area Affected | `1212471681319668` | Website `1212471681319672`; CX `1212471681319673`; B2B Specific `1212471681319671`; Platform `1212471681319669`; Mobile `1212471681319670`; Not Categorized `1212504471911634` |

Prefer a plain-text Asana description for reliable creation. If creation partially or fully fails, report the failure and check whether a task was created before retrying; never create a duplicate blindly.

## Boundary after creation

Stop at intake. Mike later validates accuracy, determines scope or a solution, and may invoke Asana Small Task Writer to create a separate development task for project 101 review and backlog.
