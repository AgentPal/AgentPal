# Pal Skill vs Agent Skill Standard

Date: 2026-06-28
Standard id: `agentpal-pal-skill-vs-agent-skill.v0.5`

## Purpose

This standard prevents role-level Pal capabilities from being confused with
runtime tool-level Agent Skills.

## Agent Skill

An Agent Skill is an execution capability for a host runtime. It explains how
the runtime performs a concrete action or uses a concrete tool.

Agent Skills may cover:

- file parsing or generation
- browser control
- spreadsheet or document handling
- CLI usage
- external tool operation
- API calling under a host runtime's permission model
- failure modes and command-level recovery

Agent Skills belong in the host runtime's skill registry, plugin system, tool
documentation, or an explicit runtime capability reference. They are not Pal
identity assets.

## Pal Skill

A Pal Skill is a Pal-owned role-level work capability. It explains how the Pal
organizes a class of work.

A Pal Skill should include:

- purpose
- activation and non-activation conditions
- required context
- knowledge references
- workflow references
- runbook references
- Agent Skill references
- external tool references
- collaboration boundaries
- approval rules
- output contract
- verification rules
- report and memory writeback rules
- examples

Pal `skills/` defaults to this kind of Pal Skill.

## Comparison

| Dimension | Agent Skill | Pal Skill |
| --- | --- | --- |
| Layer | Runtime execution layer | Pal role / organization layer |
| Primary user | Host Agent Runtime | Pal and AgentPal organization |
| Goal | Perform a concrete action well | Organize a class of work well |
| Typical content | tool steps, commands, APIs, limits, failure handling | judgement, context, knowledge, workflows, tools, collaboration, verification |
| Example | use a browser automation tool | run a website release readiness review |
| Example | edit a spreadsheet file | prepare an operations dashboard review |
| Example | call a GitHub CLI command | coordinate a release publication package |
| Storage | runtime skill registry or tool reference | Pal Pack `skills/` |
| Evidence | command/tool result | task package, output contract, verification record, report |

## What Belongs In Pal `skills/`

Pal `skills/` should contain Pal Skills that help the Pal repeatedly organize a
class of work. A Pal Skill may reference Agent Skills, workflows, runbooks, and
tools, but the Pal Skill remains the organizational method.

Recommended Pal Skill structure:

```text
skills/<pal-skill-id>/
  SKILL.md
  required-context.md
  knowledge-refs.md
  workflow-refs.md
  agent-skill-refs.md
  tool-refs.md
  collaboration.md
  approval-rules.md
  output-contract.md
  verification.md
  memory-writeback.md
  examples.md
```

Flat single-file Pal Skills are acceptable when they include the same
responsibilities in a compact form.

## Runtime Skill Registry References

When a Pal Skill needs a runtime Agent Skill, it should reference it as an
execution candidate, for example:

```yaml
agent_skill_refs:
  - browser-control
  - spreadsheet-processing
  - github-cli
tool_refs:
  - gh
  - playwright
runtime_boundary:
  execution_requires_current_runtime_evidence: true
```

The reference does not install, enable, probe, or execute the Agent Skill by
itself.

## How Pal Skills Reference Agent Skills

A Pal Skill may say:

- which Agent Skills could help
- what evidence is required before claiming execution
- what files or systems may be read or written
- when human approval is required
- how the Pal will verify the runtime result

A Pal Skill must preserve `unknown`, `missing`, `not-run`, and `blocked` when
runtime evidence is absent.

## Forbidden

Do not:

- Treat an Agent Skill as a Pal Skill.
- Put raw CLI usage or API usage directly into Pal `skills/` as the whole
  capability.
- Claim that a Pal Skill executes commands, calls APIs, or changes systems by
  itself.
- Route user requests to Pal Skills by keyword.
- Use `keyword_map`, `domain_map`, `role_map`, or deterministic task-to-Pal
  tables.
- Copy runtime Agent Skill files into Pal `skills/` unless they are rewritten as
  Pal-owned role-level methods with clear runtime references.
