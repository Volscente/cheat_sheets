# Introduction

## Definition
Poetry is a tool for dependency management and packaging in Python. 
It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. 
Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

## Installation
Run the following command from the terminal:

``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

For **MacOS with ZSH** add the `.local/bin` to the `PATH` environment variable.
Modify the `.zshrc` file with the following command:

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

### Autocompletion

For **Oh My Zsh** run the following command:

``` bash
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
```

Then add the `poetry` entry in the `plugins` array in the `~/.zshrc` file.

## pyproject.toml File
``` toml
[tool.poetry]
name = "rp-poetry"
version = "0.1.0"
description = ""
authors = ["Philipp <philipp@realpython.com>"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

Each section identified by square brackets is called "Table". If a table is too-specific, it must be prefixed with **tool**.
You now see that the only tool is poetry, but you might also have `[tool.pytest.ini_options]` for pytest.

## Virtual Environment
Poetry is able to manage virtual environments and it is not created by default when creating a new poetry project.
**NOTE:** PyCharm will ask you if you want to create one.

Otherwise, inside the project directory, use the following command:
``` bash
poetry env use python3
```

The virtual environment will be created in the directory `~/Library/Caches/pypoetry` for MacOS

# Commands

## Project Setup

### Setup new project
``` bash
# It creates a new project in the folder <repository_name> with a package
# called <package_name> in the 'src' folder
poetry new <repository_name> --name <package_name> --src
```

### Initialise existing project
``` bash
cd pre-existing-project
poetry init
```

## Virtual Environment

### Create
``` bash
poetry env use python3
```

### List Virtual Environments
``` bash
poetry env list
```

### Show Info
``` bash
poetry env info
```

### Install Libraries
``` bash
# Install the dependencies listed in pyproject.toml [tool.poetry.dependencies]
poetry install

# Use the option '--without test,docs,dev' if you want to esclude the specified group from install
poetry install --without test,docs,dev
```

### Add & Install Dependency
``` bash
# NOTE: Use '--group dev' to install in the 'dev' dependencies list
poetry add <library_name>

poetry add <library> --group dev

# Add library to a specific group
poetry add <libary> --group <group_name>

# Add GitHub Repository
poetry add git+<github_repo_url>
```

### List Installed Libraries
``` bash
poetry show
```

## Version
``` bash
# Show the current version
poetry version

# Set the new value of the version
poetry version <version>
```

| rule        | Before | After   |
|-------------|--------|---------|
| major       | 1.3.0  | 2.0.0   |
| minor       | 2.1.4  | 2.2.0   |
| patch	      | 4.1.1	 | 4.1.2   |
| premajor	  | 1.0.2	 | 2.0.0a0 |
| preminor	  | 1.0.2	 | 1.1.0a0 |
| prepatch	  | 1.0.2	 | 1.0.3a0 |
| prerelease	| 1.0.2	 | 1.0.3a0 |
| prerelease	|1.0.3a0 | 1.0.3a1 |
| prerelease	|1.0.3b0 | 1.0.3b1|


## Build
``` bash
poetry build
```

**NOTE:** The .whl file will contain all the dependencies listed in the `pyproject.toml` file, in the `[tool.poetry.dependencies]` by default

## Test
If the path `src/test` has been correctly set, the following command will run every pytest inside the folder:
``` bash
# If the venv is correctly set
pytest

# If the venv is not recognised
poetry run pytest
```
