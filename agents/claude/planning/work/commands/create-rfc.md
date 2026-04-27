# Create RFC

Generate a new RFC document from the project template, pre-filled with the provided inputs.

## Usage

```text
/create-rfc --title <title> --team <team> --author <name> --jira-epic <id> --problem <statement> [options]
```

**Arguments:** $ARGUMENTS

### Required parameters

| Parameter | Description | Example |
| :-------- | :---------- | :------ |
| `--title` | Short descriptive title of the RFC (no team prefix) | `"Online Catalog Dataset Pipeline"` |
| `--team` | Owning team name | `"Menu Intelligence"` |
| `--author` | Author full name and email | `"Simone Porreca <simone.porreca@deliveryhero.com>"` |
| `--jira-epic` | JIRA epic ID — used to derive the output path | `"VDATA-9356"` |
| `--problem` | 1–3 sentence description of the problem being solved — the motivation | `"There is no standardised way to evaluate translation quality. Model changes are deployed without evidence of improvement."` |

### Optional parameters

| Parameter | Default | Description | Example |
| :-------- | :------ | :---------- | :------ |
| `--org` | _(blank)_ | Organisation name | `"Vendor Sales and Operations"` |
| `--deadline` | 2 weeks from today | Review deadline date (YYYY-MM-DD) | `"2026-05-15"` |
| `--reviewers` | _(none)_ | Comma-separated list of reviewers in the format `"Name <email> [required\|optional]"` | `"Aishwarya Kadlag <a.kadlag@dh.com> required, Damir Valput <d.valput@dh.com> optional"` |
| `--scope-in` | _(none)_ | Comma-separated list of in-scope capabilities | `"Reference corpus construction, COMET-DA scoring pipeline"` |
| `--scope-out` | _(none)_ | Comma-separated list of out-of-scope items with reasons (format: `"item: reason"`) | `"Online monitoring: deferred to future phase, Human annotation: not scalable"` |
| `--tech-stack` | _(none)_ | Comma-separated list of libraries/services to include | `"BigQuery, GitHub Actions, unbabel-comet, LiteLLM"` |
| `--milestones` | _(none)_ | Comma-separated list of milestone names | `"Reference corpus pipeline, Offline scoring, Statistical comparison"` |
| `--out` | `docs/rfc/<jira-epic-slug>/rfc_document.md` | Override the output file path | `"docs/rfc/my_rfc/rfc_document.md"` |

---

## Example

```text
/create-rfc \
  --title "Online Catalog Dataset Pipeline" \
  --team "Menu Intelligence" \
  --author "Simone Porreca <simone.porreca@deliveryhero.com>" \
  --jira-epic "VDATA-9356" \
  --org "Vendor Sales and Operations" \
  --problem "The online catalog has no automated dataset pipeline. Catalog changes are tracked manually, making model evaluation against real-world catalog state impossible." \
  --deadline "2026-05-15" \
  --reviewers "Aishwarya Kadlag <aishwarya.kadlag@deliveryhero.com> required, Vítor Plentz <vitor.plentz@deliveryhero.com> required, Damir Valput <damir.valput@deliveryhero.com> optional" \
  --scope-in "BigQuery extraction pipeline, category stratification, GitHub Actions workflow" \
  --scope-out "Real-time monitoring: deferred to future phase, Model training: out of scope for this RFC" \
  --tech-stack "BigQuery, GitHub Actions, pandas, uv" \
  --milestones "Dataset extraction pipeline, Validation and reporting, CI integration"
```

---

## Instructions

You are generating a new RFC document. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- `--title` (required): short RFC title
- `--team` (required): owning team name
- `--author` (required): author name and email string
- `--jira-epic` (required): JIRA epic ID (e.g. `VDATA-9356`)
- `--problem` (required): problem statement string
- `--org` (optional): organisation name; leave blank if not provided
- `--deadline` (optional): review deadline as YYYY-MM-DD; if absent, default to 14 days from today's date
- `--reviewers` (optional): parse into a list of `{name, email, required|optional}` entries; if absent, leave placeholder rows
- `--scope-in` (optional): split on commas → list of in-scope items
- `--scope-out` (optional): split on commas → list of out-of-scope items; each item may have a `"item: reason"` format — split on the first colon
- `--tech-stack` (optional): split on commas → list of library/service names
- `--milestones` (optional): split on commas → ordered list of milestone names
- `--out` (optional): override the output file path

### Step 2 — Read the template

Read `docs/rfc/rfc_tempalte.md` — this is the canonical structure the RFC must follow.

Also read the existing RFC `docs/rfc/translations_evaluation_framework/rfc_document.md` as a style reference for tone, table formatting, and section depth.

### Step 3 — Determine the output path

If `--out` was provided, use it directly.

Otherwise, derive the path as:
```
docs/rfc/<jira-epic-lowercase>_<title-slug>/rfc_document.md
```
where `<title-slug>` is the title lowercased with spaces replaced by underscores (e.g. `vdata-9356_online_catalog_dataset_pipeline/rfc_document.md`).

If the directory does not exist, it will be created when writing.

### Step 4 — Generate the RFC

Produce a complete RFC document following the template structure. Apply these rules:

**Header block:**
- Set `Author(s)` from `--author`
- Set `Owner(s)` from `--team`
- Set `Org(s)` from `--org` (blank if not provided)
- Set `RFC status` to `Draft`
- Set `Review deadline` from `--deadline`
- Set today's date in the Timeline table

**Reviews table:**
- If `--reviewers` was provided, populate one row per reviewer with name, team inferred from email domain context, and Required/Optional status
- If not provided, keep the two placeholder rows from the template

**Title:**
- Format as `[RFC] {Team}: {Title}` — derive both from `--team` and `--title`

**Motivation section:**
- Expand `--problem` into 2–3 paragraphs following the template's four-point structure:
  1. What system or process is being changed
  2. The specific gap or pain point
  3. What happens without this RFC
  4. The primary requirement the proposal must satisfy
- Do not invent facts. Work only from what `--problem` states.

**Objectives section:**
- Derive 3–5 concrete objectives from the problem statement and scope items
- Each must start with a bold action label and be outcome-oriented, not task-oriented

**Scope:**
- In-Scope: populate from `--scope-in` if provided; otherwise leave placeholders with a comment
- Out-of-Scope: populate from `--scope-out` if provided; otherwise leave placeholders

**Main technical section:**
- Name it after `--title` (e.g. `# Online Catalog Dataset Pipeline`)
- Write a Methodology Overview paragraph describing the high-level approach derived from the problem and scope
- If `--milestones` was provided, generate one subsection per milestone with a placeholder description and comment block
- If not provided, keep the two generic subsection placeholders

**Tech Stack:**
- If `--tech-stack` was provided, list each item with a placeholder "why it is used" description derived from its name
- If not provided, keep the placeholder rows

**Effort Estimations:**
- If `--milestones` was provided, generate one table row per milestone with a placeholder effort estimate
- If not provided, keep the two placeholder rows
- Recommended delivery order should follow the milestone list order

**FAQs:**
- Generate 3–5 Q&A pairs anticipating the most likely reviewer questions based on the problem statement and scope
- Always include a Terminology entry if acronyms appear in the RFC

**Risks & Mitigations:**
- Generate 3–4 risks inferred from the problem and scope, with likelihood and mitigation
- Include the "Recommended First Step" callout identifying the highest-risk unknown

**Remove all template comment blocks** (`<!-- ... -->`) from the output — they are authoring instructions, not document content.

**Do not hallucinate details** — for sections where no input was provided, use clear placeholder text (e.g. `{Description}`) rather than invented content.

### Step 5 — Write the file

Write the generated RFC to the output path from Step 3.

Then report:
- The output file path
- Which sections were fully populated vs. left as placeholders (based on which optional parameters were provided)
- Any assumptions made during generation
