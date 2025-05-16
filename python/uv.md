# Introduction
## Definition
The uv library is a Python Package and Project Manager, like Poetry for example.

## Advantages
- Install and manage Python versions without the need of `pyenv`

## Installation
```bash
# Installation
pip install uv

# Update
uv self update

# Set autocompletion
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

# Features
## Python Versions
```bash
# Install specific version (uninstall for removing it)
uv python install <version>

# Reinstalling
uv python install <version> --reinstall

# List version
uv python list

# Find the location
uv python find <version>

# Pin the python version to the current project
uv python pin <version>
```

## Scripts
```bash
# Run a script
uv run <script>

# Run a script outside a project
uv run --no-project <script>

# Run a script with a dependency without installing it
uv run --with numpy example.py
uv run -- with 'numpy > 0.22' example.èy

# Ad and remove dependencies from a script
uv add --script example.py 'requests<3' 'rich'
uv remove --script
```

## Projects

