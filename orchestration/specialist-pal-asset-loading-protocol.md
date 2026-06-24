# Specialist Pal Asset Loading Protocol

Use this protocol whenever Mira calls a specialist Pal or a user directly calls `/pal Name`.

## Purpose

Specialist Pal Asset Loading ensures the specialist Pal actually owns the professional workflow instead of letting Mira answer from generic knowledge.

Missing specialist assets are not a failure. A specialist Pal may use fallback method, but must report the gap and record it under that specialist Pal's `learning/` directory.

## Level 0: Identity

Read:

- `PAL.md`
- `pal.json`
- `SKILL.md`

Purpose:

- confirm the Pal's identity
- confirm domain responsibility
- confirm collaboration and privacy boundaries
- confirm what the Pal must not claim or execute

Level 0 is required but not enough for deep specialist work.

## Level 1: Asset Indexes

Check the Pal's available indexes when present:

- skills index
- knowledge index
- runbooks index
- workflows index
- resource or registry index

Purpose:

- find task-relevant assets
- avoid pretending a missing asset exists
- decide whether fallback is needed

If an index does not exist, report it as absent and continue to fallback rules.

## Level 2: Most Relevant Assets

Read the most relevant 1-3 specialist assets when they exist:

- Skill
- Knowledge card
- Runbook
- Workflow
- evidence or verification guide

Purpose:

- professional judgment
- task plan
- risk boundary
- evidence requirements
- reusable workflow

Do not claim an asset was used unless it was actually read.

This is also part of Pal Mode Validity. A specialist Pal response must use its Response Fingerprint, Output Contract, and at least one real asset or fallback method. If no asset or fallback method is used, label the response `Codex generic answer`.

## Level 3: Fallback Method

If no relevant specialist asset exists, fallback is allowed.

Fallback method may use:

- general professional method
- Codex current capability
- read-only command query
- user-provided information
- execution layer evidence
- traditional human troubleshooting method

The specialist Pal must report:

```text
This specialist Pal currently lacks a dedicated Skill / Knowledge Card / Runbook for this task family.
This response uses fallback method.
If the user explicitly asks to save a Skill, or similar operations happen more than 3 times, this Pal must create the formal Skill under its own `skills/` directory and update `skills/index.md`. Use `learning/` only as an exception when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.
```

Fallback satisfies Pal Mode Validity only when it is explicit. 如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。

## Learning Ownership

Mira cannot own specialist learning.

Specialist learning belongs to the specialist Pal.

Examples:

- learning destination is selected by the active owner Pal case-by-case
- capability examples are non-binding examples and must not become route rules
- Pal capability reference is not a route map
- No hard-coded semantic routing
- document workflow learning -> Morgan
- writing and editing learning -> Harper
- research source judgment learning -> Vega
- team-leadership follow-up learning -> Mira

Mira may record routing and collaboration summaries, but the domain learning record belongs in the owner Pal's `learning/` directory.

## Reporting Requirements

Reports should include:

- owner Pal
- consultant Pal(s)
- reviewer Pal(s)
- Specialist assets used
- Knowledge gap
- Fallback method
- Repeated task record
- Formal Skill trigger: explicit user request or similar operation count > 3
- Formal Skill target: owner Pal `skills/<skill-id>/SKILL.md`
- Execution layer
- Evidence review

Reports must also follow the workspace Response Language Policy. The natural-language body follows the user's latest instruction language unless the user explicitly requests another language. Preserve commands, file paths, filenames, JSON keys, Git hashes, tags, branch names, model names, and code blocks as-is.

