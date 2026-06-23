<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Prompt Templates

These templates are for Codex Subagent Mode. Subagents are Codex subagent threads / workflows, not OS-level background processes.

Use these templates when Mira decides a task needs owner Pal / consultant Pal / reviewer Pal separation.

Resolve selected Pal identities, asset paths, and permissions from current contacts / registry before using a Pal-specific template. Generic templates must not map task types or keywords to specific Pals.

Default rules for all templates:

- State which Pal the subagent represents.
- State that the subagent is not Mira.
- Handle only that Pal's professional perspective.
- Read required Pal assets before answering.
- Do not process other Pal responsibilities.
- Do not modify project files unless the task and permission explicitly allow it.
- Return structured fields compatible with `templates/subagent-results/subagent-result-template.md`.
- Include `assets_read`, `output_contract_used`, `findings`, `risks`, `recommendations`, `evidence`, and `next_steps`.
- Do not self-certify `agent_id`, spawn status, wait status, or close status unless the coordinator explicitly provided them. The coordinator records runtime evidence.

If subagents are unavailable, use `orchestration/subagent-fallback-policy.md` and fall back to Simple Pal Mode.


