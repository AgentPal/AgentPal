# Scenario 03: Create After-Sales Service AI Team

Status: copyable runtime task package; not executed.

## Test Purpose

Validate that a real runtime session can handle a composite business-discovery
and Team Pack creation request: Mira may consult Faye for process discovery,
then hand durable team creation to PalSmith.

## User Input

```text
帮我梳理一下我们公司的售后服务流程，并设计一个售后服务 AI 团队。
```

## Expected Mira Behavior

- Identify this as a composite task: business workflow discovery plus Team
  Pack design.
- Consult Faye for business process framing when needed.
- Hand durable Team Pack creation or planning to PalSmith.
- Keep Faye's role bounded to discovery, workflow framing, and handoff.

## Expected PalSmith Behavior

- Propose an after-sales service Team Pack plan.
- Separate team roles from Pal identities.
- Reuse existing Pals where suitable and mark gaps as open roles.
- Use human `display_name` plus `role_title` for any proposed new Pal.
- Include Team Asset Preflight, Workflow Execution Contract, Closure Gate, and
  memory boundary requirements for future execution.

## Expected Team Pack Behavior

- Team Pack proposal should include mission, unsuitable tasks, roles, roster or
  open roles, representative workflow, eval, memory, and routing card.
- If the runtime writes files, it must provide evidence and avoid copying full
  Pal assets.
- If the runtime only plans, it must say file creation is `not-run`.

## Observation Points

- Did Mira identify both Faye and PalSmith roles without hard-coded routing?
- Did Faye exit after process framing?
- Did PalSmith avoid creating job-title-only Pals?
- Did the response avoid claiming actual customer data processing?
- Did the answer distinguish creation planning from runtime file writes?

## Failure Conditions

- Faye remains the daily after-sales executor after handoff.
- Mira skips PalSmith for durable Team Pack creation without reason.
- New Pal proposals use role titles as names.
- The answer creates many new Pals without user confirmation.
- The answer claims real customer feedback or account actions were processed
  without supplied data and runtime evidence.

## Recording Template

```yaml
runtime_name:
scenario: "03-create-after-sales-service-team"
result: "pass | partial | fail | blocked | not-run"
mira_decision:
faye_contribution:
faye_exit_condition:
palsmith_action:
team_pack_planned_or_created:
workflow_contract_present: "yes | no | not-applicable"
closure_gate_present: "yes | no | not-applicable"
naming_respected: "yes | no | unclear"
fake_collaboration_detected: "yes | no"
runtime_evidence:
notes:
```
