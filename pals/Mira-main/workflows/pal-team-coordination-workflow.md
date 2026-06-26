# Pal Team Coordination Workflow

## Trigger

A user request has multiple material stages, multiple likely owners, or requires final synthesis across specialist outputs.

## Inputs

- User objective.
- Stage list.
- Candidate owners from contacts / registry.
- Context boundaries.
- Verification needs.

## Steps

1. Break the deliverable into material stages.
2. Assign provisional owner candidates through AI judgement.
3. Identify runtime or tool execution only after Pal-layer ownership.
4. Build Context Packets for stages that need handoff or delegation.
5. Track progress, blockers, and verification evidence.
6. Synthesize results without erasing specialist ownership.

## Decision points

- Is the task composite or single-owner?
- Which stages require specialist judgement?
- Which stages need user approval?
- Is any future orchestration document being mistaken for active execution?

## Outputs

Staged judgement, stage task packages, progress reports, final synthesis, and remaining issues.

## Quality checks

- Stage owners are named before execution.
- Runtime-only implementation stages are not used.
- No active parallel child workflows are claimed.
- Verification is reported honestly.

## Required user confirmation

Required before expanding stage scope, reading broad context, or performing high-risk execution.

## Evidence to return

Return stage owner judgements, context used, execution evidence, not-run checks, and unresolved questions.
