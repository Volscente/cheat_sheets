# Personal Work Planning — Skills & Templates

A four-step workflow for turning a personal project idea into implemented code, using Claude Skills and document templates.

Tracking setup: **Notion** (ideas & docs) → **GitHub Issues** (tasks) → **GitHub Milestones** (grouped work).

---

## Workflow Overview

```
Idea / Notion page
  │
  ▼ Step 1
/create-rfc          →  RFC document            (templates/rfc_template.md)
  │
  ▼ Step 2
/general-plan        →  Initiative plan         (templates/general_plan_template.md)
  │
  ▼ Step 3  (once per GitHub Issue)
/plan --type spec    →  Tech Spec per task      (templates/tech_spec_template.md)
  │
  ▼ Step 4  (once per task)
/execute-plan        →  Implemented code
```

---

## Step 1 — Create RFC

**Skill:** `commands/create-rfc.md`  
**Template:** `templates/rfc_template.md`

Generates an RFC from a problem statement. Captures motivation, objectives, scope, milestones, tech stack, effort estimates, FAQs, and risks. Designed for personal technical projects — no business case required.

```text
/create-rfc \
  --title "CLI Tool for Automating Dotfile Sync" \
  --author "Simone Porreca" \
  --project "dotfile-manager" \
  --github-repo "simone/dotfile-manager" \
  --notion-page "https://notion.so/..." \
  --problem "Keeping dotfiles in sync across machines is manual and error-prone." \
  --scope-in "Config parser, apply command, dry-run mode" \
  --scope-out "GUI: out of scope, Cloud sync: future phase" \
  --milestones "Config parser, Apply command, CI integration"
```

**Required parameters:** `--title`, `--author`, `--problem`  
**Output:** `docs/rfc/<project-slug>_<title-slug>/rfc_document.md`

---

## Step 2 — Generate Initiative Plan

**Skill:** `commands/general-plan.md`  
**Reference:** `templates/general_plan_template.md`

Reads the RFC and produces a high-level planning document: an overview, a dependency order diagram, one section per task (scope, goal, deliverables, technical overview), and a **GitHub Issues / Milestones** grouping.

```text
/general-plan docs/rfc/dotfile-manager_cli-tool/rfc_document.md \
              docs/planning/dotfile-manager/planning.md
```

**Arguments:** `<rfc-path> <output-path>` (both required)  
**Output:** the planning document at the path you specify

---

## Step 3 — Generate Tech Spec (per task)

**Skill:** `commands/plan-task.md`  
**Templates:** `templates/tech_spec_template.md`, `templates/general_plan_template.md`

Reads the RFC and the planning doc, then generates a detailed technical spec for a single task. Links to the corresponding GitHub Issue. The spec covers technical scope, architecture diagram, tech stack, modules/files table, key function signatures with docstrings, CLI parameters, data models, testing strategy, and open questions.

```text
/plan docs/rfc/dotfile-manager_cli-tool/rfc_document.md \
      --planning docs/planning/dotfile-manager/planning.md \
      --task 2 \
      --type spec \
      --issue 12
```

**Output:** `docs/planning/<project-slug>/<issue-number>-<kebab-title>.md`

Repeat for each task in the planning document.

---

## Step 4 — Implement Tech Spec

**Skill:** `commands/execute-plan.md`

Reads the RFC (for context) and a tech spec (as the authoritative source of truth), then implements all code changes described in it. Builds a task list, implements in dependency order, runs tests and linters if configured, and updates or creates a `README.md` per modified package.

```text
/execute-plan docs/rfc/dotfile-manager_cli-tool/rfc_document.md \
              docs/planning/dotfile-manager/12-add-config-parser.md
```

**Arguments:** `<rfc-path> <spec-path>` (both required)

---

## Templates Reference

| File | Used by | Purpose |
| ---- | ------- | ------- |
| `templates/rfc_template.md` | `create-rfc` | RFC structure: header with Notion/GitHub links, motivation, objectives, scope, tech stack, milestones, FAQs, risks |
| `templates/general_plan_template.md` | `general-plan`, `plan-task` | Defines field semantics, folder/file naming conventions (`<project-slug>/<issue-number>-<title>.md`), and spec formatting rules |
| `templates/tech_spec_template.md` | `plan-task --type spec` | Fillable tech spec: scope, architecture, modules, functions, data models, testing strategy, open questions. Links to GitHub Issues. |
| `templates/open_issues_template.md` | manual | Tracks open issues discovered during planning or implementation, with observation, hypotheses, impact, and recommended actions |

---

## Differences from the Work Setup

| Aspect | Work (`planning/work/`) | Personal (`planning/personal/`) |
| ------ | ----------------------- | ------------------------------- |
| Idea tracking | JIRA Epic | Notion page |
| Task tracking | JIRA Ticket | GitHub Issue |
| Task grouping | JIRA Stories | GitHub Milestones |
| RFC tone | Business-oriented | Personal/technical |
| RFC header | Author, Team, Org, Reviewers | Author, Project, optional Reviewers |
| Output path | `docs/planning/<jira-epic>/<ticket>.md` | `docs/planning/<project-slug>/<issue>-<title>.md` |
| Build tooling | `justfile` recipes required | No `justfile` assumption |

---

## Notes

- The `general-plan` and `plan-task` commands overlap in coverage. Prefer `general-plan` for a clean initiative-level plan from scratch, and `plan-task` when you need more control (e.g. updating an existing plan or targeting a specific task with `--task`).
- When `--planning` is passed to `plan-task`, the planning doc becomes the **primary source of truth** for scope and deliverables; the RFC provides background only.
- `execute-plan` will not start writing code until it has read all files the spec names — this is by design to avoid stylistic drift.
- Test suite and linter steps in `execute-plan` are best-effort: if the project has no `pytest` or `pre-commit` configuration, the step is skipped and noted in the report.
