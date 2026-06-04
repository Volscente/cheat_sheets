# Plan from RFC

Generate a planning document from an RFC file.

## Usage

```text
/3-work-plan-task <rfc-path> [--planning <planning-path>] [--task <task-number>] [--type initiative|spec] [--epic <jira-epic>] [--ticket <jira-ticket>]
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating a planning document from an RFC. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: RFC file path (required)
- `--planning`: path to an existing initiative planning doc (e.g. `docs/vdata-8411_markup_accuracy/planning.md`)
- `--task`: task number to focus on in the planning doc (e.g. `--task 2` targets the "TASK-2" section)
- `--type`: `initiative` (default) or `spec`
- `--epic`: JIRA epic ID (e.g. `vdata-8411_markup_accuracy`)
- `--ticket`: JIRA ticket ID (e.g. `vdata-9356_online_catalog`) — if provided, implies `--type spec`

If `--ticket` is given but `--type` is not, set type to `spec`.
If neither `--type` nor `--ticket` is given, set type to `initiative`.

### Step 2 — Read inputs

Always read:

1. The RFC file at the provided path

If type is `spec`, also read:

1. `~/.claude/templates/work_tech_spec_template.md` — the fillable template to populate

If type is `initiative`, also read:

1. `~/.claude/templates/work_general_plan_template.md` — the fillable template to populate

If `--planning` was provided, read that file too. When present, it is the **primary source of truth** for scope, deliverables, effort, and task structure. The RFC provides background context only.

If `--planning` was not provided and type is `spec`, check whether a `planning.md` exists in `docs/<jira-epic>/` and read it if found.

If `--task` was provided, restrict all content derived from the planning doc to the section headed `TASK-<n>` (e.g. `## TASK-2 — ...`). Ignore all other task sections.

**Repository context (spec mode only):** If type is `spec`, check whether a `proposal.md`
exists in the same directory as the RFC file. If it does, read it and extract `context-paths`
from the YAML frontmatter. Read each listed file (paths relative to the project root).
Build an internal context summary covering: existing module boundaries, public interfaces,
key file paths, and constraints. Use this context in Step 4 to write accurate file names,
function signatures, and import paths — grounding the spec in the actual codebase rather
than inferred names. Skip silently if no `proposal.md` exists or `context-paths` is empty.

### Step 3 — Determine output path

**If type = initiative:**

- Output: `docs/<jira-epic>/planning.md` (derive a slug from the RFC title if no epic ID given)
- If `planning.md` already exists in that directory, update it rather than overwriting from scratch

**If type = spec:**

- Output: `docs/<jira-epic>/<jira-ticket>.md`
- File name is the JIRA ticket ID in lowercase (e.g. `vdata-9356_online_catalog.md`)

### Step 4 — Generate the document

**If type = initiative**, populate `~/.claude/templates/work_general_plan_template.md`. Replace every `{placeholder}` with content derived from the RFC (and planning doc if provided).

Rules:

- Add one `## TASK-N` section per task — there may be anywhere from 1 to 10+. Replicate the TASK block structure from the template for each task.
- Add one `### Story N` sub-section per story group in `## JIRA Stories` — there may be anywhere from 1 to 10+. Replicate the story block structure from the template for each group.
- Include `### Existing Infrastructure (already done)` and `### Gaps to Close` only when the RFC describes already-completed work.
- Use only information from the RFC and planning doc. Do not invent scope, deliverables, or effort estimates. Keep descriptions technical and concise.

**If type = spec**, populate `~/.claude/templates/work_tech_spec_template.md` section by section. Use `~/.claude/templates/work_general_plan_template.md` for field semantics and formatting rules:

- Title: `# <JIRA-TICKET>: <Title>`
- JIRA Ticket and JIRA Epic links (placeholder URLs if not provided: `https://deliveryhero.atlassian.net/browse/<ticket>`)
- **Technical Scope** — what files/modules change; what is explicitly out of scope
- **Architecture** — ASCII diagram of the data flow or component structure
- **Tech Stack** — new packages only, with version and justification; skip section if none
- **Implementation Details** containing:
  - Modules / Files table (File | Action | Description)
  - Key Functions with full docstrings (Args, Returns, Raises)
  - CLI Parameters table if the component has a CLI
  - Data Models / Schemas (Pydantic models or BigQuery schema tables)
  - Testing Strategy (unit, integration, edge cases)
  - Open Questions / Risks (checkbox list with owner placeholders)

When `--planning` is provided, the task description in that file defines the deliverables and scope for this spec — use it as the authoritative source, not the RFC. Use the repository context loaded in Step 2 to name real files and interfaces; fall back to names that follow logically from the scope, existing codebase patterns (e.g. the `pipelines/mds/llm_judge/` pattern for new pipelines), and the project structure in CLAUDE.md only when context is unavailable. Do not hallucinate file names.

### Step 5 — Write the file

Write the generated document to the output path from Step 3. If the directory does not exist, create it.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated
