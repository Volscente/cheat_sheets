# Create / Update Module README

Generate or update a `README.md` for a module or package inside a repository.
The README serves as a semantic summary for both humans and Claude — concise enough
to load on demand, rich enough to inform design decisions.

## Usage

```text
/create-readme --path <module-path> [--out <output-path>]
```

**Arguments:** $ARGUMENTS

### Parameters

| Parameter | Required | Description                                                  | Example            |
| :-------- | :------- | :----------------------------------------------------------- | :----------------- |
| `--path`  | Yes      | Path to the module or package directory to analyse           | `src/auth`         |
| `--out`   | No       | Override output path (default: `README.md` inside `--path`) | `docs/auth-api.md` |

---

## Instructions

You are generating or updating a `README.md` that acts as a semantic summary of a module
or package. Its purpose is to let a reader — human or Claude — understand the module's
role, boundaries, and interfaces without reading every source file.

Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- `--path` (required): path to the module or package directory
- `--out` (optional): override output file path

### Step 2 — Determine mode

Check whether a `README.md` already exists at the output path (default: `<path>/README.md`):

- If it **does not exist**: mode is **create**
- If it **exists**: mode is **update** — read the existing file now and note which sections
  are present; you will preserve accurate content and refresh stale content in Step 6

### Step 3 — Explore the module

Explore the directory at `--path` to understand its structure and behaviour:

1. **List all files** — build a map of the directory tree (one level deep is usually enough;
   recurse only if subdirectories are themselves sub-modules)
2. **Identify entry points** — files that other modules import from or that expose a public
   API: `__init__.py`, `index.ts`, `index.js`, `main.py`, `router.py`, `api.py`, etc.
3. **Read key files** — read the entry points identified above, plus any files whose names
   suggest they define core logic, data models, or public interfaces
4. **Infer external dependencies** — scan import statements for third-party packages
   (anything not from the standard library or this repository)
5. **Infer public interfaces** — from the entry points, identify exported functions, classes,
   REST endpoints, CLI commands, or events that callers outside this module use
6. **Identify constraints / invariants** — look for docstrings, comments, or decorators
   that describe SLAs, security rules, idempotency requirements, or similar invariants

Do **not** read every file exhaustively — focus on what is needed to answer the six
questions above. Stop reading a file once you have the information you need.

### Step 4 — Read the README template

Read `~/.claude/templates/readme-template.md` — this is the canonical output structure.

### Step 5 — Determine the output path

If `--out` was provided, use it directly.

Otherwise: `<path>/README.md` (inside the module directory from `--path`).

### Step 6 — Generate or update the README

Produce a README that follows the structure from Step 4. Apply these rules per section:

**Module name (heading):** Use the directory name from `--path`, formatted as title case.
If the directory name is abbreviated or unclear, expand it using what you learned in Step 3.

**Purpose:** Write 2–3 sentences describing what this module does and why it exists in the
context of the larger system. Focus on role, not implementation. Do not list files here.

**Key components:** One bullet per meaningful file, class, or service found in Step 3.
Omit trivial files: test files, config files, `__init__.py` or `index.*` with no logic.

**Public interfaces:** List the functions, classes, endpoints, events, or CLI commands
that form the contract this module exposes to callers. Omit internal helpers.
Use the inferred interfaces from Step 3. If you cannot determine the full interface from
the code, include what you found and add a `{Description}` placeholder for gaps.

**External dependencies:** List only the direct, meaningful third-party dependencies found
in Step 3. Omit standard-library modules and dev-only tools (linters, formatters, test runners).

**Constraints / invariants:** List only non-obvious rules inferred from code comments,
docstrings, decorators, or naming conventions. If none are evident, write
`None identified — add if known.` rather than inventing constraints.

**Out of scope:** Derive from what the module clearly does NOT handle — based on what is
absent from the code, what is delegated to other modules, or what is explicitly excluded
in comments. If updating an existing README, preserve any manually written out-of-scope
items that are still accurate.

**Update mode rules:** When mode is update (Step 2):

- Refresh any section whose content is demonstrably stale (e.g. lists a file that no longer
  exists, or omits a new public interface)
- Preserve sections that are still accurate, especially manually-authored content in
  **Constraints / invariants** and **Out of scope**
- Do not shrink or rewrite accurate content just because you would phrase it differently

**Remove all template comment blocks** (`<!-- ... -->`).

**Do not hallucinate details** — use `{Description}` placeholders for anything not inferable
from the code.

### Step 7 — Write the file

Write to the output path from Step 5. Create the directory if needed.

Then report:

- Output file path
- Mode used (create or update)
- Which sections were fully populated vs. contain placeholders
- Any files you read to derive the content (so the user can verify coverage)
- Any gaps where you could not infer content from the code (e.g. constraints not
  documented in source) — these are hints for the user to fill in manually
