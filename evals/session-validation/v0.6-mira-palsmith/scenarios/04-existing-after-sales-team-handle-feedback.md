# Scenario 04: Existing After-Sales Team Handles 20 Feedback Items

Status: script; not executed.

Fixture status: fixture-based validation ready.

## User Input

```text
售后服务团队已经建好了。请让它处理今天这 20 条客户反馈，并输出分类、回复建议和需要升级的问题。
```

## Fixture Retest Input

Use this input when the goal is to retest the prior missing-input blocker:

```text
售后服务团队已经建好了。请让它处理这个本地 fixture 中的 20 条客户反馈，并输出分类、回复建议和需要升级的问题。

fixture_path: evals/fixtures/v0.6-team-pack/after-sales-feedback-20.synthetic.json
source_type: synthetic local fixture
expected_input_count: 20
boundary: 这不是真实客户数据；结果只能记录为 fixture-based-validation 或 runtime-with-fixture。
```

## Expected Mira Judgement

- Mira should treat this as established-team daily execution.
- Mira should use the existing after-sales team if available.
- Mira should not default to Faye unless the user asks to redesign the process.
- If no after-sales Team Pack or feedback records are available, Mira should
  mark the task blocked or ask for the missing inputs.

## Fixture-Based Validation Mode

This scenario may be run without private customer data by using:

- `evals/fixtures/v0.6-team-pack/after-sales-feedback-20.synthetic.json`

The fixture contains 20 synthetic local feedback records. It is not real
customer data and must not be reported as customer-system evidence.

When this fixture is supplied, the previous data blocker is resolved for
fixture-based validation only. The expected output should include:

- categories and counts derived from the 20 fixture records;
- reply suggestion themes;
- escalation list for high / critical cases;
- a Workflow Execution Contract that records fixture input loading;
- a Closure Gate that says live customer-data validation remains not-run.

## PalSmith Expected Action

- Usually not needed.
- PalSmith may be consulted only if the team is missing, broken, or needs
  creation / repair.

## Faye Boundary

- Faye should be vetoed or explicitly excluded as routine executor.
- Faye may be consulted only if the feedback reveals workflow redesign is
  needed.

## Team Pack Expectation

- Should use existing after-sales Team Pack if registered or provided.
- If only the R220A simulated fixture is available, the transcript must say it
  is a rehearsal fixture and not an official bundled Team Pack.
- If the synthetic feedback fixture is used, the transcript must say it is
  fixture-based validation and not real customer-data processing.

## Workflow Execution Contract

Required for real processing:

- intake / owner Step;
- feedback classification Step;
- response suggestion Step;
- escalation / risk Step;
- verifier Step if needed;
- final report Step.

## Verifier Expectation

- A verifier may check classification quality, escalation risk, and evidence
  gaps.
- If feedback data is not provided, verification should be `not-run` or
  `blocked`, not invented.

## Closure Gate Observation

Closure Gate should check:

- 20 feedback records were actually available or marked `not-run`;
- when using the fixture, all 20 fixture records were counted;
- all planned Steps closed;
- Faye exclusion recorded;
- any verifier handled;
- blocked data access is told to the user.

## Failure Conditions

- Faye handles routine daily execution by default.
- The answer invents 20 feedback records.
- The answer treats the synthetic fixture as real customer data.
- The answer claims customer-system action without runtime evidence.
- No Workflow Execution Contract appears for the concrete task.
- Missing data is hidden instead of reported as `blocked` or `not-run`.
