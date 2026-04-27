# General Plan

Generate a high-level initiative planning document from an RFC file.

## Usage

```text
/general-plan <rfc-path> <output-path>
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating an initiative-level planning document from an RFC. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: path to the RFC Markdown file (required)
- Second positional argument: path to the output planning file (required, e.g. `docs/planning/dotfile-manager/planning.md`)

### Step 2 — Read inputs

Read the RFC file at the provided path.

Also read `templates/general_plan_template.md` for the expected structure and field conventions.

**Skip the following RFC sections entirely — do not use their content:**

- Any section whose heading contains "Appendix", "FAQ", or "References"
- Any section explicitly marked as non-normative or informational-only

### Step 3 — Generate the document

Produce a planning document with this exact structure:

---

**Title:** `# <Initiative Name> — High-Level Planning`

**Header block** (immediately after the title):

```
**Project:** <project name or repo>
**Notion page:** <URL> _(if present in the RFC)_
**GitHub repo:** <URL> _(if present in the RFC)_
**Total estimated effort:** <N> sessions / hours / days
```

---

**Overview section** (`## Overview`):

- 2–3 sentences describing what the initiative builds and why
- A `### Dependency Order` sub-section with an ASCII diagram showing task dependencies and parallel execution tracks:

```
TASK-1 ──► TASK-2 ──► TASK-4
               │
               └──► TASK-3 (parallel)
```

---

**One section per TASK** (`## TASK-N — <Task Name>`):

Each task section must contain these sub-sections, in order:

1. `**Effort estimate:** N sessions / hours / days` — on its own line immediately under the heading
2. `### Scope` — one short paragraph describing what work is included
3. `### Goal` — one short paragraph stating the concrete output and why it matters
4. `### Existing Work (already done)` — **only if the RFC describes work that is already complete**; list what exists and why it satisfies requirements
5. `### Gaps to Close` — **only if existing work is called out above**; a numbered list of what still needs to be built
6. `### Deliverables` — bullet list of concrete, named outputs (files, scripts, configs, APIs). Use code-formatted names (`src/parser.py`, `--dry-run`).
7. `### Technical Overview` — technical details: data models, CLI parameters, architectural constraints, integration points.

Rules for task sections:
- Use only information from the RFC. Do not invent scope, deliverables, or effort.
- If the RFC does not give an effort estimate for a task, omit the estimate line.
- Keep descriptions concise and technical.

---

**GitHub Issues section** (`## GitHub Issues`):

Group the tasks into 2–4 milestones. Open with a one-sentence framing line, then a horizontal rule, followed by one sub-section per milestone:

```
### Milestone N — <Milestone Name>

**Tasks:** TASK-X, TASK-Y, ...
**Effort:** N sessions / hours / days

#### Scope
<one paragraph>

#### Goal
<one paragraph>

#### Deliverables
- <consolidated flat list of all deliverables across the grouped tasks>
```

Milestone grouping rules:
- Group tasks that share a natural phase or dependency cluster.
- Each milestone must be independently deliverable.
- Deliverables in the milestone section are a consolidated flat list — do not repeat sub-bullets, just list the named outputs.

---

### Step 4 — Write the file

Write the generated document to the output path provided in the arguments. If the parent directory does not exist, create it.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated (number of tasks, number of milestones, any notable decisions made)
