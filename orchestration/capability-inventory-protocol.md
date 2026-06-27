# Capability Inventory Protocol

Capability Inventory describes what the current AgentPal environment may be able to use. It is a set of profiles, not a hard-coded routing system.

AgentPal v0.1.0-rc.1 does not automatically probe runtimes, models, Skills, plugins, MCP servers, or external agents. In v0.2, Capability Inventory remains manual or maintainer-provided. Profiles are illustrative unless a user or maintainer explicitly marks them as maintained for a specific environment.

## Purpose

Capability Inventory helps Mira or an owner Pal judge:

- which runtime may fit the task
- which model profile may fit the task
- which reasoning strength may be sufficient
- which Skill, plugin, or MCP server may help
- which Pal profile may own, consult, or verify
- which capabilities require user approval or execution-layer evidence

These profiles are judgement inputs only. They do not replace AI Judgement and must not become keyword-based dispatch rules or fixed task-domain routes.

Runtime Skill, plugin, and MCP profiles do not prove current installation. When a task may use one of them, follow `orchestration/runtime-skill-candidate-decision-protocol.md` and ask the host Runtime for current availability evidence.

## Profile Types

| Profile | Purpose |
| --- | --- |
| Runtime Profile | What a runtime can read, write, execute, configure, and report |
| Model Profile | Strengths, known limits, cost/latency tier, compatible runtimes |
| Reasoning Profile | When low, medium, high, or deep reasoning may be useful |
| Skill Profile | What a Skill does, required tools, risk, expected output |
| Plugin Profile | Plugin capabilities, permissions, and evidence needs |
| MCP Profile | MCP tools/resources exposed, access boundary, risk |
| Pal Capability Profile | Pal identity, output contract, context needs, verification role candidates |

## Profile Source

Profiles may be maintained by:

- user-provided configuration
- Pal-authored notes
- maintainer examples
- future runtime probes
- future routing memory updates

v0.2 ships templates and illustrative examples. It does not claim to know a user's installed runtime capabilities.

## Required Profile Fields

Every profile should include:

- `schema`
- `id`
- `name`
- `type`
- `example_status` or `status`
- `not_auto_detected`
- `used_for`
- `source`
- `version`
- `capabilities`
- `limits`
- `risk_notes`
- `evidence_required`
- `not_a_fixed_route`

## Use In Judgement

Mira or an owner Pal may use profiles as follows:

1. Read current contacts / registry.
2. Read task goal and constraints.
3. Perform Task Judgement before selecting profile files.
4. Decide whether a profile would materially improve the judgement.
5. Read only the relevant capability index or the smallest relevant profile.
6. Select candidate capabilities.
7. Produce a Task Package or Context Access List when execution or bounded context is needed.
8. Record outcome later only through a manual, public-safe process when appropriate.

Profile loading follows Context Slicing. Do not read all profiles by default.

## Forbidden Use

Do not use Capability Inventory to create:

- task/domain route tables
- keyword-based dispatch rules
- fixed Pal sets
- fixed runtime choices
- fixed model choices
- automatic Skill/plugin/MCP calls
- automatic local Skill scans
- hidden external Agent calls

## Future Versions

v0.2 may add manually refreshed capability inventory and Markdown self-tests.

v0.3 may add richer probes, routing memory feedback, and PalBench-driven profile tuning.
