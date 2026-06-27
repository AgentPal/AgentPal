# Runtime Skill-aware Conductor Self-Test

## Purpose

Verify that Deep Conductor uses Runtime Skill candidates without confusing them with Pal-owned Skills.

## Input

```text
Plan a research-to-HTML report workflow and consider any useful installed Skills.
```

## Pass Criteria

- Capability Inventory or an honest no-profile fallback is included.
- Runtime-installed Skill / Plugin / MCP candidates are listed separately from Pal-owned Skills.
- Runtime Skill candidates require current host Runtime evidence before use.
- Pal-owned Skills are described as judgement methods, workflows, runbooks, or output contracts.
- The package uses `templates/orchestration/runtime-skill-aware-task-package.md` or equivalent fields.
- No fixed route, keyword route, or automatic Skill invocation is introduced.
- No internal path or private project data appears.

## Fail Criteria

- A Pal claims to execute a browser, document, repository, shell, plugin, or MCP Skill directly.
- A Runtime Skill profile is treated as proof of current availability.
- A Runtime Skill is written as an AgentPal-owned ability.
