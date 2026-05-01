# Work Planning — Skills & Templates

A four-step workflow for turning a rough idea into implemented code, using Claude Skills and document templates.

---

## Workflow Overview

```txt
Idea
  │
  ▼ Step 1
/1-work-create-rfc        →  RFC document            (~/.claude/templates/work_rfc_template.md)
  │
  ▼ Step 2
/2-work-general-plan      →  Initiative plan         (~/.claude/templates/work_general_plan_template.md)
  │
  ▼ Step 3  (once per task)
/3-work-plan-task --type spec  →  Tech Spec per task (~/.claude/templates/work_tech_spec_template.md)
  │
  ▼ Step 4  (once per task)
/4-work-execute-plan      →  Implemented code
```

---

## Step 1 — Create RFC

**Command:** `~/.claude/commands/1-work-create-rfc.md`  
**Templates:** `~/.claude/templates/work_rfc_proposal_template.md`, `~/.claude/templates/work_rfc_template.md`

Generates a structured RFC document from a filled proposal file. The proposal captures motivation, objectives, scope, milestones, tech stack, effort estimates, FAQs, and risks.

**Workflow:**

1. Copy `~/.claude/templates/work_rfc_proposal_template.md` to `docs/rfc/<initiative-name>/proposal.md`.
2. Fill out the YAML frontmatter and `## Problem` section.
3. Run the command:

```text
/1-work-create-rfc --file docs/rfc/vdata-9356_online-catalog/proposal.md
```

**Parameters:**

| Parameter | Required | Description                                                        |
| :-------- | :------- | :----------------------------------------------------------------- |
| `--file`  | Yes      | Path to the filled `proposal.md`                                   |
| `--out`   | No       | Override output path (default: `rfc_document.md` next to `--file`) |

**Output:** `docs/rfc/<initiative-name>/rfc_document.md`

---

## Step 2 — Generate Initiative Plan

**Command:** `~/.claude/commands/2-work-general-plan.md`  
**Reference:** `~/.claude/templates/work_general_plan_template.md`

Reads the RFC and produces a high-level planning document: an overview, a dependency order diagram, one section per task (scope, goal, deliverables, technical overview), and a JIRA Stories grouping.

```text
/2-work-general-plan docs/rfc/vdata-9356_online_catalog/rfc_document.md \
              docs/planning/vdata-9356_online_catalog/planning.md
```

**Arguments:** `<rfc-path> <output-path>` (both required)  
**Output:** the planning document at the path you specify

---

## Step 3 — Generate Tech Spec (per task)

**Command:** `~/.claude/commands/3-work-plan-task.md`  
**Templates:** `~/.claude/templates/work_tech_spec_template.md`, `~/.claude/templates/work_general_plan_template.md`

Reads the RFC and the planning doc, then generates a detailed technical spec for a single task. The spec covers technical scope, architecture diagram, tech stack, modules/files table, key function signatures with docstrings, CLI parameters, data models, testing strategy, and open questions.

```text
/3-work-plan-task docs/rfc/vdata-9356_online_catalog/rfc_document.md \
      --planning docs/planning/vdata-9356_online_catalog/planning.md \
      --task 2 \
      --type spec \
      --epic vdata-9356_online-catalog \
      --ticket vdata-9400_add_search
```

**Output:** `docs/planning/<epic>/<ticket>.md`

Repeat for each task in the planning document.

---

## Step 4 — Implement Tech Spec

**Command:** `~/.claude/commands/4-work-execute-plan.md`

Reads the RFC (for context) and a tech spec (as the authoritative source of truth), then implements all code changes described in it. Builds a task list, implements in dependency order, runs tests and linters, and updates or creates a `README.md` per modified package.

```text
/4-work-execute-plan docs/rfc/vdata-9356_online_catalog/rfc_document.md \
              docs/planning/vdata-9356/vdata-9400_add_search.md
```

**Arguments:** `<rfc-path> <spec-path>` (both required)

---

## Templates Reference

| File                                                | Used by                                   | Purpose                                                                                                                        |
| --------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `~/.claude/templates/work_rfc_proposal_template.md` | `1-work-create-rfc` (input)               | Fillable proposal: YAML frontmatter + `## Problem` prose — the source of truth you author                                      |
| `~/.claude/templates/work_rfc_template.md`          | `1-work-create-rfc` (output)              | Canonical RFC structure: header, motivation, objectives, scope, tech stack, milestones, FAQs, risks                            |
| `~/.claude/templates/work_general_plan_template.md` | `2-work-general-plan`, `3-work-plan-task` | Defines field semantics, folder/file naming conventions, and spec formatting rules                                             |
| `~/.claude/templates/work_tech_spec_template.md`    | `3-work-plan-task --type spec`            | Fillable tech spec structure: scope, architecture, modules, functions, schemas, tests, open questions                          |
| `~/.claude/templates/work_open_issues_template.md`  | manual                                    | Tracks open issues discovered during planning or implementation, with observation, hypotheses, impact, and recommended actions |

---

## Notes

- The `general-plan` and `plan-task` commands overlap in coverage. Prefer `general-plan` for a clean initiative-level plan and `plan-task` when you need more control (e.g. updating an existing plan or targeting a specific task).
- When `--planning` is passed to `plan-task`, the planning doc becomes the **primary source of truth** for scope and deliverables; the RFC provides background only.
- `execute-plan` will not start writing code until it has read all files the spec names — this is by design to avoid stylistic drift.
