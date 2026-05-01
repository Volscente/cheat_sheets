# Execute Plan

Implement all scripts, functions, and code changes described in a spec file.

## Usage

```text
/4-work-execute-plan <rfc-path> <spec-path>
```

**Arguments:** $ARGUMENTS

## Instructions

You are implementing the code changes described in a spec file. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: path to the RFC Markdown file (required) — provides initiative-level context
- Second positional argument: path to the spec Markdown file (required) — defines exactly what to implement

### Step 2 — Read inputs

Read both files in full:

1. The RFC at the first path — for initiative context, motivation, and constraints
2. The spec at the second path — the authoritative source of truth for what to build

Also read `CLAUDE.md` for project conventions, then explore the existing codebase to understand patterns before touching any code:

- Identify every file the spec names under "Modules / Files" or equivalent
- Read each existing file that will be modified
- For new files, read 1–2 analogous existing files to match style and structure

Do not begin writing code until you have read all relevant existing files.

### Step 3 — Build a task list

Decompose the spec into discrete implementation tasks using `TaskCreate`. Create one task per logical unit of work (e.g. one task per new file or modified module, one task for tests, one task for SQL/schema changes).

Order tasks so that dependencies come first. Mark blocking relationships with `addBlocks` / `addBlockedBy`.

### Step 4 — Implement

Work through the task list in order. For each task:

1. Mark the task `in_progress` before starting.
2. Implement only what the spec describes — no extra features, no speculative abstractions.
3. Match the style of the existing file being modified or the analogous file you read in Step 2.
4. Remove only imports/variables/functions that your own changes make unused. Do not clean up pre-existing dead code.
5. Mark the task `completed` immediately after finishing it.

**Implementation rules:**

- Follow the "Modules / Files" table in the spec exactly — create or modify only those files unless a transitive dependency is unavoidable.
- Implement every function listed under "Key Functions", with the exact signature and docstring shown in the spec.
- If the spec defines CLI parameters, wire them up exactly as specified.
- If the spec defines a BigQuery schema or Pydantic model, implement it verbatim.
- If the spec defines a testing strategy, write the tests described. Do not add tests beyond what the spec calls for.
- If the spec flags open questions, do not resolve them silently — surface them in your final report.

**`justfile` commands:**

After implementing the core code, add or update a recipe in `justfile` that exposes the new feature as a `just` command. Read the existing `justfile` first to match its style and grouping. If a recipe for this feature already exists, update it only if its arguments or invocation need to change. Place the new recipe near other recipes in the same domain (e.g., near other markup or translation commands). Keep the recipe concise — one command, clear comment, sensible defaults for optional parameters.

### Step 5 — Verify

After implementing all tasks, run the project's test suite and linters:

```bash
uv run pytest
pre-commit run --all-files
```

If tests fail, diagnose the root cause and fix before reporting done. Do not skip or comment out failing tests.

### Step 6 — Document

For each Python package directory created or modified during implementation:

1. Locate the package root (the directory containing `__init__.py` or, if no package was created, the top-level project root).
2. Check whether a `README.md` exists in that directory.
   - **If it exists:** append a changelog entry at the bottom of the file using today's date (from `currentDate`) and a brief bullet-point list of what was added or changed.
   - **If it does not exist:** create a `README.md` that describes the package — its purpose, the modules it contains, key functions, and a changelog entry for today.
3. The README must include a **Usage** section showing how to run the feature — both the raw `uv run python -m ...` invocation and the `just` command added in Step 4. Include the key parameters with example values.
4. Do not create duplicate README files. One README per package directory is sufficient.
5. Keep the content concise: a short description, a usage section, and a changelog block — not a full tutorial.

### Step 7 — Report

Output a concise summary:

- Files created or modified (one line each, with path)
- Any spec open questions that remain unresolved
- Any deliberate deviations from the spec, with the reason
- Test and lint status
