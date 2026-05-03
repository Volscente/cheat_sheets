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

### Effort Estimation

Estimate effort for each task and for the initiative total. Do **not** leave placeholders — always produce a numeric estimate in **FTE-days** (1 FTE-day = 1 full working day).

**How to estimate:**

1. Assess each task's complexity based on its scope, deliverables, and technical requirements from the RFC.
2. Assume the developer uses **agentic coding tools** (Claude Code, GitHub Copilot, or similar) for implementation, testing, and boilerplate — this typically reduces effort by 30–50 % compared to fully manual coding.
3. Assign each task a numeric FTE-days estimate (decimals are fine, e.g. 0.5).
4. Sum per-task estimates to compute the total initiative effort shown in the header block.

**Rough sizing guide (with agentic coding assistance):**

| Task type | Typical estimate |
|---|---|
| Config / setup / boilerplate | 0.5 FTE-days |
| Single-module feature (CRUD, CLI flag, utility) | 0.5–1 FTE-days |
| Multi-module feature with integration | 1–2 FTE-days |
| Complex feature (new data model + pipeline + tests) | 2–3 FTE-days |

Use the RFC's own estimates when provided; otherwise derive your own using the guide above.

### Step 3 — Generate the document

Produce a planning document with this exact structure, using `docs/planning/vdata-8411_markup_accuracy/planning.md` as the style reference:

---

**Title:** `# <Initiative Name> — High-Level Planning`

**Header block** (immediately after the title):

```md
**Initiative:** <full initiative name>
**Total estimated effort:** <computed total — see Effort Estimation below> FTE-days (1 FTE = 1 day)
```

---

**Overview section** (`## Overview`):

- 2–3 sentences describing what the initiative builds and why
- A `### Dependency Order` sub-section with an ASCII diagram showing task dependencies and parallel execution tracks. Use the same arrow/box style as the reference document.

---

**One section per TASK** (`## TASK-N — <Task Name>`):

Each task section must contain these sub-sections, in order:

1. `**Effort estimate:** N FTE-days` — estimated per task (see Effort Estimation below)
2. `### Scope` — one short paragraph describing what work is included
3. `### Goal` — one short paragraph stating the concrete output and why it matters
4. `### Existing Infrastructure (already done)` — **only if the RFC describes work that is already complete**; list what already exists and why it satisfies requirements
5. `### Gaps to Close` — **only if existing infrastructure is called out above**; a numbered list of what still needs to be built to close the gap between existing work and RFC requirements
6. `### Deliverables` — bullet list of concrete, named outputs (files, scripts, BigQuery tables, CLI flags). Use code-formatted names (`scripts/foo.py`, `--batch-id`).
7. `### Technical Overview` — technical details: schema definitions (inline JSON blocks), CLI flag descriptions, architectural constraints, integration points, parallelism. Include a BigQuery schema block if any table is created.

Rules for task sections:

- Use only information from the RFC. Do not invent scope or deliverables.
- Always include an effort estimate — use the RFC's estimate if provided, otherwise derive your own using the Effort Estimation guide.
- Keep descriptions concise and technical. Avoid prose padding.

---

**JIRA Stories section** (`## JIRA Stories`):

Group the tasks into 2–4 stories. Open with a one-sentence framing line, then a horizontal rule, followed by one sub-section per story:

```md
### STORY-N — <Story Name>

**Tasks:** TASK-X, TASK-Y, ...
**Effort:** <sum of grouped task estimates> FTE-days

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
