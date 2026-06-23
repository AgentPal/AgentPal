<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# External Project AI Judgement No-Hardcode Self-Test

## Purpose

Verify that external project binding templates preserve context isolation and do not inject hard-coded semantic routing into user projects.

## Files Under Test

- `templates/project-binding/root-agents-agentpal-block-template.md`
- `projects/project-workgroup-template/agentpal/AGENTPAL.md`
- `projects/project-workgroup-template/agentpal/PAL_GROUP.md`
- `projects/project-workgroup-template/agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md`

## Pass Criteria

- No `task -> Pal` table.
- No `domain_map`.
- No keyword-triggered Subagent Mode.
- No fixed natural-language trigger that requires a Pal set.
- `active_project_root` remains the only current project in project-bound sessions.
- `agentpal_workspace_root` remains only a Pal source and routing reference.
- AgentPal workspace is not treated as project content unless the user explicitly asks about AgentPal itself.
- Explicit `/pal Name`, Codex generic, safety, availability, and missing-Pal guardrails remain deterministic.

## Test Inputs

```text
读取这个项目目录，告诉我下一步。
```

Expected: reads only `active_project_root`, not AgentPal workspace.

```text
这个项目下一版值不值得做，怎么开发，怎么验收？
```

Expected: AI judgement decides mode and perspectives case-by-case. No fixed Pal set is required.

```text
不要 Pal，只用 Codex 通用能力回答。
```

Expected: starts with `Codex generic answer:`.

## Fail Signs

- Template copies a domain-to-Pal map into an external `AGENTS.md`.
- Template says development, product, quality, risk, or system wording must route to a named Pal.
- Template lists AgentPal workspace as a second current project root.

