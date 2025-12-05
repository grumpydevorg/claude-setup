# Claude Code Setup

> A comprehensive configuration setup for Claude Code with Model Context Protocol (MCP) servers, intelligent task routing, and automated workflows.

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blue.svg)](https://claude.ai/code)
[![MCP](https://img.shields.io/badge/MCP-Enabled-green.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Commands](#commands)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a pre-configured environment for Claude Code with enhanced capabilities through:

- **MCP Servers**: Context7, Puppeteer, DeepWiki
- **Intelligent Task Routing**: Auto-complexity assessment for optimal workflow selection
- **Custom Commands**: Workflows for commits, code review, and problem-solving
- **Memory System**: File-based persistent knowledge with global and project scopes
- **Hook System**: Automated memory prompts and workflow triggers

## Quick Start

```bash
# 1. Install dependencies
pip install uv

# 2. Clone this configuration
git clone <your-repo> claude-setup
cd claude-setup

# 3. Install memory CLI (optional but recommended)
uv tool install .claude/bin/memory

# 4. Start using commands - intelligent auto-routing!
/task implement user authentication
```

## Prerequisites

Before using this setup, ensure you have:

- **Claude Code**: Installed and configured
- **Python 3.8+**: For hook script execution
- **uv**: Package manager for Python script execution
- **Node.js**: For MCP server functionality (npx)

### Installation

#### 1. Install uv (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# After installation, open a new terminal and verify:
uv --version
```

#### 2. Setup Configuration

```bash
# Copy configuration files to your project
cp -r .claude/ /your/project/
cp .mcp.json /your/project/

# Install memory CLI for persistent knowledge management
uv tool install .claude/bin/memory

# Ensure hook permissions
chmod +x .claude/hooks/memory_prompt_hook.py
```

## Features

### 🎯 Custom Commands (User-Invoked)
- **`/task`**: Intelligent task routing with auto-complexity detection
- **`/commit`**: Intelligent commit workflow with conventional standards
- **`/code-review`**: Reviews uncommitted changes before committing

### 🧠 Skills (Full Methodology - Single Source of Truth)
Skills contain complete methodologies and auto-trigger based on context.

#### Core Skills
- **`task-routing`**: Automatic complexity assessment and workflow routing
- **`investigate`**: Scientific investigation using hypothesis testing
- **`trace-flow`**: Execution/data flow tracing with verification
- **`plan-implementation`**: Planning with validation checkpoints
- **`memory`**: Persistent knowledge management (project + global scopes)

#### Universal Skills
- **`hypothesis-testing`**: Scientific debugging method
- **`decision-making`**: Technical choice framework with ADR format
- **`verification`**: Multi-level testing confirmation
- **`review-quality`**: Comprehensive code review checklist
- **`skill-creator`**: Meta-skill for creating new skills

### 🤖 Agents (Thin Runtime Config)
Agents are lightweight wrappers that reference skills:
- **`investigator`**: Runs investigate skill → INVESTIGATION_REPORT.md
- **`code-flow-mapper`**: Runs trace-flow skill → FLOW_REPORT.md
- **`planner`**: Runs plan-implementation skill → PLAN.md
- **`code-reviewer`**: Runs review-quality skill with prioritized feedback

### 🔌 MCP Servers
- **Context7**: Library documentation and code context
- **Puppeteer**: Browser automation and web scraping
- **DeepWiki**: Repository documentation fetching

### ⚡ Hook System
- **Stop Hook**: Prompts for memory updates after session completion
- **Extensible**: Easy to add custom hooks for workflow automation

## Commands

### `/task` - Intelligent Task Routing

Automatically assesses task complexity and routes to the appropriate workflow.

**Usage:**
```bash
/task [problem description]
```

**How It Works:**
1. 🧠 Analyzes task characteristics (location, scope, type, certainty)
2. 📊 Calculates complexity score using heuristics
3. 🔀 Routes to optimal workflow:
   - **Simple** (score ≤ 0): Direct problem-solving
   - **Medium** (score 1-4): Light investigation then solve
   - **Complex** (score ≥ 5): Multi-agent (investigator → flow-mapper → planner)

**Examples:**

```bash
# Simple task (specific location) → Direct solve
/task Add logging to the login function in src/auth/login.ts

# Medium task (known domain) → Light investigation
/task Refactor the authentication logic to use OAuth

# Complex task (unknown location) → Multi-agent workflow
/task Find and fix the memory leak in the application
```

**Complexity Indicators:**
- **Location**: Specific file vs "find where..." vs unknown
- **Scope**: Single file vs multi-component vs system-wide
- **Type**: Add function vs refactor vs architectural redesign
- **Certainty**: Confident vs "probably..." vs "no idea where"

### `/code-review` - Automated Code Review

Initiates code-reviewer agent to analyze uncommitted changes only.

**Usage:**
```bash
/code-review
```

**Features:**
- Focuses exclusively on uncommitted changes
- Reviews for quality, security, and maintainability
- Provides prioritized feedback:
  - 🚨 Critical issues (must fix)
  - ⚠️ Warnings (should fix)
  - 💡 Suggestions (consider improving)
- Includes specific fix examples

**Example:**
```bash
# After making changes
/code-review
# Fix any critical issues
/commit
```

### `/commit` - Intelligent Commits

Streamlined commit workflow following conventional commit standards.

**Features:**
- Diff analysis and change summarization
- Conventional commit message formatting
- Clean, focused commits

**Important:** Run `/code-review` before committing to ensure code quality.

**Example:**
```bash
# Review changes first
/code-review
# After fixing issues
/commit
```

## Configuration

### Directory Structure

```
claude-setup/
├── .claude/
│   ├── settings.json          # Permissions and hook configuration
│   ├── bin/
│   │   └── memory             # CLI for memory management
│   ├── memory/                # Project-scoped knowledge storage
│   │   ├── pattern/           # Code patterns
│   │   ├── domain/            # Domain knowledge
│   │   ├── flow/              # Execution flows
│   │   └── risk/              # Known risks
│   ├── skills/                # Full methodologies (single source of truth)
│   │   ├── task-routing/      # Complexity assessment and routing
│   │   ├── investigate/       # Scientific investigation
│   │   ├── trace-flow/        # Flow tracing
│   │   ├── plan-implementation/ # Planning methodology
│   │   ├── memory/            # Memory management
│   │   ├── hypothesis-testing/ # Scientific debugging
│   │   ├── decision-making/   # Technical choices
│   │   ├── verification/      # Testing confirmation
│   │   ├── review-quality/    # Code review checklist
│   │   └── skill-creator/     # Skill creation meta-skill
│   ├── agents/                # Thin runtime config (tools + skill pointer)
│   │   ├── investigator.md    # → uses investigate skill
│   │   ├── code-flow-mapper.md # → uses trace-flow skill
│   │   ├── planner.md         # → uses plan-implementation skill
│   │   └── code-reviewer.md   # → uses review-quality skill
│   ├── commands/              # User-invoked workflows
│   │   ├── task.md            # Intelligent task routing
│   │   ├── code-review.md     # Code review trigger
│   │   └── commit.md          # Commit workflow
│   └── hooks/
│       └── memory_prompt_hook.py  # Memory update prompts (Stop hook)
├── .mcp.json                  # MCP server configuration
└── README.md
```

### Architecture: Skills as Single Source of Truth

```
┌─────────────────────────────────────────────────────────────┐
│                     User Request                            │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┴─────────────────────┐
        ▼                                           ▼
┌───────────────┐                         ┌─────────────────┐
│    Skills     │  Auto-triggered         │    Commands     │  User-invoked
│(methodology)  │  based on context       │ (orchestration) │  with /command
└───────┬───────┘                         └────────┬────────┘
        │                                          │
        │ ┌────────────────────────────────────────┘
        │ │
        ▼ ▼
┌────────────────────────┐
│        Agents          │  Thin wrappers
│  (tools + skill ref)   │  for subagent execution
└────────────────────────┘
        │
        ▼
┌────────────────────────┐
│        Skills          │  ← Agents READ skill methodology
│  (full methodology)    │
└────────────────────────┘
```

- **Skills**: Single source of truth for HOW to do things (full methodology)
- **Agents**: Thin runtime config (tools, color) + pointer to skill
- **Commands**: Explicit orchestration (e.g., /task uses task-routing skill)

### Memory Architecture (File-Based)

File-based knowledge storage with two scopes:

```
┌─────────────────────────────────────────────────────────────┐
│                    Memory System                             │
├─────────────────────────────────────────────────────────────┤
│  Project Scope:  .claude/memory/                            │
│    - Project-specific knowledge                              │
│    - Tracked in project git repo                             │
│    - Use: memory create pattern <name> "observation"        │
│                                                              │
│  Global Scope:   ~/.claude/memory/                          │
│    - Cross-project patterns and learnings                    │
│    - Separate git repo for global knowledge                  │
│    - Use: memory create --global pattern <name> "..."       │
└─────────────────────────────────────────────────────────────┘
```

**CLI Commands:**
```bash
# Project scope (default)
memory create pattern auth-flow "Uses JWT with httpOnly cookies"
memory add pattern auth-flow "Refresh tokens in Redis"
memory show pattern auth-flow

# Global scope
memory create --global pattern api-design "RESTful naming conventions"
memory query "authentication"  # Searches both scopes
memory list                     # Lists both scopes
```

**Entity Types:**
- `pattern:<name>`: Recurring code patterns
- `domain:<area>`: Domain knowledge (auth, api, db)
- `flow:<name>`: Documented execution paths
- `risk:<name>`: Known risks and gotchas
- `project:<name>`: Project-level metadata

**Git Integration:**
- Project memories tracked in `.claude/memory/`
- Global memories tracked in `~/.claude/memory/` (separate repo)
- Git history IS the archive - use `git diff`, `git revert`
- No separate archiving needed

**Memory Trigger:** Stop hook prompts for memory updates after evolving skills are used

### Settings Configuration

The `.claude/settings.json` file contains:

```json
{
  "permissions": {
    "allow": ["WebFetch(domain:docs.anthropic.com)", ...],
    "deny": [...]
  },
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "uv run .claude/hooks/memory_prompt_hook.py"
      }]
    }]
  },
  "enabledMcpjsonServers": ["context7", "puppeteer", "mcp-deepwiki"]
}
```

### MCP Configuration

The `.mcp.json` file defines server configurations:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["@context7/claude-dev", "--minTokens", "1000"]
    },
    "puppeteer": {
      "command": "npx",
      "args": ["@puppeteer/claude-dev"]
    },
    "mcp-deepwiki": {
      "command": "npx",
      "args": ["-y", "@executeautomation/mcp-deepwiki"]
    }
  }
}
```

## Troubleshooting

### Common Issues

**Memory CLI not found:**
- Install globally: `uv tool install .claude/bin/memory`
- Or use directly: `.claude/bin/memory <command>`
- Verify installation: `which memory`

**Hook not triggering:**
- Ensure `uv` is installed and in PATH
- Check script permissions: `chmod +x .claude/hooks/memory_prompt_hook.py`
- Verify hook configuration in `.claude/settings.json`

**MCP servers not loading:**
- Verify Node.js and npx are installed
- Check `.mcp.json` configuration syntax
- Ensure MCP packages are available via npx

**Task routing incorrect:**
- The task-routing skill learns from usage
- Provide feedback if routing seems wrong
- Check `.claude/skills/task-routing/SKILL.md` for heuristics

### Debug Mode

Enable debug mode for detailed logging:

```bash
claude --debug
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with detailed description

### Adding Custom Skills

The easiest way: just ask Claude "create a skill for X" - the **skill-creator** skill auto-triggers.

Manual creation:
1. Create directory: `.claude/skills/your-skill/`
2. Create `SKILL.md` with YAML frontmatter and **full methodology**:
```yaml
---
name: your-skill
description: >
  What it does. Use when: (1) condition, (2) condition.
---

# Your Skill Methodology

## Phase 1: [First Phase]
[Detailed instructions...]

## Phase 2: [Second Phase]
[Detailed instructions...]

## Output Format
[Expected output template...]
```
3. If needed as subagent, create thin agent in `.claude/agents/`:
```yaml
---
name: your-skill-agent
tools: [required tools]
color: cyan
---
Follow methodology in `.claude/skills/your-skill/SKILL.md`.
```

**Best Practices:**
- Skills contain the **full methodology** (HOW to do it)
- Agents are **thin** (tools + pointer to skill)
- Put ALL trigger conditions in the `description` field
- Keep under 500 lines in SKILL.md body

**Resources:**
- [Agent Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)

### Adding Custom Hooks

1. Create script in `.claude/hooks/`
2. Make executable: `chmod +x .claude/hooks/your_hook.py`
3. Add configuration to `.claude/settings.json`
4. Test with sample inputs

**Resources:**
- [Hooks Reference Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Hooks Implementation Guide](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AizenvoltPrime/claude-setup&type=Date)](https://star-history.com/#AizenvoltPrime/claude-setup&Date)

## License

This configuration setup is provided as-is for Claude Code enhancement.

---

**Need help?** Check the documentation:
- [Claude Code Main Docs](https://docs.anthropic.com/claude-code)
- [Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Hooks Implementation Guide](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)

Or open an issue for project-specific questions.
