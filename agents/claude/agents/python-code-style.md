---
name: python-code-style
description: Reference for the python-code-style Claude Code sub-agent. Actual agent file lives at ~/.claude/agents/python-code-style.md
type: agent
---

# python-code-style Agent

Applies Python code style conventions when writing or reviewing `.py` files or Jupyter notebooks.

**Location:** `~/.claude/agents/python-code-style.md` (global — available in all projects)

**Trigger:** Claude may delegate to this agent automatically when it determines Python code style guidance is relevant to the task. You can also invoke it explicitly with `@python-code-style`. Auto-invocation is Claude's judgment call based on the description — it is not a deterministic file-type hook.

## Conventions enforced

### Docstrings

NumPy docstring format for all functions, methods, and classes. Always include `Parameters`, `Returns`, and `Raises`. Add `Examples` for public-facing functions.

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

### Type Hints

Type hints on all function signatures. Use `Optional[X]` instead of `X | None` for Python <=3.10 compatibility.

### Naming Conventions

| Construct             | Style                |
| --------------------- | -------------------- |
| Functions / variables | `snake_case`         |
| Classes               | `PascalCase`         |
| Constants             | `UPPER_SNAKE_CASE`   |
| Private members       | `_single_underscore` |

Avoid abbreviations unless universally understood in the domain (e.g. `df`, `cfg`).

### Logging

- Use `logging` module — never `print()` for runtime output.
- Initialise at module level: `logger = logging.getLogger(__name__)`.
- Configure formatter with datetime (seconds precision), level, and logger name.
- Build messages with f-strings.
- `DEBUG` → entry/exit and intermediate values.
- `INFO` → high-level milestones.
- `WARNING` / `ERROR` → recoverable / unrecoverable issues.

```python
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)

def load_data(path: str) -> pd.DataFrame:
    logger.debug(f"Loading data from {path}")
    df = pd.read_csv(path)
    logger.info(f"Loaded {len(df)} rows from {path}")
    return df
```
