# Fill Proposal

Fill in the missing fields of an RFC proposal file. Uses only the README files
listed in `context-paths` and the Notion page linked in `notion-page` as sources.
Existing values are never overwritten.

## Usage

```text
/0-personal-fill-proposal --file <path-to-proposal>
```

**Arguments:** $ARGUMENTS

### Parameters

| Parameter | Required | Description                    | Example                                             |
| :-------- | :------- | :----------------------------- | :-------------------------------------------------- |
| `--file`  | Yes      | Path to the proposal file to fill | `.claude/recipe-app_add-search-bar/proposal.md` |

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

**B. Notion page from `notion-page`**

If `notion-page` in the frontmatter is a non-blank URL:

- Fetch the page content.
- Extract: initiative goals, motivation, background, and any decisions already recorded.

If `notion-page` is blank, skip this step.

### Step 4 — Fill missing YAML keys

For each YAML key whose value is blank or a placeholder (e.g. `""`):

- `title`: derive a short descriptive title from the Notion page or README context.
- `project`: derive the project name from the Notion page or README context.
- `deadline`: leave blank if no date can be inferred — do not default.
- `notion-page`: leave as-is (it was the source; if blank it stays blank).
- `github-repo`: infer from README context if clearly stated; otherwise leave blank.
- `milestone`: infer from Notion or README if mentioned; otherwise leave blank.
- `tech-stack`: list technologies clearly referenced in the README files or Notion page;
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
- Write new prose below the heading, using only information drawn from the sources
  loaded in Step 3.
- Write in the same style as the comment described — concise, technical, first-person
  where natural.
- If the sources contain no relevant information for a section, write
  `{No information available from provided sources.}` as the sole content.

The sections in the proposal are:

- `## Problem` (required): describe the technical gap or pain point from the sources.
- `## Approach direction` (optional): summarise any preferred approach or architecture
  already described in the sources; leave the placeholder text if no direction is stated.
- `## Success criteria` (optional): list measurable outcomes mentioned in the sources.
- `## Constraints` (optional): list hard requirements explicitly stated in the sources.
- `## Desired tech` (optional): list technologies the sources express a preference for,
  with the stated reasoning.
- `## Integration context` (optional): describe how the solution should integrate with
  the existing system, based on the README module boundaries.
- `## Known risks / concerns` (optional): capture doubts or uncertainties raised in the
  sources.

**Do not invent information.** If a section cannot be filled from the sources, use the
placeholder text above.

### Step 6 — Write the updated file

Overwrite the file at `--file` with the updated content. Preserve:

- The exact frontmatter delimiters (`---`).
- All headings and their order.
- Any prose that was already present before you ran this command.

Then report:

- Which YAML keys were filled vs. left unchanged.
- Which markdown sections were filled vs. left as placeholders.
- Which sources were used (context-paths files loaded, whether Notion page was fetched).
- Any assumptions made.
