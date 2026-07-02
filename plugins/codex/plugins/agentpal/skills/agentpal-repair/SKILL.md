---
name: agentpal-repair
description: Repair a damaged or incomplete AgentPal thin binding in the current Codex project without duplicating AGENTS.md blocks or overwriting user content.
---

# AgentPal Repair

Use this Skill to repair a current project binding that is missing some
AgentPal thin binding files.

## Allowed Writes

Only write or restore:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the AgentPal protected block in `AGENTS.md`

## Procedure

1. Treat the current working directory as the target project root unless the user gives a different project path.
2. Inspect `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and `AGENTS.md`
   to determine the repair state.
3. Resolve the AgentPal source from `%USERPROFILE%\.agentpal\config.json`
   first. If that file is missing or points to an unavailable workspace,
   report the missing install config and ask the user to rerun the GitHub
   install command.
4. Recreate or refresh only missing or damaged thin-binding files.
5. Ensure `AGENTS.md` has exactly one Codex protected block and preserve
   user-authored content outside that block.
6. Treat the binding as damaged if `.agentpal/AGENTPAL.md`, `.agentpal/project.json`,
   or the Codex protected block still presents legacy active semantics such as
   "Current active mode: Simple Pal Mode only", `active_mode: "Simple Pal Mode"`,
   "Current v0.1 patterns", or "Current v0.1 output".
7. Refresh damaged binding text to the current v0.6 anchors:
   Team Pack first discovery, PalSmith as owner for durable Team Pack / compound
   team / reusable team / governance / repair / roster / workflow package work,
   Mira as intake-discovery-handoff-summary only for PalSmith-owned durable asset
   bodies, Team label not participant, `open_role` not contributor output, Owner
   Assignment Integrity, Workflow Execution Contract, and Closure Gate.
8. After repair, verify `.agentpal/project.json`,
   `.agentpal/AGENTPAL.md`, and the `AGENTS.md` protected block.
9. Report `status_before`, `status_after`, and changed files.

## Boundary

Repair restores a thin binding only. It does not copy full Pal assets, create
keyword routing, start services, create scanners, create databases, or start
background sync.
