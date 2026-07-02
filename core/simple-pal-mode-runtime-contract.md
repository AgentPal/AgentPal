# Legacy Conservative Pal Path Contract

Status: legacy compatibility reference only.

This file is not a current fresh-install runtime gate and must not be loaded as
the active AgentPal runtime contract. Current fresh installs use the v0.6
no-code Pal / Team orchestration gates listed in `core/agentpal-core-gate.md`.

## Legacy Conservative Patterns

- Fast Route for clear single-owner tasks
- Single Owner answer with immediate owner Pal response
- compact Task Package
- staged Task Package for composite deliverables

## Current Boundary

The legacy path remains useful as a fallback when a host cannot support a richer
no-code plan, but it does not override current v0.6 requirements:

- Team-first discovery for natural-language team requests.
- Owner Assignment Integrity for selected owners, participants, verifiers, Team
  roles, Runtime tools, Skills, plugins, and promised outputs.
- Pal / Team asset preflight.
- Workflow Execution Contract.
- Closure Gate.
- PalSmith ownership for durable Pal / Team Pack creation, repair, governance,
  roster design, and workflow package design.

## Runtime Boundary

Runtime can read files, write files, run commands, call tools, render outputs, and produce evidence when available and permitted.

Runtime is not a Pal. Runtime does not replace Pal identity, owner judgement, output contracts, or stage ownership.

When real execution happens, the active Pal reports which execution layer produced the evidence.
