# Claude Code Retest: Scenario 04 After-Sales Feedback Fixture

Status: copyable Claude Code retest prompt; not executed.

Use this when retesting the R223B Claude Code blocked result for missing 20
feedback records.

## Preconditions

- Start Claude Code in a disposable project with AgentPal enabled.
- Add or allow read access to the AgentPal workspace.
- Allow file reads for the fixture and Team Pack paths.
- Do not allow customer-system actions, network access, or file writes unless
  the validation runner explicitly records them.

## Suggested Claude Code Invocation Shape

```powershell
claude --plugin-dir "<agentpal-workspace>/integrations/claude-code/agentpal-project-binder" --add-dir "<agentpal-workspace>" --allowedTools "Read,Glob,Grep,LS" --permission-mode bypassPermissions --max-budget-usd 2.00 --effort low --model sonnet -p "<copyable prompt>"
```

Replace `<agentpal-workspace>` with the local AgentPal workspace path.

## Copyable Prompt

```text
请按 AgentPal v0.6 Team Pack runtime validation 规则复测 Scenario 04。

任务：售后服务团队已经建好了。请让它处理这个本地 fixture 中的 20 条客户反馈，并输出分类、回复建议和需要升级的问题。

fixture_path: evals/fixtures/v0.6-team-pack/after-sales-feedback-20.synthetic.json
source_type: synthetic local fixture
expected_input_count: 20
team_pack_path: evals/team-workflows/r220a-v0.6-closure-rehearsals/simulated-team-packs/after-sales-service-team
result_mode: runtime-with-fixture

边界：
- 这不是真实客户数据。
- 不要声称访问了客户系统。
- 不要把 fixture-based validation 写成 live customer validation。
- Faye 不应作为已有团队日常执行负责人。
- 如果无法读取 fixture，请明确 blocked；不要编造 20 条反馈。

请输出：
1. Mira / Team Pack 判断。
2. Team Asset Preflight 摘要。
3. Workflow Execution Contract。
4. 20 条 fixture 反馈的分类统计。
5. 回复建议主题。
6. 需要升级的问题列表。
7. Quinn 或等价 verifier 检查。
8. Closure Gate。
9. 结果状态：runtime-with-fixture-pass / partial / fail / blocked。
```

## Expected Result

The previous missing-input blocker should be resolved when Claude Code can read
the fixture. The result must still say live customer-data validation is
`not-run`.
