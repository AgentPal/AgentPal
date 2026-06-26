# Failed Test Triage Runbook

## Trigger

A build, unit test, integration test, browser check, or release gate fails.

## Inputs

- Failing command and output.
- Recent changes.
- Expected behavior.
- Test file or suite.
- Environment notes.
- Allowed investigation scope.

## Steps

1. Record the exact failing command and output.
2. Classify likely type: test bug, implementation bug, environment issue, flaky test, missing dependency, or data issue.
3. Identify minimal files to inspect.
4. Prepare a runtime investigation task with stop conditions.
5. Require fix evidence or blocker evidence.
6. Review whether the failure is resolved without masking it.

## Decision points

- Is Rhea needed for environment?
- Is the failure in scope?
- Should the test be fixed or the code?
- Is skipping the test acceptable?

## Outputs

Failed-test triage package, root-cause summary, repair task, or blocker report.

## Quality checks

- Failure text preserved.
- No blind test deletion.
- No skipped check hidden as pass.
- Fix includes prevention evidence.

## Required user confirmation

Required before changing test infrastructure, deleting tests, installing dependencies, or changing CI/release config.

## Evidence to return

Return failing output, root cause, changed files, rerun result, not-run checks, and remaining risk.
