# R238 Pal Selection And Participation Lock

## Selected Participants

```yaml
participants:
  - pal_name: Mira
    canonical_id: mira-main
    role_title: Main Pal, Leader Pal, and Conductor
    why_selected: "marketing-growth-team roster requires Mira as team-conductor; task needs intake, Team discovery, WEC, and synthesis"
    capability_card_evidence:
      - workspace/organization/contacts/capability-cards/mira-main.json
      - examples/team-packs/marketing-growth-team/roster.json
    team_roster_source: examples/team-packs/marketing-growth-team/roster.json
    task_scope: "intake, discovery, WEC, closure summary"
    not_responsible_for:
      - "professional copy body after Harper is assigned"
      - "final quality verification after Quinn is assigned"
    participation_required: true

  - pal_name: Nova
    canonical_id: nova-product
    role_title: Product and Strategy Lead
    why_selected: "target users, scope, success signal, and test execution framing require product/strategy judgement"
    capability_card_evidence:
      - workspace/organization/contacts/capability-cards/nova-product.json
      - examples/team-packs/marketing-growth-team/roster.json
    team_roster_source: examples/team-packs/marketing-growth-team/roster.json
    task_scope: "target user segments, test goals, scope boundaries"
    not_responsible_for:
      - "copy drafting as primary owner"
      - "quality final gate"
    participation_required: true

  - pal_name: Vega
    canonical_id: vega-research
    role_title: Research Intelligence Lead
    why_selected: "target user and channel hypotheses need evidence-aware framing and uncertainty labels"
    capability_card_evidence:
      - workspace/organization/contacts/capability-cards/vega-research.json
      - examples/team-packs/marketing-growth-team/roster.json
    team_roster_source: examples/team-packs/marketing-growth-team/roster.json
    task_scope: "target channels and research limitations; no live web claim"
    not_responsible_for:
      - "publishing"
      - "final product scope decision"
    participation_required: true

  - pal_name: Harper
    canonical_id: harper-writing
    role_title: Writing and Content Craft Lead
    why_selected: "用户要求输出给测试用户看的说明，属于 public-facing writing"
    capability_card_evidence:
      - workspace/organization/contacts/capability-cards/harper-writing.json
      - examples/team-packs/marketing-growth-team/roster.json
    team_roster_source: examples/team-packs/marketing-growth-team/roster.json
    task_scope: "用户可读测试说明、招募文案和反馈说明"
    not_responsible_for:
      - "source verification"
      - "release gate"
    participation_required: true

  - pal_name: Rhea
    canonical_id: rhea-system
    role_title: System and Runtime Safety Lead
    why_selected: "任务要求检查 runtime/backend/Marketplace/Release 过度宣传和 no-code 边界"
    capability_card_evidence:
      - workspace/organization/contacts/capability-cards/rhea-system.json
    team_roster_source: "none; specialist consult outside selected Team Pack"
    task_scope: "no-code, runtime, release and integration boundary review"
    not_responsible_for:
      - "marketing execution"
      - "quality final gate"
    participation_required: true

  - pal_name: Quinn
    canonical_id: quinn-quality
    role_title: Quality and Verification Lead
    why_selected: "public-facing testing plan requires final evidence, overclaim, participation, WEC, and Closure Gate review"
    capability_card_evidence:
      - workspace/organization/contacts/capability-cards/quinn-quality.json
      - examples/team-packs/marketing-growth-team/roster.json
    team_roster_source: examples/team-packs/marketing-growth-team/roster.json
    task_scope: "final verification only"
    not_responsible_for:
      - "primary copywriting"
      - "routine execution"
    participation_required: true
```

## Explicit Non-Selections

```yaml
why_not_faye: >
  任务不是从零业务流程发现，也不是业务团队 workflow 重构。Faye 不应参与已有
  marketing-growth-team 的日常推广/测试执行方案。
why_not_palsmith_for_execution: >
  已存在可复用 marketing-growth-team。PalSmith 不是日常执行者，也不需要创建或治理
  Team Pack。
why_not_atlas_if_no_dev_task: >
  用户没有要求代码实现、仓库修复或开发任务。测试入口可用说明和任务包不等于开发实现。
why_not_quinn_for_execution: >
  Quinn 只做 verification / quality gate，不做主要内容和招募方案执行。
```

## Participation Lock

```yaml
assignment_integrity:
  every_selected_participant_has_output_record: true
  every_named_verifier_has_output_record: true
  open_roles_recorded: true
  candidates_not_reported_as_participants: true
  fake_handoff_detected: false
```
