---
title: ""               # Short RFC title (no team prefix)
team: ""                # Owning team name (e.g. Menu Intelligence)
author: ""              # Full name and email (e.g. Simone Porreca <simone.porreca@deliveryhero.com>)
jira-epic: ""           # JIRA epic ID (e.g. VDATA-9356) — used to derive the output path
org: ""                 # Organisation name (e.g. Vendor Sales and Operations); leave blank if not applicable
deadline: ""            # YYYY-MM-DD; leave blank to default to 14 days from today
reviewers:
  - ""                  # Format: "Name <email> required|optional"
  #                     # e.g. "Aishwarya Kadlag <a.kadlag@dh.com> required"
tech-stack:
  - ""                  # e.g. BigQuery, GitHub Actions, pandas
scope-in:
  - ""                  # Each line is one in-scope capability
scope-out:
  - ""                  # Format: "Item: reason" (e.g. "Online monitoring: deferred to future phase")
milestones:
  - ""                  # Ordered milestone names; each maps to an Effort Estimation row
---

## Problem

<!-- Required. Describe the problem being solved.
     Cover: what system/process is affected, the specific gap or pain point, and what happens without this RFC.
     Write as much as needed — no solutions here, just the problem. -->

## Approach direction

<!-- Optional. Your initial idea or preferred high-level technical approach.
     Leave blank if you want Claude to propose the methodology freely. -->

## Success criteria

<!-- Optional. How will you know this initiative is done?
     List measurable outcomes (e.g. "pipeline runs in < 10 min at p99").
     Used to generate the Objectives section in the RFC. -->

## Constraints

<!-- Optional. Hard requirements the solution must satisfy.
     Examples: SLA targets, banned technologies, compliance rules, budget caps, infra limitations.
     Claude will not relax these when designing the approach. -->

## Desired tech

<!-- Optional. Technologies you want to use or experiment with.
     Separate from the tech-stack YAML field (which lists the existing/required stack);
     this is for new tools you want to introduce — include your reasoning if useful. -->

## Integration context

<!-- Optional. How should the solution integrate with the current system?
     E.g. "must expose a BigQuery view consumed by the downstream ML pipeline",
     "must reuse the existing Dataflow template infrastructure".
     Used to shape integration subsections in the RFC. -->

## Known risks / concerns

<!-- Optional. Doubts about your approach, technical unknowns, or stakeholder concerns.
     Used to seed the Risks & Mitigations table in the RFC. -->
