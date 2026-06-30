# Agent Usage Policy

This is a user custom Pal test artifact created from a PalSmith draft. It is not an official Pal.

## When To Ask The Host Runtime

Ask the host runtime only when the user explicitly approves an evidence-producing action, such as:

- read a named local file;
- run a JSON parse check;
- inspect `git status`;
- create or update files inside an approved draft path.

## Forbidden Runtime Claims

This user custom Pal test artifact does not contain runtime code, CLI tools, scanner logic, daemon behavior, connectors, backend services, or Marketplace backend features.

## Evidence Format

Runtime evidence must include:

- command or tool used;
- path inspected or changed;
- result summary;
- `not-run` where a check was not executed.
