---
name: agentpal-enable
description: Enable AgentPal thin binding in the current Codex project when the user says enable, install, connect, add, activate AgentPal, or add the AgentPal team.
---

# AgentPal Enable

Use this Skill to create or refresh the current project's AgentPal thin binding.
The Codex plugin is global; this Skill only connects the currently open project.

## Allowed Writes

Only write:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the AgentPal protected block in `AGENTS.md`

The protected block markers must be exactly:

```md
<!-- BEGIN AGENTPAL BINDING: codex -->
<!-- END AGENTPAL BINDING: codex -->
```

## Procedure

1. Treat the current working directory as the target project root unless the user gives a different project path.
2. Resolve the AgentPal source from the persistent install config first:
   `%USERPROFILE%\.agentpal\config.json`.
3. If the install config is present, use its `workspace_root` as
   `agentpal_workspace_root` and its `source` as the source URL.
4. If the install config is missing, fall back in this order: explicit user
   path, `AGENTPAL_HOME`, `AGENTPAL_SOURCE`, an ancestor AgentPal workspace,
   then the GitHub source fallback `https://github.com/AgentPal/AgentPal`.
5. If only a GitHub URL is available and no local workspace path is available,
   report that AgentPal is installed as a Codex plugin but the full local
   AgentPal workspace path is not configured; do not pretend full AgentPal
   source files were read.
6. Create or refresh `.agentpal/project.json` with a thin binding record.
7. Create or refresh `.agentpal/AGENTPAL.md` with the project binding
   instructions and boundary.
8. Insert or replace exactly one Codex AgentPal protected block in `AGENTS.md`.
9. Report changed files and the final binding status.

Do not ask for the AgentPal workspace path when the install config is valid.
The user should be able to say only "Add AgentPal to this project".

## Install Config

The standard install command writes this file:

```text
%USERPROFILE%\.agentpal\config.json
```

Expected shape:

```json
{
  "schema_version": "agentpal.install_config.v1",
  "workspace_root": "C:\\Users\\you\\.agentpal\\workspace",
  "installed_by": "codex",
  "source": "https://github.com/AgentPal/AgentPal.git",
  "installed_at": "2026-07-02T00:00:00.0000000Z"
}
```

Validate that `workspace_root` exists before writing it into the project
binding. If it does not exist, report `enabled_source_unknown_or_unavailable`
and ask the user to rerun the AgentPal Codex install document.

## Required Project JSON Fields

Use JSON with at least:

```json
{
  "schema_version": "agentpal.project_binding.v1",
  "binding_version": "1.0",
  "binding_type": "thin",
  "default_pal": "Mira",
  "runtime": "codex",
  "last_runtime": "codex",
  "enabled_runtimes": ["codex"],
  "agentpal_source_type": "install_config",
  "agentpal_source_detail": {
    "type": "install_config",
    "value": "C:\\Users\\you\\.agentpal\\workspace",
    "workspace_root": "C:\\Users\\you\\.agentpal\\workspace",
    "available": true
  },
  "agentpal_workspace_root": "C:\\Users\\you\\.agentpal\\workspace",
  "status": "enabled",
  "ordinary_messages_go_to": "Mira",
  "routing_policy": "ai_judgement_only",
  "keyword_routing_allowed": false,
  "allowed_project_binding_files": [
    ".agentpal/project.json",
    ".agentpal/AGENTPAL.md",
    "AGENTS.md codex runtime-qualified protected block"
  ],
  "forbidden_default_project_binding_dirs": [
    ".agentpal/memory",
    ".agentpal/state",
    ".agentpal/reports",
    ".agentpal/pals",
    ".agentpal/workflows",
    ".agentpal/evals"
  ]
}
```

Preserve existing compatible fields when refreshing the file, especially
non-Codex `enabled_runtimes`.

## Required AGENTS.md Block

Insert or replace the block bounded by:

```md
<!-- BEGIN AGENTPAL BINDING: codex -->
<!-- END AGENTPAL BINDING: codex -->
```

The block must say that this project is connected through a Codex thin binding,
that Codex should read `.agentpal/project.json` and `.agentpal/AGENTPAL.md`
before AgentPal-mode work, that Mira is the default entry Pal, and that owner
selection uses AI judgement rather than keyword routing.

## Boundary

The binding is thin. It does not copy full Pal assets, memory, reports, workflows,
evals, examples, release files, scanners, daemons, services, GUI assets,
databases, or sync state into the project.

## Acceptance Checks

After enabling, verify:

- `.agentpal/project.json` exists.
- `.agentpal/AGENTPAL.md` exists.
- `AGENTS.md` contains exactly one complete AgentPal protected block.
- Running enable a second time does not duplicate the protected block.
