# Hotfix Execute Plan

Implement all code changes described in a hotfix tech spec.

## Usage

```text
/2-hotfix-execute-plan <spec-path> [--version <patch-version>]
```

**Arguments:** $ARGUMENTS

## Instructions

You are implementing the code changes described in a hotfix tech spec. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- First positional argument: path to the hotfix tech spec Markdown file (required) — defines exactly what to implement
- `--version`: patch version string to record in `CHANGELOG.md` and `pyproject.toml` (e.g. `1.4.3`); omit if no version bump is needed

### Step 2 — Read inputs

Read the spec file in full. It is the authoritative source of truth for what to change.

Also read `CLAUDE.md` (if present) for project conventions, then explore the codebase before touching any code:

- Identify every file the spec names under "Modules / Files"
- Read each existing file that will be modified
- For new files, read 1–2 analogous existing files to match style and structure

Do not begin writing code until you have read all relevant existing files.

### Step 3 — Build a task list

Decompose the spec into discrete implementation tasks using `TaskCreate`. One task per logical unit of work (one per new file or modified module, one for tests).

Order tasks so that dependencies come first. Mark blocking relationships with `addBlocks` / `addBlockedBy`.

### Step 4 — Implement

Work through the task list in order. For each task:

1. Mark the task `in_progress` before starting.
2. Implement only what the spec describes — no extra features, no speculative abstractions.
3. Match the style of the existing file being modified or the analogous file read in Step 2.
4. Remove only imports/variables/functions that your own changes make unused. Do not clean up pre-existing dead code.
5. Mark the task `completed` immediately after finishing it.

**Implementation rules:**

- Follow the "Modules / Files" table exactly — create or modify only those files unless a transitive dependency is unavoidable.
- Implement every function listed under "Key Changes" with the exact signature and docstring shown in the spec.
- If the spec defines a testing strategy, write exactly those tests. Do not add tests beyond what the spec calls for.
- If the spec flags open questions, do not resolve them silently — surface them in the final report.
- Keep changes surgical: do not refactor surrounding code that is unrelated to the bug.

### Step 5 — Verify

Run the project's test suite and linters if configured:

```bash
pytest                        # or: uv run pytest / python -m pytest
pre-commit run --all-files    # if pre-commit is configured
```

If tests fail, diagnose the root cause and fix before reporting done. Do not skip or comment out failing tests.

Then run the manual verification steps listed under "Verification" in the spec. Document each step's result in the final report.

If no test suite is configured, note this in the final report.

### Step 6 — Update changelog

If `--version` was provided, update `CHANGELOG.md` in the project root. Use the provided version and today's date. Follow this style:

```md
## [1.4.3] - 2026-05-24

### Fixed

- **{Component}**: {What was broken and what the fix does.}
```

If `--version` was not provided, skip this step.

### Step 7 — Report

Output a concise summary:

- Files created or modified (one line each, with path)
- Result of each manual verification step from the spec
- Any spec open questions that remain unresolved
- Any deliberate deviations from the spec, with the reason
- Test and lint status (or a note if no suite is configured)
