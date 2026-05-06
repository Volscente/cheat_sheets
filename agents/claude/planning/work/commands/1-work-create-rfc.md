# Create RFC

Generate a new RFC document from a filled proposal file. All RFC content lives in the proposal;
the command only needs to know where the proposal is and where to write the output.

## Usage

```text
/1-work-create-rfc --file <path-to-proposal> [--out <output-path>]
```

**Arguments:** $ARGUMENTS

### Parameters

| Parameter | Required | Description                                                        | Example                                                               |
| :-------- | :------- | :----------------------------------------------------------------- | :-------------------------------------------------------------------- |
| `--file`  | Yes      | Path to the filled `proposal.md`                                   | `docs/rfc/vdata-9356_online_catalog_dataset_pipeline/proposal.md`     |
| `--out`   | No       | Override output path (default: `rfc_document.md` next to `--file`) | `docs/rfc/vdata-9356_online_catalog_dataset_pipeline/rfc_document.md` |

---

## Workflow

1. Copy `~/.claude/templates/work_rfc_proposal_template.md` to
   `docs/rfc/<jira-epic-lowercase>_<title-slug>/proposal.md`.
2. Fill out the YAML frontmatter and `## Problem` section (required).
   Optionally fill any of: `## Approach direction`, `## Success criteria`, `## Constraints`,
   `## Desired tech`, `## Integration context`, `## Known risks / concerns`.
3. Run `/1-work-create-rfc --file docs/rfc/<jira-epic-lowercase>_<title-slug>/proposal.md`.

---

## Example

```text
/1-work-create-rfc --file docs/rfc/vdata-9356_online_catalog_dataset_pipeline/proposal.md
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
  - `title`, `team`, `author`, `jira-epic` (required fields)
  - `org` (optional — blank if not provided)
  - `deadline` (optional — default to 14 days from today if blank)
  - `reviewers` (list, format `"Name <email> required|optional"` — parse each into name, email, and status)
  - `tech-stack` (list), `scope-in` (list), `scope-out` (list, format `"Item: reason"`)
  - `milestones` (ordered list)
- **Markdown sections** (each is optional — treat as absent if blank or missing):
  - `## Problem`: the problem statement (required)
  - `## Approach direction`: author's preferred high-level technical approach
  - `## Success criteria`: measurable outcomes the author has in mind
  - `## Constraints`: hard non-negotiable requirements
  - `## Desired tech`: new technologies the author wants to introduce, with reasoning
  - `## Integration context`: how the solution should integrate with the existing system
  - `## Known risks / concerns`: doubts, technical unknowns, or stakeholder concerns already identified

### Step 3 — Read the template and style reference

Read `~/.claude/templates/work_rfc_template.md` — this is the canonical output structure.

### Step 4 — Determine the output path

If `--out` was provided, use it directly.

Otherwise: same directory as `--file`, filename `rfc_document.md`.

### Step 5 — Generate the RFC

**Title:**

- Format as `[RFC] {team}: {title}` — from `team` and `title` frontmatter fields

**Header block:**

- `Author(s)`: from `author`
- `Owner(s)`: from `team`
- `Org(s)`: from `org` (blank if not provided)
- `RFC status`: `Draft`
- `Review deadline`: from `deadline`
- Today's date in the Timeline table

**Reviews table:**

- If `reviewers` is non-empty: one row per reviewer — name, team inferred from email domain context, Required/Optional status
- If empty: keep the two placeholder rows from the template

**Motivation section:**

- Expand the `## Problem` prose into 2–3 paragraphs following this four-point structure:
  1. What system or process is being changed
  2. The specific gap or pain point
  3. What happens without this RFC
  4. The primary requirement the proposal must satisfy
- Do not invent facts — work only from what the Problem section states

**Objectives:**

- If `## Success criteria` is non-blank: derive objectives directly from those criteria; each starts with a bold action label and is outcome-oriented, not task-oriented
- If blank: derive 3–5 concrete objectives from the problem and scope

**Scope:**

- In-Scope: from `scope-in` if non-empty
- Out-of-Scope: from `scope-out` if non-empty; each item uses the `"Item: reason"` split on the first colon
- If `## Constraints` is non-blank: add a **Constraints** paragraph after Out-of-Scope listing all non-negotiable requirements

**Main technical section:**

- Named after `title` (e.g. `# Online Catalog Dataset Pipeline`)
- Methodology Overview:
  - If `## Approach direction` is non-blank: open with the author's stated approach, then expand into the standard 2–3 paragraph methodology description
  - If blank: derive the methodology description from problem and scope as before
  - If `## Integration context` is non-blank: add an **Integration** subsection describing how the solution connects to the existing system, using the author's notes
  - If blank: omit the Integration subsection
- If `milestones` is non-empty: one subsection per milestone with a placeholder description
- If empty: two generic placeholder subsections

**Tech Stack:**

- If `tech-stack` (YAML) is non-empty: one bullet per item with a placeholder justification derived from its name (existing/required stack)
- If `## Desired tech` is non-blank: add a **Desired / experimental** subsection listing those technologies with the author's reasoning
- If both are empty: placeholder rows

**Effort Estimations:**

- If `milestones` is non-empty: one table row per milestone with placeholder effort estimate
- If empty: two placeholder rows
- Recommended delivery order follows the milestone list order

**FAQs:**

- Generate 3–5 Q&A pairs anticipating likely reviewer questions from the problem and scope
- Always include a Terminology entry if acronyms appear in the RFC

**Risks & Mitigations:**

- If `## Known risks / concerns` is non-blank: use those as the first rows of the table; add likelihood and mitigation for each
- Supplement with additional risks inferred from the problem and scope (omit if the author's list is already comprehensive)
- Include the "Recommended First Step" callout identifying the highest-risk unknown

**Remove all template comment blocks** (`<!-- ... -->`).

**Do not hallucinate details** — use `{Description}` placeholders for anything not provided.

### Step 6 — Write the file

Write to the output path from Step 4. Create the directory if needed.

Then report:

- Output file path
- Which sections were fully populated vs. left as placeholders
- Any assumptions made during generation
