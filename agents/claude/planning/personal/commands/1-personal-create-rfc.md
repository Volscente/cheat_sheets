# Create RFC

Generate a new RFC document from a filled proposal file. All RFC content lives in the proposal;
the command only needs to know where the proposal is and where to write the output.

## Usage

```text
/1-personal-create-rfc --file <path-to-proposal> [--out <output-path>]
```

**Arguments:** $ARGUMENTS

### Parameters

| Parameter | Required | Description                                                        | Example                                                 |
| :-------- | :------- | :----------------------------------------------------------------- | :------------------------------------------------------ |
| `--file`  | Yes      | Path to the filled `proposal.md`                                   | `.claude/rfc/recipe-app_add-search-bar/proposal.md`     |
| `--out`   | No       | Override output path (default: `rfc_document.md` next to `--file`) | `.claude/rfc/recipe-app_add-search-bar/rfc_document.md` |

---

## Workflow

1. Copy `~/.claude/templates/personal_rfc_proposal_template.md` to
   `.claude/rfc/<initiative-name>/proposal.md`.
2. Fill out the YAML frontmatter and `## Problem` section (required).
   Optionally fill any of: `## Approach direction`, `## Success criteria`, `## Constraints`,
   `## Desired tech`, `## Integration context`, `## Known risks / concerns`.
3. Run `/1-personal-create-rfc --file .claude/rfc/<initiative-name>/proposal.md`.

---

## Example

```text
/1-personal-create-rfc --file .claude/rfc/recipe-app_add-search-bar/proposal.md
```

---

## Instructions

You are generating a new RFC document. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- `--file` (required): path to the filled proposal file
- `--out` (optional): override output file path

### Step 2 — Read the proposal file

Read the file at the path from `--file`. Extract:

- **YAML frontmatter** (between `---` delimiters): parse all fields:
  - `title`, `project`, `author`, `deadline`
  - `notion-page`, `github-repo`, `milestone` (optional — omit corresponding RFC header rows if blank)
  - `tech-stack` (list — the existing/required stack), `scope-in` (list), `scope-out` (list, format `"Item: reason"`)
  - `milestones` (ordered list)
- **Markdown sections** (each is optional — treat as absent if blank or missing):
  - `## Problem`: the problem statement (required)
  - `## Approach direction`: author's preferred high-level approach
  - `## Success criteria`: measurable outcomes the author has in mind
  - `## Constraints`: hard non-negotiable requirements
  - `## Desired tech`: new technologies the author wants to use, with reasoning
  - `## Integration context`: how the solution should integrate with the existing system
  - `## Known risks / concerns`: doubts or uncertainties the author already identified

### Step 3 — Read the RFC template

Read `~/.claude/templates/personal_rfc_template.md` — this is the canonical output structure.

### Step 4 — Determine the output path

If `--out` was provided, use it directly.

Otherwise: same directory as `--file`, filename `rfc_document.md`.

### Step 5 — Generate the RFC

**Header block:**

- `Author`: from `author`
- `Project`: from `project`
- `RFC status`: `Draft`
- `Review deadline`: from `deadline`; if blank, default to 14 days from today
- `Notion page`: link if `notion-page` is non-blank, otherwise omit the row
- `GitHub repo`: link if `github-repo` is non-blank, otherwise omit the row
- `Milestone`: link if `milestone` is non-blank, otherwise omit the row
- Today's date in the Timeline table

**Motivation section:**

- Write exactly **1 paragraph** using the `## Problem` prose from the proposal
- End with: `For full context, see the [Notion initiative page](<notion-page-url>).` (omit this sentence if `notion-page` is blank)
- Do not expand into personal motivation — that is Notion's job

**Objectives:**

- If `## Success criteria` is non-blank: derive objectives directly from those criteria; each starts with a bold action label and is outcome-oriented
- If blank: derive 3–5 concrete, verifiable objectives from the problem and scope

**Scope:**

- In-Scope: from `scope-in` if non-empty
- Out-of-Scope: from `scope-out` if non-empty; each item uses the `"Item: reason"` split on the first colon
- If `## Constraints` is non-blank: add a **Constraints** paragraph after Out-of-Scope listing all non-negotiable requirements

**Main technical section:**

- Named after `title`
- Approach Overview:
  - If `## Approach direction` is non-blank: open with the author's stated approach, then expand into 1–2 paragraphs of high-level design
  - If blank: derive 1–2 paragraphs of high-level design from problem and scope
  - If `## Integration context` is non-blank: add a subsection **Integration** describing how the solution connects to the existing system, using the author's notes
  - If blank: omit the Integration subsection
- If `milestones` is non-empty: one subsection per milestone with placeholder description
- If empty: two generic placeholder subsections

**Tech Stack:**

- If `tech-stack` (YAML) is non-empty: one bullet per item with placeholder justification derived from the tool name (existing/required stack)
- If `## Desired tech` is non-blank: add a **Desired / experimental** subsection listing those technologies with the author's reasoning
- If both are empty: placeholder rows

**Effort Estimations:**

- If `milestones` is non-empty: one table row per milestone with placeholder effort and a `#{issue}` placeholder for the GitHub Issue number
- If empty: placeholder rows

**FAQs:**

- Generate 3–5 Q&A pairs from the problem and scope
- Always include a Terminology entry if acronyms appear

**Risks & Open Questions:**

- If `## Known risks / concerns` is non-blank: use those as the first rows of the table; add likelihood and mitigation for each
- Supplement with 1–2 additional risks inferred from the problem and scope (omit if the author's list is already comprehensive)

**Remove all template comment blocks** (`<!-- ... -->`).

**Do not hallucinate details** — use `{Description}` placeholders for anything not provided.

### Step 6 — Write the file

Write to the output path from Step 4. Create the directory if needed.

Then report:

- Output file path
- Which sections were fully populated vs. left as placeholders
- Any assumptions made (e.g., deadline defaulted)
