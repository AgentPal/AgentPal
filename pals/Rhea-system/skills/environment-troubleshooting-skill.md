# environment-troubleshooting

## Purpose

Turn environment failures into safe, staged, evidence-based troubleshooting plans.

## When to use

Use for missing commands, version mismatch, PATH issues, dependency failures, permission errors, runtime unavailability, network failures, or failing local tools.

## Inputs

Error text, goal, operating system, working directory, command attempted, tool versions if known, recent changes, and allowed diagnostics.

## Required context

Environment troubleshooting knowledge, runtime capability assessment, permission boundary review, and evidence review.

## Process

1. Summarize the symptom and task goal.
2. Identify likely failure classes.
3. Start with read-only diagnostics.
4. Avoid install or system changes until evidence supports them.
5. Define branching next steps based on results.
6. Define recovery and rollback needs.

## Output

Troubleshooting task package with read-only checks, risk level, decision points, evidence required, and follow-up gates.

## Quality bar

The plan must avoid "try random commands" and must separate diagnosis from repair.

## User confirmation points

Ask before installs, PATH changes, environment variable writes, service changes, or dependency upgrades.

## No-code boundary

This skill creates a troubleshooting plan only. Runtime performs approved checks.

## Common mistakes

- Jumping to reinstall.
- Ignoring working directory.
- Assuming the same fix works across runtimes.
- Claiming repair without rerun evidence.

## Example

For "pnpm not found", first request read-only evidence: command availability, PATH summary, package manager presence, and project package manager hints.

