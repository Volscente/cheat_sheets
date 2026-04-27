# Create RFC

Generate a new RFC document from the project template, pre-filled with the provided inputs.

## Usage

```text
/create-rfc --title <title> --author <name> --problem <statement> [options]
```

**Arguments:** $ARGUMENTS

### Required parameters

| Parameter | Description | Example |
| :-------- | :---------- | :------ |
| `--title` | Short descriptive title of the RFC | `"CLI Tool for Automating Dotfile Sync"` |
| `--author` | Author name | `"Simone Porreca"` |
| `--problem` | 1–3 sentence description of the problem or opportunity being addressed | `"Keeping dotfiles in sync across machines is manual and error-prone. There is no automated way to apply changes after a pull."` |

### Optional parameters

| Parameter | Default | Description | Example |
| :-------- | :------ | :---------- | :------ |
| `--project` | _(blank)_ | Project or repo name | `"dotfile-manager"` |
| `--github-repo` | _(none)_ | GitHub repository URL or `owner/repo` | `"simone/dotfile-manager"` |
| `--notion-page` | _(none)_ | URL of the related Notion page | `"https://notion.so/..."` |
| `--deadline` | 2 weeks from today | Review deadline (YYYY-MM-DD) | `"2026-05-15"` |
| `--reviewers` | _(none)_ | Comma-separated list of reviewer names and optional/required status | `"Alice required, Bob optional"` |
| `--scope-in` | _(none)_ | Comma-separated list of in-scope capabilities | `"Config parser, apply command, dry-run mode"` |
| `--scope-out` | _(none)_ | Comma-separated list of out-of-scope items with reasons (`"item: reason"`) | `"GUI: out of scope, Cloud sync: future phase"` |
| `--tech-stack` | _(none)_ | Comma-separated list of libraries/tools to include | `"Python, click, watchdog"` |
| `--milestones` | _(none)_ | Comma-separated list of milestone names | `"Config parser, Apply command, CI workflow"` |
| `--out` | `docs/rfc/<project-slug>_<title-slug>/rfc_document.md` | Override the output file path | `"docs/rfc/my_rfc/rfc_document.md"` |

---

## Example

```text
/create-rfc \
  --title "CLI Tool for Automating Dotfile Sync" \
  --author "Simone Porreca" \
  --project "dotfile-manager" \
  --github-repo "simone/dotfile-manager" \
  --problem "Keeping dotfiles in sync across machines is manual and error-prone. There is no automated way to detect changes in the repo and apply them without running commands by hand." \
  --deadline "2026-05-15" \
  --scope-in "Config parser, apply command, dry-run mode, file conflict detection" \
  --scope-out "GUI: out of scope for this RFC, Cloud sync: deferred to future phase" \
  --tech-stack "Python, click, watchdog, pytest" \
  --milestones "Config parser, Apply command, Conflict detection, CI integration"
```

---

## Instructions

You are generating a new RFC document. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- `--title` (required): short RFC title
- `--author` (required): author name
- `--problem` (required): problem or motivation statement
- `--project` (optional): project or repo name; leave blank if not provided
- `--github-repo` (optional): GitHub repo URL or `owner/repo` string; leave blank if not provided
- `--notion-page` (optional): Notion page URL; leave blank if not provided
- `--deadline` (optional): review deadline as YYYY-MM-DD; if absent, default to 14 days from today's date
- `--reviewers` (optional): parse into a list of `{name, required|optional}` entries; if absent, remove the Reviews table
- `--scope-in` (optional): split on commas → list of in-scope items
- `--scope-out` (optional): split on commas → list of out-of-scope items; each item may have a `"item: reason"` format — split on the first colon
- `--tech-stack` (optional): split on commas → list of library/tool names
- `--milestones` (optional): split on commas → ordered list of milestone names
- `--out` (optional): override the output file path

### Step 2 — Read the template

Read `templates/rfc_template.md` — this is the canonical structure the RFC must follow.

### Step 3 — Determine the output path

If `--out` was provided, use it directly.

Otherwise, derive the path as:
```
docs/rfc/<project-slug>_<title-slug>/rfc_document.md
```
where `<project-slug>` is `--project` lowercased with spaces replaced by underscores, and `<title-slug>` is `--title` lowercased with spaces replaced by underscores.

If `--project` was not provided, use only `<title-slug>`.

If the directory does not exist, it will be created when writing.

### Step 4 — Generate the RFC

Produce a complete RFC document following the template structure. Apply these rules:

**Header block:**
- Set `Author(s)` from `--author`
- Set `Project` from `--project` (blank if not provided)
- Set `RFC status` to `Draft`
- Set `Review deadline` from `--deadline`
- Set `GitHub repo` link if `--github-repo` was provided, otherwise omit the row
- Set `Notion page` link if `--notion-page` was provided, otherwise omit the row
- Set today's date in the Timeline table

**Reviews table:**
- If `--reviewers` was provided, populate one row per reviewer with name and Required/Optional status
- If not provided, remove the Reviews table and its comment entirely

**Title:**
- Format as `[RFC] {Title}` — derive from `--title`

**Context section:**
- Write 1–2 sentences placing the RFC in the context of `--project` (or the title slug if no project was given)
- Link to `--notion-page` and `--github-repo` if provided

**Motivation section:**
- Expand `--problem` into 2–3 paragraphs describing:
  1. The current situation or gap
  2. The specific pain point, limitation, or opportunity
  3. What would be different once this is built
- Do not invent facts. Work only from what `--problem` states.
- Write in a direct, personal tone — not a business case.

**Objectives section:**
- Derive 3–5 concrete objectives from the problem statement and scope items
- Each must start with a bold action label and be outcome-oriented, not task-oriented

**Scope:**
- In-Scope: populate from `--scope-in` if provided; otherwise leave placeholders
- Out-of-Scope: populate from `--scope-out` if provided; otherwise leave placeholders

**Main technical section:**
- Name it after `--title`
- Write an Approach Overview paragraph describing the high-level design derived from the problem and scope
- If `--milestones` was provided, generate one subsection per milestone with a placeholder description
- If not provided, keep the two generic subsection placeholders

**Tech Stack:**
- If `--tech-stack` was provided, list each item with a placeholder "why it is used" description derived from its name
- If not provided, keep the placeholder rows

**Effort Estimations:**
- If `--milestones` was provided, generate one table row per milestone with a placeholder effort estimate
- If not provided, keep the two placeholder rows

**FAQs:**
- Generate 3–5 Q&A pairs anticipating likely questions based on the problem and scope
- Always include a Terminology entry if acronyms appear in the RFC

**Risks & Open Questions:**
- Generate 2–4 risks or open questions inferred from the problem and scope

**Remove all template comment blocks** (`<!-- ... -->`) from the output.

**Do not hallucinate details** — for sections where no input was provided, use clear placeholder text (e.g. `{Description}`) rather than invented content.

### Step 5 — Write the file

Write the generated RFC to the output path from Step 3.

Then report:
- The output file path
- Which sections were fully populated vs. left as placeholders
- Any assumptions made during generation
