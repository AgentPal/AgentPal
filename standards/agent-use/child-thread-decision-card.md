# Child-thread Decision Card Standard

Status: v0.5 no-code protocol

## Purpose

The Child-thread Decision Card records when AgentPal recommends or starts a
bounded Codex background thread, subthread, or host-provided subagent candidate.
It fixes the R158 enum gap by keeping child-thread shape out of `codex_mode`.

This card is an evidence and merge-back protocol. It is not proof that a child
thread was created unless a current host thread id or equivalent runtime
evidence is recorded.

## Required Fields

- `parent_task_id`
- `child_task_id`
- `child_role`
- `child_owner_pal`
- `child_verifier_pal`
- `codex_mode`
- `child_thread_type`
- `subthread_subagent_decision`
- `allowed_context`
- `forbidden_context`
- `expected_output`
- `evidence_required`
- `merge_back_plan`
- `close_policy`
- `privacy_boundary`
- `authorization_status`
- `created_thread_id`
- `runtime_evidence`
- `result_status`

## `codex_mode` Rule

`codex_mode` must use the exact R157 enum:

- `normal_chat`
- `plan_mode`
- `goal_mode`
- `owner_verifier`
- `parallel_review`
- `sequential_chain`
- `external_agent_handoff`
- `fallback`

Do not invent child-thread mode values such as:

- `background_thread_review`
- `child_thread_review`
- `subtask_mode`
- `subagent_mode`
- `review_thread`

If the task needs to express child-thread behavior, use:

- `child_thread_type`
- `subthread_subagent_decision`
- `created_thread_id`

## When To Consider A Child Thread

Consider a child thread only when current host evidence says background
threads, subthreads, or subagents are available and at least one condition is
true:

- the task can be split into weakly dependent work packages;
- independent product, document, quality, privacy, or other reviews add value;
- owner and verifier should be isolated to avoid self-certification;
- different资料 or file groups should be read separately to reduce context
  pollution;
- multiple Delivery Packs, modules, or file groups can be reviewed separately;
- the user explicitly asks for parallel work and the capability profile
  confirms support;
- a Pal Skill, workflow, or project memory explicitly specifies subthread use.

## When Not To Start A Child Thread

Do not start a child thread when:

- the task is a simple answer, rewrite, or single-step judgement;
- customer-private material lacks a Context Access List and authorization;
- capability support is unknown;
- child tasks strongly depend on upstream results and should be sequential;
- launch cost is higher than review value;
- the user or project workflow forbids parallel distribution.

## Merge-back Rule

The parent thread must summarize child outputs as evidence, not hidden
reasoning. It must preserve each child thread's `result_status`, not-run items,
and evidence limits. If a child thread violates the enum rule or privacy
boundary, Quinn should mark that child result partial or fail and prevent it
from being used as pass evidence.

