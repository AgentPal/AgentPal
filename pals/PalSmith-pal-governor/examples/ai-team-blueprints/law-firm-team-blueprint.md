# Law Firm AI Team Blueprint

This is a blueprint, not an installed Pal. After user confirmation, PalSmith can generate corresponding Pal Creation / Team Creation Task Packages.

## 适合谁

Small law firms or legal operations teams that need internal drafting, intake organization, knowledge retrieval, and review support while preserving professional boundaries.

## 用户可以怎么说

```text
/pal PalSmith 帮我设计一个律所 AI 工作团队。
```

## 推荐团队规模

4 Pals. This stays within the default 3-5 range.

## 推荐 Pal 列表

| Pal | Role | Responsibilities | Not Responsible For | Visibility |
| --- | --- | --- | --- | --- |
| Intake Organizer | intake | matter summaries, missing information lists, timeline drafts | legal advice, client acceptance | team-local |
| Research Assistant | research | source list, jurisdiction notes, citation summaries | final legal interpretation | team-local |
| Drafting Assistant | drafting | memo outlines, clause alternatives, client-letter drafts | final document approval | team-local |
| Ethics Verifier | verifier | confidentiality, unauthorized-practice, citation and disclaimer checks | owning client strategy | global candidate |

## Owner / Verifier / Consultant

- Owner: Intake Organizer for matter context.
- Verifier: Ethics Verifier.
- Consultants: Research Assistant and Drafting Assistant.

## Team-Local vs Global Contacts

Keep the team local by default. Ethics Verifier may become a global contact only if its scope is general safety review, not legal advice.

## Shared Knowledge

- firm-approved disclaimers
- jurisdiction boundaries
- document style guide
- citation format expectations
- confidentiality handling rules

## Shared Workflows

- client intake summary
- legal research brief
- memo draft review
- client-letter draft review
- confidentiality and source check

## Context Packet Rules

Pass only matter-specific facts explicitly approved by the user. Do not pass private client files, privileged communications, or full case records by default.

## Quality Gate

Before stable status, every Pal must state that it does not provide final legal advice. Ethics Verifier must block unsupported authority claims and unauthorized-practice wording.

## Eval Lab Starter

- Intake summary from user-provided facts.
- Research question with jurisdiction scope.
- Draft memo outline.
- Risky request asking for guaranteed legal outcome.
- Confidentiality boundary check.

## Runtime Task Package 入口

Start with `AI Team Builder Task Package`, then `Pal Team Governance Task Package` for professional-boundary review before any creation package.

## 用户确认问题

- Which jurisdiction and practice area should the team support?
- Is this for internal drafting only?
- What confidentiality rules should be hard constraints?
- Which reference materials may the Runtime read?
- Should any Pal be global, or should all remain team-local?

## 不建议一开始创建的 Pal

- Court filing automation Pal.
- Client advice Pal.
- Billing or trust-account Pal.
- Any Pal that claims to replace attorney review.
