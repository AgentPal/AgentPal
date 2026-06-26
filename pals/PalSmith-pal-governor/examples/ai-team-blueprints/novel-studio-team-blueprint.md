# Novel Studio AI Team Blueprint

This is a blueprint, not an installed Pal. After user confirmation, PalSmith can generate corresponding Pal Creation / Team Creation Task Packages.

## 适合谁

Writers who want a small creative studio for outlining, character consistency, scene drafting, revision, and continuity review.

## 用户可以怎么说

```text
/pal PalSmith 帮我搭建一个小说工作室 AI 团队。
```

## 推荐团队规模

5 Pals. This stays within the default 3-5 range.

## 推荐 Pal 列表

| Pal | Role | Responsibilities | Not Responsible For | Visibility |
| --- | --- | --- | --- | --- |
| Story Architect | structure | premise, arcs, chapter outline, pacing | final creative decisions | team-local |
| Character Keeper | continuity | character profiles, motivations, relationship notes | rewriting the author's voice | team-local |
| Scene Drafter | drafting | scene drafts, sensory detail, dialogue alternatives | publishing decisions | team-local |
| Revision Editor | editing | clarity, rhythm, consistency suggestions | replacing human author approval | team-local |
| Canon Verifier | verifier | timeline, lore, contradiction checks | owning plot direction | global candidate |

## Owner / Verifier / Consultant

- Owner: Story Architect.
- Verifier: Canon Verifier.
- Consultants: Character Keeper, Scene Drafter, Revision Editor.

## Team-Local vs Global Contacts

Keep creative Pals team-local for each project. Canon Verifier can become global if it reviews only project-supplied canon and not private drafts by default.

## Shared Knowledge

- premise
- world rules
- character sheets
- chapter outline
- style preferences
- banned tropes or sensitive topics

## Shared Workflows

- outline review
- character consistency pass
- scene draft request
- revision pass
- canon check

## Context Packet Rules

Pass only the relevant chapter, scene, character sheet, or canon note. Do not pass the full manuscript unless the user approves.

## Quality Gate

Before stable status, each Pal needs a sample response, voice boundary, and clear rule that the author owns final creative choices.

## Eval Lab Starter

- Create a chapter outline from premise.
- Check character contradiction.
- Draft one scene from an outline.
- Revise a paragraph for tension.
- Refuse to claim authorship or publishing readiness without user approval.

## Runtime Task Package 入口

Start with `AI Team Builder Task Package`, then create only the accepted Pals through Pal creation packages.

## 用户确认问题

- What genre and language should the team support?
- Should the team follow a specific style guide?
- Can the Runtime read existing manuscript files?
- Should the team be private to one novel?
- Which Pal should be created first?

## 不建议一开始创建的 Pal

- Marketing Pal.
- Publishing contract Pal.
- Full-manuscript memory Pal without privacy confirmation.
- Trend-chasing Pal that overrides the author's taste.
