#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
UserPromptSubmit Hook: Task Medium Directory Preparation

## Purpose
Automatically creates isolated directory instances for task_medium workflow sessions.
Each instance gets a unique ID and dedicated workspace for investigation reports.

## Trigger
Activates when user prompt starts with: /task_medium

## Input (stdin JSON)
{
    "prompt": "/task_medium [problem description]",
    "cwd": "/path/to/project"
}

## Output (stdout)
Text message injected into prompt context, informing Claude about the created directory:
"Directory claude-instance-{id} has been automatically created for this task session..."

## Behavior
1. Detects /task_medium prefix in user prompt
2. Scans claude-code-storage/ for existing claude-instance-* directories
3. Generates next available instance ID (incrementing)
4. Creates: claude-code-storage/claude-instance-{id}/
5. Injects context message with instance path and problem description

## Directory Structure Created
claude-code-storage/
├── claude-instance-1/    # First session
│   ├── INVESTIGATION_REPORT.md
│   ├── FLOW_REPORT.md
│   └── PLAN.md
├── claude-instance-2/    # Second session
└── claude-instance-3/    # Third session

## Exit Codes
0: Always (non-blocking hook - failures print warnings but don't abort)

## Example Usage
User types: "/task_medium Debug authentication timeout"
Hook creates: claude-code-storage/claude-instance-5/
Claude receives: "Directory claude-instance-5 has been automatically created...
                  Problem to solve: Debug authentication timeout"
"""

import json
import os
import sys
import re
from pathlib import Path
from typing import Literal, TypedDict


# Input/Output type definitions
class HookInput(TypedDict):
    """Type-safe input from Claude Code UserPromptSubmit hook."""

    prompt: str
    cwd: str


class DirectoryResult(TypedDict):
    """Type-safe result from directory creation."""

    success: bool
    path: str
    error: str | None


def get_next_instance_id(base_dir: Path) -> int:
    """Find the next available instance ID by checking existing directories."""
    if not base_dir.exists():
        return 1

    existing_dirs = [
        d
        for d in base_dir.iterdir()
        if d.is_dir() and d.name.startswith("claude-instance-")
    ]

    if not existing_dirs:
        return 1

    # Extract numbers from directory names
    numbers = []
    for dir_path in existing_dirs:
        match = re.search(r"claude-instance-(\d+)", dir_path.name)
        if match:
            numbers.append(int(match.group(1)))

    return max(numbers) + 1 if numbers else 1


def create_instance_directory(cwd: str, instance_id: int) -> DirectoryResult:
    """Create the claude-instance directory and return type-safe result."""
    try:
        base_dir = Path(cwd) / "claude-code-storage"
        instance_dir = base_dir / f"claude-instance-{instance_id}"

        # Create directories with proper permissions
        base_dir.mkdir(exist_ok=True)
        instance_dir.mkdir(exist_ok=True)

        return DirectoryResult(success=True, path=str(instance_dir), error=None)
    except Exception as e:
        return DirectoryResult(success=False, path="", error=str(e))


def validate_prompt(prompt: str) -> bool:
    """Check if prompt starts with /task_medium and requires directory setup."""
    # Strip whitespace and check for /task_medium at the start
    cleaned_prompt = prompt.strip()
    return cleaned_prompt.startswith("/task_medium")


def main() -> Literal[0]:
    """Main hook execution logic. Always returns 0 (non-blocking)."""
    try:
        # Read JSON input from stdin
        raw_data = json.load(sys.stdin)
        input_data: HookInput = HookInput(
            prompt=raw_data.get("prompt", ""), cwd=raw_data.get("cwd", os.getcwd())
        )
    except json.JSONDecodeError:
        # Not a JSON input, exit silently
        return 0

    # Check if this is a task_medium prompt
    if not validate_prompt(input_data["prompt"]):
        # Not a task_medium prompt, exit silently to allow normal processing
        return 0

    # Get next instance ID
    base_dir = Path(input_data["cwd"]) / "claude-code-storage"
    instance_id = get_next_instance_id(base_dir)

    # Create instance directory
    result = create_instance_directory(input_data["cwd"], instance_id)

    if result["success"]:
        # Extract the original problem from the prompt (after /task_medium)
        problem_text = input_data["prompt"].replace("/task_medium", "").strip()

        # Output context message that will be added to the prompt
        context_msg = f"Directory claude-instance-{instance_id} has been automatically created for this task session. The subagents must create the INVESTIGATION_REPORT.md, FLOW_REPORT.md and PLAN.md files inside claude-code-storage/claude-instance-{instance_id}/."
        if problem_text:
            context_msg += f" Problem to solve: {problem_text}"

        print(context_msg)
    else:
        # Output error but don't block processing
        print(
            f"Warning: Failed to create instance directory: {result['error']}",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
