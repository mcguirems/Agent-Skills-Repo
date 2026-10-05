# Source Scope

Use Mike McGuire, Product Lead at MyVeloFit, as the subject. Resolve authenticated identity where tools require it; use these identifiers only after checking they still identify the expected records.

## Source priorities

1. Asana: requirements, product/design planning, task creation, PM reviews, decisions, handoffs, and verified completions.
2. PostHog: investigation activity and saved artifacts, rather than an unverified metric report.
3. ChatGPT work: queries, research, design revisions, skill development, and documentation work not necessarily recorded in Asana. Available history is selective; do not imply full access.
4. Google Drive: created/modified documents, spreadsheets, and directories, plus substantive content when useful. Shared file activity is not automatically Mike’s work.
5. Slack: low volume but useful for direct action items, support investigations, and decisions absent from projects. Follow current permissions for private-channel access.
6. Gmail: very low signal. Keep searches bounded and stop when results are notifications or irrelevant mail.

## Known source anchors

- Asana workspace: MyVeloFit, `1204834634202873`.
- Mike’s Asana user: `1208559323290496`.
- Development Work Queue: `1213229356688869`.
- Mike’s Slack user: `U07RR6JKESK`; email `mike@myvelofit.com`.
- PostHog: MyVeloFit, US region, project `105438`.
- Skills Inventory: `https://docs.google.com/spreadsheets/d/1b2J-aevOgmBT5LM9dFk4cDldPze5ec0uSw_XjD82xa0/edit`.

Discover tools and schemas at runtime rather than hard-coding calls. Use Asana’s quick object search before specialized search. Request comments/subtasks where they establish dated contributions. Date searches must include completed work and tasks created for other assignees. A current modified timestamp later than the reporting period does not exclude dated in-period comments or creation.

For PostHog, load the connected app’s matching skills first. Use list/read tools for artifact metadata. Notebook creation-date filters do not discover older notebooks edited last week; inspect modification metadata too. Avoid project-get if it returns a project token unnecessary for the task; prefer projects-get and select the verified target. Never claim a notebook’s “surveys live” statement proves launch when other evidence says draft.

## Default Asana project status set

| Project | ID |
| --- | --- |
| 150 - Platform Experience Updates | 1209978877044614 |
| 151 - Fit Feature Redesign | 1210098098262241 |
| 021 - Product Bugs and Changes | 1208572728438762 |
| 022 - Feature Request and Product Ideas | 1208958482143213 |
| 155 - iOS MVF App Develpoment | 1210880186328689 |

Keep current project names as returned by Asana. Prefer structured current_status_update.status_type over legacy color fields. Read its created_at and text, including next steps, and summarize faithfully. Default statuses do not imply these projects changed during the week.
