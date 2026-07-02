# Claude Code Retest: Scenario 05 WorkBuddy Fixture

Status: copyable Claude Code retest prompt; not executed.

Use this when retesting the WorkBuddy source blocker without network access.

## Preconditions

- Start Claude Code in a disposable project with AgentPal enabled.
- Add or allow read access to the AgentPal workspace.
- Allow file reads for the fixture and Research Team paths.
- Do not enable web browsing or external source collection for this fixture
  retest.

## Suggested Claude Code Invocation Shape

```powershell
claude --plugin-dir "<agentpal-workspace>/integrations/claude-code/agentpal-project-binder" --add-dir "<agentpal-workspace>" --allowedTools "Read,Glob,Grep,LS" --permission-mode bypassPermissions --max-budget-usd 2.00 --effort low --model sonnet -p "<copyable prompt>"
```

Replace `<agentpal-workspace>` with the local AgentPal workspace path.

## Copyable Prompt

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
- 如果无法读取 fixture，请明确 blocked；不要编造 WorkBuddy 来源。

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

The previous missing-source blocker should be resolved when Claude Code can read
the fixture. The result must still say live WorkBuddy source validation is
`not-run` / `live-source-needed`.
