# General Plan

Generate a high-level initiative planning document from an RFC file.

## Usage

```text
/2-personal-general-plan <rfc-path> <output-path>
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating an initiative-level planning document from an RFC. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: path to the RFC Markdown file (required)
- Second positional argument: path to the output planning file (required, e.g. `.claude/planning/recipe-app/planning.md`)

### Step 2 — Read inputs

Read the RFC file at the provided path.

Also read `~/.claude/templates/general_plan_template.md` for the expected structure and field conventions.

**Skip the following RFC sections entirely — do not use their content:**

- Any section whose heading contains "FAQ" or "References"
- Any section explicitly marked as non-normative

### Step 3 — Generate the document

Produce a planning document with this exact structure:

---

**Title:** `# <Initiative Name> — High-Level Planning`

**Header block** (immediately after the title):

```
**Project:** <project name>
**GitHub repo:** <URL> (if present in the RFC)
**GitHub Milestone:** <URL> (if present in the RFC)
**Notion page:** <URL> (if present in the RFC)
**Total estimated effort:** <N> sessions / hours / days
```

---

**Overview section** (`## Overview`):

- 2–3 sentences describing what the initiative builds and what it changes technically (not personal motivation — that is in Notion)
- A `### Dependency Order` sub-section with an ASCII diagram:

```
TASK-1 ──► TASK-2 ──► TASK-4
               │
               └──► TASK-3 (parallel)
```

---

**One section per TASK** (`## TASK-N — <Task Name>`):

Each task maps to one GitHub Issue. Each section must contain, in order:

1. `**GitHub Issue:** #{number}` — placeholder if no issue number is known yet
2. `**Effort estimate:** N sessions / hours / days` — omit if RFC has no estimate
3. `### Scope` — one short paragraph: what work is included
4. `### Goal` — one short paragraph: concrete output and why it matters technically
5. `### Existing Work (already done)` — only if the RFC describes work already complete
6. `### Gaps to Close` — only if "Existing Work" is present; numbered list of what still needs building
7. `### Deliverables` — bullet list of named outputs (`src/search.py`, `--query` flag). Use code formatting.
8. `### Technical Overview` — data models, CLI parameters, architectural constraints, integration points

Rules:
- Use only information from the RFC. Do not invent scope, deliverables, or effort.
- Keep descriptions concise and technical.

---

**GitHub Issues section** (`## GitHub Issues`):

Group tasks into 2–4 milestones. One sub-section per milestone:

```
### Milestone N — <Milestone Name>

**Tasks:** TASK-X, TASK-Y, ...
**Effort:** N sessions / hours / days

#### Scope
<one paragraph>

#### Goal
<one paragraph>

#### Deliverables
- <consolidated flat list of named outputs>
```

Grouping rules:
- Group tasks that share a natural phase or dependency cluster
- Each milestone must be independently deliverable
- Deliverables are a consolidated flat list — no nested bullets

---

### Step 4 — Write the file

Write the generated document to the output path. Create the parent directory if needed.

Then report:

- The output file path
- Number of tasks, number of milestones, any notable decisions made
