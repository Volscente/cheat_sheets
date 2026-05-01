# Planning Guidelines

## Two documents, two readers

| Document | Reader | Purpose |
| -------- | ------ | ------- |
| **Notion initiative page** | You | What you're building and why — personal context, outcomes, status at a glance |
| **RFC** (`.claude/rfc/`) | Claude | How it will be built — technical design, scope, risks, milestones |
| **Initiative plan** (`.claude/planning/`) | Claude | Task breakdown, dependency order, deliverables — drives `plan-task` and `execute-plan` |
| **Tech spec** (`.claude/planning/`) | Claude | Per-issue implementation contract — functions, schemas, tests |

## Notion structure

```
Goals table (one row per project)
└── Project page
    └── Initiative sub-page  ←→  GitHub Milestone
        ├── What (1–2 sentences, plain language)
        ├── Why (personal motivation)
        ├── Success looks like (outcomes, not implementation)
        ├── RFC link (if created)
        └── GitHub Issues list
```

**Initiative page** (what to put in Notion):
- **What**: 1–2 sentences describing the feature/system in plain terms
- **Why**: Personal motivation — why this matters to you right now
- **Success looks like**: Outcome-oriented bullets (what changes when this is done)
- **RFC link**: Link to the RFC document in the repo (if one was created)
- **GitHub Milestone**: Link to the milestone
- **GitHub Issues**: Links to individual issues

## Tech Spec

Specs are pure technical documents for Claude. No personal motivation — that lives in Notion. The spec answers _how_ something gets built.

### Folder Structure

```text
.claude/
└── planning/
    └── <project-slug>/
        ├── planning.md                        ← initiative-level plan
        ├── <issue-number>-<kebab-title>.md    ← spec per GitHub Issue
        └── ...
```

Example:

```text
.claude/
└── planning/
    └── recipe-app/
        ├── planning.md
        ├── 12-implement-search-index.md
        ├── 13-build-search-ui.md
        └── 14-add-keyboard-shortcuts.md
```

### File Naming Convention

- **Initiative plan:** `.claude/planning/<project-slug>/planning.md`
- **Tech spec:** `.claude/planning/<project-slug>/<issue-number>-<kebab-title>.md`

`<project-slug>` is the GitHub repo name or a short descriptive slug.

### Spec File Structure

````markdown
# #{issue-number}: {Title}

**GitHub Issue:** <URL>
**GitHub Milestone:** <URL>
**Notion page:** <URL>

---

## Technical Scope

Which files, modules, and interfaces change. What is explicitly out of scope.

## Architecture

ASCII diagram. Describe how the new code integrates with existing components.

## Tech Stack

New packages or dependencies introduced:

| Package        | Version | Justification |
| -------------- | ------- | ------------- |
| `package-name` | `>=x.y` | Why this, not an alternative |

## Implementation Details

### Modules / Files

| File                   | Action | Description         |
| ---------------------- | ------ | ------------------- |
| `src/module/file.py`   | Create | What this file does |
| `src/existing/file.py` | Modify | What changes        |

### Key Functions

```python
def function_name(param: Type) -> ReturnType:
    """
    Brief description.

    Args:
        param: Description.

    Returns:
        Description.

    Raises:
        ErrorType: When.
    """
```

### Data Models / Schemas

Pydantic models, dataclasses, or database schema with field descriptions.

### Testing Strategy

- Unit tests: what to mock, what to test directly
- Integration tests: which boundaries to test end-to-end
- Edge cases: explicit list

### Open Questions / Risks

- [ ] Question or risk — target resolution date

---
````
