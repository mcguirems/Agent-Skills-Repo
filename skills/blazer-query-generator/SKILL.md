---
name: blazer-query-generator
description: Draft MyVeloFit Blazer PostgreSQL queries grounded in privately supplied current schema context. Use for SQL drafting, reporting, funnels, and query revisions; requires authorized schema knowledge outside this public package.
---

# Blazer Query Generator

## Load authoritative private context

Read [schema requirements](references/schema-requirements.md). Require current MyVeloFit schema content, conventionally `schema_main.md`, before generating production SQL. The schema is intentionally excluded from this public package.

Look first in authorized project knowledge or a private master knowledge base; also accept an uploaded schema file, complete pasted schema content, or an accessible authorized Google Doc reference. Open and read the actual relevant source content. A filename, link, remembered summary, or prior query is not a substitute. Record which source and known update date were used; do not invent freshness or claim access to unseen content.

Verify the source documents tables, columns, and types and is compatible with PostgreSQL. Check all parts needed for the requested query. If the schema is absent, unreadable, empty, invalid, contradictory, incompatible, or lacks a required definition, stop before drafting production SQL. Ask for current authorized schema context through any supported private channel. Do not guess missing definitions, infer joins from names, or silently produce generic production-looking SQL.

Read optional private `Docs_main.md` or equivalent current documentation for Blazer smart variables, linked columns, charts, and cohorts. If absent, continue only with schema-grounded PostgreSQL and state that MVF-specific Blazer configuration could not be verified. Do not invent configuration or internal routes.

## Keep schema knowledge current

Schemas change over time. Prefer the most recent explicitly identified authoritative source and resolve conflicting versions before using affected definitions. When the user supplies an updated schema, use it in the working context and ask them to replace obsolete project/master knowledge copies. Update a persistent knowledge source only if the host supports it and the user authorizes that write. Clearly distinguish context used now from a durable knowledge update; never promise automatic LLM memory synchronization. Do not treat remembered schema fragments as authoritative.

## Draft the query

1. Clarify the metric, population, date range, grouping, and exclusions when unclear. Use a bounded date range; do not assume all time.
2. Verify each referenced table and column against the loaded private schema. Verify join keys and relationship meaning using supplied schema/documentation. If a necessary relationship is unverified, stop that query and request the missing relationship information.
3. Use PostgreSQL syntax. Suggest sorting/grouping when useful. Use documented smart variables and linkable IDs only when verified in privately supplied Blazer documentation. Suggest charts only when verified configuration and output structure support them.
4. Use only minimum required private schema details. Return SQL and a concise explanation, not a schema dump. Do not reproduce unrelated private structure, credential values, or customer records. Include sensitive fields only if genuinely needed for an authorized query.
5. Put SQL in a fenced `sql` block. State material assumptions; do not leave unverified schema or joins inside production SQL. Provide illustrative output only if helpful and clearly labeled as illustrative, with no customer data.
6. Never claim execution or database validation unless actually performed. Remind the user to review and run the query manually in authorized Blazer.

## Platforms

Use any host able to read authorized schema context and return text. No database connection is required for drafting.

### ChatGPT Work

Prefer reusable private project knowledge or an accessible master knowledge source. Use available connected tools to retrieve authorized Google Docs when supplied; if unavailable or access fails, ask for pasted content or an upload. Do not require a fresh attachment in every chat when current source content is already accessible.

### Codex

Read authorized workspace schema files or securely accessible knowledge sources. Keep private schema outside the public skill folder. Return SQL for manual Blazer execution; do not execute against production as part of this drafting workflow.

See [usage](how-to-use-this-skill.md), [team instructions](team-instructions.md), and [installation](Install-this-skill.md).
