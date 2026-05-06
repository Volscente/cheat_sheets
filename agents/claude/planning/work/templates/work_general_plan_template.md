# {Initiative Name} — High-Level Planning

**RFC:** [{RFC Title}]({RFC_PATH})
**JIRA Epic:** [{JIRA-EPIC} — {Epic Name}]({JIRA_EPIC_URL})
**Total estimated effort:** {N} FTE-days (1 FTE = 1 day)

---

## Overview

{2–3 sentences describing what the initiative builds and what it changes technically. No business rationale — that lives in JIRA.}

### Dependency Order

```txt
TASK-1 ──► TASK-2 ──► TASK-4
               │
               └──► TASK-3 (parallel)
```

---

<!-- Repeat this block for every task (TASK-1, TASK-2, … TASK-N). -->

## TASK-1 — {Task Name}

**Effort estimate:** {N} FTE-days

### Scope

{One short paragraph: what work is included in this task.}

### Goal

{One short paragraph: concrete output and why it matters technically.}

### Deliverables

- `{src/module/file.py}` — {description}
- `{--cli-flag}` — {description}

### Technical Overview

{Data models, CLI parameters, architectural constraints, integration points.}

---

## TASK-2 — {Task Name}

**Effort estimate:** {N} FTE-days

### Scope

{One short paragraph.}

### Goal

{One short paragraph.}

### Existing Infrastructure (already done)

{Only include this section if the RFC describes infrastructure already in place.}

### Gaps to Close

{Only include when "Existing Infrastructure" is present. Numbered list of what still needs building.}

1. {Gap 1}
2. {Gap 2}

### Deliverables

- `{src/module/file.py}` — {description}

### Technical Overview

{Data models, CLI parameters, architectural constraints, integration points.}

---

## JIRA Stories

<!-- Repeat the Story block for every story group (Story 1, 2, … N). -->

### Story 1 — {Story Name}

**Tasks:** TASK-1, TASK-2
**Effort:** {N} FTE-days

#### Scope

{One paragraph covering what this story delivers end-to-end.}

#### Goal

{One paragraph: concrete outcome when this story is complete.}

#### Deliverables

- {Named output 1}
- {Named output 2}

---

### Story 2 — {Story Name}

**Tasks:** TASK-3, TASK-4
**Effort:** {N} FTE-days

#### Scope

{One paragraph.}

#### Goal

{One paragraph.}

#### Deliverables

- {Named output 1}
- {Named output 2}
