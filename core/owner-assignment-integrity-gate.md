# Owner Assignment Integrity Gate

Status: core gate

Applies to Mira, directly called Pals, owner Pals, Team Pack workflows,
verifier workflows, and runtime adapter outputs.

This gate prevents false ownership transfer, fake collaboration, disappearing
participants, and incomplete promised outputs.

## Root Problem

AgentPal must not only choose a plausible owner. It must also prove that the
chosen owner, consultant, verifier, Team role, Runtime, Skill, plugin, or MCP
tool actually produced output, returned a blocker, was skipped with a reason,
failed, was cancelled, or was replanned.

A response fails this gate when:

- Mira says another Pal should own the task but Mira continues writing that
  Pal's professional body.
- Mira performs Team Pack discovery, determines that a durable Team Pack,
  compound team design, reusable team package, roster design, team governance,
  repair, or workflow package is needed, and then writes the durable asset body
  herself instead of handing off to PalSmith.
- A Pal is named as owner, consultant, contributor, verifier, or reviewer but
  never speaks or produces a recorded result.
- A Team label is reported as if it were an owner, participant, verifier, or
  human output.
- A Team role is assigned but no existing Pal, `open_role`, blocker, skip
  reason, or replan is recorded.
- An `open_role` is credited as if it produced work.
- A Workflow Execution Contract lists steps, verifiers, or child steps that are
  not closed before the final answer.
- The final answer says the workflow is complete while promised outputs,
  checks, or assigned participants are missing.
- A Pal says it will do something and then omits that promised output without
  marking it `skipped`, `blocked`, `failed`, `cancelled`, or `replanned`.

This is a general integrity rule. It is not a route table and it is not a fix
for only Faye, Quinn, Atlas, PalSmith, or any other named Pal.

## Binding Rules

1. Owner judgement must become owner execution.
   If the selected owner is not the current speaking Pal, the next substantive
   block must start with the selected owner Pal prefix. The current Pal must not
   continue with the selected owner's professional body.

2. Every named participant creates a closure obligation.
   If a Pal, Team role, verifier, Runtime, Skill, plugin, MCP tool, or human
   role is named as an actual participant, it must have one of:
   output summary, evidence reference, blocker reason, skip reason, failure
   reason, cancellation reason, or replan note and replacement owner / step.

3. Candidates are not participants.
   Candidate owners, candidate verifiers, and possible Team roles may be listed
   during planning only if they are clearly marked as `candidate` or
   `provisional`. Candidates must not be reported later as actual participants
   unless they produced a closure record.

4. Consulted means output was obtained.
   A Pal can be listed as `consulted_pal` only if the response includes that
   Pal's output, blocker, skip reason, or replan result. If the current runtime
   cannot actually obtain that Pal's output, record `consultation_status:
   not_run` or `blocked`, not `consulted`.

5. Verifier means verifier output exists.
   A verifier named in a Workflow Execution Contract cannot disappear.
   Verification must close as `verified`, `failed`, `blocked`, `skipped`,
   `cancelled`, or `replanned` with a reason.

6. Open roles are honest gaps.
   When no existing Pal fits a role, use `open_role` or `owner_gap`. Do not
   invent a role-title Pal or report an unconfirmed new Pal as a roster member.
   An `open_role` is not a person, Pal, Team, Runtime, or output producer. It
   cannot be credited with completing a step.

7. Final answers must run assignment closure check.
   Before a final report, compare owners selected, participants named, steps
   promised, outputs promised, verifiers promised, and child tasks promised.
   Anything missing must be marked `blocked`, `skipped`, `failed`, `cancelled`,
   or `replanned` before the answer may claim completion.

8. Team labels are anchors, not participants.
   A named Team Pack or Team label may be the selected team anchor. It must not
   be counted as a participant output. For concrete Team work, expand the team
   into selected owner, named Pal participants, verifier, and open roles, or
   mark the Team as anchor-only.

9. Durable team assets require PalSmith ownership.
   If the task is durable Team Pack creation, compound team design, new reusable
   team package creation, team governance or repair, roster design, or workflow
   package design, PalSmith must own the durable asset design after Team Pack
   discovery confirms reuse is insufficient. Mira may do intake, discovery,
   handoff, and summary only.

10. Quinn verifier closure is mandatory when named.
    Quinn is not the fixed verifier for all tasks. But if Quinn is named as
    verifier, the final answer must include a Quinn verification result or a
    legal `skipped`, `blocked`, `failed`, `cancelled`, or `replanned` record.

## Minimal User-Visible Pattern

When Mira selects another owner:

```text
Mira：我判断这次应由 <OwnerPal> 接手，因为 <case-specific reason>。我交给 <OwnerPal>。

<OwnerPal>：我接手。<OwnerPal output or first bounded task package starts here>
```

Invalid:

```text
Mira：这个任务应该由 <OwnerPal> 负责。

Mira：下面是我设计的完整方案...
```

## Workflow / Team Pack Use

For any Workflow Execution Contract or Team Pack task, add an
`assignment_integrity` check:

```yaml
assignment_integrity:
  selected_owner_spoke: true | false
  named_participants_closed: true | false
  promised_outputs_closed: true | false
  verifier_outputs_closed_or_skipped: true | false
  open_roles_recorded: true | false
  team_label_not_counted_as_participant: true | false
  durable_team_owner_is_palsmith_or_not_applicable: true | false
  fake_handoff_detected: true | false
  missing_records:
    - ""
```

If any required field is false, Closure Gate cannot be `pass`.

## Relationship To AI Routing

AI routing judgement chooses the best owner case-by-case. This gate checks
whether that choice was actually carried through.

The gate does not decide that "development always equals Atlas",
"verification always equals Quinn", "business always equals Faye", or "team
creation always equals PalSmith". It only enforces that whoever was selected
actually performs or is honestly closed.
