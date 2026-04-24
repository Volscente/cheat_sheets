# Execute Plan

Implement all scripts, functions, and code changes described in a spec file.

## Usage

```text
/execute-plan <rfc-path> <spec-path>
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

### Step 5 — Verify

After implementing all tasks, run the project's test suite and linters:

```bash
uv run pytest
pre-commit run --all-files
```

If tests fail, diagnose the root cause and fix before reporting done. Do not skip or comment out failing tests.

### Step 6 — Report

Output a concise summary:

- Files created or modified (one line each, with path)
- Any spec open questions that remain unresolved
- Any deliberate deviations from the spec, with the reason
- Test and lint status
