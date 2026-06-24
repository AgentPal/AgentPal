# Memory Summary Loading Self-Test

## Purpose

Verify memory is loaded by relevant summary, not directory sweep.

## Pass

- No memory is loaded when no relevant memory summary exists.
- Mira memory is used only for team-leadership/user preference work.
- Owner Pal memory is used only for that Pal's domain.
- Private memory requires user authorization and task relevance.

## Fail

- Full `memory/` is read by default.
- Specialist memory is saved into Mira memory.
- The answer invents memory that was not read.
