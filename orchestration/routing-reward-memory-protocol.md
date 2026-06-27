# Routing Reward Memory Protocol

Routing Reward Memory records whether a routing or capability decision worked. It is AgentPal's practical learning loop.

This is not model training. It is not a hard-coded route table. It is structured memory for future AI Judgement.

AgentPal v0.1.0-rc.1 ships this as a design protocol and template guidance, not as an automatic runtime feature.

## Record Fields

Each routing record should include:

- `record_id`
- `created_at`
- `task_summary`
- `task_type`
- `pal`
- `agent_runtime`
- `topology`
- `model`
- `reasoning_strength`
- `skill_plugin_mcp`
- `context_read_count`
- `index_known_count`
- `verification_result`
- `false_completion_caught`
- `user_accepted`
- `human_intervention_count`
- `rework_count`
- `failure_reason`
- `next_time_recommendation`
- `privacy_review`

## Storage Guidance

Possible future storage locations:

- `memory/routing/`
- owner Pal `learning/`
- central `workspace/projects/<project-id>/memory/routing-memory.md`
- private runtime memory outside the public release package

Public releases should include only templates and synthetic examples.

## Privacy Boundary

Do not store:

- raw private user content
- credentials or secrets
- customer data
- full project files
- sensitive logs
- local absolute paths in public files

Summarize enough to improve routing without preserving sensitive content.

## How It Informs Judgement

Routing Reward Memory may answer:

- which topology worked for similar tasks
- which runtime or model profile was too slow or too weak
- which Skill helped
- which verification step caught false completion
- what caused rework
- what should be tried next time

It must not say a future task must use the same owner, runtime, Skill, or topology. It provides candidates and evidence only.

Routing Reward Memory is based on real results, not static labels. A strong model is not automatically stable inside a particular Agent harness. A weaker or cheaper model may be cost-effective for bounded execution tasks when verification is strong. Runtime, Skill, plugin, MCP, Pal, and model profiles should be corrected by observed outcomes.

## Relationship To PalBench

PalBench aggregates routing records into evaluation data. Individual records explain one decision; PalBench looks for repeated patterns.
