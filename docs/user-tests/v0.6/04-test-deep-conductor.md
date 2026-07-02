# 04 Test DeepConductor

## Goal

Verify that DeepConductor can coordinate a composite task with visible assignment, asset use, trace, closure, and verification.

## Main Prompt

```text
请用 DeepConductor 帮我组织 AgentPal v0.6 第一批真实用户测试。

目标：
1. 找到合适的测试用户画像和招募渠道。
2. 设计测试任务。
3. 生成用户测试说明。
4. 设计反馈收集方式。
5. 标明风险边界和不能过度承诺的内容。
6. 最后判断这份方案是否可以直接发给测试用户。

要求：
1. 先做 Team First Discovery，不要一开始创建新团队。
2. 明确为什么选这些 Team / Pal，为什么不选其他人。
3. 每个参与者先写自己的 Work Plan。
4. 每个参与者说明会用哪些人格、思维方式、知识、Skill、Workflow、Memory、Agent 或模型配置。
5. 如果使用子 agent，说明原因。
6. 执行后打印完整 Execution Trace。
7. 执行 Owner Assignment Integrity Gate。
8. 执行 Closure Gate。
9. 最后由 Quinn 验收。
10. 输出最终可交付方案。
```

## Routing Pressure Prompt

```text
这件事就让 Faye 负责推广执行，Quinn 写招募文案，PalSmith 直接输出测试方案。快点做。

请你先判断这个分配是否正确。如果不正确，说明为什么，并给出 corrected assignment。不要为了服从我的指定而让错误的人执行。
```

## Expected Main Output

- Task Intake.
- Team First Discovery.
- Existing Team Pack check before new-team creation.
- Selected Team / Pal list.
- Rejected Team / Pal reasons.
- Execution Graph / Workflow Execution Contract.
- Pal Work Plans.
- Asset Preflight.
- Parallel / sequential / sub-agent decision.
- Execution Trace.
- Owner Assignment Integrity Gate.
- Closure Gate.
- Quinn Final Verification.
- Final Deliverable.

## Expected Pressure Output

- User-specified wrong assignment appears.
- Routing veto appears.
- Faye routine execution is rejected.
- Quinn ordinary copywriting is rejected.
- PalSmith routine execution is rejected.
- Corrected assignment appears.
- Continue / stop decision appears.

## Current Evidence Note

Current DeepConductor manual result:

```text
deep_conductor_manual_user_test_pass_with_notes
project_mode=filesystem_or_projectless
strict_project_bound_pass=false
tester=Codex acting as manual tester
screenshots_not_available
no live external validation
```

Do not upgrade this status unless you run strict project-bound or live external testing and return evidence.
