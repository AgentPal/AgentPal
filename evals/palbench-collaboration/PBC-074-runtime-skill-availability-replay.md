# PBC-074 Runtime Skill Availability Replay

## User input

Replay a task that may use a host Runtime-installed Skill.

## Expected Context Packet

Runtime Skill-aware package with named Skill/plugin/MCP candidates, availability check, fallback, and verification requirements.

## Expected workflow

Check only named current-session candidates. Do not scan all host capabilities.

## Expected output

Availability result: `available`, `unavailable`, `unknown`, or `blocked`, plus fallback and verification notes.

## Failure modes

- treats Runtime Skill as Pal Skill;
- assumes availability from examples;
- no fallback;
- no verification of Skill output.

## Scoring rubric

- 0: capability is assumed or confused with Pal ownership.
- 1: availability is mentioned but fallback or verification is missing.
- 2: bounded availability check with fallback and evidence requirements.
