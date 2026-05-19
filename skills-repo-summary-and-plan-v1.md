---
doc_id: skills-repo-summary-and-plan
title: Skills Repository Summary and Plan
doc_type: project
status: active
version: 1.0
date_created: 2026-05-13
date_modified: 2026-05-13
owner: Mike McGuire
author: Mike McGuire
confidentiality: internal
source: internal
tags: [skills, codex, repository, flowershow, planning]
related: [system-front-matter-standard]
---

# Skills Repository Summary and Plan

## Purpose

Create a portable, version-controlled repository for custom Codex skills that can also power a human-readable Flowershow website.

This repository should support:
- skill sharing
- transportability
- version history
- human-readable documentation
- future publishing

---

## Core Decision

Use a dedicated Git repository as the source of truth for custom skills and their publishing docs.

Keep runtime skills and published docs separate:

- `skills/` contains the actual skill folders used by Codex
- `docs/` contains human-facing documentation pages for Flowershow

This avoids mixing agent-optimized `SKILL.md` files with human-friendly explanation pages.

---

## Recommended Model

### Runtime / Canonical Content

Each skill should keep its canonical operational files:
- `SKILL.md`
- `scripts/`
- `references/`
- `assets/` if needed

Example:

```text
skills/
  add-front-matter/
    SKILL.md
  mvf-restricted-boundary/
    SKILL.md
    scripts/
    references/
```

### Human-Facing Publishing Layer

Each skill should also have a standalone documentation page in `docs/`.

These pages should explain:
- what the skill does
- when to use it
- when not to use it
- important constraints
- included supporting files
- example requests
- canonical skill path

Example:

```text
docs/
  index.md
  add-front-matter.md
  mvf-restricted-boundary.md
```

---

## Why This Structure

### Benefits

- portable: the repo can be cloned or shared
- durable: Git tracks changes to skills and docs
- publishable: Flowershow can render `docs/` directly
- maintainable: `SKILL.md` stays optimized for Codex, docs stay optimized for humans
- scalable: more skills can be added without changing the structure

### Important Rule

`SKILL.md` is canonical for skill behavior.

The `docs/*.md` files are summaries and publishing pages, not the operational source of truth.

This rule should be stated clearly in the repository.

---

## Recommended Repository Structure

```text
skills-repo/
  README.md
  skills/
    add-front-matter/
      SKILL.md
    mvf-restricted-boundary/
      SKILL.md
      scripts/
      references/
  docs/
    index.md
    add-front-matter.md
    mvf-restricted-boundary.md
```

Optional later additions:

```text
  docs/assets/
  docs/templates/
  tools/
    sync-skills.sh
    generate-docs.py
```

---

## Publishing Strategy

Flowershow should publish the `docs/` folder, not the raw `skills/` tree by itself.

Reasons:
- raw `SKILL.md` files are structured for Codex skill triggering
- published docs should explain skills in a cleaner and more readable way
- this reduces confusion if a skill has scripts, references, or internal implementation details

Possible doc pattern per skill:
- Name
- Status
- Purpose
- When to use
- When not to use
- Inputs
- Outputs
- Included files
- Example requests
- Notes or limitations
- Canonical runtime location

---

## Source of Truth Decision

Two models were considered:

### Option A: Repository is canonical

Edit skills in the Git repository, then sync them into `~/.codex/skills`.

Pros:
- cleaner version control
- better portability
- easier publishing workflow

Cons:
- requires a sync workflow

### Option B: Local skill folders are canonical

Edit in `~/.codex/skills`, then copy or export to the repo.

Pros:
- matches current workflow
- simpler at the very beginning

Cons:
- more drift risk
- weaker publishing workflow

### Recommendation

Start with Option B if speed matters.

Move toward Option A once the repository exists and the structure is stable.

This reduces initial friction while preserving a better long-term model.

---

## Initial Skills To Include

1. `add-front-matter`
2. `mvf-restricted-boundary`

These are the best starting point because:
- they are custom
- they are already active
- they represent two useful patterns:
  - metadata normalization
  - content boundary handling

---

## First Build Plan

### Phase 1: Repository Setup

1. Create a new project folder for the skills repository.
2. Initialize a Git repository.
3. Create top-level folders:
   - `skills/`
   - `docs/`
4. Add a root `README.md` explaining purpose and structure.

### Phase 2: Import Initial Skills

1. Copy `add-front-matter` into `skills/add-front-matter/`
2. Copy `mvf-restricted-boundary` into `skills/mvf-restricted-boundary/`
3. Verify all bundled scripts and references come with each skill

### Phase 3: Create Human Docs

1. Create `docs/index.md`
2. Create `docs/add-front-matter.md`
3. Create `docs/mvf-restricted-boundary.md`
4. Add a note that `skills/*/SKILL.md` is canonical

### Phase 4: Prepare Flowershow

1. Confirm Flowershow is pointed at the repository
2. Publish `docs/`
3. Check navigation and readability
4. Refine page templates if needed

### Phase 5: Improve Workflow

1. Decide whether repo or local install is canonical
2. Add a sync workflow if needed
3. Optionally generate human docs from skill metadata later

---

## Open Decisions For The New Project

These should be resolved in the new repository:

- final repository name
- whether the repo lives inside `000-CODEX`, `000-CODEX-Projects`, or elsewhere
- whether `skills/` or `docs/` is considered canonical
- whether sync should be manual or scripted
- whether published docs should be hand-written or partially generated

---

## Suggested Immediate Next Step

Create the new project folder for the skills repository and restart work there using this document as the kickoff reference.

At that point, the first tasks should be:

1. scaffold the repo structure
2. import the first two custom skills
3. draft the Flowershow-facing docs

