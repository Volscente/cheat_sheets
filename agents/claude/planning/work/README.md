# Work Planning — Skills & Templates

A four-step workflow for turning a rough idea into implemented code, using Claude Skills and document templates.

---

## Workflow Overview

```
Idea
  │
  ▼ Step 1
/create-rfc          →  RFC document            (templates/rfc_template.md)
  │
  ▼ Step 2
/general-plan        →  Initiative plan         (templates/general_plan_template.md)
  │
  ▼ Step 3  (once per task)
/plan --type spec    →  Tech Spec per task      (templates/tech_spec_template.md)
  │
  ▼ Step 4  (once per task)
/execute-plan        →  Implemented code
```

---

## Step 1 — Create RFC

**Skill:** `commands/create-rfc.md`  
**Template:** `templates/rfc_template.md`

Generates a structured RFC document from a problem statement and a set of parameters. The RFC captures motivation, objectives, scope, milestones, tech stack, effort estimates, FAQs, and risks.

```text
/create-rfc \
  --title "Online Catalog Dataset Pipeline" \
  --team "Menu Intelligence" \
  --author "Simone Porreca <simone.porreca@deliveryhero.com>" \
  --jira-epic "VDATA-9356" \
  --problem "The online catalog has no automated dataset pipeline." \
  --deadline "2026-05-15" \
  --reviewers "Alice <alice@company.com> required, Bob <bob@company.com> optional" \
  --scope-in "BigQuery extraction, GitHub Actions workflow" \
  --scope-out "Real-time monitoring: deferred to future phase" \
  --milestones "Dataset extraction, Validation, CI integration"
```

**Required parameters:** `--title`, `--team`, `--author`, `--jira-epic`, `--problem`  
**Output:** `docs/rfc/<jira-epic>_<title-slug>/rfc_document.md`

---

## Step 2 — Generate Initiative Plan

**Skill:** `commands/general-plan.md`  
**Reference:** `templates/general_plan_template.md`

Reads the RFC and produces a high-level planning document: an overview, a dependency order diagram, one section per task (scope, goal, deliverables, technical overview), and a JIRA Stories grouping.

```text
/general-plan docs/rfc/vdata-9356_online_catalog/rfc_document.md \
              docs/planning/vdata-9356_online_catalog/planning.md
```

**Arguments:** `<rfc-path> <output-path>` (both required)  
**Output:** the planning document at the path you specify

---

## Step 3 — Generate Tech Spec (per task)

**Skill:** `commands/plan-task.md`  
**Templates:** `templates/tech_spec_template.md`, `templates/general_plan_template.md`

Reads the RFC and the planning doc, then generates a detailed technical spec for a single task. The spec covers technical scope, architecture diagram, tech stack, modules/files table, key function signatures with docstrings, CLI parameters, data models, testing strategy, and open questions.

```text
/plan docs/rfc/vdata-9356_online_catalog/rfc_document.md \
      --planning docs/planning/vdata-9356_online_catalog/planning.md \
      --task 2 \
      --type spec \
      --epic vdata-9356 \
      --ticket vdata-9400
```

**Output:** `docs/planning/<epic>/<ticket>.md`

Repeat for each task in the planning document.

---

## Step 4 — Implement Tech Spec

**Skill:** `commands/execute-plan.md`

Reads the RFC (for context) and a tech spec (as the authoritative source of truth), then implements all code changes described in it. Builds a task list, implements in dependency order, runs tests and linters, and updates or creates a `README.md` per modified package.

```text
/execute-plan docs/rfc/vdata-9356_online_catalog/rfc_document.md \
              docs/planning/vdata-9356/vdata-9400.md
```

**Arguments:** `<rfc-path> <spec-path>` (both required)

---

## Templates Reference

| File | Used by | Purpose |
| ---- | ------- | ------- |
| `templates/rfc_template.md` | `create-rfc` | Canonical RFC structure: header, motivation, objectives, scope, tech stack, milestones, FAQs, risks |
| `templates/general_plan_template.md` | `general-plan`, `plan-task` | Defines field semantics, folder/file naming conventions, and spec formatting rules |
| `templates/tech_spec_template.md` | `plan-task --type spec` | Fillable tech spec structure: scope, architecture, modules, functions, schemas, tests, open questions |
| `templates/open_issues_template.md` | manual | Tracks open issues discovered during planning or implementation, with observation, hypotheses, impact, and recommended actions |

---

## Notes

- The `general-plan` and `plan-task` commands overlap in coverage. Prefer `general-plan` for a clean initiative-level plan and `plan-task` when you need more control (e.g. updating an existing plan or targeting a specific task).
- When `--planning` is passed to `plan-task`, the planning doc becomes the **primary source of truth** for scope and deliverables; the RFC provides background only.
- `execute-plan` will not start writing code until it has read all files the spec names — this is by design to avoid stylistic drift.
