# Fill Proposal

Fill in the missing fields of an RFC proposal file. Uses only the README files
listed in `context-paths` and the JIRA epic linked in `jira-epic` as sources.
Existing values are never overwritten.

## Usage

```text
/0-work-fill-proposal --file <path-to-proposal>
```

**Arguments:** $ARGUMENTS

### Parameters

| Parameter | Required | Description                       | Example                                                           |
| :-------- | :------- | :-------------------------------- | :---------------------------------------------------------------- |
| `--file`  | Yes      | Path to the proposal file to fill | `docs/vdata-9356_online_catalog_dataset_pipeline/proposal.md` |

---

## Instructions

You are filling in a partially-completed RFC proposal file. You must use **only**
the sources listed inside the file itself. You must not read any other file in the
repository.

### Step 1 — Parse arguments

Parse `$ARGUMENTS`:

- `--file` (required): path to the proposal file to fill

### Step 2 — Read the proposal file

Read the file at the path from `--file`. Extract:

- **YAML frontmatter** (between `---` delimiters): for every key, note whether its
  value is already filled or blank/placeholder.
- **Markdown sections**: each section after the frontmatter is delimited by a
  `## Heading` and contains a `<!-- ... -->` comment block that describes what
  belongs there. Treat a section as *empty* if it contains only the comment block
  (no prose below it).

### Step 3 — Load external sources

You are allowed to read **only** the following two source types. Do not read or
reference any other file or URL.

**A. README files from `context-paths`**

If `context-paths` in the frontmatter contains at least one non-blank entry:

- Each path is relative to the directory from which you were invoked (the project root).
- Read each listed file.
- Extract: module purpose, key components, public interfaces, external dependencies,
  and any stated constraints or invariants.

If `context-paths` is empty or absent, skip this step.

**B. JIRA epic from `jira-epic`**

If `jira-epic` in the frontmatter is a non-blank value (e.g. `VDATA-9356`):

- Attempt to fetch the JIRA epic page using the organization's JIRA instance URL.
  If the URL is not known, ask the user for the full JIRA epic URL before proceeding.
- Extract: epic goal, motivation, background, acceptance criteria, and any decisions
  already recorded.
- If fetching fails (e.g. authentication required), note the limitation and proceed
  using only the README context from Step 3A.

If `jira-epic` is blank, skip this step.

### Step 4 — Fill missing YAML keys

For each YAML key whose value is blank or a placeholder (e.g. `""`):

- `title`: derive a short descriptive title from the JIRA epic or README context.
- `team`: derive the owning team name from the JIRA epic or README context;
  otherwise leave blank.
- `author`: do not fill — leave blank for the author to complete.
- `jira-epic`: leave as-is (it was the source; if blank it stays blank).
- `org`: infer from the JIRA epic if clearly stated; otherwise leave blank.
- `deadline`: leave blank if no date can be inferred — do not default.
- `reviewers`: leave blank — this is for the author to decide.
- `tech-stack`: list technologies clearly referenced in the README files or JIRA epic;
  omit anything not mentioned.
- `scope-in`: list capabilities explicitly described as in-scope in the sources.
- `scope-out`: list items explicitly described as out-of-scope; format each as
  `"Item: reason"` using the reason from the source.
- `milestones`: list milestone names in order if the sources describe a phased delivery;
  otherwise leave blank.
- `context-paths`: do not modify — this field is already set by the author.

**Do not change any key that already has a non-blank, non-placeholder value.**

### Step 5 — Fill empty markdown sections

For each section that is empty (contains only a `<!-- ... -->` comment block and no prose):

- Remove the comment block.
- Write new prose below the heading. Keep it **high-level** — no implementation detail,
  no code, no specific API names unless they appear verbatim in the sources.
- Draw primarily from the sources loaded in Step 3. Where the sources are thin or
  ambiguous, use reasonable inference and good judgment to produce a useful draft.
- If you cannot produce even a reasonable draft for a section, ask the user a single
  focused question for that section before writing — do not ask more than one question
  per section, and group all questions together before writing anything to disk.
- After any clarifications are answered (or if none were needed), write all sections
  in one pass.

The sections in the proposal are:

- `## Problem` (required): one concise paragraph describing the technical gap or pain
  point. Cover what system or process is affected and what happens without this RFC.
  Focus on *why* something needs to change, not *how*.
- `## Approach direction` (optional): 1–3 sentences on the preferred high-level direction
  if the sources suggest one; omit the section body if no direction can be inferred.
- `## Success criteria` (optional): a short bullet list of measurable, user-visible
  outcomes. Stay outcome-oriented, not implementation-oriented.
- `## Constraints` (optional): a bullet list of hard requirements (SLA targets, banned
  technologies, compliance rules, infra limitations). Only include items the sources
  explicitly treat as non-negotiable.
- `## Desired tech` (optional): a brief list of technologies the sources favour, with
  a one-line reason for each. Omit if no preference is expressed.
- `## Integration context` (optional): 1–2 sentences on how the solution fits into the
  existing system, based on module boundaries visible in the README files.
- `## Known risks / concerns` (optional): a short bullet list of uncertainties, technical
  unknowns, or stakeholder concerns raised in the sources, or reasonably inferred from
  the scope.

### Step 6 — Write the updated file

Overwrite the file at `--file` with the updated content. Preserve:

- The exact frontmatter delimiters (`---`).
- All headings and their order.
- Any prose that was already present before you ran this command.

Then report:

- Which YAML keys were filled vs. left unchanged.
- Which markdown sections were filled vs. left as placeholders.
- Which sources were used (context-paths files loaded, whether JIRA epic was fetched).
- Any assumptions made.
