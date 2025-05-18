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
### Commands
```bash
# Create a new project
uv init <project_name>

# Add dependencies
uv add requests
uv add 'requests==2.31.0'
uv add git+https://github.com/psf/requests
v add -r requirements.txt -c constraints.txt

# Build distributions
uv build
uv publish

# Virtual environment
uv sync # Sync the project's dependencies with the environment.
uv lock # Create a lockfile for the project's dependencies.
uv run # Run a command in the project environment.
uv tree # View the dependency tree for the project.
```

### project.toml
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "spam-eggs"
version = "2020.0.0"
dependencies = [
  "httpx",
  "gidgethub[httpx]>4.0.0",
  "django>2.1; os_name != 'nt'",
  "django>2.0; os_name == 'nt'",
]
requires-python = ">=3.8"
authors = [
  {name = "Pradyun Gedam", email = "pradyun@example.com"},
  {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
  {name = "Another person"},
  {email = "different.person@example.com"},
]
maintainers = [
  {name = "Brett Cannon", email = "brett@example.com"}
]
description = "Lovely Spam! Wonderful Spam!"
readme = "README.rst"
license = "MIT"
license-files = ["LICEN[CS]E.*"]
keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python"
]

[project.optional-dependencies]
gui = ["PyQt5"]
cli = [
  "rich",
  "click",
]

[project.urls]
Homepage = "https://example.com"
Documentation = "https://readthedocs.org"
Repository = "https://github.com/me/spam.git"
"Bug Tracker" = "https://github.com/me/spam/issues"
Changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

[project.scripts]
spam-cli = "spam:main_cli"

[project.gui-scripts]
spam-gui = "spam:main_gui"

[project.entry-points."spam.magical"]
tomatoes = "spam:main_tomatoes"
```

## Files
- `.python-version` &rarr; Pin the Python version
- `.venv` &rarr; Include the virtual environment

# Tools
Many Python packages provide applications that can be used as tools.

```bash
# Run a tool (e.g., "ruff")
uvx ruff # Option 1
uv tool run ruff # Option 2

# Use arguments (e.g., "hello from uv")
uvx pycowsay hello from uv

# Specific tool version
uvx ruff@0.3.0 check
uvx --from 'ruff==0.3.0' ruff check
uvx --from 'ruff>0.2.0,<0.3.0' ruff check

# Specify source
uvx --from git+https://github.com/httpie/cli httpie
uvx --from git+https://github.com/httpie/cli@3.2.4 httpie

# Install tool
uv tool install ruff # Installed in /bin and used like "ruff --version"
```
