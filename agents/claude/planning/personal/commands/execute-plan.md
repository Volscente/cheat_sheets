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

- First positional argument: path to the RFC Markdown file (required) — provides initiative-level context and motivation
- Second positional argument: path to the spec Markdown file (required) — defines exactly what to implement

### Step 2 — Read inputs

Read both files in full:

1. The RFC at the first path — for project context, motivation, and constraints
2. The spec at the second path — the authoritative source of truth for what to build

Also read `CLAUDE.md` (if present) for project conventions, then explore the existing codebase to understand patterns before touching any code:

- Identify every file the spec names under "Modules / Files" or equivalent
- Read each existing file that will be modified
- For new files, read 1–2 analogous existing files to match style and structure

Do not begin writing code until you have read all relevant existing files.

### Step 3 — Build a task list

Decompose the spec into discrete implementation tasks using `TaskCreate`. Create one task per logical unit of work (e.g. one task per new file or modified module, one task for tests).

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
- If the spec defines a Pydantic model or data schema, implement it verbatim.
- If the spec defines a testing strategy, write the tests described. Do not add tests beyond what the spec calls for.
- If the spec flags open questions, do not resolve them silently — surface them in your final report.

### Step 5 — Verify

After implementing all tasks, run the project's test suite and linters if they are configured:

```bash
pytest                        # or: uv run pytest
pre-commit run --all-files    # if pre-commit is configured
```

If tests fail, diagnose the root cause and fix before reporting done. Do not skip or comment out failing tests.

If no test suite is configured, note this in the final report.

### Step 6 — Document

For each package directory created or modified during implementation:

1. Locate the package root (the directory containing `__init__.py`, or the top-level project root if no package was created).
2. Check whether a `README.md` exists in that directory.
   - **If it exists:** append a changelog entry at the bottom using today's date and a brief bullet-point list of what was added or changed.
   - **If it does not exist:** create a `README.md` describing the package — its purpose, the modules it contains, key functions, and a changelog entry for today.
3. The README must include a **Usage** section showing how to run the feature, with key parameters and example values.
4. Do not create duplicate README files. One README per package directory is sufficient.
5. Keep the content concise: a short description, a usage section, and a changelog block.

### Step 7 — Report

Output a concise summary:

- Files created or modified (one line each, with path)
- Any spec open questions that remain unresolved
- Any deliberate deviations from the spec, with the reason
- Test and lint status (or a note if no suite is configured)
