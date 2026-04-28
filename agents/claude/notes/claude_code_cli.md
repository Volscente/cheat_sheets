# Claude Code CLI

## Overview

### Resources

- [Documentation](https://code.claude.com/docs/en/quickstart)
- [MCP Server](https://code.claude.com/docs/en/mcp)
- [Complete Guide](https://blakecrosley.com/guides/claude-code)
- [Claude Commands](https://blakecrosley.com/guides/claude-code-cheatsheet)

### Theory

Claude Code is an agentic CLI that reads your codebase, executes commands, and modifies files through a layered system of permissions, hooks, MCP integrations, and subagents. Master five core systems (configuration, permissions, hooks, MCP, and subagents) and you unlock force-multiplier productivity.

When you give Claude a task, it works through three phases: gather context, take action, and verify results. The agentic loop is powered by two components: models that reason and tools that act. Claude Code serves as the agentic harness around Claude: it provides the tools, context management, and execution environment that turn a language model into a capable coding agent.

You can extend what Claude knows with **skills**, connect to external services with **MCP**, automate workflows with **hooks**, and offload tasks to **subagents**.

![Extend Claude Code](./images/extend_claude_code.png)

## Modes

There are 3 main modes that can be changed with `Shift + Tab`:

- Ask &rarr; It is the default one
- Code
- Planning &rarr; Combined with a small model like Haiku or a reasoning Opus (also use `/fast` for small changes.)

## CLI

```bash
# Open claude code CLI
claude

# Session with name
claude -n "auth-refactor"

# Resume session
claude --resume auth-refacto
/resume auth-refactor
```

## Claude Commands

###  List

```bash
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
/compact <prompt_what_to_keep>

# Change to fast mode
/fast

# Allow to check the token usage on the fly
/statusline
```

### Agents

- Command `/agents`
- It is possible to create an agent for example that supervise the security aspects.
- The agent can be requested through the console
- They are just Markdown files, for example a "security" agent
- Some agents that make sense are the "Research" and "Reviewer" agent

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

```markdown
---
description: Security-focused code review
allowed-tools: Read, Grep, Glob
model: claude-sonnet-4-5
---

Review this code for security vulnerabilities:

1. Injection attacks (SQL, command, XSS)
2. Authentication and authorization flaws
3. Sensitive data exposure
4. Insecure dependencies

Focus on actionable findings with specific line references.
```

- The Command Frontmatter Options:

```markdown
---
description: Brief description for /help
allowed-tools: Read, Edit, Bash(npm:*)
model: opus
argument-hint: [arg1] [arg2]
disable-model-invocation: false
---
```

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

- Custom commands can be organised like:

```text
.claude/commands/
├── backend/
│   ├── test.md
│   └── deploy.md
├── frontend/
│   ├── test.md
│   └── build.md
└── review.md
```

## Files

### Introduction

- The `CLAUDE.md` can be stored at global-level (home dir) or at project-level

### CLAUDE.md

- It is created through `/init`.
- It includes like the instructions and a description to what is inside the repository and how Claude should interact with it.
- It is very usefull in order to have subsequent interaction between Claude and the repository. It acts like a snapshot of the current codebase status, especially usefull when you change between Claude sessions.
- It should be continuoysly updated &rarr; it is possible just to use again `/init` command &rarr; alternatively you can specify what to add by using `# <tell_what_to_add>`.

#### Rules

- Stored in `.claude/rules` as Markdown files. It is a way to split `CLAUDE.md` &rarr; Ask Claude to split it into the rules
- `code-style.md`: rules on how to style the code
- `testing.md`: rules on how to build unit tests
- `security.md`: rules on how to secure the system
- `frontedn/styles.md`

### Memory

- Stored in the global-leve and it is a `MEMORY.md` file
- Includes information about the specific project

### Output Style

It is possible to configure with:

```bash
/output-style Explanatory # Detailed explanations with reasoning
/output-style Learning # Educational format with concepts explained
/output-style Concise # Minimal output, just essentials
```

Or configure in `.claude/styles/` a Markdown file with a name like `my-style.md`:

```markdown
# my-style

## Instructions

- Always explain the WHY behind each decision
- Include relevant documentation links
- Format code examples with comments
- End with a "What to do next" section

## Format

Use markdown headers for organization.
Keep explanations under 200 words per section.
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
- Use the Agent Model Tiering in order to route sub-agents exploration to cheaper model and save cost
- You can pass parameters as in "Custom Commands"

### MCP

- They enable Claude Code to communicate with data sources, services and APIs
- Use the command `claude mcp add` to install a specific MCP server
- It creates a `.mcp.json` file
- Once they are connected, they can be used in normal prompts

### SKills

Skills represent a fundamentally different approach to extending Claude Code. Unlike slash commands that you invoke explicitly, skills are model-invoked—Claude automatically discovers and uses them based on context. You embed domain expertise into a skill, and Claude draws on that expertise whenever the situation calls for it, without you needing to remember to ask

## Data Scientist Setup Example

A practical layout for a Data Scientist project using rules and agents to enforce conventions automatically.

### Directory Structure

```text
.claude/
├── rules/
│   ├── code-style.md       # Docstrings (NumPy), type hints, logging
│   ├── data-science.md     # Seeds, leakage prevention, pipeline structure
│   └── testing.md          # pytest conventions, fixtures, parametrize
└── agents/
    ├── reviewer.md         # Code review: critical / warning / suggestion report
    └── notebook-cleaner.md # Prepares notebooks for sharing (header, logs, seeds)
```

See the sample files in `agents/claude/rules/` and `agents/claude/agents/` for full content.

### How Rules Work

Rules in `.claude/rules/` are loaded automatically at the start of every session — no invocation needed. Claude applies them to every file it touches.

```bash
# After adding rules, Claude will automatically:
# - Write NumPy docstrings on any new/modified function
# - Use logging instead of print()
# - Add type hints to function signatures
```

The more specific the rule, the more consistent the output. Prefer concrete examples in rule files over abstract descriptions.

### How Agents Work

Agents in `.claude/agents/` are spawned by Claude when the task fits their description, or you can invoke them explicitly.

```bash
# Invoke the reviewer agent on a specific file
"Use the reviewer agent to review src/preprocessing.py"

# Invoke the notebook cleaner
"Use the notebook-cleaner agent on notebooks/eda.ipynb"
```

Agents run in an isolated context window, which means they do not pollute your main session with intermediate reasoning. Only the final report comes back.

### Agent vs Rule — When to Use Which

| Situation | Use |
| --- | --- |
| Always enforce docstring style | Rule (`code-style.md`) |
| Always enforce logging over print | Rule (`code-style.md`) |
| On-demand review before committing | Agent (`reviewer.md`) |
| Prepare a notebook before sharing | Agent (`notebook-cleaner.md`) |
| Catch data leakage patterns always | Rule (`data-science.md`) |

### Updating Rules

Ask Claude to update a rule file directly when a convention changes:

```bash
"Update .claude/rules/code-style.md: we now use Google docstring format, not NumPy"
```
