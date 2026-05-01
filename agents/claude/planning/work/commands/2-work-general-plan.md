# General Plan

Generate a high-level initiative planning document from an RFC file.

## Usage

```text
/2-work-general-plan <rfc-path> <output-path>
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating an initiative-level planning document from an RFC. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: path to the RFC Markdown file (required)
- Second positional argument: path to the output planning file (required, e.g. `docs/planning/vdata-8411_markup_accuracy/planning.md`)

### Step 2 — Read inputs

Read the RFC file at the provided path.

Also read `docs/planning/vdata-8411_markup_accuracy/planning.md` as the canonical reference for structure and style.

**Skip the following RFC sections entirely — do not use their content:**

- Any section whose heading contains "Appendix", "Append", or "FAQ"
- Any section explicitly marked as non-normative or informational-only

### Step 3 — Generate the document

Produce a planning document with this exact structure, using `docs/planning/vdata-8411_markup_accuracy/planning.md` as the style reference:

---

**Title:** `# <Initiative Name> — High-Level Planning`

**Header block** (immediately after the title):

```md
**Initiative:** <full initiative name>
**Total estimated effort:** <N> FTE-days (1 FTE = 1 day)
```

---

**Overview section** (`## Overview`):

- 2–3 sentences describing what the initiative builds and why
- A `### Dependency Order` sub-section with an ASCII diagram showing task dependencies and parallel execution tracks. Use the same arrow/box style as the reference document.

---

**One section per TASK** (`## TASK-N — <Task Name>`):

Each task section must contain these sub-sections, in order:

1. `**Effort estimate:** N FTE-days` — on its own line immediately under the heading
2. `### Scope` — one short paragraph describing what work is included
3. `### Goal` — one short paragraph stating the concrete output and why it matters
4. `### Existing Infrastructure (already done)` — **only if the RFC describes work that is already complete**; list what already exists and why it satisfies requirements
5. `### Gaps to Close` — **only if existing infrastructure is called out above**; a numbered list of what still needs to be built to close the gap between existing work and RFC requirements
6. `### Deliverables` — bullet list of concrete, named outputs (files, scripts, BigQuery tables, CLI flags). Use code-formatted names (`scripts/foo.py`, `--batch-id`).
7. `### Technical Overview` — technical details: schema definitions (inline JSON blocks), CLI flag descriptions, architectural constraints, integration points, parallelism. Include a BigQuery schema block if any table is created.

Rules for task sections:

- Use only information from the RFC. Do not invent scope, deliverables, or effort.
- If the RFC does not give an effort estimate for a task, omit the estimate line.
- Keep descriptions concise and technical. Avoid prose padding.

---

**JIRA Stories section** (`## JIRA Stories`):

Group the tasks into 2–4 stories. Open with a one-sentence framing line, then a horizontal rule, followed by one sub-section per story:

```md
### STORY-N — <Story Name>

**Tasks:** TASK-X, TASK-Y, ...
**Effort:** N FTE-days

#### Scope

<one paragraph>

#### Goal

<one paragraph>

#### Deliverables

- <bullet list of all deliverables across the grouped tasks, consolidated>
```

Story grouping rules:

- Group tasks that share a natural phase or dependency cluster (e.g. ground truth construction, evaluation pipeline, automation/sustainability).
- Each story must be independently deliverable.
- Deliverables in the story section are a consolidated flat list across all its tasks — do not repeat sub-bullets, just list the named outputs.

---

### Step 4 — Write the file

Write the generated document to the output path provided in the arguments. If the parent directory does not exist, create it.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated (number of tasks, number of stories, any notable decisions made)
