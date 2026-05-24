---
title: ""               # Short description of the bug/issue
project: ""             # Project or repo name
author: "Simone Porreca"
severity: ""            # critical | high | medium
affected-versions:
  - ""                  # Version strings where bug is present (e.g. v1.2.3)
environments:
  - ""                  # Affected environments (e.g. production, staging)
github-issue: ""        # URL or issue number; omit row in hotfix doc if blank
github-repo: ""         # owner/repo (e.g. simone/recipe-app); omit row if blank
tech-stack:
  - ""                  # Relevant technologies (e.g. Python, PostgreSQL)
context-paths:
  - ""                  # Optional: paths to relevant source files Claude should read.
                        # Paths are relative to the root of the target project repo.
                        # E.g. "src/payments/checkout.py", "src/payments/README.md"
---

## Symptom

<!-- Required. What is the observable failure? Describe what users or systems experience.
     E.g. "Users receive a 500 error when submitting the checkout form since v1.4.2." -->

## Root cause

<!-- Optional. Your hypothesis about what is causing the bug.
     Leave blank if unknown — Claude will investigate based on the symptom and context paths. -->

## Fix approach

<!-- Optional. Your initial idea or preferred fix strategy.
     Leave blank if you want Claude to propose the approach freely. -->

## Verification steps

<!-- Required. How will you confirm the fix works in each affected environment?
     List concrete, observable checks (manual steps, test commands, monitoring queries). -->

## Scope

<!-- Optional. What is explicitly in and out of scope for this hotfix?
     Keep it tight — list only what must change to resolve the symptom.
     Format out-of-scope items as "Item: reason" (e.g. "Refactor payment module: separate initiative"). -->

## Known risks

<!-- Optional. What could go wrong when applying this fix?
     E.g. side effects on related features, data migration risks, cache invalidation issues. -->
