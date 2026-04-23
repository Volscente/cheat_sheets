---
name: Testing
description: pytest conventions and test structure for data science projects
type: rule
---

# Testing

## Framework

- Use **pytest** exclusively — no `unittest`.
- Mirror the source tree: `src/preprocessing.py` → `tests/test_preprocessing.py`.

## Fixtures

- Use `@pytest.fixture` for reusable data objects (sample DataFrames, configs).
- Place shared fixtures in `tests/conftest.py`.

```python
# tests/conftest.py
import pytest
import pandas as pd

@pytest.fixture
def sample_df() -> pd.DataFrame:
    return pd.DataFrame({
        "age": [25, 30, None],
        "salary": [50000, 60000, 55000],
        "label": [0, 1, 0],
    })
```

## Parametrize

- Use `@pytest.mark.parametrize` for data-driven tests instead of duplicating test functions.

```python
@pytest.mark.parametrize("col,expected_dtype", [
    ("age", "float64"),
    ("salary", "int64"),
])
def test_column_dtype(sample_df, col, expected_dtype):
    assert sample_df[col].dtype == expected_dtype
```

## What to Test

- Input validation: assert that bad inputs raise the right errors.
- Output shape and dtype: transformations return the expected structure.
- Determinism: functions with a fixed seed return the same result across calls.
- Edge cases: empty DataFrames, single-row inputs, all-null columns.

## Coverage

- Aim for ≥80% coverage on `src/` modules.
- Do not test private helpers exhaustively — focus on the public interface.
