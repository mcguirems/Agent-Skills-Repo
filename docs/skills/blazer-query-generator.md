---
title: Blazer Query Generator
description: "Last updated: October 2, 2026"
status: active
---

# Blazer Query Generator

SOURCE:
- [Download the installable `.zip`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/blazer-query-generator/blazer-query-generator.zip)
- [Download the skill source on GitHub](https://github.com/mcguirems/Agent-Skills-Repo/tree/main/skills/blazer-query-generator)
- [Direct `SKILL.md`](https://raw.githubusercontent.com/mcguirems/Agent-Skills-Repo/main/skills/blazer-query-generator/SKILL.md)

## Purpose

`blazer-query-generator` drafts PostgreSQL queries for MyVeloFit Blazer using current schema context supplied separately in an authorized private environment.

## Private Schema Requirement

The production schema is intentionally excluded from this public package. Before producing production SQL, the skill requires authorized access to a current `schema_main.md` or equivalent schema source.

If the schema is missing, unreadable, or insufficient, the skill stops rather than inventing tables, columns, types, or joins. Optional private `Docs_main.md` content can supply current Blazer variables, links, chart rules, and cohort configuration.

## When To Use

Use this skill when you need to:

- draft a schema-grounded PostgreSQL report query
- revise an existing Blazer query
- define a metric, funnel, population, date range, or grouping
- identify assumptions and missing relationship information before execution

## When Not To Use

Do not use this skill without authorized, current schema context. It does not connect to the production database, execute SQL, validate live results, or grant access to MyVeloFit data.

## Safety Model

- private schema files remain outside the public skill
- only the minimum required schema information is used
- undocumented joins and Blazer configuration are not inferred
- generated SQL must be reviewed and run manually in authorized Blazer

## Included Files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `agents/openai.yaml`
- `references/schema-requirements.md`
- user and team instructions
- `blazer-query-generator.zip`

## Installation Notes

Installing the ZIP provides the public workflow only. Authorized users must supply the private schema separately at runtime through approved project knowledge, an accessible private document, pasted content, or a file upload.

## Example Requests

- “Use `$blazer-query-generator` with the supplied schema to count new accounts by day.”
- “Review this Blazer query and verify every table, column, and join.”
- “Draft a PostgreSQL funnel query for this bounded reporting period.”
