# Planning Guidelines

## Technical Specs

Specs are pure technical documents for engineers. No business rationale. The spec answers
_how_ something gets built; JIRA answers _why_.

### Folder Structure

Below an example of the folder structure where:

- `vdata-8417_mds_translation_evaluation`: the JIRA Epic
- `vdata-8860_implement-comet-da`: the JIRA task

```text
docs/
└── planning/
    ├── vdata-8417_mds_translation_evaluation/
    │   ├── vdata-8860_implement-comet-da.md
    │   └── ...
    └── ...
```

### File Naming Convention

```text
docs/planning/{JIRA_epic}/{jira_ticket}/{kebab-case-title}.md
```

Examples: `docs/planning/VDATA/VDATA-8860/implement-comet-da.md`

The JIRA ticket folder makes the link to the ticket explicit and searchable.

### Spec File Structure

````markdown
# {JIRA-ticket}: {Title}

**JIRA Ticket:** <URL>
**JIRA Epic:** <URL>

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

### Testing Strategy

- Unit tests: what to mock, what to test directly
- Integration tests: which boundaries to test end-to-end
- Edge cases: explicit list of non-obvious scenarios to cover

### Open Questions / Risks

- [ ] Question or risk description — owner, target resolution date

---
