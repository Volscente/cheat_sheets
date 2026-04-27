# Create RFC

Generate a new RFC document from the project template. The RFC is a **technical document for Claude** — it captures how something will be built. Personal motivation and context live in the Notion initiative page; the RFC links back to it and keeps its Motivation section brief.

## Usage

```text
/create-rfc --title <title> --project <project> --author <name> --problem <statement> [options]
```

**Arguments:** $ARGUMENTS

### Required parameters

| Parameter | Description | Example |
| :-------- | :---------- | :------ |
| `--title` | Short descriptive title of the RFC | `"Add Search Bar"` |
| `--project` | Project or repo name | `"recipe-app"` |
| `--author` | Author name | `"Simone Porreca"` |
| `--problem` | Technical gap being addressed — 1–2 sentences, no personal motivation | `"The app has no search capability. With 200+ recipes, users cannot find entries without scrolling the full list."` |

### Optional parameters

| Parameter | Default | Description | Example |
| :-------- | :------ | :---------- | :------ |
| `--notion-page` | _(none)_ | URL of the Notion initiative page (personal context lives here) | `"https://notion.so/..."` |
| `--github-repo` | _(none)_ | GitHub repo as `owner/repo` | `"simone/recipe-app"` |
| `--milestone` | _(none)_ | GitHub Milestone name | `"Add Search Bar"` |
| `--deadline` | 2 weeks from today | Review deadline (YYYY-MM-DD) | `"2026-05-15"` |
| `--scope-in` | _(none)_ | Comma-separated in-scope capabilities | `"Search index, search UI, keyboard shortcut"` |
| `--scope-out` | _(none)_ | Comma-separated out-of-scope items (`"item: reason"`) | `"Fuzzy search: future phase, Filters: separate initiative"` |
| `--tech-stack` | _(none)_ | Comma-separated libraries/tools | `"Python, Flask, whoosh"` |
| `--milestones` | _(none)_ | Comma-separated milestone names (each maps to a GitHub Issue) | `"Search index, Search UI, Keyboard shortcut"` |
| `--out` | `docs/rfc/<project-slug>_<title-slug>/rfc_document.md` | Override output path | `"docs/rfc/my-rfc/rfc_document.md"` |

---

## Example

```text
/create-rfc \
  --title "Add Search Bar" \
  --project "recipe-app" \
  --author "Simone Porreca" \
  --github-repo "simone/recipe-app" \
  --notion-page "https://notion.so/Add-Search-Bar-abc123" \
  --milestone "Add Search Bar" \
  --problem "The app has no search capability. With 200+ saved recipes, users cannot find entries without scrolling the full list." \
  --scope-in "Full-text search index, search UI component, keyboard shortcut" \
  --scope-out "Fuzzy matching: future phase, Filters by tag: separate initiative" \
  --tech-stack "whoosh, Flask, pytest" \
  --milestones "Implement search index, Build search UI, Add keyboard shortcut"
```

---

## Instructions

You are generating a new RFC document. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- `--title` (required): short RFC title
- `--project` (required): project or repo name
- `--author` (required): author name
- `--problem` (required): technical gap statement (1–2 sentences)
- `--notion-page` (optional): Notion initiative page URL
- `--github-repo` (optional): GitHub repo as `owner/repo`
- `--milestone` (optional): GitHub Milestone name
- `--deadline` (optional): YYYY-MM-DD; if absent, default to 14 days from today
- `--scope-in` (optional): split on commas → list of in-scope items
- `--scope-out` (optional): split on commas → list of out-of-scope items; each may have `"item: reason"` format — split on the first colon
- `--tech-stack` (optional): split on commas → list of library/tool names
- `--milestones` (optional): split on commas → ordered list of milestone names
- `--out` (optional): override output file path

### Step 2 — Read the template

Read `templates/rfc_template.md` — this is the canonical structure.

### Step 3 — Determine the output path

If `--out` was provided, use it directly.

Otherwise:
```
docs/rfc/<project-slug>_<title-slug>/rfc_document.md
```
where `<project-slug>` is `--project` lowercased with spaces/hyphens replaced by underscores, and `<title-slug>` is `--title` lowercased with spaces replaced by underscores.

### Step 4 — Generate the RFC

**Header block:**
- `Author`: from `--author`
- `Project`: from `--project`
- `RFC status`: `Draft`
- `Review deadline`: from `--deadline`
- `Notion page`: link if `--notion-page` provided, otherwise omit the row
- `GitHub repo`: link if `--github-repo` provided, otherwise omit the row
- `Milestone`: link if `--milestone` provided, otherwise omit the row
- Today's date in the Timeline table

**Motivation section:**
- Write exactly **1 paragraph** stating the technical gap from `--problem`
- End with: `For full context, see the [Notion initiative page](<notion-page-url>).` (omit this sentence if `--notion-page` was not provided)
- Do not expand into personal motivation — that is Notion's job

**Objectives:**
- Derive 3–5 concrete, verifiable objectives from the problem and scope
- Each starts with a bold action label and is outcome-oriented

**Scope:**
- In-Scope: from `--scope-in` if provided
- Out-of-Scope: from `--scope-out` if provided

**Main technical section:**
- Named after `--title`
- Approach Overview: 1–2 paragraphs describing the high-level design derived from problem and scope
- If `--milestones` provided: one subsection per milestone with placeholder description
- If not: two generic placeholder subsections

**Tech Stack:**
- If `--tech-stack` provided: one bullet per item with placeholder justification derived from the tool name
- If not: placeholder rows

**Effort Estimations:**
- If `--milestones` provided: one table row per milestone with placeholder effort and a `#{issue}` placeholder for the GitHub Issue number
- If not: placeholder rows

**FAQs:**
- Generate 3–5 Q&A pairs from the problem and scope
- Always include a Terminology entry if acronyms appear

**Risks & Open Questions:**
- Generate 2–4 risks or open questions inferred from the problem and scope

**Remove all template comment blocks** (`<!-- ... -->`).

**Do not hallucinate details** — use `{Description}` placeholders for anything not provided.

### Step 5 — Write the file

Write to the output path from Step 3. Create the directory if needed.

Then report:
- Output file path
- Which sections were fully populated vs. left as placeholders
- Any assumptions made
