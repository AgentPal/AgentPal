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

# Capability Layer

Capability cards describe what a Runtime, model, Skill, plugin, MCP, tool, or non-Pal runtime can do. They do not make that resource a Pal.

Morgan builds or refreshes capability cards before delegating real file work, especially batch operations and sensitive document handling.

## Source: skill-capability-matrix.md

# Skill Capability Matrix

| Skill | Runtime | Best for | Not suitable for | Trigger | Refresh rule | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| unknown | unknown | unknown | unknown | unknown | plugin scan | unknown |

## Source: task-routing-matrix.md

# Capability Consideration Matrix

This file is a capability reference, not a route map.

No hard-coded semantic routing. AI judgement is required case-by-case before selecting a runtime, Pal collaborator, model, or execution path.

| Situation | Possible planner capability | Possible executor capability | Review |
|---|---|---|---|
| File organization | document/file workflow capability | runtime with filesystem access candidate | evidence review; high-risk review may be considered |
| Document summary | document summary capability | document-capable runtime candidate | document evidence review |
| Spreadsheet cleaning | spreadsheet planning capability | spreadsheet-capable runtime candidate | human review for money/formulas |
| PDF extraction | PDF planning capability | PDF-capable runtime candidate | extraction evidence review |
| Software install issue | system/environment perspective may be considered | runtime candidate | evidence review |
| Code project folder cleanup | development perspective may be considered | runtime candidate | evidence review |



