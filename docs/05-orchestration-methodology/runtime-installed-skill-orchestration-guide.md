# Runtime-installed Skill Orchestration Guide

Runtime-installed Skill Orchestration is a no-code AgentPal method for naming host Runtime capability candidates inside a Task Package.

It helps a Pal say: "This task may benefit from a host Runtime Skill, plugin, MCP tool, browser tool, office-document tool, repository-analysis tool, or other installed capability. The current Runtime must confirm availability and execute it if allowed."

It does not make AgentPal a Runtime, tool caller, scanner, installer, validator, or automation layer.

## What A Runtime-installed Skill Is

A Runtime-installed Skill is a capability supplied by the host Runtime or its plugin/MCP/tool surface. Examples include:

- an office document Skill in a host agent;
- a browser inspection Skill;
- a repository analysis Skill;
- a plugin exposed by the host Runtime;
- an MCP tool made available by the host Runtime.

The Skill is installed, invoked, permissioned, and evidenced by the host Runtime. AgentPal may describe it as a candidate in a Task Package, but AgentPal does not own it.

## Runtime-installed Skill vs Pal-owned Skill

Pal-owned Skills are public no-code methods stored under a Pal Pack. They describe judgement, intake, context slicing, task packaging, verification, and learning behavior.

Runtime-installed Skills are host capabilities. They may perform file conversion, browsing, repository analysis, external data lookup, document rendering, or other execution-layer work when the Runtime supports them.

Keep them separate:

- `pal_owned_skills_used`: Pal methods used to prepare the package.
- `runtime_skill_candidates`: host Runtime capabilities that might execute or inspect something.
- `plugin_candidates`: host plugins that might be available.
- `mcp_tool_candidates`: host MCP tools that might be available.

Do not copy Runtime Skills into Pal Packs. Do not put Pal-owned Skills into runtime availability checks.

## How Deep Conductor Uses Capability Profiles

When a complex no-code plan needs capability awareness, Deep Conductor may read the smallest relevant profile slice:

- Runtime profiles;
- Skill profiles;
- plugin profiles;
- MCP profiles;
- Pal profiles when owner judgement needs them.

Profiles are judgement inputs. They do not prove that a Skill is installed in the current Runtime, and they do not create a fixed route.

## Pal Suggestion Pattern

A Pal may actively suggest Runtime Skill candidates when the task would benefit from a specialized host capability.

Example:

```text
Morgan: This document-output stage may benefit from an office-document Runtime Skill if the host Runtime has one. I will keep Morgan's Pal-owned document planning separate from the host Runtime Skill candidate, and the package will ask the Runtime to confirm availability before use.
```

The suggestion remains conditional until the host Runtime confirms availability and returns evidence.

## Standard Flow

1. Identify task need.
2. Check minimal capability profiles.
3. Ask Runtime to confirm availability if needed.
4. Generate a Runtime Skill-aware Task Package.
5. Host Runtime executes or reports unavailable.
6. Pal verifies returned evidence.
7. Write Runtime Skill Usage Memory when the result is useful and public/private boundaries allow it.

## Fallback When Unavailable

If the Runtime cannot confirm the Skill, the package must fall back to one of:

- an ordinary Runtime Task Package without the specialized Skill;
- a different host capability candidate;
- a user confirmation request to install, enable, or choose another Runtime;
- a blocked/not-run report when execution would be unsafe or impossible without the Skill.

Fallback is part of the package. It is not an afterthought.

## Risks

- Treating a profile as proof of installation.
- Treating a successful previous use as a hard rule.
- Mixing Pal-owned Skill learning with Runtime Skill availability.
- Letting a Runtime Skill output bypass Pal verification.
- Leaking private local paths, source material, or credentials into public examples or memory.
- Creating a keyword-to-Skill rule that bypasses AI judgement.

## Do Not Do

- AgentPal does not directly call Runtime Skills.
- AgentPal does not automatically scan local Runtime Skills.
- AgentPal does not install host Runtime Skills.
- AgentPal does not turn Skill candidates into fixed routes.
- AgentPal does not treat a success experience as a hard rule for next time.
- AgentPal does not claim execution without current Runtime evidence.
