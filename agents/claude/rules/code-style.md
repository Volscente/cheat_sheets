---
name: Code Style
description: Enforce docstring format, type hints, and logging conventions
type: rule
---

# Code Style

## Docstrings

- Use **NumPy docstring format** for all functions, methods, and classes.
- Always include `Parameters`, `Returns`, and `Raises` sections when applicable.
- Add an `Examples` section for public-facing functions.

```python
def preprocess(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    """
    Remove nulls and encode the target column.

    Parameters
    ----------
    df : pd.DataFrame
        Raw input data.
    target_col : str
        Name of the column to encode.

    Returns
    -------
    pd.DataFrame
        Cleaned and encoded DataFrame.

    Raises
    ------
    ValueError
        If `target_col` is not present in `df`.
    """
```

## Type Hints

- Add type hints on all function signatures (arguments and return type).
- Use `Optional[X]` instead of `X | None` for Python <3.10 compatibility.

## Logging

- Use the `logging` module — never use `print()` for runtime output.
- Initialise the logger at module level: `logger = logging.getLogger(__name__)`.
- Use `DEBUG` for function entry/exit and intermediate values.
- Use `INFO` for high-level progress milestones.
- Use `WARNING` / `ERROR` for recoverable / unrecoverable issues.

```python
import logging

logger = logging.getLogger(__name__)

def load_data(path: str) -> pd.DataFrame:
    logger.debug("Loading data from %s", path)
    df = pd.read_csv(path)
    logger.info("Loaded %d rows from %s", len(df), path)
    return df
```
