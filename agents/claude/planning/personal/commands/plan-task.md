# Plan from RFC

Generate a planning document from an RFC file.

## Usage

```text
/plan <rfc-path> [--planning <planning-path>] [--task <task-number>] [--type initiative|spec] [--milestone <name>] [--issue <number>]
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating a planning document from an RFC. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: RFC file path (required)
- `--planning`: path to an existing initiative planning doc (e.g. `docs/planning/dotfile-manager/planning.md`)
- `--task`: task number to focus on in the planning doc (e.g. `--task 2` targets the "TASK-2" section)
- `--type`: `initiative` (default) or `spec`
- `--milestone`: GitHub Milestone name (e.g. `"Config Parser"`) — used to derive the output folder
- `--issue`: GitHub Issue number (e.g. `--issue 42`) — if provided, implies `--type spec`

If `--issue` is given but `--type` is not, set type to `spec`.
If neither `--type` nor `--issue` is given, set type to `initiative`.

### Step 2 — Read inputs

Always read:

1. The RFC file at the provided path

If type is `spec`, also read:

2. `templates/tech_spec_template.md` — the fillable template to populate
3. `templates/general_plan_template.md` — defines field semantics and formatting rules

If type is `initiative`, also read:

2. `templates/general_plan_template.md` — defines the structure and formatting rules

If `--planning` was provided, read that file too. When present, it is the **primary source of truth** for scope, deliverables, effort, and task structure. The RFC provides background context only.

If `--planning` was not provided and type is `spec`, look for a `planning.md` in `docs/planning/<project-slug>/` and read it if found.

If `--task` was provided, restrict all content derived from the planning doc to the section headed `TASK-<n>`. Ignore all other task sections.

### Step 3 — Determine output path

**If type = initiative:**

- Derive `<project-slug>` from the RFC's project name or title
- Output: `docs/planning/<project-slug>/planning.md`
- If `planning.md` already exists in that directory, update it rather than overwriting from scratch

**If type = spec:**

- Output: `docs/planning/<project-slug>/<issue-number>-<kebab-title>.md`
- File name is `<issue-number>-<kebab-title>` where the title comes from `--task` heading in the planning doc, or from the RFC section if no planning doc is available

### Step 4 — Generate the document

**If type = initiative**, produce a planning document following the structure defined in `templates/general_plan_template.md`:

- Title: `# <Initiative Name> — High-Level Planning`
- Header block: project name, Notion page link (if in RFC), GitHub repo link (if in RFC), total estimated effort
- **Overview** section: 2–3 sentence summary + ASCII dependency diagram
- One section per **TASK**: numbered, with Effort estimate, Scope, Goal, Deliverables, and Technical Overview sub-sections. Where the RFC describes existing work that is already done, call it out in an "Existing Work" sub-section. Where gaps remain, list them in a "Gaps to Close" sub-section.
- **GitHub Issues** section at the end: group tasks into 2–4 milestones. Each milestone has Scope, Goal, and Deliverables.

Use only information from the RFC (and the planning doc if provided). Do not invent scope, deliverables, or effort estimates. Keep descriptions technical and concise.

**If type = spec**, populate `templates/tech_spec_template.md` section by section:

- Title: `# #{issue-number}: <Title>`
- GitHub Issue link (placeholder URL if not provided: `https://github.com/<owner>/<repo>/issues/<number>`)
- GitHub Milestone and Notion Page links if present in the RFC or planning doc
- **Technical Scope** — what files/modules change; what is explicitly out of scope
- **Architecture** — ASCII diagram of the data flow or component structure
- **Tech Stack** — new packages only, with version and justification; skip section if none
- **Implementation Details** containing:
  - Modules / Files table (File | Action | Description)
  - Key Functions with full docstrings (Args, Returns, Raises)
  - CLI Parameters table if the component has a CLI
  - Data Models / Schemas (Pydantic models or other data structures)
  - Testing Strategy (unit, integration, edge cases)
  - Open Questions / Risks (checkbox list with target dates)

When `--planning` is provided, the task description in that file defines the deliverables and scope for this spec — use it as the authoritative source, not the RFC. Infer implementation details from the existing codebase patterns. Do not hallucinate file names — only name files that follow logically from the scope and the project structure.

### Step 5 — Write the file

Write the generated document to the output path from Step 3. If the directory does not exist, create it.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated
