# AI Team Builder Protocol

Status: PalSmith v0.6 no-code protocol update.

AI Team Builder turns a plain user goal into a small, understandable Pal team design before any files are created.

## Trigger Judgement

Any current Pal may consider PalSmith when AI judgement says the request is about Pal team design, Pal creation, or Pal asset governance. This is not keyword routing. AgentPal Core does not act as a semantic classifier or planner.

Mira commonly calls this protocol when the user asks to create, assemble, or
govern a durable team. Other Pals may call it when their current task exposes a
Pal / Team asset gap.

## Wizard Steps

1. Understand the user's goal.
2. Identify the business or creative scenario.
3. Decide whether an existing Team Pack can be reused.
4. Recommend team size.
5. Propose team name and stable `team_id`.
6. Propose Pal list from current contacts / registry when possible.
7. Decide whether any new Pal is truly needed.
8. For every new Pal, apply the human-name + role-title naming rule.
9. Define each Pal's responsibilities.
10. Define what each Pal does not own.
11. Select owner Pal.
12. Select verifier Pal when verification is needed.
13. Select consultant Pals when they add material value.
14. Mark team-local Pals vs global-contact candidates.
15. Propose shared knowledge.
16. Propose shared workflow.
17. Propose team eval and closure gate.
18. Draft team Context Packet.
19. Draft team capability map.
20. Draft Team Asset Preflight and member Pal Asset Preflight requirements.
21. Ask user confirmation before creation task package.

## Team Size Rule

- Simple team: 2-3 Pals.
- Default team: 3-5 Pals.
- Standard team: 4-5 Pals.
- Complex team: 6-8 Pals.
- More than 8 Pals requires a reason and explicit user confirmation.

## Forbidden Defaults

- Do not create 10+ Pals from one short request.
- Do not add every Pal to global contacts.
- Do not give every Pal handoff permission.
- Do not give every Pal user memory access.
- Do not create a Pal whose display name is only a job title.
- Do not assign Faye to routine business execution after a workflow and team
  exist unless the task is process redesign.
- Do not turn team examples into keyword routes.
- Do not claim automatic parallel execution, background scheduling, or Runtime
  team dispatch.

## Output

A beginner-friendly design proposal first, then a Runtime Task Package only
after the user accepts the design.

The Runtime Task Package should reference:

- `core/team-asset-preflight-protocol.md`;
- `core/team-pal-asset-priority-protocol.md`;
- `core/pal-asset-preflight-protocol.md`;
- `orchestration/workflow-execution-contract-protocol.md`;
- `orchestration/workflow-closure-gate-protocol.md`;
- `standards/pal-asset/pal-naming-and-import-conflict-protocol.md`.
