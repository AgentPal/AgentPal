# runtime-capability-assessment

## Purpose

Assess what the current Runtime can safely do, what evidence is available, what permissions are needed, and what must be marked not-run.

## When to use

Use before any task that depends on local commands, file reads or writes, package managers, external tools, system state, browser access, network access, or project workspace access.

## Inputs

User goal, requested action, current Runtime name if known, available tool list if known, workspace path, allowed actions, forbidden actions, and expected evidence.

## Required context

Rhea role boundary, Runtime evidence rules, current AgentPal no-code boundary, and relevant project or Pal asset scope.

## Process

1. Identify the requested capability: read, write, command, network, browser, install, delete, move, system setting, release action, or external connector.
2. Identify whether the Runtime actually exposes that capability.
3. Separate Pal-layer planning from Runtime execution.
4. Mark unknown capability as unknown until inspected.
5. Define evidence required before any completion claim.
6. Mark unsafe or unavailable actions as blocked or not-run.

## Output

Runtime capability assessment with capability, evidence source, risk level, allowed/forbidden actions, approval needs, and not-run items.

## Quality bar

The assessment must not claim capability or execution unless current Runtime evidence proves it.

## User confirmation points

Ask before file writes, destructive actions, privileged operations, external network actions involving sensitive data, installs, or system setting changes.

## No-code boundary

This skill creates a safety assessment only. It does not add code, CLI, scanner, validation tooling, installer, daemon, or UI to AgentPal.

## Common mistakes

- Assuming a Runtime can run a command because another Runtime can.
- Treating a plan as execution.
- Omitting not-run items.
- Ignoring filesystem boundary.

## Example

Input: "Check if release is safe." Output: "Runtime can read files and run git checks. Package installation is not needed. Evidence required: no-code scan result, JSON parse result, diff check, and status summary."

