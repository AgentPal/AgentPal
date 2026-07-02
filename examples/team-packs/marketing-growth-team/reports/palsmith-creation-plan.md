# PalSmith Creation Plan: Marketing Growth Team

Status: v0.6 Team Pack creation case. This is a no-code creation plan and generated example asset set, not a runtime team scheduler.

## User Request

"Create a promotion team responsible for AgentPal content topics, promotional copy, visual requirements, publishing plans, and performance retrospectives."

## Need Understanding

The user is asking for a durable team, not a one-off content draft. The team needs stable roles, shared workflow, public-safe knowledge, an eval gate, routing boundaries, and repeatable reports.

## Team Goal

Create a reusable Marketing Growth Team for AgentPal promotion work.

## Consultation Decision

| Candidate | Consult? | Reason |
| --- | --- | --- |
| Faye | no for creation; optional only for workflow redesign | This is not from-zero business process discovery. Faye must not become a routine promotion executor. |
| Nova | yes | Promotion needs audience, value proposition, positioning, and message strategy. |
| Vega | optional | Use when topics need trend evidence, source notes, or claim boundaries. |
| Luma | unavailable | `Luma` is not registered in the current central contacts. Do not reference Luma as an existing Pal. |
| Quinn | conditional | Use for public claim risk, brand risk, and completion review when risk warrants it. |
| Harper | yes | Existing Pal for writing, copy, tone, and public-facing content. |

## Existing Pal Sufficiency

Existing Pals cover most of the team:

- Mira: team conductor.
- Nova: positioning lead.
- Vega: research support.
- Harper: copy lead.
- Quinn: conditional quality reviewer.

Missing durable capabilities:

- visual direction / visual production;
- real publishing operation / analytics retrieval.

These are represented as open roles for this Team Pack. No new Pal is created in this pass because the user did not ask to create a dedicated visual or publishing Pal, and current official contacts do not include a registered visual Pal.

## New Pal Decision

- new_pals_needed: no
- reason: the Team Pack can be useful with existing Pals plus open roles. Creating new Pals would require additional user confirmation, naming, role scope, source material, and evals.

If the user later requests new Pal creation, suggested human-name + role-title options:

| Suggested display_name | role_title | contact_label |
| --- | --- | --- |
| Iris | Visual Direction Lead | Iris · Visual Direction |
| Rowan | Publishing Operations Lead | Rowan · Publishing Ops |

Forbidden display names:

- `Visual Pal`
- `Design Pal`
- `Promotion Pal`
- `Copywriting Pal`

## Naming Conflict Handling

Before creating any new Pal, PalSmith must check current contacts and aliases. If the human display name conflicts, keep the stable `canonical_id` and disambiguate through `contact_label`, not by turning the role into the display name.

## Team Pack Plan

- target_path: `examples/team-packs/marketing-growth-team/`
- team_id: `marketing-growth-team`
- display_name: `Marketing Growth Team`
- default_entry_pal: `mira-main`
- Team Asset Preflight: required before team tasks.
- member Pal Asset Preflight: required for assigned member work.
- Workflow Execution Contract: required for concrete weekly content tasks.
- Closure Gate: required before final reports.

## Initial Workflow

`workflows/weekly-agentpal-promotion-content.md` initializes the recurring workflow:

1. promotion objective;
2. content themes;
3. copy;
4. visual requirements;
5. risk / brand review;
6. publishing plan;
7. retrospective.

## Initial Eval

`evals/definition-of-done.md` checks campaign goal, audience, topics, copy, visual requirements, current/future AgentPal claim boundaries, publishing evidence, verification decision, and writeback decision.

## Creation Result

This pass creates the Team Pack example and the creation plan. It does not register the team globally, create new Pals, update central contacts, or run real publishing.
