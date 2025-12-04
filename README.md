# Claude Code Setup

> A comprehensive configuration setup for Claude Code with Model Context Protocol (MCP) servers, custom commands, and automated workflows.

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

- **MCP Servers**: Context7, Puppeteer, Sequential Thinking, DeepWiki
- **Custom Commands**: Intelligent workflows for commits, tasks, and problem-solving
- **Hook System**: Automated directory management and workflow triggers
- **Structured Workflows**: Organized task management with reporting and planning

## Quick Start

```bash
# 1. Install dependencies
pip install uv

# 2. Clone this configuration
git clone <your-repo> claude-setup
cd claude-setup

# 3. Start using commands
/task_medium implement user authentication
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

# Ensure hook permissions
chmod +x .claude/hooks/task_medium_prep_hook.py
```

## Features

### 🎯 Custom Commands (User-Invoked)
- **`/commit`**: Intelligent commit workflow with conventional standards
- **`/code-review`**: Reviews uncommitted changes before committing
- **`/task_medium`**: Advanced problem-solving with automated directory management
- **`/task_easy`**: Simplified task workflow for lighter needs

### 🧠 Skills (Full Methodology - Single Source of Truth)
Skills contain complete methodologies and auto-trigger based on context.

#### Evolving Skills (With Memory - CONTEXT.yaml)
These skills learn and adapt to your specific project:
- **`investigate`**: Scientific investigation using hypothesis testing. Learns project structure, common patterns.
- **`trace-flow`**: Execution/data flow tracing with verification phase. Learns architectural patterns.
- **`plan-implementation`**: Planning with validation checkpoints. Learns estimation accuracy, risk patterns.
- **`memory-management`**: Meta-skill for managing CONTEXT.yaml lifecycle across evolving skills.

#### Static Skills (Universal Methodology)
These skills use universal methods that don't change per project:
- **`task-decomposition`**: Systematic task breakdown (functional, layer, workflow, risk-based strategies)
- **`hypothesis-testing`**: Scientific debugging method (Observe → Hypothesize → Predict → Test → Analyze)
- **`decision-making`**: Technical choice framework with evaluation matrices and ADR format
- **`verification`**: Confirm changes work (unit, integration, system, regression levels)
- **`review-quality`**: Comprehensive review checklist (correctness, security, maintainability, performance)
- **`skill-creator`**: Meta-skill for creating new skills following Anthropic best practices

### 🤖 Agents (Thin Runtime Config)
Agents are lightweight wrappers that reference skills for their methodology:
- **`investigator`**: Runs investigate skill with restricted tools → INVESTIGATION_REPORT.md
- **`code-flow-mapper`**: Runs trace-flow skill → FLOW_REPORT.md
- **`planner`**: Runs plan-implementation skill → PLAN.md
- **`code-reviewer`**: Runs review-quality skill with prioritized feedback

### 🔌 MCP Servers
- **Context7**: Library documentation and code context
- **Puppeteer**: Browser automation and web scraping  
- **Sequential Thinking**: Advanced reasoning and problem-solving
- **DeepWiki**: Repository documentation fetching

### ⚡ Hook System
- **UserPromptSubmit**: Automatic directory creation for task workflows
- **Extensible**: Easy to add custom hooks for workflow automation
- **Documentation**: [Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks) | [Hooks Guide](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)

## Commands

### `/task_medium` - Advanced Problem Solving

Automated workflow for complex problem-solving with structured investigation and planning.

**Usage:**
```bash
/task_medium [problem description]
```

**Features:**
- ✅ Automatic `claude-instance-{id}` directory creation
- ✅ Sequential thinking for complex reasoning
- ✅ Multi-agent workflow with specialized subagents
- ✅ Codebase investigation with INVESTIGATION_REPORT.md generation
- ✅ Code flow mapping with FLOW_REPORT.md analysis
- ✅ Structured planning with PLAN.md output
- ✅ Incremental instance numbering
- ✅ Edge case handling and best practices focus

**Example:**
```bash
/task_medium implement user authentication system
```

**Workflow:**
1. 🔧 Hook detects `/task_medium` prompt
2. 📁 Creates `claude-code-storage/claude-instance-{id}/` directory
3. 🔍 Investigator agent analyzes codebase using sequential thinking
4. 📄 Generates comprehensive INVESTIGATION_REPORT.md with related files
5. 🗺️ Code-flow-mapper agent traces execution paths and file interconnections
6. 📊 Generates detailed FLOW_REPORT.md with code relationships
7. 📋 Planner agent reads both reports and creates comprehensive PLAN.md
8. 👤 User reviews and approves plan

### `/code-review` - Automated Code Review

Initiates code-reviewer agent to analyze uncommitted changes only.

**Usage:**
```bash
/code-review
```

**Features:**
- Focuses exclusively on uncommitted changes
- Reviews modified files for quality, security, and maintainability
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

### `/task_easy` - Simplified Tasks

Lightweight task workflow for simpler problem-solving needs.

## Configuration

### Directory Structure

```
claude-setup/
├── .claude/
│   ├── settings.json          # Permissions and hook configuration
│   ├── skills/                # FULL methodology (single source of truth)
│   │   ├── investigate/       # EVOLVING - Scientific investigation
│   │   │   ├── SKILL.md       # Hypothesis-testing methodology
│   │   │   └── CONTEXT.yaml   # Project-specific patterns learned
│   │   ├── trace-flow/        # EVOLVING - Code flow tracing
│   │   │   ├── SKILL.md       # Flow tracing + verification
│   │   │   └── CONTEXT.yaml   # Architectural patterns learned
│   │   ├── plan-implementation/ # EVOLVING - Implementation planning
│   │   │   ├── SKILL.md       # Planning + validation checkpoints
│   │   │   └── CONTEXT.yaml   # Estimation calibration, risk patterns
│   │   ├── memory-management/ # Meta-skill for CONTEXT.yaml lifecycle
│   │   ├── task-decomposition/ # Systematic task breakdown
│   │   ├── hypothesis-testing/ # Scientific debugging method
│   │   ├── decision-making/   # Technical choice framework
│   │   ├── verification/      # Confirm changes work
│   │   ├── review-quality/    # Comprehensive review checklist
│   │   └── skill-creator/     # Meta-skill for creating skills
│   ├── agents/                # THIN runtime config (tools + skill pointer)
│   │   ├── investigator.md    # → uses investigate skill
│   │   ├── code-flow-mapper.md # → uses trace-flow skill
│   │   ├── planner.md         # → uses plan-implementation skill
│   │   └── code-reviewer.md   # → uses review-quality skill
│   ├── commands/              # Explicit orchestration
│   │   ├── task_medium.md     # Chains: investigator → flow-mapper → planner
│   │   ├── task_easy.md       # Simple task workflow
│   │   ├── code-review.md     # Explicit review trigger
│   │   └── commit.md          # Commit workflow
│   └── hooks/
│       └── task_medium_prep_hook.py  # Auto directory creation
├── .mcp.json                  # MCP server configuration
├── claude-code-storage/       # Auto-generated task directories
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
- **Commands**: Explicit multi-agent orchestration (e.g., /task_medium chains 3 agents)

### Memory Architecture (CONTEXT.yaml)

Evolving skills use a tiered memory system stored in CONTEXT.yaml:

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTEXT.yaml                              │
├─────────────────────────────────────────────────────────────┤
│  core:     ← Always loaded (highest value patterns)         │
│    - "Entry points in src/routes/"                          │
│    - "Tests use Jest + testing-library"                     │
├─────────────────────────────────────────────────────────────┤
│  domain:   ← Loaded when context matches                    │
│    auth:                                                     │
│      - "Auth middleware in src/middleware/"                 │
│    database:                                                 │
│      - "Prisma schema in prisma/schema.prisma"             │
├─────────────────────────────────────────────────────────────┤
│  archive:  ← Searchable but not auto-loaded                 │
│    - "Legacy /old folder - rarely relevant"                 │
└─────────────────────────────────────────────────────────────┘
```

**Entry Types:**
- `pattern`: Recurring code structure or architectural convention
- `learning`: Discovery about how something works
- `gotcha`: Non-obvious behavior or common mistake
- `decision`: Past technical decision with rationale
- `flow`: Documented execution path

**Memory Lifecycle:** Add → Update (confidence) → Promote/Demote → Prune → Consolidate

### Settings Configuration

The `.claude/settings.json` file contains:

```json
{
  "permissions": {
    "allow": ["WebFetch(domain:docs.anthropic.com)", ...],
    "deny": [...]
  },
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/task_medium_prep_hook.py"
          }
        ]
      }
    ]
  },
  "enabledMcpjsonServers": ["context7", "puppeteer", "sequential-thinking", ...]
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
    }
  }
}
```

## Troubleshooting

### Common Issues

**Hook not triggering:**
- Ensure `uv` is installed and in PATH
- Check script permissions: `chmod +x .claude/hooks/task_medium_prep_hook.py`
- Verify hook configuration in `.claude/settings.json`

**Directory creation fails:**
- Check file system permissions
- Ensure `claude-code-storage/` parent directory exists
- Review hook script logs for error details

**MCP servers not loading:**
- Verify Node.js and npx are installed
- Check `.mcp.json` configuration syntax
- Ensure MCP packages are available via npx

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
- Under 500 lines in SKILL.md body

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