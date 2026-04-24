---
name: sql-reviewer
description: Reference for the sql-reviewer Claude Code sub-agent. Actual agent file lives at ~/.claude/agents/sql-reviewer.md
type: agent
---

# sql-reviewer Agent

Reviews SQL queries for correctness, safety, performance, and style.

**Location:** `~/.claude/agents/sql-reviewer.md` (global — available in all projects)

**Model:** `claude-opus-4-6`

**Tools:** `Read`, `Grep`, `Glob` (read-only — no modifications)

**Trigger:** Claude may delegate to this agent automatically when it determines a SQL review is relevant. You can also invoke it explicitly with `@sql-reviewer`. Auto-invocation is Claude's judgment call based on the description — it is not a deterministic file-type hook.

## Checks performed

### Critical

| Issue | Risk |
|---|---|
| `UPDATE`/`DELETE` without `WHERE` | Full-table data loss |
| Dynamic SQL via string concatenation | SQL injection |
| Multi-statement mutations without a transaction | Inconsistent state on partial failure |

### Warning

| Issue | Why it matters |
|---|---|
| `SELECT *` | Breaks on schema changes, pulls unnecessary data |
| Non-SARGable predicates (e.g. `WHERE YEAR(col) = 2024`) | Prevents index use, causes full scans |
| Implicit type conversions in `JOIN`/`WHERE` | Silent full scans |
| Correlated subqueries (execute once per row) | Rewrite as `JOIN` or window function |
| `DISTINCT` masking a JOIN problem | Symptom, not a fix |
| Missing `LIMIT` on unfiltered large-table queries | Unbounded result sets |
| Hardcoded magic values | Should be parameters or named constants |

### Suggestion

- Long queries that would be clearer as CTEs.
- Inconsistent casing: keywords `UPPERCASE`, identifiers `lowercase`.
- Missing or inconsistent table aliases.
- Repeated subexpressions that could be a CTE or temp table.
- Missing comments on non-obvious business logic.

## Output format

Markdown report grouped by severity. Each finding includes a reference, a one-sentence explanation, and a corrected snippet when the fix is non-obvious.

Ends with: `N critical, N warnings, N suggestions`.
