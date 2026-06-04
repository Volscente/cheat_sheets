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
- Second positional argument: path to the output planning file (required, e.g. `docs/vdata-8411_markup_accuracy/planning.md`)

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

Populate `~/.claude/templates/work_general_plan_template.md`. Replace every `{placeholder}` with content derived from the RFC.

Rules:

- Add one `## TASK-N` section per task in the RFC — there may be anywhere from 1 to 10+. Replicate the TASK block structure from the template for each task.
- Add one `### Story N` sub-section per story group in `## JIRA Stories` — there may be anywhere from 1 to 10+. Replicate the story block structure from the template for each group.
- Omit `### Existing Infrastructure (already done)` and `### Gaps to Close` from a task section unless the RFC explicitly describes work that is already complete.
- Group tasks into stories by natural phase or dependency cluster. Each story must be independently deliverable. The deliverables list in each story is a consolidated flat list — no nested bullets.
- Use only information from the RFC. Do not invent scope or deliverables.
- Always include an effort estimate — use the RFC's estimate if provided, otherwise derive your own using the Effort Estimation guide.
- Keep descriptions concise and technical. Avoid prose padding.

---

### Step 4 — Write the file

Write the generated document to the output path provided in the arguments. If the parent directory does not exist, create it.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated (number of tasks, number of stories, any notable decisions made)
