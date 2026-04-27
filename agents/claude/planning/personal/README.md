# Personal Work Planning — Skills & Templates

A workflow for turning a personal project idea into implemented code, using Notion for personal context and GitHub Issues for task tracking.

---

## The Notion/RFC Split

Two documents exist for every initiative — they serve different readers:

| | Notion initiative page | RFC (`docs/rfc/`) |
|---|---|---|
| **Reader** | You | Claude |
| **Answers** | What am I building and why? | How will it be built? |
| **Motivation** | Full personal context — written for yourself | 1-paragraph technical framing + link to Notion |
| **Language** | Plain, personal, outcome-focused | Technical, precise, design-focused |
| **Lives in** | Notion | Your repo |

The RFC Motivation section is intentionally brief. It states the technical gap and links to Notion for the full context. No duplication.

---

## Notion Structure

```
Goals table (one row per project)
└── Recipe App                          ← project page
    ├── Add Search Bar                  ← initiative sub-page → GitHub Milestone
    └── Improve Load Time               ← initiative sub-page → GitHub Milestone
```

**Initiative sub-page content (Notion):**

| Field | What to write |
|---|---|
| **What** | 1–2 sentences in plain language |
| **Why** | Personal motivation — why this matters to you right now |
| **Success looks like** | Outcome bullets (what changes when this is done) |
| **RFC** | Link to `docs/rfc/.../rfc_document.md` in the repo |
| **GitHub Milestone** | Link to the milestone |
| **GitHub Issues** | Links to individual issues |

No sprints. Issues are prioritized directly on the milestone and worked in any order.

---

## Workflow Overview

```
Notion initiative page
  │
  ▼ Step 1 (for complex initiatives only)
/create-rfc          →  RFC document            (templates/rfc_template.md)
  │
  ▼ Step 2
/general-plan        →  Initiative plan         (templates/general_plan_template.md)
  │
  ▼ Step 3  (once per GitHub Issue)
/plan --type spec    →  Tech Spec               (templates/tech_spec_template.md)
  │
  ▼ Step 4
/execute-plan        →  Implemented code
```

> **When to skip the RFC:** If the design is obvious and there are no real architectural unknowns, go straight from the Notion page to `/general-plan`. The RFC earns its cost when you need to think through tradeoffs before writing a single line of code.

---

## Step 1 — Create RFC

**Skill:** `commands/create-rfc.md` | **Template:** `templates/rfc_template.md`

Generates a technical RFC. The Motivation section is a single paragraph — personal context stays in Notion.

```text
/create-rfc \
  --title "Add Search Bar" \
  --project "recipe-app" \
  --author "Simone Porreca" \
  --github-repo "simone/recipe-app" \
  --notion-page "https://notion.so/Add-Search-Bar-abc123" \
  --milestone "Add Search Bar" \
  --problem "The app has no search capability. With 200+ saved recipes, users cannot find entries without scrolling the full list." \
  --scope-in "Full-text search index, search UI component, keyboard shortcut" \
  --scope-out "Fuzzy matching: future phase, Tag filters: separate initiative" \
  --tech-stack "whoosh, Flask, pytest" \
  --milestones "Implement search index, Build search UI, Add keyboard shortcut"
```

**Output:** `docs/rfc/recipe-app_add-search-bar/rfc_document.md`

---

## Step 2 — Generate Initiative Plan

**Skill:** `commands/general-plan.md` | **Reference:** `templates/general_plan_template.md`

Reads the RFC and produces a task breakdown with a dependency diagram and a GitHub Issues/Milestones grouping.

```text
/general-plan docs/rfc/recipe-app_add-search-bar/rfc_document.md \
              docs/planning/recipe-app/planning.md
```

**Output:** `docs/planning/recipe-app/planning.md`

---

## Step 3 — Generate Tech Spec (once per GitHub Issue)

**Skill:** `commands/plan-task.md` | **Templates:** `templates/tech_spec_template.md`, `templates/general_plan_template.md`

Generates a detailed technical spec for one task, linked to its GitHub Issue.

```text
/plan docs/rfc/recipe-app_add-search-bar/rfc_document.md \
      --planning docs/planning/recipe-app/planning.md \
      --task 1 \
      --type spec \
      --issue 12
```

**Output:** `docs/planning/recipe-app/12-implement-search-index.md`

Repeat for each task.

---

## Step 4 — Implement

**Skill:** `commands/execute-plan.md`

Reads the RFC (context) and spec (source of truth), builds a task list, implements in dependency order, runs tests, and updates package READMEs.

```text
/execute-plan docs/rfc/recipe-app_add-search-bar/rfc_document.md \
              docs/planning/recipe-app/12-implement-search-index.md
```

---

## Templates Reference

| File | Used by | Purpose |
|---|---|---|
| `templates/rfc_template.md` | `create-rfc` | Technical RFC: 1-paragraph motivation + link to Notion, objectives, scope, approach, tech stack, milestones, risks |
| `templates/general_plan_template.md` | `general-plan`, `plan-task` | Folder conventions, spec structure, field semantics |
| `templates/tech_spec_template.md` | `plan-task --type spec` | Per-issue spec: scope, architecture, modules, functions, schemas, tests, open questions |
| `templates/open_issues_template.md` | manual | Track open issues found during planning or implementation |

---

## Practical Example

**Scenario:** You have a Recipe App project. You want to add a search bar. You've already written the Notion initiative page.

### What Notion looks like

```
Goals table
└── Recipe App  (project page)
    └── Add Search Bar  (initiative sub-page)
        ├── What:    Full-text search across all saved recipes from the nav bar.
        ├── Why:     With 200+ recipes, finding a specific dish means scrolling
        │            for 30+ seconds. The app is frustrating to use daily.
        ├── Success: Can find any recipe by name or ingredient in <3 seconds.
        │            Works on mobile without a keyboard covering the results.
        ├── RFC:     docs/rfc/recipe-app_add-search-bar/rfc_document.md
        ├── Milestone: github.com/simone/recipe-app/milestone/3
        └── Issues:  #12 Search index · #13 Search UI · #14 Keyboard shortcut
```

### What the RFC looks like (excerpt)

```markdown
# [RFC] Add Search Bar — Recipe App

| Author        | Simone Porreca                                    |
| Project       | recipe-app                                        |
| RFC status    | Draft                                             |
| Notion page   | [Add Search Bar](https://notion.so/abc123)        |
| GitHub repo   | [simone/recipe-app](https://github.com/...)       |
| Milestone     | [Add Search Bar](https://github.com/.../milestone/3) |

## Motivation

The app has no search capability. With 200+ saved recipes, users cannot find
entries without scrolling through the full list — O(n) discovery for a growing
collection. For full context, see the [Notion initiative page](https://notion.so/abc123).

## Objectives
- **Build search index**: index all recipe titles and ingredients on save
- **Enable instant lookup**: return results for any query in under 200ms locally
- **Surface via UI**: expose search from the nav bar with keyboard shortcut support
...
```

### What the resulting file tree looks like

```
docs/
├── rfc/
│   └── recipe-app_add-search-bar/
│       └── rfc_document.md          ← Step 1 output
└── planning/
    └── recipe-app/
        ├── planning.md              ← Step 2 output
        ├── 12-implement-search-index.md   ← Step 3 output (Issue #12)
        ├── 13-build-search-ui.md          ← Step 3 output (Issue #13)
        └── 14-add-keyboard-shortcut.md    ← Step 3 output (Issue #14)
```

### Command sequence

```bash
# Step 1 — RFC (skip if design is obvious)
/create-rfc --title "Add Search Bar" --project "recipe-app" \
  --author "Simone Porreca" --github-repo "simone/recipe-app" \
  --notion-page "https://notion.so/abc123" \
  --problem "The app has no search. With 200+ recipes, discovery is O(n) scrolling." \
  --milestones "Implement search index, Build search UI, Add keyboard shortcut"

# Step 2 — Initiative plan
/general-plan docs/rfc/recipe-app_add-search-bar/rfc_document.md \
              docs/planning/recipe-app/planning.md

# Step 3 — Tech spec per issue (repeat for #13, #14)
/plan docs/rfc/recipe-app_add-search-bar/rfc_document.md \
      --planning docs/planning/recipe-app/planning.md \
      --task 1 --type spec --issue 12

# Step 4 — Implement (repeat per spec)
/execute-plan docs/rfc/recipe-app_add-search-bar/rfc_document.md \
              docs/planning/recipe-app/12-implement-search-index.md
```

---

## Differences from the Work Setup

| Aspect | Work (`planning/work/`) | Personal (`planning/personal/`) |
|---|---|---|
| Project tracking | JIRA Epic → JIRA Ticket | Notion Project → GitHub Issue |
| Task grouping | JIRA Stories | GitHub Milestones |
| Goals table | Per initiative | **Per project** (initiatives are sub-pages) |
| Sprints | Optional | **Removed** — issues are worked in priority order |
| RFC Motivation | Business-oriented, 2–3 paragraphs | Technical gap only, 1 paragraph + Notion link |
| RFC required? | Usually yes | **Optional** — only for complex designs |
| Build tooling | `justfile` recipes | No assumption — test/lint steps are best-effort |
| Output paths | `docs/planning/<jira-epic>/<ticket>.md` | `docs/planning/<project-slug>/<issue>-<title>.md` |
