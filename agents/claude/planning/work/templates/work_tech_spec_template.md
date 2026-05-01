# {JIRA-TICKET}: {Title}

**JIRA Ticket:** [{JIRA-TICKET}]({JIRA_TICKET_URL})
**JIRA Epic:** [{JIRA-EPIC} — {Epic Name}]({JIRA_EPIC_URL})

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

```
CLI: uv run python -m {module.path}
          │  --{arg-1} <value>  --{arg-2} <value>  [--{flag}]
          │
          ▼
    {entry_function}({dependencies})
    ┌──────────────────────────────────────────────┐
    │  {Describe data source or upstream system}   │
    └──────────────────────────────────────────────┘
          │  → {output type}
          │
          ▼  {Concurrency model, e.g. ThreadPoolExecutor(max_workers)}
    {core_function}({inputs})
          │
          │  ── {STEP 1: description} ─────────────────────────────────
          ├── {function_a}({args}) → {output}
          │
          │  ── {STEP 2: description} ─────────────────────────────────
          └── {function_b}({args}) → {output}
                    │
                    ▼
          {result_function}({inputs}) → {output type}
                    │
                    ▼
    {write_function}({client}, {records}, {destination})
```

### {Why a notable design decision was made}

{Explain the design decision and the trade-offs considered. Use sub-bullets if comparing alternatives.}

---

## Tech Stack

{No new packages required. All dependencies are already in the project: / New packages or dependencies introduced:}

| Package       | {Already Used In / Version} | {Location / Justification}         |
| ------------- | --------------------------- | ---------------------------------- |
| `{package-1}` | `{>=x.y / path/to/usage}`   | {Why this package, not an alternative} |
| `{package-2}` | `{>=x.y / path/to/usage}`   | {Why this package, not an alternative} |

### {Notable dependency or client — e.g. API client setup}

{Describe how the client is initialised, any credentials or environment variables required, and a code snippet if relevant.}

```python
{client initialisation code}
```

{Describe retry logic, model selection rationale, or other usage constraints.}

```python
{retry decorator or wrapper code}
```

### {Second notable dependency, if applicable}

{Describe reuse pattern, import path, and what NOT to re-implement.}

```python
{import and usage snippet}
```

---

## Implementation Details

### Modules / Files

| File                    | Action           | Description                               |
| ----------------------- | ---------------- | ----------------------------------------- |
| `{path/to/runner.py}`   | Create           | {CLI runner: what it orchestrates}        |
| `{path/to/schemas.py}`  | Create           | {Pydantic models for structured output}   |
| `{path/to/prompts.py}`  | Create           | {Prompt templates for each call or step}  |
| `{path/to/schema.json}` | Create           | {BigQuery JSON schema definition}         |
| `{path/to/utils.py}`    | Reuse            | {Functions reused — do not re-implement}  |

---

### Key Functions

```python
def {load_function}(
    {client}: {ClientType},
    {param}: {Type},
    {param2}: {Type},
) -> {ReturnType}:
    """{One-line summary of what this function does.}

    {One paragraph describing the logic: what it queries or loads, how it
    groups or filters data, and what shape the result takes.}

    Args:
        {client}: {Description.}
        {param}: {Description.}
        {param2}: {Description.}

    Returns:
        {Description of the return value.}

    Raises:
        {ErrorType}: {When this error is raised.}
        {ErrorType}: {When this error is raised.}
    """
```

```python
def {step_one_function}(
    {client}: {ClientType},
    {input}: {Type},
    {param}: {Type},
) -> {ResultType}:
    """{One-line summary — e.g. "Call 1 — Extract X from Y."}

    {Describe what input is sent, what the model/service receives, and what
    structured output is returned. Note what is intentionally excluded.}

    Args:
        {client}: {Description.}
        {input}: {Description.}
        {param}: {Description.}

    Returns:
        {Description of the return value and its shape.}
        {Describe fallback behaviour on error, e.g. returns empty result and logs.}

    Raises:
        {ErrorType}: {Propagated only if retry logic is exhausted.}
    """
```

```python
def {step_two_function}(
    {client}: {ClientType},
    {input_from_step_one}: list[{StepOneResult}],
    {context_items}: list[{ContextType}],
) -> {ResultType}:
    """{One-line summary — e.g. "Call 2 — Match X to Y."}

    {Describe what inputs are sent (and what is intentionally withheld vs.
    step 1), what the model/service receives, and what structured output is
    returned.}

    Args:
        {client}: {Description.}
        {input_from_step_one}: {Output of step_one_function.}
        {context_items}: {Description of the context provided.}

    Returns:
        {Description of the return value.}
        {Describe fallback behaviour on error.}

    Raises:
        {ErrorType}: {Propagated only if retry logic is exhausted.}
    """
```

```python
def {orchestrate_function}(
    {client}: {ClientType},
    {unit}: {UnitType},
) -> list[{RecordType}]:
    """{One-line summary — orchestrates the full pipeline for a single unit.}

    {Describe the sequence of steps: data loading, step 1, step 2, derived
    computations, and error handling. Note concurrency model (this function
    runs per-unit; the caller handles parallelism).}

    Args:
        {client}: {Description.}
        {unit}: {Description of the processing unit, e.g. a vendor batch.}

    Returns:
        {Description. Note empty-list fallback on failure.}

    Raises:
        {ErrorType}: {When this error is raised.}
    """
```

```python
def {write_function}(
    {client}: {ClientType},
    {records}: list[{RecordType}],
    {destination}: str,
) -> int:
    """{One-line summary — e.g. "Write results to BigQuery, creating the table if needed."}

    {Describe write mode (append/overwrite), table creation behaviour, and
    schema source.}

    Args:
        {client}: {Description.}
        {records}: {Validated record objects to persist.}
        {destination}: {Fully qualified destination ID, e.g. BQ table ID.}

    Returns:
        {Number of rows written.}

    Raises:
        {ErrorType}: {On write failure.}
    """
```

---

### CLI Parameters

| Parameter       | Type     | Default              | Description                           |
| --------------- | -------- | -------------------- | ------------------------------------- |
| `--{param-1}`   | `str`    | required             | {What this parameter controls}        |
| `--{param-2}`   | `int`    | `{default_value}`    | {What this parameter controls}        |
| `--{flag-1}`    | `flag`   | `False`              | {What enabling this flag does}        |
| `--{param-3}`   | `str`    | `None`               | {What this parameter controls}        |
| `--{flag-2}`    | `flag`   | `False`              | {What enabling this flag does}        |
| `--{param-4}`   | `str`    | `${ENV_VAR}`         | {What this parameter controls}        |

---

### Data Models / Schemas

**Pydantic models** (`{path/to/schemas.py}`):

```python
# ── {Step 1} output ──────────────────────────────────────────────────────────

class {StepOneItem}(BaseModel):
    {field_1}: {type} = Field(description="{Description}")
    {field_2}: {type} = Field(description="{Description}")
    {field_3}: {type} | None = Field(default=None, description="{Description, if optional}")


class {StepOneResult}(BaseModel):
    {items}: list[{StepOneItem}] = Field(
        description="{Description of the list}"
    )


# ── {Step 2} input (passed as context) ───────────────────────────────────────

class {ContextItem}(BaseModel):
    {field_1}: {type} = Field(description="{Description}")
    {field_2}: {type} | None = Field(default=None, description="{Description}")
    {field_3}: {type} = Field(description="{Description}")


# ── {Step 2} output ───────────────────────────────────────────────────────────

class {StepTwoItem}(BaseModel):
    {input_field_1}: {type} = Field(description="{Description}")
    {input_field_2}: {type} = Field(description="{Description}")
    {matched_field_1}: {type} = Field(description="{Description}")
    {matched_field_2}: {type} = Field(description="{Description}")


class {StepTwoResult}(BaseModel):
    {matched_items}: list[{StepTwoItem}] = Field(
        description="{Description}"
    )
    {unmatched_inputs}: list[str] = Field(
        default_factory=list,
        description="{Description}",
    )
    {unmatched_context}: list[str] = Field(
        default_factory=list,
        description="{Description}",
    )


# ── Final persisted record ────────────────────────────────────────────────────

class {Record}(BaseModel):
    {id_field}: str = Field(description="{Description}")
    {entity_field}: str = Field(description="{Description}")
    {input_field}: {type} = Field(description="{Description}")
    {derived_field}: {type} = Field(
        description="{Description, e.g. formula}"
    )
```

**BigQuery schema** (`{path/to/schema.json}`):

| Field            | Type      | Mode     | Description                              |
| ---------------- | --------- | -------- | ---------------------------------------- |
| `{field_1}`      | STRING    | REQUIRED | {Description}                            |
| `{field_2}`      | STRING    | REQUIRED | {Description}                            |
| `{field_3}`      | FLOAT     | REQUIRED | {Description}                            |
| `{field_4}`      | STRING    | NULLABLE | {Description}                            |
| `{field_5}`      | FLOAT     | REQUIRED | {Description, e.g. formula}              |
| `created_at`     | TIMESTAMP | REQUIRED | Record creation timestamp                |

**Table:** `{gcp-project}.{dataset}.{table}`
**Partitioned by:** `DATE(created_at)`
**Clustered by:** `{cluster_field_1}, {cluster_field_2}`

---

### Testing Strategy

**Unit tests** (`tests/{module}/test_{runner}.py`):

- Mock `{ExternalClient}` — verify {what each call receives and does not receive}
- Verify `{derived_value}` formula: `{formula}`
- Mock `{StorageClient}` — verify {correct destination and record structure}
- Test Pydantic validation: {missing fields, edge values, null optionals}
- Test edge case: `{field} = {edge_value}` → {expected behaviour}

**Integration test** (manual, requires {auth prerequisites}):

```bash
uv run python -m {module.path} \
    --{param-1} <test-value> \
    --{param-2} 1 \
    --{output-param} ./eval_outputs/{test_dir} \
    --dry-run
```

Verify: {what a passing integration test looks like — output created, schema matches, no unhandled exceptions}.

**Edge cases:**

- {Edge case 1} → {expected handling}
- {Edge case 2} → {expected handling}
- {Edge case 3} → {expected handling}
- {Edge case 4} → {expected handling}

---

### Open Questions / Risks

- [ ] **{Risk or question title}:** {Description.} **Owner:** @{owner} **Target:** {date or milestone}
- [ ] **{Risk or question title}:** {Description.} **Owner:** @{owner} **Target:** {date or milestone}
