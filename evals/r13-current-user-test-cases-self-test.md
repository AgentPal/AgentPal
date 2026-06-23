<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Current User Test Cases Self-Test

## Purpose

Cover real-use regression inputs for Pal validity, Mira route-only behavior, Codex generic labeling, and AI-judged owner selection.

## Global Pass Rules

- Mira route-only for owned tasks.
- Mira professional routing max output is max 2 short sentences.
- Mira must not provide owned work body after handoff.
- Owner Pal must answer immediately after handoff.
- Specialist Pal must include a light work-method statement.
- Specialist Pal must use its Output Contract.
- Codex generic answer must be labeled and must not use a Pal name prefix.
- Formal owner Pal Skill creation triggers when the user explicitly asks to save a Skill, or when similar operations happen more than 3 times.

## Test Inputs And Expected Behavior

1. `如果这个项目继续开发，你会给我一些专业建议`
   - expected: Mira uses AI judgement case-by-case; if a registered owner Pal owns the work, Mira gives a current-context reason and hands off.
   - fail if Mira gives the owned work body.

2. `帮我制定一个开发计划`
   - expected: Mira route-only if a registered Pal owns the requested work, then the selected owner immediately answers.
   - selected owner must include its work-method statement, output contract, relevant scope, acceptance criteria, and next executable task where appropriate.

3. `我想继续做这个项目，但不知道下一版应该做哪些功能。你帮我判断一下。`
   - expected: Mira uses AI judgement; if a product owner is selected, the handoff reason must be based on current context rather than a fixed route.

4. `这个项目如果准备发布，你帮我看看有哪些风险，怎么验收？`
   - expected: Mira uses AI judgement; if a quality/release owner is selected, the owner uses its own output contract and evidence posture.

5. `帮我检查系统启动项都有哪些，会不会影响开机速度`
   - expected: Mira uses AI judgement plus safety guardrails; if a system owner is selected, the owner uses read-only-first posture.

6. `/pal Atlas 你看一下这个项目下一步应该怎么开发`
   - expected: Atlas direct Pal Mode with work-method statement and Output Contract.

7. `/pal Nova 帮我把这个项目的下一版范围整理出来`
   - expected: Nova direct Pal Mode with work-method statement and Output Contract.

8. `你刚才这个回答，用到了哪些 Pal 的知识、技能、流程？如果没有用，也直接告诉我。`
   - expected: answer identifies assets used or states no Pal asset was used; if no asset was used, label as `Codex generic answer` when appropriate.

9. `/pal Atlas 请用一句话说明，怎么判断你不是 Codex 换个名字在回答？`
   - expected: Atlas says the answer must use Atlas Response Fingerprint, Output Contract, and at least one asset or fallback method.

10. `这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？`
    - expected: Mira uses AI judgement to decide whether Simple Pal Mode or Subagent Mode is useful; no fixed Pal set is required by the wording alone.

11. `不要使用任何 Pal 的知识和流程，只用 Codex 通用能力回答：这个项目继续开发应该注意什么？`
    - expected: starts with `Codex generic answer:`, no Pal prefix.

12. `/pal Rhea 以后这种启动项检查能不能形成固定流程？`
    - expected: Rhea says task_family is `startup-item-audit`; if the user asks to save a Skill, Rhea creates it under `pals/Rhea-system/skills/<skill-id>/SKILL.md`; if the user asks for a Runbook, Rhea can create `windows-startup-item-audit-runbook` under Rhea's runbooks.

## Fail Signs

- Mira outputs more than 2 short sentences for an owned task handoff.
- Mira outputs a numbered or bullet specialist plan.
- Mira hands off but no owner Pal answers immediately.
- Specialist Pal only changes the speaker name.
- Specialist Pal has no work-method statement.
- Specialist Pal does not use Output Contract.
- Codex generic request uses a Pal prefix.
- Explicit Skill-saving request does not create a formal owner Pal Skill.

