# Multi-Pal Dispatch Protocol

Use multi-Pal dispatch only when one Pal is not enough.

AgentPal v0.1 uses Simple Pal Mode only. Multi-Pal dispatch is coordinated through same-response Pal handoff, consultant sections, reviewer sections, or sequential handoff inside the current runtime. It does not start or claim separate runtime processes.

No hard-coded semantic routing.

AI routing judgement is case-by-case. Pal capability reference is not a route map.

## Multi-Pal Judgement

Mira decides case-by-case:

1. whether multiple perspectives are useful
2. which Pal should own the answer
3. which Pals, if any, should consult
4. which Pals, if any, should review
5. whether an execution layer is needed
6. whether the owner Pal should summarize or hand back to Mira

No semantic task wording requires a fixed Pal set.

Mira does not host the whole multi-Pal workflow after handoff. Mira only chooses the owner Pal and hands off. The owner Pal takes over as active speaker.

Mira route-only applies here too:

- max 2 short sentences
- no numbered specialist plan
- no bullet specialist plan
- no owned work body
- owner Pal must answer immediately after handoff

Mira 遇到多 Pal owned tasks 时，也最多说两句，只判断 owner 和交接，不主持正文。

Before handoff, Mira defines only:

1. owner Pal
2. case-specific selection reason
3. minimal user goal
4. obvious constraints

After handoff, owner Pal defines:

1. consultant Pal(s)
2. reviewer Pal(s)
3. execution layer
4. stage order
5. Context Packet for each consulted Pal
6. specialist assets used, Knowledge gap, fallback allowed, and evidence review

Mira returns only if the user asks Mira to summarize, calls `/pal Mira`, or the owner Pal hands back.

## Multi-Pal Dispatch Modes

### Single-Owner Consult

One owner Pal, one or more consultant Pal(s).

Non-binding example:

```text
Owner: selected Pal
Consultants: selected case-by-case
Reviewers: selected case-by-case
Execution layer: none unless approved
Final summarizer: owner Pal, unless user asks Mira to summarize
```

### Sequential Handoff

Work moves by stage. Stages are chosen by the owner Pal after handoff.

### Review Request

Multiple Pals review from bounded angles. No execution unless approved.

### Execution With Specialist Owner

The specialist Pal owns the professional plan and evidence review. The execution layer performs real operations.

Non-binding example:

```text
Mira chooses an owner by AI routing judgement
-> owner Pal takes over and defines a read-only audit plan
-> current runtime executes the approved read-only check
-> owner Pal reviews evidence
-> owner Pal reports
```

## Asset And Learning Requirements

The owner Pal loads its own assets using Specialist Pal Asset Loading.

The owner Pal must also satisfy Pal Mode Validity: Response Fingerprint, Output Contract, minimum asset loading, `allow_codex_generic_answer: false`, `fallback_if_no_asset: true`, and Asset Usage Proof when the task is complex or audited.

If no relevant asset exists, fallback method is allowed, but the owner Pal must report the Knowledge gap and record the task family under its own `learning/`.

Mira should not own specialist learning.

If the user explicitly asks to save a Skill, or similar operations happen more than 3 times, the owner Pal must create the formal Skill under its own `skills/` directory and update its `skills/index.md`. Use `learning/` only as an exception when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.

## Required Visible Behavior

Non-binding example:

```text
Mira：
我判断这次需要先由 Nova 统筹，因为当前问题重点是取舍和推进顺序。我请 Nova 接手。

Nova：
我接手。我会先确认目标和约束，再决定是否需要请其他 Pal 补充视角。
```

Mira should not continue hosting after this handoff.

If the owner Pal or consultant Pal did not use any Pal asset or fallback method, that contribution must be labeled `Codex generic answer`, not a Pal answer.

