# {Initiative Name} — High-Level Planning

**Project:** {project name}
**GitHub repo:** [{project name}]({GITHUB_REPO_URL})
**GitHub Milestone:** [{Milestone Name}]({GITHUB_MILESTONE_URL})
**Notion page:** [{Initiative Name}]({NOTION_URL})
**Total estimated effort:** {N} FTE-days (1 FTE = 1 day)

---

## Overview

{2–3 sentences describing what the initiative builds and what it changes technically. No personal motivation — that lives in Notion.}

### Dependency Order

```txt
TASK-1 ──► TASK-2 ──► TASK-4
               │
               └──► TASK-3 (parallel)
```

---

<!-- Repeat this block for every task (TASK-1, TASK-2, … TASK-N). -->

## TASK-1 — {Task Name}

**GitHub Issue:** #{number}
**Effort estimate:** {N} FTE-days

### Scope

{One short paragraph: what work is included in this task.}

### Goal

{One short paragraph: concrete output and why it matters technically.}

### Deliverables

- `{src/module.py}` — {description}
- `{--cli-flag}` — {description}

### Technical Overview

{Data models, CLI parameters, architectural constraints, integration points.}

---

## TASK-2 — {Task Name}

**GitHub Issue:** #{number}
**Effort estimate:** {N} FTE-days

### Scope

{One short paragraph.}

### Goal

{One short paragraph.}

### Existing Work (already done)

{Only include this section if the RFC describes work already complete.}

### Gaps to Close

{Only include when "Existing Work" is present. Numbered list of what still needs building.}

1. {Gap 1}
2. {Gap 2}

### Deliverables

- `{src/module.py}` — {description}

### Technical Overview

{Data models, CLI parameters, architectural constraints, integration points.}

---

## GitHub Issues

<!-- Repeat the Milestone block for every milestone group (Milestone 1, 2, … N). -->

### Milestone 1 — {Milestone Name}

**Tasks:** TASK-1, TASK-2
**Effort:** {N} FTE-days

#### Scope

{One paragraph covering what this milestone delivers end-to-end.}

#### Goal

{One paragraph: concrete outcome when this milestone is complete.}

#### Deliverables

- {Named output 1}
- {Named output 2}

---

### Milestone 2 — {Milestone Name}

**Tasks:** TASK-3, TASK-4
**Effort:** {N} FTE-days

#### Scope

{One paragraph.}

#### Goal

{One paragraph.}

#### Deliverables

- {Named output 1}
- {Named output 2}
