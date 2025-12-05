#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Stop Hook: Memory Update Prompt for Evolving Skills

## Purpose
Detects when investigation, tracing, or planning skills were used and prompts
the user to save learnings to the knowledge graph memory system.

## Trigger
Activates at end of conversation (Stop hook) when specific skill patterns are detected.

## Input (stdin JSON)
{
    "transcript": [
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
    ]
}

## Output (stdout JSON)
When skills detected:
{
    "continue": true,
    "stopReason": "end_turn",
    "decision": "block",
    "message": "💡 **Memory Update Opportunity**\n\nEvolving skills used: investigate, trace-flow\n..."
}

When no skills detected:
{
    "continue": true
}

## Detection Patterns
Searches transcript for keywords indicating skill usage:

**investigate**:
  - "investigation_report", "investigating", "found files", "hypothesis", "evidence"

**trace-flow**:
  - "flow_report", "tracing", "execution path", "data flow", "call chain"

**plan-implementation**:
  - "plan.md", "implementation plan", "steps to implement", "approach"

## Behavior
1. Reads conversation transcript from stdin
2. Searches for skill-specific keywords (case-insensitive)
3. If detected: Shows user-facing message with memory commands
4. If not detected: Passes through silently

## Message Format
Suggests memory commands:
- `memory create TYPE NAME "observation"` - Create new entity
- `memory add TYPE NAME "observation"` - Add to existing entity

Types: project, domain, pattern, flow, risk

## Exit Codes
0: Always (hook returns JSON, never blocks execution)

## Example Usage
After investigation session:
Claude creates INVESTIGATION_REPORT.md
Hook detects "investigation_report" in transcript
User sees: "💡 Memory Update Opportunity\nEvolving skills used: investigate\n..."
User can run: memory create pattern auth-flow "Uses JWT tokens with 15min expiry"
"""

import json
import sys
from typing import Literal, TypedDict


# Type definitions
class TranscriptMessage(TypedDict):
    """Single message in conversation transcript."""

    role: Literal["user", "assistant"]
    content: str


class HookInput(TypedDict):
    """Type-safe input from Claude Code Stop hook."""

    transcript: list[TranscriptMessage]


class HookOutput(TypedDict, total=False):
    """Type-safe output to Claude Code (total=False allows optional fields)."""

    continue_: bool  # Renamed to avoid Python keyword conflict
    stopReason: Literal["end_turn"]
    decision: Literal["block"]
    message: str


SkillName = Literal["investigate", "trace-flow", "plan-implementation"]


def detect_evolving_skill_usage(transcript: list[TranscriptMessage]) -> list[SkillName]:
    """Detect which evolving skills were likely used."""
    skills_used = []

    # Convert transcript to searchable string
    content = str(transcript).lower()

    # Detection patterns for each evolving skill
    patterns = {
        "investigate": [
            "investigation_report",
            "investigation report",
            "investigating",
            "found files",
            "related files",
            "hypothesis",
            "evidence",
        ],
        "trace-flow": [
            "flow_report",
            "flow report",
            "tracing",
            "execution path",
            "data flow",
            "call chain",
        ],
        "plan-implementation": [
            "plan.md",
            "implementation plan",
            "planning",
            "steps to implement",
            "approach",
        ],
    }

    for skill, keywords in patterns.items():
        if any(keyword in content for keyword in keywords):
            skills_used.append(skill)

    return skills_used


def main() -> Literal[0]:
    """Main hook execution logic. Always returns 0 (non-blocking)."""
    try:
        raw_data = json.loads(sys.stdin.read())
        input_data: HookInput = HookInput(transcript=raw_data.get("transcript", []))
    except json.JSONDecodeError:
        # No input or invalid JSON - continue without prompt
        output: HookOutput = {"continue_": True}
        print(json.dumps({"continue": output["continue_"]}))
        return 0

    skills_used = detect_evolving_skill_usage(input_data["transcript"])

    if skills_used:
        skills_list = ", ".join(skills_used)
        result: HookOutput = {
            "continue_": True,
            "stopReason": "end_turn",
            "decision": "block",  # This will show message to user
            "message": f"""
💡 **Memory Update Opportunity**

Evolving skills used: {skills_list}

Consider saving learnings with:
- `memory create TYPE NAME "observation"` - Create new knowledge entity
- `memory add TYPE NAME "observation"` - Add to existing entity

Types: project, domain, pattern, flow, risk

Or say "update memory" to review and save discoveries.

To skip: just continue with your next request.
""",
        }
        print(
            json.dumps(
                {
                    "continue": result["continue_"],
                    "stopReason": result["stopReason"],
                    "decision": result["decision"],
                    "message": result["message"],
                }
            )
        )
    else:
        print(json.dumps({"continue": True}))

    return 0


if __name__ == "__main__":
    sys.exit(main())
