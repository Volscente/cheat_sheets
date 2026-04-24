---
name: python-testing
description: Reference for the python-testing Claude Code sub-agent. Actual agent file lives at ~/.claude/agents/python-testing.md
type: agent
---

# python-testing Agent

Applies pytest conventions and test structure when writing or reviewing Python tests.

**Location:** `~/.claude/agents/python-testing.md` (global — available in all projects)

**Trigger:** Claude may delegate to this agent automatically when it determines pytest guidance is relevant to the task. You can also invoke it explicitly with `@python-testing`. Auto-invocation is Claude's judgment call based on the description — it is not a deterministic file-type hook.

## Conventions enforced

### Framework

Use **pytest** exclusively — no `unittest`. Mirror the source tree: `src/preprocessing.py` → `tests/test_preprocessing.py`.

### Naming

`test_<function_name>_<scenario>` — e.g. `test_preprocess_drops_nulls`. The name must communicate intent without reading the body.

### Docstrings

Every test function and fixture must have a one-line docstring. State _what_ is being verified and _why_ — not _how_.

### Structure: Arrange – Act – Assert

```python
def test_preprocess_drops_nulls(sample_df):
    """preprocess removes rows where the target column is null."""
    # Arrange
    df_with_null = sample_df.copy()
    df_with_null.loc[0, "label"] = None

    # Act
    result = preprocess(df_with_null, target_col="label")

    # Assert
    assert result["label"].isna().sum() == 0
```

### Fixtures

`@pytest.fixture` for reusable objects. Shared fixtures in `tests/conftest.py`. One-line docstring per fixture.

```python
@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Three-row DataFrame with age (nullable), salary, and binary label."""
    return pd.DataFrame({
        "age": [25, 30, None],
        "salary": [50000, 60000, 55000],
        "label": [0, 1, 0],
    })
```

### Parametrize

`@pytest.mark.parametrize` for data-driven tests — never duplicate test functions.

```python
@pytest.mark.parametrize("col,expected_dtype", [
    ("age", "float64"),
    ("salary", "int64"),
])
def test_column_dtype(sample_df, col, expected_dtype):
    """Column dtypes match expected types after loading."""
    assert sample_df[col].dtype == expected_dtype
```

### Exception Testing

`pytest.raises` with `match=` to assert error message when relevant.

```python
def test_preprocess_raises_on_missing_column(sample_df):
    """preprocess raises ValueError when target_col is absent from the DataFrame."""
    with pytest.raises(ValueError, match="not present"):
        preprocess(sample_df, target_col="nonexistent_col")
```

### What to Test

- Input validation: bad inputs raise the right errors.
- Output shape and dtype: transformations return the expected structure.
- Determinism: functions with a fixed seed return the same result across calls.
- Edge cases: empty DataFrames, single-row inputs, all-null columns.
- Private helpers: test each internal function individually — every piece of logic verified in isolation.

### Coverage

Aim for ≥80% coverage on `src/` modules.
