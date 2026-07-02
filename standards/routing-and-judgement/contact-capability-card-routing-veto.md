# Contact Capability Card Routing Veto

This standard mirrors the central contacts protocol in
`workspace/organization/contacts/routing-veto.md`.

It applies to Mira, directly called Pals, current owner Pals, and project-bound
runtime sessions.

## Principle

Capability cards are boundary-aware judgement inputs. They are not semantic
routes.

The AI first makes a case-specific candidate selection from the user request,
context, deliverable, risk, current contacts, available team roster, and host
runtime evidence. Then it checks the selected Pal's capability card. If the
assignment conflicts with an explicit forbidden boundary, Routing Veto applies.

## Required Outcome

When veto applies, the task must not proceed with that Pal as owner for the
forbidden role. The current AI should:

- select another candidate Pal;
- create a child step for the proper specialist;
- use a team roster when a relevant team exists;
- ask the user for confirmation when ownership is ambiguous;
- or mark the route blocked.

The final plan or report should include a short veto reason.

## Non-Goals

- no keyword routes;
- no fixed `development = Atlas` rule;
- no fixed `quality = Quinn` rule;
- no fixed `business = Faye` rule;
- no runtime plugin, CLI, database, background service, or UI.
