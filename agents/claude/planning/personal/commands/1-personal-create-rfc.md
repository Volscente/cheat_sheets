# Create RFC

Generate a new RFC document from a filled proposal file. The proposal supplies the
problem, constraints, and preferences; Claude designs the solution and writes the RFC.

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
   Optionally list module README.md paths in `context-paths` to give Claude design context.
3. Run `/1-personal-create-rfc --file .claude/rfc/<initiative-name>/proposal.md`.

---

## Example

```text
/1-personal-create-rfc --file .claude/rfc/recipe-app_add-search-bar/proposal.md
```

---

## Instructions

You are designing and writing a new RFC document. The proposal is your input — it defines
the problem, constraints, and preferences. The actual solution design is your responsibility.
Follow these steps exactly.

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
  - `context-paths` (optional list — paths to module README.md files relative to the project root)
- **Markdown sections** (each is optional — treat as absent if blank or missing):
  - `## Problem`: the problem statement (required)
  - `## Approach direction`: author's preferred high-level approach; treat as a solution proposal, not the answer. You can challenge it.
  - `## Success criteria`: measurable outcomes the author has in mind
  - `## Constraints`: hard non-negotiable requirements
  - `## Desired tech`: new technologies the author wants to use, with reasoning
  - `## Integration context`: how the solution should integrate with the existing system
  - `## Known risks / concerns`: doubts or uncertainties the author already identified

### Step 3 — Load repository context

If `context-paths` is non-empty and contains at least one non-blank entry:

- Read each listed file (paths are relative to the directory from which you were invoked,
  i.e. the project root)
- For each file, extract: module purpose, key components, public interfaces, external
  dependencies, and any stated constraints or invariants
- Build an internal context summary of the existing system: which modules exist, what
  they own, and where the boundaries lie

If `context-paths` is empty or absent, continue to Step 4 and note the absence in the
final report.

### Step 4 — Read the RFC template

Read `~/.claude/templates/personal_rfc_template.md` — this is the canonical output structure.

### Step 5 — Determine the output path

If `--out` was provided, use it directly.

Otherwise: same directory as `--file`, filename `rfc_document.md`.

### Step 6 — Design the solution

Before writing the RFC, reason through the design. This step drives all technical content
in the RFC.

Using the problem statement, scope, constraints, and repository context from Steps 2–3:

1. **Identify the system boundary**: which existing modules (from context-paths READMEs)
   are affected, extended, or left untouched by this initiative
2. **Propose a concrete technical approach**: architecture, data flow, key interfaces
   - If `## Approach direction` is non-blank: treat it as the author's preferred direction
     and a starting constraint. Either adopt it with justification, or explain concisely
     why a different direction better serves the objectives
   - If blank: derive the approach independently from the problem, scope, and context
3. **Identify integration points**: how the new work connects to existing modules,
   using the context summary from Step 3; supplement with any `## Integration context` notes
4. **Derive objectives**: 3–5 concrete, verifiable outcomes that this design achieves;
   use `## Success criteria` from the proposal to refine or constrain them if present
5. **Identify genuine risks**: 2–4 design-specific risks (not just abstract concerns);
   use `## Known risks / concerns` from the proposal as additional input

This designed solution — not the proposal — drives the RFC content in Step 7.

### Step 7 — Generate the RFC

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

- Derived from the Step 6 design; `## Success criteria` refines or constrains them
- Each starts with a bold action label and is outcome-oriented
- 3–5 objectives total

**Scope:**

- In-Scope: from `scope-in` if non-empty
- Out-of-Scope: from `scope-out` if non-empty; each item uses the `"Item: reason"` split on the first colon
- If `## Constraints` is non-blank: add a **Constraints** paragraph after Out-of-Scope listing all non-negotiable requirements

**Main technical section:**

- Named after `title`
- Approach Overview:
  - Present the approach designed in Step 6 (1–2 paragraphs of concrete high-level design)
  - If `## Approach direction` was non-blank: briefly note the author's stated direction and
    explain how the designed approach relates to it (adopted, challenged, rejected, extended, or refined). It is important that, if the approach direction does not makes sense, propose an alternative.
  - If blank: present the approach without reference to a stated preference
  - Integration subsection: describe how the solution connects to existing modules using the
    Step 6 integration analysis and any `## Integration context` notes from the proposal;
    omit this subsection entirely if Step 3 produced no context and the proposal's
    `## Integration context` is also blank
- If `milestones` is non-empty: one subsection per milestone with placeholder description
- If empty: two generic placeholder subsections

**Tech Stack:**

- If `tech-stack` (YAML) is non-empty: one bullet per item with justification derived from
  the Step 6 design and existing module context (not just from the item name)
- If `## Desired tech` is non-blank: add a **Desired / experimental** subsection listing
  those technologies with the author's reasoning
- If both are empty: placeholder rows

**Effort Estimations:**

- If `milestones` is non-empty: one table row per milestone with placeholder effort and a `#{issue}` placeholder for the GitHub Issue number
- If empty: placeholder rows

**FAQs:**

- Generate 3–5 Q&A pairs derived from the Step 6 design — anticipate questions a reviewer
  would ask about the concrete approach, not just the general problem
- Always include a Terminology entry if acronyms appear

**Risks & Open Questions:**

- Step 6 design risks come first; add likelihood and mitigation for each
- `## Known risks / concerns` from the proposal supplement and are merged/deduplicated
- Add 1–2 additional inferred risks only if the combined list is fewer than 3 entries

**Remove all template comment blocks** (`<!-- ... -->`).

**Do not hallucinate details** — use `{Description}` placeholders for anything not provided.

### Step 8 — Write the file

Write to the output path from Step 5. Create the directory if needed.

Then report:

- Output file path
- Which `context-paths` files were loaded (or note if none were provided)
- Which sections were fully populated vs. left as placeholders
- Where (if at all) the designed approach diverged from the proposal's `## Approach direction`, and why
- Any assumptions made (e.g., deadline defaulted)
