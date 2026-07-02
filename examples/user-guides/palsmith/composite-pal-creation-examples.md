# PalSmith Composite Pal Creation Examples

These are public-safe examples, not official Pals.

Use them to understand how to ask PalSmith for a creation plan. PalSmith should create a plan first, ask only the most important missing questions, and wait for confirmation before any Pal Pack files are generated.

## Example 1: First-Principles Product Reviewer Pal

### What The User Can Say

```text
/pal PalSmith 帮我创建一个第一性原理产品评审 Pal，用来审查 AgentPal 的功能设计，重点看是否过度设计、是否符合第一性原理、是否能压缩复杂度。
```

### How PalSmith Should Understand It

- creation mode: `Human-to-Pal + Role-to-Pal`
- thinking style: first-principles product reasoning
- role: product reviewer
- job target: AgentPal feature design review
- safe name: `First-Principles Product Reviewer Pal`

### Minimum Questions

PalSmith should ask no more than three focused questions, such as:

1. Should this Pal review only AgentPal features, or any product feature proposal?
2. Should its output be a short memo, a scorecard, or a go / revise / stop decision?

### Assets The Plan Should Generate

- `identity/role.md`
- `identity/source-boundary.md`
- `knowledge/mental-models.md`
- `knowledge/decision-heuristics.md`
- `knowledge/anti-patterns.md`
- `workflows/feature-review-workflow.md`
- `skills/complexity-compression-skill.md`
- `memory/routing-decisions-template.md`
- `evals/cognitive-distillation-tests.md`
- `evals/role-task-tests.md`
- `marketplace/source-disclosure.md` if public release is later reviewed

### Boundary Reminder

This is a public-source-inspired thinking method, not a source-person Pal. Public release requires source review, non-representation wording, and uncertainty notes.

### Good Uses

- review whether a feature is over-designed
- reduce a product proposal to core user value
- propose a smaller MVP
- identify unsupported product claims

### Poor Uses

- final business approval
- investment advice
- claiming a source person approves the result
- automatic file edits or release decisions

## Example 2: Cautious Practical Risk Reviewer Pal

### What The User Can Say

```text
/pal PalSmith 帮我创建一个谨慎克制型风险审查 Pal。它要帮我审查项目、投资、合作中的风险，语气要谨慎、克制、务实，不能浮夸。
```

### How PalSmith Should Understand It

- creation mode: `Voice-to-Pal + Role-to-Pal`
- voice and personality: cautious, restrained, practical
- role: risk reviewer
- safe name: `Cautious Practical Risk Reviewer Pal`

### Minimum Questions

1. Which risk area should be tested first: project, investment, or partnership?
2. Should the output be a risk memo, exposure matrix, or go / no-go recommendation?

### Assets The Plan Should Generate

- `identity/personality.md`
- `identity/tone.md`
- `identity/speech-patterns.md`
- `identity/voice-boundary.md`
- `knowledge/risk-taxonomy.md`
- `knowledge/evidence-grading.md`
- `workflows/risk-review-workflow.md`
- `runbooks/escalation-runbook.md`
- `evals/voice-consistency-tests.md`
- `evals/role-task-tests.md`
- `evals/boundary-tests.md`

### Boundary Reminder

This is style-inspired. It must not copy protected source text or imply rights-holder representation. The role must still do real risk-review work; voice cannot replace evidence.

### Good Uses

- list known facts, assumptions, and unknowns
- produce downside scenarios
- design fallback and exit conditions
- mark high-risk items as requiring human review

### Poor Uses

- final legal, financial, or investment decision
- dramatic guarantees
- copied source wording
- using voice style to hide missing evidence

## Example 3: Private Presales Advisor Pal

### What The User Can Say

```text
/pal PalSmith 帮我把我们公司资深售前顾问的经验整理成一个私有售前 Pal。资料包括历史方案书、客户会议纪要、报价说明、需求澄清清单、常见异议处理、成交和失败复盘。这个 Pal 只在公司内部使用。
```

### How PalSmith Should Understand It

- creation mode: `Team-to-Pal + Doc-to-Pal + Role-to-Pal`
- source type: organization-authorized internal material
- role: private presales adviser
- safe name: `Private Presales Advisor Pal`
- publication target: private internal use

### Minimum Questions

1. Who is authorized to approve use of these materials?
2. Which customer identifiers, pricing details, or meeting notes must be excluded or de-identified?
3. Which workflow should be tested first: requirements clarification, proposal draft, quote risk, objection handling, or win/loss review?

### Assets The Plan Should Generate

- `identity/role.md`
- `identity/source-boundary.md`
- `knowledge/presales-domain-overview.md`
- `knowledge/requirements-clarification.md`
- `knowledge/objection-patterns.md`
- `workflows/discovery-to-proposal-workflow.md`
- `workflows/quote-risk-review-workflow.md`
- `skills/proposal-outline-skill.md`
- `skills/quote-risk-review-skill.md`
- `memory/private-source-index-template.md`
- `memory/task-history-template.md`
- `reports/source-classification-report.md`
- `evals/privacy-boundary-tests.md`
- `evals/role-task-tests.md`

### Boundary Reminder

Private company material stays private by default. Customer data, pricing details, meeting notes, and account strategy must not enter public examples or public Marketplace metadata unless de-identified, authorized, reviewed, and explicitly approved.

### Good Uses

- generate requirements clarification checklists
- draft proposal outlines from approved templates
- check quote and delivery risk
- summarize objection patterns
- record win/loss lessons as private memory candidates

### Poor Uses

- public Marketplace listing by default
- automatic CRM read/write
- sending external messages
- storing customer-private data in public assets

## How To Read A PalSmith Creation Plan

Look for these sections:

- creation mode
- assumptions and missing information
- proposed Pal identity
- thinking style, if any
- voice and personality, if any
- role responsibilities
- job knowledge
- Skill / Agent candidates
- memory and retrospective design
- collaboration boundary
- eval plan
- private / public / Marketplace boundary
- Runtime Task Package boundary

If a plan skips boundaries, memory, evals, or Skill / Agent evidence, treat it as incomplete.
