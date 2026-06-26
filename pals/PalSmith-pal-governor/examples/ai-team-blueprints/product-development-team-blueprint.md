# Product Development AI Team Blueprint

This is a blueprint, not an installed Pal. After user confirmation, PalSmith can generate corresponding Pal Creation / Team Creation Task Packages.

## 适合谁

Founders, product managers, and small teams that need help turning ideas into requirements, prioritization, design review, delivery planning, and quality evidence.

## 用户可以怎么说

```text
/pal PalSmith 帮我搭建一个产品开发 AI 团队。
```

## 推荐团队规模

5 Pals. This stays within the default 3-5 range.

## 推荐 Pal 列表

| Pal | Role | Responsibilities | Not Responsible For | Visibility |
| --- | --- | --- | --- | --- |
| Discovery Partner | product-discovery | user problem framing, assumptions, interview questions | making business commitments | team-local |
| Requirement Writer | requirements | PRD drafts, acceptance criteria, scope boundaries | final roadmap approval | team-local |
| Design Reviewer | design-review | workflow critique, usability risks, accessibility notes | producing hidden UI implementation | team-local |
| Delivery Planner | delivery | milestones, dependency questions, rollout plan | executing code or deployment | team-local |
| Quality Verifier | verifier | test evidence checklist, release risk report | declaring release without evidence | global candidate |

## Owner / Verifier / Consultant

- Owner: Requirement Writer for artifact coordination.
- Verifier: Quality Verifier.
- Consultants: Discovery Partner, Design Reviewer, Delivery Planner.

## Team-Local vs Global Contacts

Quality Verifier can be a global contact if it follows evidence-first reporting. Keep product-specific Pals team-local by default.

## Shared Knowledge

- product vision
- target users
- scope boundaries
- design principles
- release criteria
- known constraints

## Shared Workflows

- idea intake
- PRD drafting
- design review
- delivery planning
- release readiness review

## Context Packet Rules

Pass only the current feature, user segment, PRD section, or design artifact. Do not pass private customer research or roadmap files without confirmation.

## Quality Gate

Before stable status, each Pal needs clear ownership, acceptance examples, refusal boundaries, and a Quality Verifier pass that separates evidence from assumptions.

## Eval Lab Starter

- Turn an idea into a problem statement.
- Draft acceptance criteria.
- Review a product flow.
- Create a rollout checklist.
- Identify missing evidence before release.

## Runtime Task Package 入口

Start with `AI Team Builder Task Package`, then use `Pal Readiness Review Task Package` before marking the team stable or publish-ready.

## 用户确认问题

- Is this for a product team, solo builder, or agency?
- What product area should the team support first?
- Which private product docs may be read?
- Should output be public-safe?
- Which Pal should be created first?

## 不建议一开始创建的 Pal

- Deployment Pal.
- Payment or billing automation Pal.
- Customer-data mining Pal.
- Roadmap decision Pal that overrides human product ownership.
