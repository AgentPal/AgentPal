# Workflow Final Report Template

Use this after the Closure Gate runs.

```markdown
# Workflow Final Report

## User Goal

<Restate the user goal.>

## Workflow Summary

- workflow_id:
- mode:
- team_id:
- owner_pal:
- risk_level:
- closure_gate_outcome: pass | partial | blocked | fail

## Actual Participants

| Participant | Type | Role | Step IDs | Actual Output Or Status |
| --- | --- | --- | --- | --- |
|  | pal | owner |  |  |

Do not list a participant here unless the contract contains output, evidence, blocker, skip, cancel, failure, or replan record for that participant.

## Step Closure

| Step | Assignee | Status | Output / Evidence | Context Access List | Notes |
| --- | --- | --- | --- | --- | --- |
| S1 |  |  |  |  |  |

## Verification

| Verified Step | Verifier | Result | Evidence | Remaining Risk |
| --- | --- | --- | --- | --- |
|  |  | pass |  |  |

If verification was skipped, say `skipped` and include the skip reason. Do not call it passed.

## Skipped / Blocked / Failed / Cancelled / Replanned

| Step | Status | Reason | Effect On User Goal | Replacement |
| --- | --- | --- | --- | --- |
|  | skipped |  |  |  |

## Child Step Return

| Parent Step | Child Step | Child Status | Returned Output / Reason | Parent Handling |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Context Boundary

- Context Access Lists used:
- Reads outside allowed context: none | listed below | unknown
- Parallel review isolation preserved: yes | no | not applicable
- Unknown or not-run evidence:

## Memory / Routing Writeback

- Pal Memory: none | candidate | written | blocked
- Team Memory: none | candidate | written | blocked
- Routing Memory: none | candidate | written | blocked
- Runtime Skill usage memory: none | candidate | written | blocked
- Verification memory: none | candidate | written | blocked
- Privacy notes:

## Remaining Risks

- <risk or none>

## Next Step

<Recommended next step, unblock request, or done statement.>
```

## Report Rule

If Closure Gate outcome is not `pass`, the report must not say the workflow fully completed. Use `partial`, `blocked`, or `failed` language and name the open risk.
