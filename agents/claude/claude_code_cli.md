# Claude Code CLI

## Overview

- [Documentation](https://code.claude.com/docs/en/quickstart)

## Modes

There are 3 main modes that can be changed with `Shift + Tab`:

- Ask &rarr; It is the default one
- Code
- Planning

## Commands

###  List

```bash
# Open claude code CLI
claude

# Initialise a Claude repo with CLAUDE.md
/init

# Create a new agent for the selected repository
/agents

# Change the model
/models

# Exit chat
/exit

# Clear the session memory
/clear

# Compatch the session into a summary (usefull for long sessions)
/compact
```

### Agents

- Command `/agents`
- It is possible to create an agent for example that supervise the security aspects.
- The agent can be requested through the console.

### Tasks

- Command `/tasks`
- They are background tasks like web server of frontend

### Context

- Add context into a prompt by using `@path_to_the_file`
- You can also use the commands `/exit`, `/clear` or `/compact`
- Use double ESC for going back in the session memory history to a previous point in the session time
- Some configurations are saved in `settings.local.json`

## Files

### CLAUDE.md

- It is created through `/init`.
- It includes like the instructions and a description to what is inside the repository and how Claude should interact with it.
- It is very usefull in order to have subsequent interaction between Claude and the repository. It acts like a snapshot of the current codebase status, especially usefull when you change between Claude sessions.
- It should be continuoysly updated &rarr; it is possible just to use again `/init` command &rarr; alternatively you can specify what to add by using `# <tell_what_to_add>`.
