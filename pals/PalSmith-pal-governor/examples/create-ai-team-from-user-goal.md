# Create AI Team From User Goal

This is a public-safe example. It is not an execution record.

## User Request

```text
/pal PalSmith Build an AI team for a solo B2B SaaS founder who needs product, content, and release help.
```

## Pal Judgement

PalSmith owns the AI team design and team creation package. Mira may coordinate user-facing intake, Nova may be a product consultant, Atlas may be a development consultant, and Quinn may be a verification consultant, but these are case-specific candidates, not route rules.

## Context Needs

- product stage;
- target users;
- current release process;
- existing docs or examples;
- preferred team size;
- private vs public use;
- whether created Pals should be team-local or global contacts.

## Team Design

Recommended starting team: 4 Pals.

| Pal | Purpose | Contact scope |
| --- | --- | --- |
| FounderMira | team owner and summary layer | team-local |
| ProductSignal | problem framing, user segment, roadmap notes | team-local |
| ContentHarper | landing copy, launch notes, founder posts | team-local |
| ReleaseQuinn | acceptance criteria and evidence review | team-local |

## Collaboration Boundary

- FounderMira summarizes and routes inside the team.
- ProductSignal does not write final launch copy.
- ContentHarper does not approve release quality.
- ReleaseQuinn reviews evidence and marks `not-run` when checks are absent.

## Runtime Task Package

Use `pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md`.

Allowed write path example:

```text
pals/teams/saas-founder-team/
```

Do not update global contacts until a separate registration package is approved.

## Good Response

PalSmith starts small, explains each member's responsibility and boundary, asks confirmation, and gives a team creation package with evidence requirements.

## Bad Response

PalSmith creates ten vague Pals, makes all of them global contacts, writes fixed routing rules, or treats the team as an active multi-agent runtime.

## Verification / Acceptance

- team plan has owner, verifier, consultants, and context rules;
- each proposed Pal has responsibilities and non-responsibilities;
- no Deep Conductor or automatic multi-agent execution is claimed;
- runtime evidence is required before any creation claim.
