# Plan from RFC

Generate a planning document from an RFC file.

## Usage

```text
/plan <rfc-path> [--planning <planning-path>] [--task <task-number>] [--type initiative|spec] [--epic <jira-epic>] [--ticket <jira-ticket>]
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating a planning document from an RFC. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: RFC file path (required)
- `--planning`: path to an existing initiative planning doc (e.g. `docs/planning/vdata-8411_markup_accuracy/planning.md`)
- `--task`: task number to focus on in the planning doc (e.g. `--task 2` targets the "TASK-2" section)
- `--type`: `initiative` (default) or `spec`
- `--epic`: JIRA epic ID (e.g. `vdata-8411`)
- `--ticket`: JIRA ticket ID (e.g. `vdata-9356`) — if provided, implies `--type spec`

If `--ticket` is given but `--type` is not, set type to `spec`.
If neither `--type` nor `--ticket` is given, set type to `initiative`.

### Step 2 — Read inputs

Always read:

1. The RFC file at the provided path
2. `docs/planning/general_plan_template.md` — defines the spec format

If `--planning` was provided, read that file too. When present, it is the **primary source of truth** for scope, deliverables, effort, and task structure. The RFC provides background context only.

If `--planning` was not provided and type is `spec`, check whether a `planning.md` exists in `docs/planning/<jira-epic>/` and read it if found.

If `--task` was provided, restrict all content derived from the planning doc to the section headed `TASK-<n>` (e.g. `## TASK-2 — ...`). Ignore all other task sections.

### Step 3 — Determine output path

**If type = initiative:**

- Output: `docs/planning/<jira-epic>/planning.md` (derive a slug from the RFC title if no epic ID given)
- If `planning.md` already exists in that directory, update it rather than overwriting from scratch

**If type = spec:**

- Output: `docs/planning/<jira-epic>/<jira-ticket>.md`
- File name is the JIRA ticket ID in lowercase (e.g. `vdata-9356.md`)

### Step 4 — Generate the document

**If type = initiative**, produce a planning document that follows the structure of `docs/planning/vdata-8411_markup_accuracy/planning.md` (read it as a reference):

- Title: `# <Initiative Name> — High-Level Planning`
- Header block: initiative name, RFC reference, total estimated effort
- **Overview** section: 2–3 sentence summary of what the initiative builds and why
- **Dependency Order** section: ASCII diagram showing task dependencies and parallel tracks
- One section per **TASK**: numbered, with Effort estimate, Scope, Goal, Deliverables, and Technical Overview sub-sections. Where the RFC describes existing infrastructure that is already done, call it out explicitly in an "Existing Infrastructure" sub-section. Where gaps remain, list them in a "Gaps to Close" sub-section.
- **JIRA Stories** section at the end: group tasks into 2–4 stories. Each story has Scope, Goal, and Deliverables.

Use only information from the RFC (and the planning doc if provided). Do not invent scope, deliverables, or effort estimates. Keep descriptions technical and concise.

**If type = spec**, produce a technical spec that follows the structure defined in `docs/planning/general_plan_template.md` and uses `docs/planning/vdata-8417_mds_translation_evaluation/vdata-8860_implement-comet-da.md` as a style reference:

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

When `--planning` is provided, the task description in that file defines the deliverables and scope for this spec — use it as the authoritative source, not the RFC. Infer implementation details from the existing codebase patterns (e.g. the `pipelines/mds/llm_judge/` pattern for new pipelines). Do not hallucinate file names — only name files that follow logically from the scope and the project structure in CLAUDE.md.

### Step 5 — Write the file

Write the generated document to the output path from Step 3. If the directory does not exist, create it.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated
