# Skills Index

## Purpose

This directory lists Pal Skills owned by `[Pal name]`.

Pal Skills are role-level work capabilities. They help the Pal organize recurring work through context, judgement, approval rules, output contracts, verification, and memory or learning writeback.

## What Belongs Here

- Pal-owned methods for recurring work.
- Skill packages or single-file Skills with purpose, activation conditions, required context, output contract, verification, and writeback rules.
- References to related knowledge, workflows, runbooks, examples, and evals.
- References to Agent / Runtime Skill candidates when the Pal Skill may need host-runtime execution.

## What Does Not Belong Here

- Agent Skills, Runtime Skills, plugins, MCP tools, or tool installation files.
- Raw CLI command docs copied as the whole Skill.
- API client docs, connector configs, scanner configs, validator logic, or daemon instructions.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic dispatch tables.
- Reports, memory records, raw research dumps, private credentials, tokens, or secrets.

Raw CLI command docs should not be stored as a Pal Skill unless rewritten as a Pal-owned method with context, approval, runtime boundary, verification, and memory writeback rules.

Agent Skills should be referenced, not stored here.

## Current Assets

| Asset | Purpose | Status | Notes |
| --- | --- | --- | --- |
| `[asset path]` | `[short purpose]` | `present` | `[public-safe note]` |

## Candidate Assets

| Candidate | Reason | Review status |
| --- | --- | --- |
| `[candidate skill]` | `[why it may become a Pal Skill]` | `needs-review` |

## Review Notes

- Check that every item is a Pal Skill, not a Runtime / Agent Skill.
- Check that command or tool references are evidence candidates for the host Runtime only.
- Mark uncertain items as `unknown` instead of promoting them.

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`

## Public Safety Boundary

Do not store credentials, tokens, secrets, private user material, customer data, or private runtime evidence in this index.

## External Project Boundary

This index belongs in a Pal Pack in the AgentPal central workspace or approved central record. Do not write Pal Skills into an external project `.agentpal/` directory by default.
