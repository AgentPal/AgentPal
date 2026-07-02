# Routing Veto Protocol

Routing Veto is a boundary check after AI owner judgement selects a candidate
Pal. It is not keyword routing and must not become a fixed route table.

## When To Use

Use this protocol when Mira or a current owner Pal is about to assign, delegate,
hand off, consult, or name a verifier from central contacts.

## Required Check

1. Select candidate Pal(s) by case-specific AI judgement from the current user
   request, expected deliverable, context, risk, available runtime evidence, and
   current contacts.
2. Read the selected candidate's Contact Capability Card when it exists.
3. Check:
   - `forbidden_task_types`
   - `team_roles_forbidden`
   - `do_not_use_when`
   - `handoff_after`
   - `risk_notes`
4. If the current assignment clearly matches a forbidden boundary, trigger
   Routing Veto.
5. After veto, choose another Pal, create a team or child step, ask the user for
   confirmation, or mark the route `blocked`.
6. Record a short reason in the task plan, routing explanation, or report.

## Veto Outcomes

When veto applies, the selected Pal must not continue as owner for the forbidden
assignment. The current AI should choose one of these outcomes:

- select another Pal by case-specific judgement;
- use an existing Team Pack and its roster when the task is team-shaped;
- create a child Step for the right specialist while the current owner keeps
  only its valid stage;
- ask the user for confirmation when ownership remains ambiguous;
- mark the route `blocked` or `replanned` when no safe owner is available.

## Veto Reason Shape

```text
vetoed_pal: Faye
reason: Faye is for business flow design and team setup; this request is routine execution after the team already exists.
next_action: use the existing team owner or select a concrete executor Pal by AI judgement.
```

## Common Boundary Examples

- Faye may own FDE business flow discovery, blueprinting, team setup, and
  workflow design. Veto Faye as primary owner for established-team daily
  execution, coding, video editing, routine copywriting, testing, or release
  verification.
- Quinn may own acceptance, evidence review, quality judgement, and release
  gates. Veto Quinn as primary implementer, routine executor, or claimed test
  runner without runtime evidence.
- Atlas may own development planning, repository handoff, technical
  implementation judgement, and engineering evidence review. Veto Atlas as a
  universal owner for non-development work or as final independent verifier.
- PalSmith may own Pal / Team creation, upgrade, import/export, capability map,
  readiness, and governance work. Veto PalSmith as owner for ordinary business,
  product, writing, video, coding, or release execution.

## Important Boundary

Routing Veto prevents clearly invalid assignments. It does not choose owners by
keywords. A task word such as "code", "test", "business", "video", or "release"
must never automatically select or reject a Pal without case-specific judgement.
