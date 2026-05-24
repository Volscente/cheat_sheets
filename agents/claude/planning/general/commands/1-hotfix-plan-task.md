# Hotfix Plan Task

Generate a tech spec for a hotfix from a hotfix description file.

## Usage

```text
/1-hotfix-plan-task <hotfix-path> --output <output-path>
```

**Arguments:** $ARGUMENTS

## Instructions

You are generating a hotfix tech spec from a hotfix description file. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: hotfix description file path (required)
- `--output`: path where the spec file will be written (required)

### Step 2 — Read inputs

Read the hotfix description file at the provided path. Extract all YAML frontmatter fields and all section content.

**Repository context:** Extract `context-paths` from the hotfix description frontmatter. Read each listed file (paths relative to the project root where the hotfix will be applied). Build an internal context summary covering: relevant module boundaries, public interfaces, key file paths, and any data flows that touch the symptom area. Use this context in Step 4 to name real files, functions, and interfaces — grounding the spec in the actual codebase. Skip silently if `context-paths` is empty or blank.

**Root cause investigation:** If the `## Root cause` section in the hotfix description is blank or absent, investigate using the symptom, the tech stack, and the repository context loaded above. Form a hypothesis and mark it clearly as `(inferred)` in the output. If a root cause hypothesis is provided, treat it as the starting point and refine it using context.

**Fix approach investigation:** If the `## Fix approach` section is blank or absent, propose a minimal fix approach based on the confirmed or inferred root cause. Prefer surgical changes over refactors. If a fix approach is provided, use it as the direction and elaborate.

### Step 3 — Produce the tech spec

Produce a Markdown document with the sections below. Use `---` as a horizontal divider between each section.

#### Header

```markdown
# [HOTFIX] {title}

**Severity:** {severity}
**Affected versions:** {affected-versions joined by ", "}
**Environments:** {environments joined by ", "}
**GitHub Issue:** {github-issue — omit row if blank}
**GitHub Repo:** {github-repo — omit row if blank}
**Tech stack:** {tech-stack joined by ", "}
```

#### Symptom

Exact content from `## Symptom` in the hotfix description.

#### Root Cause Analysis

Either the confirmed or refined root cause from the hotfix description, or the inferred hypothesis (marked `(inferred)`) with the reasoning chain. Include an ASCII diagram only when it helps clarify a non-obvious data flow or call chain.

#### Technical Scope

List in-scope files and components that must change to resolve the symptom — use real file paths from repository context where available. List out-of-scope items drawn from `## Scope` in the hotfix description.

#### Implementation Details

A **Modules / Files** table with columns: File, Action (Create / Modify / Delete), Description of the change.

A **Key Changes** sub-section: for each file in the table, describe the specific lines, functions, or configuration that must change. Write full function signatures with docstrings only for new or significantly altered functions; for small targeted changes, a concise prose description suffices.

Omit CLI Parameters and Data Models sub-sections unless the fix directly involves a CLI or a schema change.

#### Verification

Drawn from `## Verification steps` in the hotfix description, elaborated with concrete commands where context allows. Structured as manual checks (per environment), automated test commands, and edge cases to validate.

#### Open Questions / Risks

Seeded from `## Known risks` in the hotfix description, plus any risks identified during root cause analysis. Each item formatted as:

```markdown
- [ ] **{Risk or question}:** {Description.} **Target:** {date or "TBD"}
```

Do not invent scope, file paths, or function names that cannot be derived from the hotfix description or the repository context.

### Step 4 — Write the file

Write the document to the path given by `--output`. Create intermediate directories if needed. If the file already exists, update it rather than overwriting from scratch.

Then report:

- The output file path
- 2–3 bullet summary of the root cause conclusion and the fix approach chosen
