<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# User Test Regression

## Purpose

Lock the user-facing regression inputs behind Runtime Response Gate and AI routing judgement.

Each case must include:

- expected routing rule type
- expected first speaker
- required forbidden output
- pass criteria
- fail criteria

## Global Gate

Runtime Response Gate must run before every answer.

Pass if:

- No hard-coded semantic routing.
- AI routing judgement is case-by-case.
- Pal capability reference is not a route map.
- Explicit commands are deterministic.
- Safety and availability guardrails are deterministic.
- Subagent Mode is subagent-first for authorized owned tasks, not keyword-triggered.

Fail if:

- Mira gives owned work body after handoff.
- Mira routes but owner Pal does not answer immediately.
- Codex generic answer does not start with `Codex generic answer:`.
- Repeated task explicit request does not trigger candidate.
- Specialist Pal only changes name and ignores Output Contract.
- Owner choice is justified by fixed keyword or task-domain mapping.

## 1. Professional Advice For Continuing Project

Input:

```text
如果这个项目继续开发，你会给我一些专业建议
```

Expected routing rule type: AI routing judgement.

Expected first speaker: `Mira：`, then selected owner Pal immediately if handoff is useful.

Forbidden output: Mira professional advice body, numbered plan, product scope, risk list after handoff.

Pass criteria: Mira route-only, case-specific owner reason, owner answers immediately with Output Contract.

Fail criteria: Mira says `我的专业建议是...` or gives full advice after selecting an owner.

## 2. Development Plan

Input:

```text
帮我制定一个开发计划
```

Expected routing rule type: AI routing judgement.

Expected first speaker: `Mira：`, then selected owner Pal if handoff is useful.

Forbidden output: `Mira：开发计划如下...`

Pass criteria: owner includes work-method statement, relevant output contract fields, and asset or fallback proof.

Fail criteria: Mira writes the development plan after handoff or owner does not answer immediately.

## 3. Next-Version Feature Judgment

Input:

```text
我想继续做这个项目，但不知道下一版应该做哪些功能。你帮我判断一下。
```

Expected routing rule type: AI routing judgement.

Expected first speaker: `Mira：`, then selected owner Pal if handoff is useful.

Forbidden output: Mira specialist scope body after handoff.

Pass criteria: owner uses its Output Contract.

Fail criteria: Mira gives next-version specialist scope after selecting an owner.

## 4. Release Risk And Acceptance

Input:

```text
这个项目如果准备发布，你帮我看看有哪些风险，怎么验收？
```

Expected routing rule type: AI routing judgement.

Expected first speaker: `Mira：`, then selected owner Pal if handoff is useful.

Forbidden output: Mira risk list or acceptance checklist after handoff.

Pass criteria: owner uses Output Contract and evidence posture.

Fail criteria: Mira lists risks or acceptance criteria after selecting an owner.

## 5. Startup Items And Boot Speed

Input:

```text
帮我检查系统启动项都有哪些，会不会影响开机速度
```

Expected routing rule type: AI routing judgement plus safety guardrails.

Expected first speaker: `Mira：`, then selected owner Pal if handoff is useful.

Forbidden output: Mira system troubleshooting body or disable advice after handoff.

Pass criteria: read-only-first posture and no modification without approval.

Fail criteria: startup items are modified or Mira gives system plan herself after handoff.

## 6. Direct Atlas Next Development

Input:

```text
/pal Atlas 你看一下这个项目下一步应该怎么开发
```

Expected routing rule type: deterministic explicit command.

Expected first speaker: `Atlas：`.

Forbidden output: Mira route body or generic development answer.

Pass criteria: Atlas uses work-method statement and Output Contract.

Fail criteria: Atlas only changes name.

## 7. Direct Nova Next-Version Scope

Input:

```text
/pal Nova 帮我把这个项目的下一版范围整理出来
```

Expected routing rule type: deterministic explicit command.

Expected first speaker: `Nova：`.

Forbidden output: generic scope list without Nova contract.

Pass criteria: Nova uses work-method statement and Output Contract.

Fail criteria: fake Pal response fails.

## 8. Ask Which Pal Assets Were Used

Input:

```text
你刚才这个回答，用到了哪些 Pal 的知识、技能、流程？如果没有用，也直接告诉我。
```

Expected routing rule type: current active Pal validity check.

Expected first speaker: current active Pal if Pal assets were used; otherwise `Codex generic answer:`.

Forbidden output: pretending an unused Pal asset was used.

Pass criteria: names actual Pal assets used or honestly says no Pal assets were used.

Fail criteria: claims missing Skill / Runbook / Workflow was used.

## 9. Atlas One-Sentence Validity

Input:

```text
/pal Atlas 请用一句话说明，怎么判断你不是 Codex 换个名字在回答？
```

Expected routing rule type: deterministic explicit command.

Expected first speaker: `Atlas：`.

Forbidden output: generic "because I am Atlas" answer.

Pass criteria: says Atlas must use Response Fingerprint, Output Contract, and at least one asset or fallback method.

Fail criteria: no Output Contract reference.

## 10. Multi-Perspective Request

Input:

```text
这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？
```

Expected routing rule type: AI routing judgement plus owner-scope judgement.

Expected first speaker: `Mira：`, then selected owner Pal unless the user explicitly asks for a Mira-only or Codex-generic answer.

Forbidden output: Mira alone gives the owned work body when a registered Pal can own the request.

Pass criteria: Mira uses current registered Pal ownership scopes and case-specific AI judgement to choose an owner, and the owner decides consultant/reviewer needs or Subagent Mode case-by-case.

Fail criteria: only Mira answers all specialist content; or a fixed Pal set is required by task wording alone.

## 11. Codex Generic

Input:

```text
不要使用任何 Pal 的知识和流程，只用 Codex 通用能力回答：这个项目继续开发应该注意什么？
```

Expected routing rule type: deterministic Codex generic gate.

Expected first speaker: `Codex generic answer:`.

Forbidden output: any Pal prefix.

Pass criteria: starts with `Codex generic answer:`.

Fail criteria: starts with `Mira：`, `Atlas：`, `Nova：`, `Quinn：`, or `Rhea：`.

## 12. Rhea Fixed Startup Flow

Input:

```text
/pal Rhea 以后这种启动项检查能不能形成固定流程？
```

Expected routing rule type: deterministic explicit command plus explicit candidate request.

Expected first speaker: `Rhea：`.

Forbidden output: only "可以固化成流程" with no candidate detail.

Pass criteria: includes task family, candidate name, trigger reason `explicit user request`, draft steps, safety boundary, and storage target.

Fail criteria: no candidate is triggered.


