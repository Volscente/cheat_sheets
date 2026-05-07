# {Module / Package Name}

<!-- Required. Replace with the module or package name. -->

## Purpose

<!-- Required. 2–3 sentences: what this module does and why it exists.
     Focus on the role it plays in the larger system, not on implementation.
     Good: "Handles all authentication flows and issues JWT tokens consumed by downstream services."
     Bad: "Contains auth.py and token.py." -->

{Description of what this module does and why it exists.}

## Key components

<!-- Required. Bullet list of the main files, classes, or services inside this module.
     One line per item. Omit trivial files (tests, config, __init__.py with no logic).
     Format: **name** — one-line description -->

- **{file / class / service}** — {one-line description}

## Public interfaces

<!-- Required. What other modules, services, or callers invoke from this module.
     List the functions, classes, REST endpoints, events, or CLI commands that form
     the contract this module exposes. Omit internal helpers.
     Format: `symbol` — description -->

- `{function / class / endpoint / event}` — {description}

## External dependencies

<!-- Required. Key third-party libraries or external services this module relies on.
     Only list direct, meaningful dependencies — not transitive or dev-only ones.
     Format: **name** — what it is used for -->

- **{library / service}** — {what it is used for}

## Constraints / invariants

<!-- Required if any exist. Non-obvious rules, SLAs, security boundaries, or
     behavioural guarantees this module must uphold. Write as statements of fact.
     Examples:
       - All writes must be idempotent; callers may retry without side effects.
       - Token expiry must not exceed 24 h (compliance requirement).
     Omit if there are genuinely no non-obvious constraints. -->

- {Constraint or invariant}

## Out of scope

<!-- Required. What this module explicitly does NOT handle and why.
     This is as important as what it does — it prevents scope creep during design.
     Format: **What** — reason -->

- **{Capability}** — {reason it is excluded from this module}
