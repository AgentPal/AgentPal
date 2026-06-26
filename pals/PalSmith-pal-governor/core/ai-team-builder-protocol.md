# AI Team Builder Protocol

Status: PalSmith v0.3 no-code protocol.

AI Team Builder turns a plain user goal into a small, understandable Pal team design before any files are created.

## Trigger Judgement

Any current Pal may consider PalSmith when AI judgement says the request is about Pal team design, Pal creation, or Pal asset governance. This is not keyword routing. AgentPal Core does not act as a semantic classifier or planner.

## Wizard Steps

1. Understand the user's goal.
2. Identify the business or creative scenario.
3. Recommend team size.
4. Propose Pal list.
5. Define each Pal's responsibilities.
6. Define what each Pal does not own.
7. Select owner Pal.
8. Select verifier Pal.
9. Select consultant Pals.
10. Mark team-local Pals vs global-contact candidates.
11. Propose shared knowledge.
12. Propose shared workflow.
13. Draft team Context Packet.
14. Draft team capability map.
15. Draft team Eval Lab plan.
16. Ask user confirmation before creation task package.

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

## Output

A beginner-friendly design proposal first, then a Runtime Task Package only after the user accepts the design.
