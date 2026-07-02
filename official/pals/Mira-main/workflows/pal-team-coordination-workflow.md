# Pal Team Coordination Workflow

## Trigger

A user request has multiple material stages, multiple likely owners, or requires final synthesis across specialist outputs.

For v0.6, this workflow also covers requests that should use an existing Team
Pack or should be handed to PalSmith for Team Pack creation planning.

## Inputs

- User objective.
- Stage list.
- Candidate owners from contacts / registry.
- Candidate Team Pack, if named or clearly relevant.
- Team Pack files, when selected: `TEAM.md`, `team.json`, `roster.json`, and
  the minimum relevant team workflow / eval / knowledge / runbook / memory
  placeholders.
- Context boundaries.
- Verification needs.

## Entry Judgement

Mira judges the entry case before creating any task package:

- ordinary single-owner task: use Fast Route to the owner Pal when appropriate;
- composite task without stable team assets: stage the work and select owner
  Pals case-by-case;
- user names a team or describes a team-like goal in natural language: inspect matching or fitting Team Packs first, then verify fit;
- user asks to create, assemble, find, or use a team: first run Team Pack discovery; if a fitting Team Pack exists, select and reuse it before considering PalSmith;
- user asks to discover or redesign a business process: Faye may advise the
  workflow framing, then PalSmith may create the Team Pack if durable assets are
  needed;
- existing team daily execution: use the Team Pack and member Pals, not Faye as
  a default executor, unless the process itself must be redesigned.

These are judgement patterns, not keyword routes.

## Steps

1. Break the deliverable into material stages.
2. Assign provisional owner candidates through AI judgement.
3. Run Team Pack first discovery when the request is team-like, then decide whether an existing Team Pack is needed.
4. If a Team Pack is selected, run Team Asset Preflight before member work.
5. Select the Team Workflow and Team Eval that fit the task.
6. Generate a Workflow Execution Contract.
7. Assign workflow steps to team roles and candidate Pals through current
   contacts, roster, and Pal boundary checks.
8. Require each selected member Pal to run Pal Asset Preflight before work.
9. Identify runtime or tool execution only after Pal-layer ownership.
10. Build Context Packets for stages that need handoff or delegation.
11. Track progress, blockers, skipped steps, and verification evidence.
12. Apply the Closure Gate before final delivery.
13. Prepare public-safe Team / Pal / Routing Memory candidates when useful.
14. Synthesize results without erasing specialist ownership.

## Decision points

- Is the task composite or single-owner?
- Is the user asking for an existing Team Pack or a new Team Pack?
- Does the Team Pack workflow fit the current task and project constraints?
- Which stages require specialist judgement?
- Does any assigned Pal's boundary veto the team role?
- Should an existing Team Pack be reused before PalSmith is involved?
- If PalSmith is involved, what Team Pack first discovery result proves creation / repair / governance is needed?
- Which stages need user approval?
- Is any future orchestration document being mistaken for active execution?

## Outputs

Staged judgement, Team Asset Preflight summary, Workflow Execution Contract,
member Pal Asset Preflight summaries, stage task packages, progress reports,
Closure Gate result, final synthesis, and remaining issues.

## Quality checks

- Stage owners are named before execution.
- Team Pack selection is justified by current task fit, not by keyword.
- Team Workflow and Team Eval are identified when team mode is used.
- Pal boundaries override team assignments.
- Faye is used for business process discovery or redesign, not routine business
  execution after a team workflow already exists.
- Runtime-only implementation stages are not used.
- No active parallel child workflows are claimed.
- Verification is reported honestly.

## Required user confirmation

Required before expanding stage scope, reading broad context, creating or
upgrading Team Pack / Pal Pack assets, changing contacts / registry, or
performing high-risk execution.

## Evidence to return

Return Team Pack inspected, team workflow selected, stage owner judgements,
context used, execution evidence, not-run checks, skipped steps, veto / replan
decisions, and unresolved questions.
