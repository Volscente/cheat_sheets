# Planning Guidelines

## Tech Specs

Specs are pure technical documents. No motivation or business rationale — those live in the RFC and in the GitHub Issue description. The spec answers _how_ something gets built.

### Folder Structure

```text
docs/
└── planning/
    └── <project-slug>/
        ├── planning.md         ← initiative-level plan
        ├── <issue-number>-<kebab-title>.md   ← spec per GitHub Issue
        └── ...
```

Example:

```text
docs/
└── planning/
    └── my-cli-tool/
        ├── planning.md
        ├── 12-add-config-parser.md
        └── 18-add-output-formatter.md
```

### File Naming Convention

- **Initiative plan:** `docs/planning/<project-slug>/planning.md`
- **Tech spec:** `docs/planning/<project-slug>/<issue-number>-<kebab-title>.md`

`<project-slug>` is the GitHub repo name or a short descriptive slug for the project.

### Spec File Structure

````markdown
# #{issue-number}: {Title}

**GitHub Issue:** <URL>
**GitHub Milestone:** <URL> _(optional)_
**Notion Page:** <URL> _(optional)_

---

## Technical Scope

Which files, modules, and interfaces change. What is explicitly out of scope.

## Architecture

Component diagram, data flow, or sequence diagram (ASCII).
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

### Data Models / Schemas

Pydantic models, dataclasses, or database schema with field descriptions.

### Testing Strategy

- Unit tests: what to mock, what to test directly
- Integration tests: which boundaries to test end-to-end
- Edge cases: explicit list of non-obvious scenarios to cover

### Open Questions / Risks

- [ ] Question or risk description — target resolution date

---
````
