# Codex Retest: Scenario 05 WorkBuddy Fixture

Status: copyable Codex retest prompt; not executed.

Use this when retesting the WorkBuddy source blocker without network access.

## Preconditions

- Run inside the AgentPal workspace or a Codex project that can read the
  AgentPal workspace.
- Do not browse the web.
- Do not claim current WorkBuddy facts.

## Copyable User Prompt

```text
请按 AgentPal v0.6 Team Pack runtime validation 规则复测 Scenario 05。

任务：请使用 Research Team 基于这个本地 fixture 分析 WorkBuddy 专家团，给我一份来源可靠性、产品定位、竞争优势和不确定性的简报。

fixture_path: evals/fixtures/v0.6-team-pack/workbuddy-expert-group.synthetic.json
source_type: synthetic local fixture
team_pack_path: examples/team-packs/research-team
result_mode: runtime-with-fixture

边界：
- 这个 fixture 不是 live web source。
- 不要声称做了外部实时调研。
- 不要把 fixture-derived 观察写成当前 WorkBuddy 产品事实。
- live external validation 仍然是 not-run / live-source-needed。

请输出：
1. Mira / Research Team 判断。
2. Team Asset Preflight 摘要。
3. Workflow Execution Contract。
4. 基于 fixture 的 WorkBuddy 专家团结构分析。
5. 与 AgentPal Pal / Team 的对比点。
6. 来源可靠性与不确定性。
7. Quinn verifier 检查。
8. Closure Gate。
9. 结果状态：runtime-with-fixture-pass / partial / fail / blocked。
```

## Expected Result

The previous missing-source blocker should be resolved for fixture-based
validation only. Live WorkBuddy source validation remains not-run.
