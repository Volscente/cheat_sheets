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

| Task type                                           | Typical estimate |
| --------------------------------------------------- | ---------------- |
| Config / setup / boilerplate                        | 0.5 FTE-days     |
| Single-module feature (CRUD, CLI flag, utility)     | 0.5–1 FTE-days   |
| Multi-module feature with integration               | 1–2 FTE-days     |
| Complex feature (new data model + pipeline + tests) | 2–3 FTE-days     |

Use the RFC's own estimates when provided; otherwise derive your own using the guide above.

### Step 3 — Generate the document

Read the template file at `~/.claude/templates/work_general_plan_template.md`. Use it as the exact structure for the output document, filling in each placeholder with content derived from the RFC.

Rules:

- Repeat the TASK section for each task; repeat the STORY section for each story.
- Use only information from the RFC. Do not invent scope or deliverables.
- Always include an effort estimate — use the RFC's estimate if provided, otherwise derive your own using the Effort Estimation guide.
- Keep descriptions concise and technical. Avoid prose padding.
- Omit `### Existing Infrastructure (already done)` and `### Gaps to Close` from a task section unless the RFC explicitly describes work that is already complete.
- Group tasks into 2–4 stories by natural phase or dependency cluster. Each story must be independently deliverable. The deliverables list in each story is a consolidated flat list across all its tasks.
- Dependency Order: use an ASCII arrow/box diagram showing task dependencies and parallel execution tracks.

---

### Step 4 — Write the file

Write the generated document to the output path provided in the arguments. If the parent directory does not exist, create it.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated (number of tasks, number of stories, any notable decisions made)
