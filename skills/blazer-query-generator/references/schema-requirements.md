# Private schema requirements

Requires privately supplied MyVeloFit schema context, conventionally `schema_main.md`. The production schema is intentionally excluded from this public package.

Only authorized users should provide the schema through an approved private environment. Prefer reusable project knowledge or a private master knowledge base. Also accept file uploads, current schema pasted as text, or authorized Google Doc references whose actual contents can be read. No exact filename is required for pasted or document-based equivalents.

The schema must document the actual tables, columns, and PostgreSQL types needed for the query. Verified relationships must be available for joins. Never replace missing definitions with memory, examples, or guessed structure. If source content is missing, inaccessible, empty, invalid, incompatible, or insufficient, stop before production SQL and ask for the current authorized source.

Optional but recommended: privately supplied `Docs_main.md` or equivalent documentation for current MVF Blazer smart variables, linked columns, charts, and cohorts. Without it, draft schema-grounded PostgreSQL only and disclose that MVF-specific configuration is unverified.

Schemas evolve. Maintain a known update date in the private knowledge source when available. Replace obsolete project/master knowledge copies after schema changes; do not publish them with this skill. New pasted/uploaded content updates the current working context, but does not automatically update durable LLM memory. Write back to private knowledge only with explicit authorization and supported capabilities. Resolve conflicting versions before generating affected SQL.
