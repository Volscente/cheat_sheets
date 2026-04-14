# Planning Guidelines

A three-tier planning workflow for developing coding features and implementations.
Each tier owns distinct content — no content is duplicated across tiers.

```text
Notion (WHY + WHAT)
  └── GitHub Issues (WHICH task + tracking)
        └── specs/ (HOW it gets built)
```

---

## Tier 1: Notion (Strategy)

Notion is the single source of truth for business context. All rationale, background, and
high-level scope live here and are referenced downward — never copied.

### Main Feature Page

One page per feature or major initiative.

| Section             | Content                                              |
| ------------------- | ---------------------------------------------------- |
| **Scope**           | What is and is not included in this feature          |
| **Rationale**       | Why this feature, what problem it solves             |
| **Background**      | Prior work, constraints, decisions that led here     |
| **Deliverables**    | Measurable outcomes that define success              |
| **Sprint Overview** | Table: sprint number, goal, status, link to sub-page |

### Sprint Sub-Pages

One sub-page per sprint. Sprint pages are about execution — they do not repeat the feature's
Scope/Rationale/Background, which already live on the main page.

| Section                | Content                                             |
| ---------------------- | --------------------------------------------------- |
| **Sprint Goal**        | One sentence: what this sprint achieves             |
| **GitHub Issues**      | Table with issue number, title, assignee, status    |
| **Dependencies**       | Other sprints or external work this sprint waits on |
| **Definition of Done** | Conditions that close this sprint                   |

---

## Tier 2: GitHub Issues (Tracking)

GitHub Issues are the tactical layer. They do not re-state business context from Notion —
instead they link to it and focus on what needs to be done and how to verify it.

### Issue Structure

```markdown
Title: [Sprint N] Brief description of the task

## Notion Sprint

<URL to the Notion sprint sub-page>

## Scope

What this specific issue covers (narrow, concrete — not the feature scope).

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] ...

## Notes

Pointers to the spec file, known constraints, or implementation hints.

## Checklist

- [ ] Spec file updated (`specs/planning/gh-{number}-{title}.md`)
- [ ] Tests written
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] README.md updated (if applicable)
- [ ] Project version bumped (if applicable)
```

### Linking to Notion

Notion page URLs contain a UUID suffix that remains stable even if the page is renamed:
`https://www.notion.so/workspace/Page-Name-<uuid>`

Use that URL directly in the issue body. Optionally, add a **Notion URL** custom field
in GitHub Projects for filtering and dashboards.

The mapping is: one Notion sprint sub-page → one or more GitHub Issues.
Each issue links back to its Notion sprint page; the sprint page lists all its issues.

### What Does Not Belong in a GitHub Issue

- Scope/Rationale/Background — those are in Notion; link, don't copy.
- Changelog (Added/Changed) — issues describe intent. Changelogs describe outcomes.
  Record actual changes in the PR description and in `CHANGELOG.md`.

---

## Tier 3: Repository Specs (Technical)

Specs are pure technical documents for engineers. No business rationale. The spec answers
_how_ something gets built; Notion answers _why_.

### Folder Structure

```text
specs/
└── planning/
    ├── gh-42-add-user-auth.md
    ├── gh-43-token-refresh-flow.md
    └── ...
```

> **Why `specs/` and not `docs/`?** `docs/` is the default source directory for MkDocs
> and conflicts with other documentation tooling. `specs/` is unambiguous.

### File Naming Convention

```text
gh-{issue-number}-{kebab-case-title}.md
```

Examples: `gh-42-add-user-auth.md`, `gh-107-migrate-db-schema.md`

The issue number makes the link to GitHub explicit and searchable.

### Spec File Structure

````markdown
# gh-{number}: {Title}

**GitHub Issue:** #{number}
**Notion Sprint:** <URL>

---

## Technical Scope

Which files, modules, and interfaces change. What is explicitly out of scope.

## Architecture

Component diagram, data flow, or sequence diagram (ASCII or linked image).
Describe how the new code integrates with existing components.

## Tech Stack

New packages or dependencies introduced:

| Package        | Version | Justification                        |
| -------------- | ------- | ------------------------------------ |
| `package-name` | `>=x.y` | Why this package, not an alternative |

## Implementation Details

### Modules / Files

| File                   | Action | Description         |
| ---------------------- | ------ | ------------------- |
| `src/module/file.py`   | Create | What this file does |
| `src/existing/file.py` | Modify | What changes        |

### Key Functions

```python
def function_name(param: Type, param2: Type) -> ReturnType:
    """
    Brief description.

    Args:
        param: Description.
        param2: Description.

    Returns:
        Description.

    Raises:
        ErrorType: When.
    """
    ...
```
````

### Data Models / Schemas

Pydantic models, dataclasses, or DB schema changes with field descriptions.

## Testing Strategy

- Unit tests: what to mock, what to test directly
- Integration tests: which boundaries to test end-to-end
- Edge cases: explicit list of non-obvious scenarios to cover

## Open Questions / Risks

- [ ] Question or risk description — owner, target resolution date

```text

---

## Cross-Tier Reference Map

```

┌─────────────────────────────────────────────┐
│ NOTION │
│ Feature Main Page │
│ Scope · Rationale · Background │
│ Deliverables · Sprint Overview │
│ │ │
│ Sprint Sub-Page (per sprint) │
│ Goal · Issue Table · Dependencies · DoD │
└──────────────────┬──────────────────────────┘
│ URL reference
▼
┌─────────────────────────────────────────────┐
│ GITHUB ISSUES │
│ Scope (narrow) · Acceptance Criteria │
│ Notes · Checklist │
│ [links back to Notion sprint] │
└──────────────────┬──────────────────────────┘
│ issue number in filename
▼
┌─────────────────────────────────────────────┐
│ specs/planning/gh-{N}-{title}.md │
│ Technical Scope · Architecture │
│ Tech Stack · Implementation Details │
│ Testing Strategy · Open Questions │
│ [links back to GitHub issue + Notion] │
└─────────────────────────────────────────────┘

```

Each tier links to the tier above it for context. Content flows down; references flow up.
```
