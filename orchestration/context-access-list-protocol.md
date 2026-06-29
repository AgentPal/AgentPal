# Context Access List Protocol

Context Access List extends Context Slicing by describing exactly what a Pal, runtime, Skill, plugin, MCP server, or verifier may use for a specific workflow step.

AgentPal v0.1.0-rc.1 does not automatically enforce access lists. This protocol is a design and audit asset that supports Task Packages, PalBench, and future orchestration.

Context Access Lists may be stage-level. A research stage, implementation stage, document stage, system stage, and verification stage can each receive a different Context Access List.

## Relationship To Existing Protocols

This protocol builds on:

- `orchestration/pal-context-slicing-protocol.md`
- `orchestration/context-packet-minimalism-protocol.md`
- `orchestration/task-package-output-contract.md`
- `RESOURCE_INDEX.md`

## Required Fields

- `workflow_id`
- `step_id`
- `stage_id`
- `stage_goal`
- `recipient_type`
- `recipient_id`
- `recipient_candidate`
- `task`
- `can_read_paths`
- `can_read_summaries`
- `can_receive_outputs_from`
- `cannot_read`
- `need_output`
- `sensitive_context_boundary`
- `private_memory_boundary`
- `content_read_budget`
- `index_known_paths`
- `content_read_files`
- `output_contract`
- `verification_required`

`need_output` states the exact deliverable expected from the recipient. `output_contract` names the structure or contract the deliverable must follow.

`recipient_candidate` records a possible Pal, Runtime, Skill, plugin, MCP server, or verifier for that stage. It is a candidate, not a fixed route.

## Recipient Types

- `pal`
- `runtime`
- `skill`
- `plugin`
- `mcp`
- `verifier`
- `team-leader-summary`

## Default Cannot Read

Unless explicitly justified and approved, recipients cannot read:

- full AgentPal workspace
- all Pal Packs
- all project files
- unrelated Pal memory
- private user memory
- credentials, tokens, secrets, private logs
- unapproved external directories
- other independent reviewers' drafts before the isolation stage ends

Stage-level defaults:

- a content stage should not receive implementation-only private state unless needed
- an implementation stage should not read unrelated Pal persona files by default
- a verification stage should not read every draft or reasoning trace by default
- a Runtime candidate should receive a Pal-layer Task Package before execution rather than bypassing the Pal layer

## Index-Known Versus Content-Read

`index_known_paths` are navigation hints. They are not evidence that content was read.

`content_read_files` are files opened and used as content.

Any asset report or PalBench record should keep these separate.

## Verification

If `verification_required` is true, the step must define:

- expected evidence
- acceptance criteria
- failure conditions
- who or what verifies

## v0.1 Boundary

In v0.1, Context Access Lists are templates and audit aids. They do not create a sandbox and do not grant runtime permissions.

In v0.1, a staged CAL can be included inside a staged Task Package. It does not start Deep Conductor or automatic multi-agent execution.

## Example: Quinn Rechecking A Claude Code Binding

Synthetic access list:

- `recipient_id`: `Quinn-quality`
- `task`: recheck whether an R30 Claude Code project binding test passed
- `can_read_paths`: `reports/R30-ClaudeCode-binding-report.md`, `evals/claude-code-one-prompt-install-self-test.md`, `docs/04-runtime-guides/02-use-with-claude-code.md`
- `can_read_summaries`: recent project-binding memory summary, if public-safe
- `cannot_read`: private user memory, unrelated Pal persona files, unauthorized external directories, raw local credentials, all project files
- `need_output`: pass/fail, failure points, evidence gaps, files requiring rework
- `output_contract`: quality review result with evidence table
- `verification_required`: true
