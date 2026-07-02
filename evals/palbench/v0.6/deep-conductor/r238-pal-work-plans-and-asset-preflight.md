# R238 Pal Work Plans And Asset Preflight

## Team Asset Preflight

```yaml
team_id: marketing-growth-team
task_summary: "AgentPal v0.6 首批 GitHub 用户测试招募与测试执行方案"
team_pack_used: true
team_files_checked:
  - examples/team-packs/marketing-growth-team/TEAM.md
  - examples/team-packs/marketing-growth-team/team.json
  - examples/team-packs/marketing-growth-team/roster.json
  - examples/team-packs/marketing-growth-team/workflows/weekly-agentpal-promotion-content.md
  - examples/team-packs/marketing-growth-team/evals/definition-of-done.md
  - examples/team-packs/marketing-growth-team/routing/team-routing-card.json
selected_workflow: examples/team-packs/marketing-growth-team/workflows/weekly-agentpal-promotion-content.md
team_assets_missing: []
member_pal_preflights_required: [Mira, Nova, Vega, Harper, Rhea, Quinn]
verification_required: true
```

## Pal Work Plans

### Mira

```yaml
pal: Mira
assigned_step: S1/S7
what_i_will_do: "接收目标、做 Team First Discovery、生成 WEC、收束最终报告"
tone_and_voice: "清晰、协调、不过度承诺"
thinking_basis:
  - "Mira is conductor, not substitute specialist"
knowledge_assets:
  - official/pals/Mira-main/PAL.md
  - official/pals/Mira-main/core/routing-protocol.md
skill_assets:
  - official/pals/Mira-main/SKILL.md
workflow_assets:
  - official/pals/Mira-main/workflows/pal-team-coordination-workflow.md
team_assets:
  - examples/team-packs/marketing-growth-team/TEAM.md
runtime_or_agent_usage: "Codex writes evidence files; AgentPal does not auto-execute"
expected_output: "Task intake, Team discovery, WEC, final synthesis"
handoff_target: "Nova, Vega, Harper, Rhea, Quinn step records"
```

### Nova

```yaml
pal: Nova
assigned_step: S2
what_i_will_do: "定义首批测试用户、测试目标、成功信号和范围边界"
knowledge_assets:
  - official/pals/Nova-product/PAL.md
  - workspace/organization/contacts/capability-cards/nova-product.json
team_assets:
  - examples/team-packs/marketing-growth-team/roster.json
expected_output: "目标用户和测试范围"
handoff_target: "Harper and Quinn"
```

### Vega

```yaml
pal: Vega
assigned_step: S3
what_i_will_do: "给出渠道和用户来源判断，并标记没有 live web research 的限制"
knowledge_assets:
  - official/pals/Vega-research/PAL.md
  - workspace/organization/contacts/capability-cards/vega-research.json
team_assets:
  - examples/team-packs/marketing-growth-team/routing/team-routing-card.json
runtime_or_agent_usage: "no live web browsing in this trace"
expected_output: "渠道假设、证据限制、下一步 live validation 建议"
handoff_target: "Harper and Quinn"
```

### Harper

```yaml
pal: Harper
assigned_step: S4
what_i_will_do: "写用户可读测试说明和反馈说明"
knowledge_assets:
  - official/pals/Harper-writing/PAL.md
  - workspace/organization/contacts/capability-cards/harper-writing.json
team_assets:
  - examples/team-packs/marketing-growth-team/evals/definition-of-done.md
expected_output: "可直接给首批测试用户看的测试说明"
handoff_target: "Quinn"
```

### Rhea

```yaml
pal: Rhea
assigned_step: S5
what_i_will_do: "审查 no-code、runtime、Marketplace、Release、GitHub 过度宣传边界"
knowledge_assets:
  - official/pals/Rhea-system/PAL.md
  - workspace/organization/contacts/capability-cards/rhea-system.json
expected_output: "边界风险清单和禁止宣传项"
handoff_target: "Quinn"
```

### Quinn

```yaml
pal: Quinn
assigned_step: S6
what_i_will_do: "验证参与者、资产、WEC、Closure Gate、overclaim scan 和最终可交付性"
knowledge_assets:
  - official/pals/Quinn-quality/PAL.md
  - official/pals/Quinn-quality/SKILL.md
  - official/pals/Quinn-quality/core/output-contract.md
  - workspace/organization/contacts/capability-cards/quinn-quality.json
team_assets:
  - examples/team-packs/marketing-growth-team/evals/definition-of-done.md
expected_output: "final verification verdict"
handoff_target: "Mira final synthesis"
```

## Missing Assets

```yaml
missing_assets:
  RESOURCE_INDEX.md: "root index absent after slimming; agentpal.json and direct paths used instead"
  live_web_sources: "not run; this trace does not claim current GitHub trend evidence"
  real_GitHub_issue_discussion: "not run; plan only"
```
