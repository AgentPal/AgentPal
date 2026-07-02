# Pal Asset Preflight Protocol

Status: v0.6 current protocol draft. Markdown / JSON protocol only; no scanner, daemon, validator, CLI, UI, or background runtime is introduced.

## Purpose

Pal Asset Preflight prevents a Pal from answering a substantive task from name, persona, or generic model knowledge while ignoring its own assets.

Use this protocol before important Pal-owned work so the Pal can prove:

- it is the right owner or should refuse / transfer;
- it selected only task-relevant assets instead of reading the whole Pal Pack;
- it knows which knowledge, Skills, workflows, runbooks, memory, and evals are required;
- it can create concrete child steps when another Pal is needed;
- it can report missing assets without pretending readiness.

This protocol complements `core/pal-asset-execution-contract.md` and `core/asset-loading-gate.md`.

## When To Run Full Preflight

Run full Pal Asset Preflight for:

- Pal creation, Pal upgrade, import, export, health, or publication work;
- team tasks where a member Pal receives a workflow step;
- tool-backed deliverables;
- work that changes identity, role, voice, knowledge, Skill, workflow, memory, collaboration, discovery, or eval behavior;
- QA, regression, release, safety, privacy, legal, financial, medical, or security-sensitive work;
- tasks where the user asks which assets were used.

## When Lightweight Preflight Is Enough

Use lightweight preflight for:

- greetings or ordinary conversation;
- one-line clarification;
- spelling, link, heading, or tiny wording fixes;
- summaries that only rely on already-loaded current-turn evidence.

Lightweight preflight still must not invent missing assets, claim unused tools, or bypass responsibility boundaries.

## Preflight Order

1. Read the workspace `RESOURCE_INDEX.md` when the task may require non-local asset discovery.
2. Read the target Pal root entries: `PAL.md`, `pal.json`, `SKILL.md`, and `core/output-contract.md` or equivalent.
3. Check responsibility boundaries before choosing assets.
4. Select only task-relevant assets from indexes such as `knowledge/index.md`, `skills/index.md`, `workflows/index.md`, `runbooks/index.md`, `memory/index.md`, and `evals/definition-of-done.md`.
5. Load the smallest useful set, normally 1-3 specific task assets after root entries and indexes.
6. Record missing assets and choose a go / no-go label from `core/asset-loading-gate.md`.
7. If another Pal is needed, create a named child step in the task plan or Workflow Execution Contract. Do not rely on a casual verbal delegation.
8. After work, produce an Asset Use Summary when the task is substantive or tool-backed.

When the work is represented in a Workflow Execution Contract, run Pal Asset
Preflight before the Pal-owned Step moves to `running`. The Step should record
the preflight result or an honest `blocked` / `skipped` / `replanned` status.

## Responsibility Check

The Pal must answer:

- Is this task inside my role and boundaries?
- Does a Team Pack assign this step to me?
- Does my Pal boundary allow the assigned step?
- Should I refuse, ask for replan, consult another Pal, or create a child step?

If the task is outside the Pal boundary, the Pal must not continue as if the assignment were valid. The Owner Pal or team conductor must replan.

## Context Budget Rule

Preflight is not permission to read the whole workspace, all Pals, all memories, or all team assets. Read indexes first, then only the assets needed for this task.

Directory listing and index visibility are not the same as reading content. Reports should distinguish `index_known` from `content_read` when that detail matters.

## Child Step Rule

When another Pal is required, create a child step with:

- child_step_id
- owner_pal
- purpose
- required_assets
- expected_output
- verification_required
- status

This is a no-code planning record. It is not automatic subagent execution and does not call external Agents by itself.

For Workflow Execution Contract tasks, the child step must use the contract
fields from `templates/orchestration/workflow-execution-contract.md`, including
`parent_step_id`, `context_access_list`, `output_contract`, and
`verification_required`.

## Required Fields

Use `templates/pal/pal-asset-preflight.md` when explicit evidence is needed.

Minimum fields:

- `pal_id`
- `task_summary`
- `team_context`
- `responsibility_check`
- `required_assets`
- `missing_assets`
- `need_delegate`
- `need_child_steps`
- `output_contract`
- `verification_required`

## Failure Cases

Mark the task as `fail_asset_usage_regression` or produce a Missing Asset Plan when:

- the Pal only used a name prefix;
- task-relevant assets existed but were ignored;
- a host tool replaced Pal judgement;
- the Pal claimed a Skill, workflow, memory, or eval that was not loaded;
- the Pal accepted a team assignment that violates its own boundary;
- missing core assets were smoothed into a pass.
