# Plan from RFC

Generate a planning document from an RFC file.

## Usage

```text
/3-personal-plan-task <rfc-path> [--planning <planning-path>] [--task <task-number>] [--type initiative|spec] [--issue <number>]
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating a planning document from an RFC. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: RFC file path (required)
- `--planning`: path to an existing initiative planning doc (e.g. `.claude/planning/recipe-app/planning.md`)
- `--task`: task number to focus on (e.g. `--task 2` targets the `TASK-2` section in the planning doc)
- `--type`: `initiative` (default) or `spec`
- `--issue`: GitHub Issue number (e.g. `--issue 12`) — if provided, implies `--type spec`

If `--issue` is given but `--type` is not, set type to `spec`.
If neither `--type` nor `--issue` is given, set type to `initiative`.

### Step 2 — Read inputs

Always read:

1. The RFC file at the provided path

If type is `spec`, also read:

2. `~/.claude/templates/tech_spec_template.md` — the fillable template to populate
3. `~/.claude/templates/general_plan_template.md` — field semantics and formatting rules

If type is `initiative`, also read:

2. `~/.claude/templates/general_plan_template.md` — structure and formatting rules

If `--planning` was provided, read that file too. It is the **primary source of truth** for scope, deliverables, effort, and task structure. The RFC provides background context only.

If `--planning` was not provided and type is `spec`, look for a `planning.md` in `.claude/planning/<project-slug>/` (derive the slug from the RFC's project name) and read it if found.

If `--task` was provided, restrict all content derived from the planning doc to the section headed `TASK-<n>`. Ignore all other task sections.

### Step 3 — Determine output path

**If type = initiative:**

- Derive `<project-slug>` from the RFC's project name (lowercase, spaces → hyphens)
- Output: `.claude/planning/<project-slug>/planning.md`
- If `planning.md` already exists in that directory, update it rather than overwriting from scratch

**If type = spec:**

- Output: `.claude/planning/<project-slug>/<issue-number>-<kebab-title>.md`
- `<kebab-title>` comes from the TASK heading in the planning doc, or from the RFC section if no planning doc is available
- Use `issue-000` as a placeholder if no issue number was provided

### Step 4 — Generate the document

**If type = initiative**, produce a planning document following `~/.claude/templates/general_plan_template.md`:

- Title: `# <Initiative Name> — High-Level Planning`
- Header block: project, GitHub repo, Milestone, Notion page (all from RFC if present), total effort
- **Overview**: 2–3 sentence technical summary + ASCII dependency diagram
- One **TASK** section per milestone: GitHub Issue placeholder, Effort, Scope, Goal, Deliverables, Technical Overview. Add "Existing Work" and "Gaps to Close" sub-sections only where the RFC calls out already-completed work.
- **GitHub Issues** section: group tasks into 2–4 milestones with Scope, Goal, Deliverables

Use only RFC information (and planning doc if provided). Do not invent scope, deliverables, or effort.

**If type = spec**, populate `~/.claude/templates/tech_spec_template.md`:

- Title: `# #{issue-number}: <Title>` (use `#issue-000` placeholder if no issue number)
- GitHub Issue link: `https://github.com/<owner>/<repo>/issues/<number>` (placeholder if not provided)
- GitHub Milestone and Notion page links (from RFC or planning doc if present)
- **Technical Scope**: files/modules that change; explicit out-of-scope items
- **Architecture**: ASCII diagram of data flow or component structure
- **Tech Stack**: new packages only with version and justification; omit section if none
- **Implementation Details**:
  - Modules / Files table
  - Key Functions with full docstrings (Args, Returns, Raises)
  - CLI Parameters table (if the component has a CLI)
  - Data Models / Schemas
  - Testing Strategy (unit, integration, edge cases)
  - Open Questions / Risks (checkbox list with target dates)

When `--planning` is provided, the task section in that file defines deliverables and scope — use it as authoritative, not the RFC. Infer implementation details from existing codebase patterns. Do not hallucinate file names — only name files that follow logically from the scope.

### Step 5 — Write the file

Write to the output path from Step 3. Create the directory if needed.

Then report:

- The output file path
- A 2–3 bullet summary of what was generated
