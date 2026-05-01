# #{issue-number}: {Title}

**GitHub Issue:** [{issue-number} — {Title}]({GITHUB_ISSUE_URL})
**GitHub Milestone:** [{Milestone Name}]({GITHUB_MILESTONE_URL})
**Notion page:** [{Initiative Name}]({NOTION_URL})

---

## Technical Scope

**In scope:**

- `{path/to/file.py}` — {What this file does}
- `{path/to/schema.py}` — {What this file does}

**Out of scope:**

- {Out-of-scope item 1}
- {Out-of-scope item 2}

---

## Architecture

```txt
CLI: python -m {module.path}
          │  --{arg-1} <value>  --{arg-2} <value>  [--{flag}]
          │
          ▼
    {entry_function}({dependencies})
    ┌──────────────────────────────────────────────┐
    │  {Describe data source or upstream system}   │
    └──────────────────────────────────────────────┘
          │  → {output type}
          │
          ▼
    {core_function}({inputs})
          │
          ├── {function_a}({args}) → {output}     ── STEP 1
          │
          └── {function_b}({args}) → {output}     ── STEP 2
                    │
                    ▼
          {result_function}({inputs}) → {output type}
```

### {Why a notable design decision was made}

{Explain the decision and the tradeoffs considered.}

---

## Tech Stack

{No new packages required. / New packages introduced:}

| Package       | Version | Justification                          |
| ------------- | ------- | -------------------------------------- |
| `{package-1}` | `>=x.y` | {Why this package, not an alternative} |

---

## Implementation Details

### Modules / Files

| File                   | Action | Description                              |
| ---------------------- | ------ | ---------------------------------------- |
| `{path/to/runner.py}`  | Create | {CLI runner: what it orchestrates}       |
| `{path/to/schemas.py}` | Create | {Data models for structured output}      |
| `{path/to/utils.py}`   | Reuse  | {Functions reused — do not re-implement} |

---

### Key Functions

```python
def {load_function}(
    {param}: {Type},
    {param2}: {Type},
) -> {ReturnType}:
    """{One-line summary.}

    {Describe what it loads, how it filters/transforms, and what shape it returns.}

    Args:
        {param}: {Description.}
        {param2}: {Description.}

    Returns:
        {Description of the return value.}

    Raises:
        {ErrorType}: {When this error is raised.}
    """
```

```python
def {core_function}(
    {input}: {Type},
    {param}: {Type},
) -> {ResultType}:
    """{One-line summary.}

    {Describe what input is received, what processing happens, and what is returned.}

    Args:
        {input}: {Description.}
        {param}: {Description.}

    Returns:
        {Description of the return value.}

    Raises:
        {ErrorType}: {When this error is raised.}
    """
```

---

### CLI Parameters

| Parameter     | Type   | Default           | Description                    |
| ------------- | ------ | ----------------- | ------------------------------ |
| `--{param-1}` | `str`  | required          | {What this parameter controls} |
| `--{param-2}` | `int`  | `{default_value}` | {What this parameter controls} |
| `--{flag-1}`  | `flag` | `False`           | {What enabling this flag does} |

---

### Data Models / Schemas

```python
class {InputModel}(BaseModel):
    {field_1}: {type} = Field(description="{Description}")
    {field_2}: {type} = Field(description="{Description}")
    {field_3}: {type} | None = Field(default=None, description="{Description}")


class {OutputModel}(BaseModel):
    {result_field}: list[{ItemType}] = Field(description="{Description}")
    {meta_field}: str = Field(description="{Description}")
```

---

### Testing Strategy

**Unit tests** (`tests/{module}/test_{file}.py`):

- Mock `{ExternalService}` — verify {what each call receives}
- Test Pydantic validation: {missing fields, edge values, null optionals}
- Test edge case: `{field} = {edge_value}` → {expected behaviour}

**Integration test** (manual):

```bash
python -m {module.path} \
    --{param-1} <test-value> \
    --dry-run
```

Verify: {what a passing integration test looks like}.

**Edge cases:**

- {Edge case 1} → {expected handling}
- {Edge case 2} → {expected handling}

---

### Open Questions / Risks

- [ ] **{Risk or question}:** {Description.} **Target:** {date or milestone}
- [ ] **{Risk or question}:** {Description.} **Target:** {date or milestone}
