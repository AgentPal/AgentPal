# Cross-Border Commerce AI Team Blueprint

This is a blueprint, not an installed Pal. After user confirmation, PalSmith can generate corresponding Pal Creation / Team Creation Task Packages.

## 适合谁

Small sellers, operators, or agencies that need help with product selection, listings, ads, customer support, and operational review.

## 用户可以怎么说

```text
/pal PalSmith 帮我搭建一个跨境电商 AI 团队。
```

## 推荐团队规模

5 Pals. This stays within the default 3-5 range.

## 推荐 Pal 列表

| Pal | Role | Responsibilities | Not Responsible For | Visibility |
| --- | --- | --- | --- | --- |
| Market Scout | product-research | product ideas, competitor notes, demand signals | legal compliance, final purchasing decisions | team-local |
| Listing Writer | content | product titles, bullet points, FAQ drafts | claims approval, platform policy judgement | team-local |
| Ad Planner | growth | campaign hypotheses, test plans, budget questions | spending money, changing ad accounts | team-local |
| Support Drafter | service | reply drafts, refund wording, tone consistency | binding customer decisions | team-local |
| Commerce Verifier | verifier | consistency checks, risk notes, publish readiness | owning business strategy | global candidate |

## Owner / Verifier / Consultant

- Owner: Market Scout for team intake and task routing.
- Verifier: Commerce Verifier.
- Consultants: Listing Writer, Ad Planner, Support Drafter.

## Team-Local vs Global Contacts

Start with all Pals team-local except Commerce Verifier. Promote only Pals with clear reusable value to global contacts after testing.

## Shared Knowledge

- product categories and excluded categories
- target countries and languages
- platform policy excerpts supplied by the user
- brand voice notes
- support tone rules

## Shared Workflows

- product idea intake
- listing draft review
- ad test planning
- customer reply drafting
- weekly operational review

## Context Packet Rules

Pass only the product, market, platform, language, and task-specific evidence needed for the current step. Do not pass all store data or private customer data by default.

## Quality Gate

Before stable status, each Pal needs responsibility clarity, sample outputs, non-responsibility notes, and evidence that Commerce Verifier can review high-risk claims.

## Eval Lab Starter

- Product idea request.
- Listing improvement request.
- Ad test planning request.
- Customer complaint reply request.
- Risky request that asks for unsupported claims.

## Runtime Task Package 入口

Start with `AI Team Builder Task Package`. After user confirmation, use `Pal Team Creation Task Package` plus one `Pal Creation Task Package` per accepted Pal if needed.

## 用户确认问题

- Which marketplace and country should the team focus on?
- Should the team be private, team-local, or partially global?
- Which Pals should be created first?
- Is any store, customer, or sales data allowed to be read?
- Should PalSmith prepare files now or only produce the design?

## 不建议一开始创建的 Pal

- Finance automation Pal.
- Account-login Pal.
- Legal compliance Pal without verified legal source boundaries.
- Large analytics Pal that requires private sales databases.
