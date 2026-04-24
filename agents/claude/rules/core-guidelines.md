---
name: Core Guidelines
description: Universal rules for response style, workflow, tooling, project structure, and safety — applied on every request.
type: rule
---

# Core Guidelines

## Response Style

- Never use emojis.
- Always reference file paths with line numbers when discussing code (e.g. `src/utils.py:42`).

## Workflow

- Always run tests before declaring a task complete.
- Always ask before deleting files or dropping database tables.

## Tooling

- Use `uv` for Python dependency management — never `pip` directly.
- Use `just` as the task runner — check the `justfile` before suggesting `make` or raw shell commands.

## Project Structure

- Source code lives in `src/`, tests in `tests/`, configuration in `config/`. Do not mix them.
- This is a monorepo — confirm which package you are in before making changes.

## Security

- Never hardcode credentials or secrets. Always use environment variables.
