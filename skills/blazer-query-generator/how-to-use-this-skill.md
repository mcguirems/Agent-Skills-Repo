# How to use this skill

1. Make current authorized schema available in project knowledge or a private master knowledge base. Alternatively upload `schema_main.md`, paste its contents, or provide an accessible private Google Doc. Optional `Docs_main.md` verifies Blazer configuration.
2. Invoke `$blazer-query-generator` and specify the metric, population, date range, grouping, and exclusions.
3. Review the source/date disclosure and assumptions, then review and run the SQL manually in authorized Blazer.

When the schema changes, update the project/master knowledge source and remove or supersede stale copies. Pasting an update changes current context; durable LLM memory is not automatically refreshed. Missing or unverifiable schema/relationships stop SQL generation.

In ChatGPT Work, prefer reusable private project knowledge or connected private documents. In Codex, supply private workspace files outside the public skill folder or an authorized retrievable source.
