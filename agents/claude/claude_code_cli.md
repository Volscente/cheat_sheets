# Claude Code CLI

## Overview

- [Documentation](https://code.claude.com/docs/en/quickstart)
- [MCP Server](https://code.claude.com/docs/en/mcp)

Claude Code is an agentic CLI that reads your codebase, executes commands, and modifies files through a layered system of permissions, hooks, MCP integrations, and subagents. Master five core systems (configuration, permissions, hooks, MCP, and subagents) and you unlock force-multiplier productivity.

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

### Custom Commands

- Store them in `.claude/commands/command-name.md`
- They are Markdown files in which you can specify, for example, how to build UI components (e.g., naming convention, syntax, tests, etc.)
- You can use the `@` to specify paths inside this Markdown file
- Add command components by adding the following on top of the Markdown file:

```markdown
---
description: Create a UI component in /UI/component
argument-hint: Component name | Component summary
---
```

- After you parse the arguments like:

```markdown
Parse $ARGUMENTS to get the following values:

- [name]: component name get from $ARGUMENTS
- [summary]: component summary get from $ARGUMENTS
```

- Afterwards you can use them in the Markdown file through `[name]` for example

## Files

### CLAUDE.md

- It is created through `/init`.
- It includes like the instructions and a description to what is inside the repository and how Claude should interact with it.
- It is very usefull in order to have subsequent interaction between Claude and the repository. It acts like a snapshot of the current codebase status, especially usefull when you change between Claude sessions.
- It should be continuoysly updated &rarr; it is possible just to use again `/init` command &rarr; alternatively you can specify what to add by using `# <tell_what_to_add>`.

### Memory

- It is used for storing general planning goals, deliverables and phases' descriptions

memory/
├── MEMORY.md
├── project_phase_overview.md
├── sprint_1.md
├── sprint_2.md
├── sprint_3.md
└── backlog.md

In `MEMORY.md`ß:

```markdown
## Active Work

- [Phase Overview](project_phase_overview.md) — Goals, deliverables, 3-sprint breakdown
- [Sprint 1](sprint_1.md) — Current sprint
- [Sprint 2](sprint_2.md)
- [Sprint 3](sprint_3.md)

## Future

- [Backlog](backlog.md) — Long-term features, exploratory ideas, nice-to-haves

For `backlog.md`, use project-type memory with this structure:

---

name: Long-term backlog and exploratory features
description: Ideas and features not yet assigned to a sprint
type: project

---

## Exploratory / Research Phase

- [Idea name] — brief description, why it matters

## Nice-to-have Features

- [Feature] — brief description

## Architectural Improvements

- [Improvement] — brief description

This way:

- Backlog is automatically loaded (visible to Claude in every conversation)
- But clearly separated from active sprint work
- Easy to promote items from backlog → sprint when ready
- Keeps MEMORY.md clean and scannable (index role only)
```

## Components

### Introduction

Core components to care for the correct usage of Claude Code:

1. Configuration hierarchy: controls behavior
2. Permission system: gates operations
3. Hook system: enables deterministic automation &rarr; Calling specicific tools (e.g., linting) when needed
4. MCP protocol: extends capabilities
5. Subagent system: handles complex multi-step tasks

### Subagents

- **Delegation Layer**: subagents prevent context bloat by isolating exploration in clean context windows, returning only summaries
- **Model Tiering**: route to subagents specialised in writing unit tests, analyse security, etc.
- They are created inside `.claude/agents` folder
- Each Agent is just a Markdown file with its instructions
- You can pass parameters as in "Custom Commands"

### MCP

- They enable Claude Code to communicate with data sources, services and APIs
- Use the command `claude mcp add` to install a specific MCP server
- It creates a `.mcp.json` file
- Once they are connected, they can be used in normal prompts
