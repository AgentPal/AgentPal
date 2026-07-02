# Asset Loading Gate

Status: R198 global no-code gate.

Use this gate before substantive Pal-owned work. It keeps Pal work grounded in
assets instead of names, persona-only prompts, generic model knowledge, or blind
tool calls.

For v0.6 pre-task evidence, use `core/pal-asset-preflight-protocol.md` and
`templates/pal/pal-asset-preflight.md`. When a Team Pack governs the task, run
`core/team-asset-preflight-protocol.md` before the individual Pal preflight.

## Gate Questions

Before acting, answer these questions:

1. Who is the current target Pal?
2. What is the task type?
3. Does the task need identity assets?
4. Does the task need voice or personality assets?
5. Does the task need thinking, cognitive model, or decision assets?
6. Does the task need domain knowledge?
7. Does the task need Pal-owned Skills?
8. Does the task need workflows or runbooks?
9. Does the task need runtime / Agent usage policy?
10. Does the task need memory or learning scope?
11. Does the task need eval or quality gate assets?
12. Which asset paths are required?
13. Which assets were loaded?
14. Which assets are missing?
15. Is the task allowed to continue?
16. Does it need a Missing Asset Plan?
17. Does it need user confirmation before any write or tool call?

## Go / No-Go Labels

Use one of these labels:

- `go_lightweight`: enough for simple chat, typo fix, or narrow clarification.
- `go_asset_grounded`: required assets loaded and reflected in the plan.
- `go_with_limited_fallback`: some assets missing, but safe fallback is named.
- `partial_then_missing_asset_plan`: answer the safe portion and propose missing
  assets.
- `blocked_missing_core_asset`: stop because core assets are missing.
- `blocked_user_confirmation_required`: stop before write, tool call, private
  memory, publication, contacts, discovery, or Marketplace-impacting action.

## Required Minimal Asset Set

For most substantive owner-Pal tasks:

- `PAL.md`
- `pal.json`
- `SKILL.md`
- task-relevant `core/output-contract.md` or equivalent
- 1-3 relevant knowledge, workflow, Skill, runtime policy, or eval assets

For user custom Pals, use their own `SKILL.md` read order when present.

## Tool Use Gate

Before any host tool call, the Pal must state:

- which Pal-owned assets shaped the tool request;
- why the tool is useful;
- what the tool is not allowed to decide;
- how the Pal will review the tool output;
- whether the tool call requires user confirmation.

If no Pal-owned asset shaped the request, do not call the tool as Pal work.

Tool output cannot substitute for Pal assets. After the host tool returns, the
Pal must review the result against its own loaded quality, workflow, eval, or
output-contract assets before claiming usefulness or completion.

## Output Requirement

For complex tasks, emit or internally maintain a Task Asset Packet before the
work and an Asset Use Summary after the work.

For lightweight tasks, a concise one-sentence asset note is sufficient when the
user asks.

## Team Task Note

When the task is governed by a Team Pack, the Team Asset Preflight selects the
team workflow, team eval, team knowledge, and member steps first. Each assigned
member Pal then runs this gate for its own step. Team assignment cannot override
the Pal's own responsibility boundary.
