#!/usr/bin/env python3
"""
Stop hook that prompts for memory updates after evolving skills are used.

Triggers when:
- Investigation, tracing, or planning activities detected
- Patterns or learnings discovered
- Reports generated
"""

import json
import sys


def detect_evolving_skill_usage(transcript: list) -> list[str]:
    """Detect which evolving skills were likely used."""
    skills_used = []

    # Convert transcript to searchable string
    content = str(transcript).lower()

    # Detection patterns for each evolving skill
    patterns = {
        "investigate": [
            "investigation_report", "investigation report",
            "investigating", "found files", "related files",
            "hypothesis", "evidence"
        ],
        "trace-flow": [
            "flow_report", "flow report", "tracing",
            "execution path", "data flow", "call chain"
        ],
        "plan-implementation": [
            "plan.md", "implementation plan", "planning",
            "steps to implement", "approach"
        ]
    }

    for skill, keywords in patterns.items():
        if any(keyword in content for keyword in keywords):
            skills_used.append(skill)

    return skills_used


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        # No input or invalid JSON - continue without prompt
        print(json.dumps({"continue": True}))
        return

    transcript = input_data.get("transcript", [])
    skills_used = detect_evolving_skill_usage(transcript)

    if skills_used:
        skills_list = ", ".join(skills_used)
        result = {
            "continue": True,
            "stopReason": "end_turn",
            "decision": "block",  # This will show message to user
            "message": f"""
💡 **Memory Update Opportunity**

Evolving skills used: {skills_list}

Consider saving learnings with:
- `mcp__memory__create_entities` - Create new knowledge nodes
- `mcp__memory__add_observations` - Add patterns/learnings to existing nodes

Or say "update memory" to review and save discoveries.

To skip: just continue with your next request.
"""
        }
    else:
        result = {"continue": True}

    print(json.dumps(result))


if __name__ == "__main__":
    main()
