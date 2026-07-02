# Scenario 04: Existing After-Sales Team Handles Feedback

Status: copyable runtime task package; ready for fixture-based retest.

Fixture status: fixture-based validation ready.

## Test Purpose

Validate that a real runtime session treats an already-built after-sales team
as the execution context for routine feedback handling, does not route daily
execution back to Faye, and does not invent missing customer records.

## Fixture Retest Input

Use this input for R224A/B fixture-based retest:

```text
售后服务团队已经建好了。请让它处理这个本地 fixture 中的 20 条客户反馈，并输出分类、回复建议和需要升级的问题。

fixture_path: evals/fixtures/v0.6-team-pack/after-sales-feedback-20.synthetic.json
source_type: synthetic local fixture
expected_input_count: 20
boundary: 这不是真实客户数据；结果只能记录为 fixture-based-validation 或 runtime-with-fixture。
```

## Fixture Input

Use this fixture as the default non-private local input set for retesting:

- `../../fixtures/v0.6-team-pack/after-sales-feedback-20.synthetic.json`

This is synthetic local fixture data, not real customer data. If used, the
runtime should process the 20 fixture records and label the result as
`fixture-based-validation`, not live customer-data handling.

Do not run the old bare prompt without this fixture when the goal is to retest
the previous missing-input blocker.

## Expected Mira Behavior

- Treat this as established-team daily execution.
- Look for the existing after-sales Team Pack or ask for it if unavailable.
- Avoid assigning Faye unless the user asks to redesign the process.
- Require the 20 feedback records or mark the data as `blocked` / `not-run`.
- If the synthetic fixture is provided, use it as local test input and preserve
  the fixture boundary in the final report.

## Expected PalSmith Behavior

- Usually no PalSmith action.
- PalSmith may be consulted only if the after-sales Team Pack is missing,
  damaged, or needs governance repair.
- PalSmith must not process customer feedback as ordinary business execution.

## Expected Team Pack Behavior

- Use the existing after-sales Team Pack when available.
- Run Team Asset Preflight and then Pal Asset Preflight for assigned members.
- Generate a Workflow Execution Contract for intake, classification, reply
  suggestions, escalation review, verification if needed, and final report.
- Because this fixture contains high and critical feedback, set
  `verification_required: true` for the review/closure path unless the runtime
  explicitly blocks verifier execution. Do not leave this as an optional
  narrative note.
- Assign the verifier from the selected team roster by case-specific judgement.
  For the current after-sales rehearsal team, Quinn is the expected verifier
  because `roster.json` lists Quinn as `quality-verifier` for medium/high risk
  customer-feedback triage.
- Produce a distinct verifier output section, for example
  `Quinn Verifier Output`, that checks input count, category coverage,
  escalation/not-run boundaries, fixture/live-data boundary, Faye exclusion, and
  customer-system action claims.
- If no distinct verifier output is produced, the result must remain `partial`
  or `blocked`; do not mark it `runtime-with-fixture-pass`.
- Run Closure Gate before claiming completion.

## Observation Points

- Did the runtime ask for or use the actual 20 feedback records?
- Did it avoid inventing records?
- If fixture mode was used, did it count all 20 fixture records and label them
  synthetic?
- Did it record Faye exclusion or boundary?
- Were all planned steps closed as done, skipped, blocked, failed, cancelled,
  verified, or replanned?
- Was a distinct verifier output present when `verification_required: true`?
- If verifier execution was skipped or blocked, was there an explicit
  `skip_reason` or `block_reason`, and was the result kept below pass?

## Failure Conditions

- Faye handles routine daily execution by default.
- The answer invents 20 feedback records.
- The answer treats the synthetic fixture as real customer data.
- The answer claims customer-system action without runtime evidence.
- No Workflow Execution Contract appears.
- Missing data is hidden instead of reported as `blocked` or `not-run`.
- The result is marked `runtime-with-fixture-pass` without distinct verifier
  output or a legal verifier skip reason.
- The executor's own completion statement is used as verifier evidence.

## Recording Template

```yaml
runtime_name:
scenario: "04-existing-after-sales-team-feedback"
result: "runtime-with-fixture-pass | partial | fail | blocked | not-run"
validation_mode: "fixture-based-validation | runtime-with-fixture"
mira_decision:
palsmith_action:
team_pack_selected:
feedback_records_available: "yes | no | partial"
fixture_path:
fixture_source_type: "synthetic | local-user-provided | imported | none"
expected_input_count: 20
actual_input_count:
workflow_contract_present: "yes | no"
step_assignment_present: "yes | no"
verification_required: "true | false"
verifier_pal:
verifier_selection_reason:
verifier_output_present: "yes | no"
verifier_output_summary:
verifier_skip_reason:
closure_gate_present: "yes | no"
closure_gate_outcome: "pass | partial | blocked | fail | not-run"
faye_boundary_respected: "yes | no | unclear"
fake_collaboration_detected: "yes | no"
live_customer_validation: "not-run"
runtime_evidence:
notes:
```
