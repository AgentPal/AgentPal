# Capability Reference

This embedded Pal capability reference is not a route map.

No hard-coded semantic routing. Owner selection, collaborator selection, runtime selection, and collaboration-shape decisions are made case-by-case by AI judgement from the current request, context, registered Pal ownership scopes, available assets, risk, and user constraints.

## Source: agent-capability-matrix.md

# Agent Capability Matrix

| Agent | Type | Best for | Not suitable for | Prompt style | Refresh rule | Last checked | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| unknown | unknown | unknown | unknown | unknown | before dispatch | YYYY-MM-DD | unknown |

## Source: model-capability-matrix.md

# Model Capability Matrix

| Model | Tier | Best for | Not suitable for | Prompt style | Refresh rule | Last checked | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| unknown | unknown | unknown | unknown | unknown | model change or key task | YYYY-MM-DD | unknown |

## Source: plugin-capability-matrix.md

# Plugin Capability Matrix

| Plugin/MCP | Runtime | Best for | Not suitable for | Permission notes | Refresh rule | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| unknown | unknown | unknown | unknown | unknown | config change | unknown |

## Source: README.md

# Capabilities

This directory records capability profiles for models, Skills, plugins, tools, runtime agents, and Pal contacts.

Nova uses capability profiles to route work responsibly:

- Product definition stays with Nova.
- Research questions may need a collaborator resolved from current contacts / registry.
- Development-oriented consultation may involve a collaborator resolved from current contacts / registry when the active owner judges it useful case-by-case.
- Real execution goes to the selected runtime or non-Pal runtime.

Capability records do not make an item a Pal contact.

## Source: skill-capability-matrix.md

# Skill Capability Matrix

| Skill | Runtime | Best for | Not suitable for | Trigger | Refresh rule | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| unknown | unknown | unknown | unknown | unknown | plugin scan | unknown |

## Source: task-routing-matrix.md

# Capability Consideration Matrix

This file is a capability reference, not a route map.

No hard-coded semantic routing. AI judgement is required case-by-case before selecting a runtime, Pal collaborator, model, or execution path.

| Situation | Possible capability to consider | Possible model | Strength | Useful Skills/Plugins | Prompt Detail |
| --- | --- | --- | --- | --- | --- |
| Architecture decision | strong reasoning or product/technical collaboration candidate | strongest | high | repo analysis | medium |
| Scoped implementation | coding runtime candidate | medium | medium | coding skills | high |
| UI smoke test | runtime with browser capability candidate | medium | medium | Playwright/MCP | high |
| Docs cleanup | bounded low-cost/current runtime candidate | low/medium | low | markdown | medium |
| Release verification | reliable evidence-producing runtime candidate | high | high | smoke/check scripts | high |



