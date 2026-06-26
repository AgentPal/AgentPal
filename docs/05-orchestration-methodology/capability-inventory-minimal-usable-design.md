# Capability Inventory Minimal Usable Design

Capability Inventory in v0.2 is a manual or maintainer-provided profile set. It is an input to AI judgement, not an automatic scanner and not a routing table.

## Minimal Profile Types

v0.2 uses three practical profile types:

- runtime profile: what a host runtime can probably read, write, run, and report;
- model profile: what a model is suitable for and what evidence supports that claim;
- Skill profile: what a Skill can help with, required tools, inputs, outputs, limits, and risks.

## Required Common Fields

Every profile should include:

- `schema`;
- `id`;
- `name`;
- `type`;
- `status`;
- `source`;
- `version`;
- `non_binding`;
- limits;
- risk notes;
- evidence required;
- profile note.

## Runtime Profile Minimum

Runtime profiles should answer:

- can it read files?
- can it write files?
- can it run commands?
- which instruction files can it read?
- can it access external directories?
- does it support Skills, plugins, or MCP?
- what evidence can it return?

Existing examples:

- `capabilities/runtime-profiles/codex.example.json`
- `capabilities/runtime-profiles/claude-code.example.json`
- `capabilities/runtime-profiles/generic-cli.example.json`

These examples are illustrative. They are not scans of the user's current environment.

## Model Profile Minimum

Model profiles should answer:

- where the model is available;
- strengths and limits;
- reasoning modes;
- default reasoning;
- cost and latency tier;
- evidence behind the profile.

Model profiles must not claim benchmark superiority unless a separate validated benchmark supports it.

## Skill Profile Minimum

Skill profiles should answer:

- what the Skill does;
- where it is available;
- required tools;
- inputs and outputs;
- limits and risks;
- evidence required when the Skill is used.

Skill profiles do not trigger execution by themselves.

## How Profiles Are Used

Mira or an owner Pal may use profiles when judging:

- whether a runtime can safely execute a Task Package;
- whether a model is suitable for a high-reasoning or low-risk step;
- whether a Skill is a candidate for a task.

Profiles must not become:

- keyword routing;
- fixed task/domain maps;
- proof that a tool is available in the current session;
- permission to skip evidence.

## v0.2 Boundary

Allowed:

- hand-written profiles;
- illustrative examples;
- profile templates;
- documentation that explains how to verify current availability.

Not allowed:

- automatic scanner;
- validator script;
- environment probe;
- hidden runtime discovery;
- fake profile data for a user's machine.

## Acceptance

Capability Inventory is minimally usable when a maintainer can fill a profile, a Pal can cite it as a non-binding judgement input, and the final answer still requires current runtime evidence before execution claims.
