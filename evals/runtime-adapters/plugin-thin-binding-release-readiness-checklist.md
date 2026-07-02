# Plugin Thin Binding Release Readiness Checklist

## Status

Current for AgentPal plugin release-readiness review.

This checklist is a manual release gate for the Codex AgentPal plugin and the Claude Code AgentPal project binder. It checks whether both adapters still behave as thin project bindings.

## Scope

Review these surfaces:

- `plugins/codex/agentpal-codex-plugin/`
- `integrations/claude-code/agentpal-project-binder/`
- `docs/04-runtime-guides/project-thin-binding.md`
- `standards/project-binding/`
- `templates/project-binding/`
- `evals/runtime-adapters/plugin-enable-disable-smoke-test.py`

Do not use this checklist to approve tags, GitHub Releases, background services, installers, or runtime orchestration.

## Required Smoke Command

Run from the AgentPal workspace root:

```bash
python evals/runtime-adapters/plugin-enable-disable-smoke-test.py
```

Expected result:

- all tests pass;
- temporary project directories are cleaned up by the test runner;
- no central Pal assets are modified.

## Thin Binding Boundary

Pass only if both adapters still create or update project-local binding files only:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- `AGENTS.md` protected block for Codex-style binding
- `CLAUDE.md` protected block for Claude Code binding

Fail if either adapter creates or requires:

- background services, daemons, scanners, validators, installers, databases, accounts, sync systems, or GUI managers;
- project-local copies of official Pal Packs, contacts, registry bodies, memory, state, reports, workflows, evals, examples, release notes, or PalBench records;
- hard-coded keyword routing or fixed domain-to-Pal route tables.

## Enable / Repair

Pass only if enable and repair are idempotent:

- repeated enable does not duplicate protected blocks;
- repair restores missing `.agentpal/project.json`;
- repair restores missing `.agentpal/AGENTPAL.md`;
- repair restores the current runtime's missing protected block;
- repair preserves user-authored content outside protected blocks.

## Disable

Pass only if disable is runtime-safe:

- removing the Codex binding removes only the `AGENTS.md` AgentPal block and Codex runtime entry;
- removing the Claude Code binding removes only the `CLAUDE.md` AgentPal block and Claude runtime entry;
- user-authored `AGENTS.md` and `CLAUDE.md` content remains;
- shared `.agentpal/` metadata is kept when another runtime binding is still present;
- central AgentPal workspace files are never deleted.

## Status

Pass only if status is read-only and reports missing or damaged binding artifacts honestly.

Codex status should distinguish at least:

- `not_enabled`
- `enabled_complete`
- `enabled_missing_project_json`
- `enabled_missing_agents_protected_block`
- `enabled_source_unknown_or_unavailable`
- `enabled_incomplete`

Claude Code status should distinguish at least:

- `unbound`
- `complete`
- `partial`
- `damaged`
- `legacy-block`

## Protocol Alignment Watch Items

These items are release-blocking if the target release claims full canonical project-thin-binding alignment:

- `project.json` new writes include the canonical required fields from `docs/04-runtime-guides/project-thin-binding.md`.
- `enabled_runtimes` and `last_runtime` are maintained when Codex and Claude Code bindings coexist.
- New protected blocks use the canonical runtime-qualified markers:
  - `<!-- BEGIN AGENTPAL BINDING: codex -->` / `<!-- END AGENTPAL BINDING: codex -->`
  - `<!-- BEGIN AGENTPAL BINDING: claude-code -->` / `<!-- END AGENTPAL BINDING: claude-code -->`
- Legacy `<!-- AGENTPAL:BEGIN -->` / `<!-- AGENTPAL:END -->` blocks are accepted only as migration input and are not emitted by new writes.
- README examples, Skill instructions, templates, helper scripts, and smoke tests agree on marker names, required fields, and allowed files.
- Full-repo old marker scan has no hits in public templates, prompts, runtime guides, plugin README files, or active usage docs.
- Any remaining old marker hit is either helper/test migration recognition code or a file under `archive/migration-from-v0.3/` with an explicit legacy note.

## Evidence To Record

Record these in the release report:

- smoke command and result;
- changed plugin or integration files;
- whether Codex and Claude Code coexistence was tested;
- whether runtime-qualified markers are current for this release;
- whether legacy marker migration was tested;
- the old marker scan command and every allowed exception file;
- any `not-run` checks and reason;
- remaining risk before publishing.
