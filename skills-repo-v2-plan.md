To continue this session, run

codex resume 019e26be-b756-7421-8e9e-9cfba918e64f

michaelmcguire@Yeti-MacBook-Pro 000-skills-repo % 

---
doc_id: skills-repo-v2-plan
title: Skills Repository V2 Plan
doc_type: project
status: active
version: 2.0
date_created: 2026-05-14
date_modified: 2026-05-14
owner: Mike McGuire
author: Mike McGuire
confidentiality: internal
source: internal
tags: [skills, codex, llm, workflow, capture, automation, planning]
related: [skills-repo-summary-and-plan, system-front-matter-standard]
---

# Skills Repository V2 Plan

## Purpose

Design an automated system to capture LLM work, extract reusable instructions and workflows from that work, curate them into durable repository assets, and selectively publish human-readable documentation.

This V2 plan expands the original repository concept from a static skill library into a broader operational knowledge system.

---

## Core Reframe

V1 primarily treated the repository as a place to store skills and related documentation.

V2 treats the repository as a pipeline:

1. capture work
2. extract reusable knowledge
3. review and promote approved assets
4. publish selected outputs

This is the central design shift.

The system should not only store skills.
It should help transform day-to-day LLM work into reusable operational assets.

---

## Primary Goals

The system should support:

- automatic or semi-automatic capture of LLM work sessions
- extraction of reusable instructions, prompt patterns, skills, and workflows
- version-controlled storage of canonical assets
- human review before promotion into official skills or docs
- selective sharing across internal and publishable surfaces
- future expansion into a broader Codex and LLM operating system

---

## Non-Goals For V2

To keep scope controlled, V2 should not attempt to solve all of the following immediately:

- full autonomous classification with no human review
- perfect archival of every token from every conversation
- public publishing of raw session transcripts
- automatic trust that every useful-looking instruction is production-ready
- deep analytics dashboards before the capture and curation model is stable

---

## Core Design Principle

Raw session capture is not the same thing as canonical knowledge.

The system needs distinct stages:

- raw evidence
- processed candidates
- approved canonical assets
- human-facing published documentation

Without this separation, the repository will drift into a noisy archive rather than a usable system.

---

## Proposed Content Model

### 1. Captures

Raw or lightly processed records of LLM work.

Examples:

- exported session notes
- copied transcripts
- task summaries
- prompt and instruction snapshots
- file-change context
- session metadata

### 2. Candidates

Extracted items that appear reusable but are not yet canonical.

Examples:

- possible new skills
- prompt templates
- reusable workflows
- references worth preserving
- examples for docs

### 3. Canonical Assets

Approved items that become part of the operating system.

Examples:

- `skills/`
- `playbooks/`
- `templates/`
- `policies/`
- curated `docs/`

### 4. Published Outputs

Human-readable material intended for browsing or sharing.

Examples:

- Flowershow pages
- internal docs
- public-safe subsets later

---

## Recommended Repository Structure

```text
skills-repo/
  README.md
  skills/
    <skill-name>/
      SKILL.md
      scripts/
      references/
      assets/
  playbooks/
    <workflow-name>.md
  templates/
    <template-name>.md
  docs/
    index.md
    skills/
    playbooks/
    system/
  captures/
    inbox/
    processed/
    rejected/
  registry/
    sessions/
    assets/
  tools/
    ingest/
    extract/
    promote/
    publish/
  policies/
    classification.md
    review-rules.md
    publishing-rules.md
```

---

## Canonical Source Rules

The repository should explicitly define canonical ownership:

- `skills/*/SKILL.md` is canonical for skill behavior
- `playbooks/*.md` is canonical for multi-step operating workflows
- `templates/*.md` is canonical for reusable document or prompt structures
- `docs/` is human-facing explanation, not the operational source of truth
- `captures/` is evidence, not truth
- `registry/` is machine-readable inventory and metadata

These rules should be documented in the root `README.md`.

---

## Asset Types

V2 needs more than one reusable asset class.

### Skills

Use for bounded operational capabilities that Codex can trigger directly.

Examples:

- add front matter
- apply restricted boundary rules
- extract transcript into structured summary

### Playbooks

Use for broader human-and-agent workflows that involve sequencing, decision rules, and checkpoints.

Examples:

- how to convert a successful session into a production-ready skill
- how to publish an internal skill safely
- how to review extracted candidates

### Templates

Use for repeatable output structures.

Examples:

- session summary template
- skill documentation page template
- candidate extraction record template

### Policies

Use for governance and safety.

Examples:

- what may be published
- what must remain internal
- what requires manual review

---

## V2 Pipeline

### Stage 1: Capture

Collect records of work into `captures/inbox/`.

Initial acceptable inputs:

- manually exported or copied chat/session markdown
- project notes tied to a session
- summaries written after a session
- related file paths or diffs if available

Important point:
V2 does not need perfect automation on day one.
Semi-automated intake is acceptable if the downstream structure is solid.

### Stage 2: Normalize

Convert incoming material into a standard record structure.

Expected outputs:

- session id
- date
- project or domain
- tools used
- models used if known
- files touched
- short summary
- extracted candidate blocks
- sensitivity classification

Normalized records should move into `captures/processed/` and/or `registry/sessions/`.

### Stage 3: Extract

Identify reusable assets from captured work.

Extraction targets:

- candidate skills
- candidate playbooks
- prompt or instruction patterns
- examples for docs
- reusable references

The extractor should prefer precision over recall at first.
Missing some candidates is better than flooding the system with junk.

### Stage 4: Review

Human review decides whether a candidate should be:

- promoted
- revised
- merged into an existing asset
- rejected

This is where quality control happens.

### Stage 5: Promote

Approved candidates move into canonical repo locations.

Examples:

- candidate skill -> `skills/<name>/`
- candidate workflow -> `playbooks/<name>.md`
- candidate doc summary -> `docs/...`

### Stage 6: Publish

Generate or refresh human-facing docs for internal browsing and later public sharing.

Publishing should operate only on canonical assets, never directly on raw captures.

---

## Metadata Model

At minimum, each captured session or extracted candidate should support:

- `id`
- `title`
- `date_created`
- `date_modified`
- `source_type`
- `project`
- `status`
- `tags`
- `sensitivity`
- `derived_from`
- `related_assets`

Suggested sensitivity values:

- `public`
- `internal`
- `restricted`

This will matter later when deciding what can be published or shared.

---

## Review Model

V2 should assume human approval before canonization.

Suggested statuses for candidates:

- `new`
- `triaged`
- `needs-edit`
- `approved`
- `rejected`
- `merged`

Suggested review questions:

1. Is this actually reusable beyond a single session?
2. Is it better represented as a skill, playbook, template, or note?
3. Does it contain internal or restricted content?
4. Is the instruction operationally clear enough to execute?
5. Does an asset like this already exist?

---

## Publishing Model

The repository should support at least two publishing surfaces over time:

### Internal Knowledge Surface

Contains:

- full skill docs
- playbooks
- examples
- internal references where allowed

### External / Shareable Surface

Contains only:

- public-safe skill summaries
- general patterns
- sanitized examples
- non-sensitive workflows

The external surface should be derived from approved canonical content, not raw captures.

---

## Recommended First Automation Scope

Do not start with full transcript ingestion plus full publishing.

Start with one narrow but valuable path:

`captured session -> extracted candidate skill/playbook -> reviewed canonical asset`

This delivers value quickly and keeps the information model clean.

---

## First Three Tools To Build

### 1. Session Ingest Tool

Purpose:
Take a raw markdown note, transcript, or session summary and wrap it in standard front matter plus a normalized storage location.

Possible output:

- `captures/inbox/<date>-<slug>.md`
- `registry/sessions/<id>.json`

### 2. Candidate Extract Tool

Purpose:
Read a captured session and produce one or more candidate records.

Extraction targets:

- skill candidate
- playbook candidate
- template candidate
- supporting example snippets

Possible output:

- `captures/processed/<id>.md`
- `registry/assets/<candidate-id>.json`

### 3. Promote Tool

Purpose:
Take an approved candidate and scaffold or update the canonical asset location.

Possible outputs:

- new `skills/<name>/SKILL.md`
- new `playbooks/<name>.md`
- new `docs/skills/<name>.md`

---

## Suggested Early Commands

These can start as lightweight scripts:

- `ingest-session`
- `extract-candidates`
- `promote-candidate`
- `build-docs-index`

The point is not sophisticated tooling at first.
The point is repeatable structure.

---

## Open Design Decisions

These should be resolved before implementation gets too far:

### 1. Ingestion Source

What is the default input?

Options:

- copied Codex transcript
- markdown work log
- project post-session note
- git diff plus human summary

### 2. Canonicality

Should this repo become the place where new skills are authored first, or only the place where mature assets are promoted?

### 3. Review Threshold

How much cleanup is required before a candidate becomes canonical?

### 4. Publishing Split

Should internal and external docs live in one repo with filtering, or separate repos later?

### 5. Taxonomy

What exactly distinguishes:

- skill
- playbook
- template
- note

This should be defined early so the system does not become ambiguous.

---

## Recommended V2 Implementation Order

### Phase 1: Define The Operating Model

1. finalize folder structure
2. define asset taxonomy
3. define capture metadata and sensitivity model
4. define review statuses

### Phase 2: Build Manual-To-Structured Intake

1. create `captures/inbox/`
2. create session front matter template
3. create initial ingest script
4. create sample captured sessions

### Phase 3: Build Candidate Extraction

1. define candidate record format
2. create extraction template
3. create first extraction script
4. test on 3 to 5 real sessions

### Phase 4: Build Promotion Workflow

1. define approval process
2. create promote script
3. scaffold canonical assets from approved candidates
4. track relationships in `registry/`

### Phase 5: Build Human-Facing Docs

1. create docs templates for skills and playbooks
2. generate indexes
3. prepare internal browsing structure
4. add Flowershow once content quality is stable

---

## Recommendation

The most practical V2 approach is:

- treat sessions as raw source material
- extract reusable assets from them
- require review before canonization
- publish only from the canonical layer

This keeps the system useful, scalable, and safe.

It also avoids the common failure mode where a knowledge repo becomes a dumping ground rather than a working operating system.

---

## Immediate Next Step

Before writing automation code, create the repository scaffold and define three schemas:

1. session capture record
2. candidate asset record
3. canonical skill/playbook documentation template

Once those exist, the first automation scripts can be implemented against a stable model.
