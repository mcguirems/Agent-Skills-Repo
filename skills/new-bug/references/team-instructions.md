# New Bug Skill — Team Instructions v1

## Purpose

Use `$new-bug` in ChatGPT to turn Slack bug reports into standardized, untriaged tasks in **021 — Product Bugs and Changes**.

The skill checks project 021 for existing reports before creating a task. It does not scope the solution or create a development task in project 101.

## Before using the skill

You need:

1. Access to the shared **New Bug** skill in ChatGPT.
2. A connected Slack account with access to the relevant conversation.
3. A connected Asana account with access to project 021.

Run the skill from **ChatGPT**. It cannot currently be triggered by mentioning `@Codex` inside Slack.

## Option 1: Create a bug from a Slack link

Copy the Slack message or thread link and enter:

> `$new-bug [Slack link]`

The skill will:

1. Read the selected message and its thread.
2. Review the available supporting evidence.
3. Check all project 021 tasks for duplicates.
4. Create the bug in **Incoming — New** when it is not already logged.
5. Return a link to the new Asana task.

If the bug already exists, no task will be created. The skill will return the existing Asana task link.

## Option 2: Find recent Slack reports

Enter:

> `$new-bug`

The skill will:

1. Review the last 14 days of messages from all users in `#bugs-ui-ux-problem-reports`.
2. Compare possible bugs against all project 021 tasks.
3. If no unlogged candidates are found, search only your own recent public Slack activity elsewhere.
4. Show up to five unlogged candidates for you to choose from.
5. List explicitly resolved discussions separately as **Resolved — no task required**.

To create a listed candidate, respond with its number:

> `Create option 1.`

The skill does not search private channels or direct messages without permission and does not search other people's activity outside `#bugs-ui-ux-problem-reports`.

## Duplicate and variant handling

- Exact Slack-source matches are treated as duplicates.
- Reports describing the same behavior may be flagged as possible duplicates for confirmation.
- Completed, obsolete and not-required project 021 tasks are included in the duplicate check.
- A separate variant may be created only when explicitly requested and when it materially changes the customer type, account tier, platform or affected workflow.

Example:

> `Create a separate version for B2B Level 1–3 accounts and link the original task.`

## After a bug is created

The task is added to **021 > Incoming — New** with:

- No assignee.
- No due date.
- The Slack reporter and source link.
- Only custom fields supported by the available evidence.
- No proposed solution, scope or acceptance criteria.

ChatGPT will confirm:

> **New bug created from Slack report:**  
> [Asana task title and link]

Screenshots must be added manually. Download them from Slack, open the bug using the provided link, and add them under **+ Attachments**.

## What happens next

Mike reviews the incoming task for accuracy, determines its scope and possible solution, and decides whether to use **Asana Small Task Writer** to prepare a separate development task for project 101 review and backlog.
