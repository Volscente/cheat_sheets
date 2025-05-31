# File
## Sample
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.12
    hooks:
      - id: ruff check --fix
      - id: ruff format
```

# Commands
## Basic
```bash
# Install
pre-commit install

# Update from the .pre-commit-config.yaml file
pre-commit autoupdate
```
