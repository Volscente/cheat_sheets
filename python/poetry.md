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