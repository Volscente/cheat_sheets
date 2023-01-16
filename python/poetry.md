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


# Commands

## Project Setup

### Setup new project
``` bash
poetry new <repository_name>
```

### Initialise existing project
``` bash
cd pre-existing-project
poetry init
```