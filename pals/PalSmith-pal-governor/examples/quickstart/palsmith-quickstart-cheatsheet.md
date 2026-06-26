# PalSmith Quickstart Cheatsheet

Status: PalSmith v0.4 quickstart aid.

This cheatsheet is for users who want a one-page reminder of how to start with PalSmith. It is not a command script, not a route table, and not proof that any Runtime action has happened.

## Common One-Sentence Entrances

```text
/pal PalSmith 帮我创建一个个人工作 Pal
/pal PalSmith 帮我搭建一个跨境电商 AI 团队
/pal PalSmith 这个 Pal 可以发布了吗
/pal PalSmith 从 GitHub 导入这个 Pal，并验证能不能用
/pal PalSmith 这个 Pal 是否真的能被 /pal 调用
```

These are few-shot examples. AgentPal does not route by keyword. The current Pal and current Brain / AI judge whether PalSmith should consult, receive a delegation, or receive a handoff.

## What PalSmith Asks First

- What outcome should the Pal or team own?
- What should it not own?
- Is this private, team-local, or a global contact candidate?
- Should memory be excluded, explicitly scoped, or not read at all?
- Is the output for drafting, testing, internal use, or public release?
- Is the user asking for a plan only, or a confirmed Runtime Task Package?

## When User Confirmation Is Required

Confirmation is required before:

- creating or overwriting files
- copying, importing, or exporting a Pal
- reading private memory, state, reports, or project data
- writing registry / contacts entries
- changing lifecycle or publish-readiness status
- running a network fetch through the current Agent Runtime
- restoring a snapshot or rollback target

## When PalSmith Uses Each Path

| Path | Use It When AI Judgement Says | First Output |
| --- | --- | --- |
| Pal Creation | the user wants one new Pal | design + Pal Creation Task Package |
| AI Team Builder | the user wants a small AI team | 3-5 Pal team proposal |
| Team Governance | the team needs owner/verifier/contact boundaries | governance report |
| Eval Lab | the user asks if a Pal can be used | eval checklist and result |
| Readiness Review | the user asks if a Pal can publish | readiness matrix result |
| Import Verification | the source is GitHub or local external content | staging and risk plan |
| Export | the user wants a shareable or private copy | clean or with-memory export package |

## What PalSmith Will Not Do Automatically

- install software
- run a CLI, scanner, validator, importer, exporter, daemon, or UI
- execute imported scripts
- add ordinary Skills to contacts
- publish to GitHub
- read all memory by default
- mark something `publish-ready` without evidence
- treat a blueprint as an installed Pal

## Best First Reply Shape

```text
PalSmith：I understand the goal. I will first design a small Pal or team, list responsibilities and non-responsibilities, ask for confirmation, then prepare a Runtime Task Package. I will not write files or claim runtime execution without evidence.
```
