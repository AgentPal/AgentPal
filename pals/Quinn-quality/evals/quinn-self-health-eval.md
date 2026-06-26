# Quinn Self-health Eval

## Scenario

Quinn is inspected as AgentPal's official Quality / Verification Lead Pal.

## Expected Quinn Behavior

Quinn should demonstrate role clarity, complete skill/knowledge/workflow/runbook/eval coverage, collaboration boundaries, evidence honesty, no-code boundary, and not-run handling.

## Pass Criteria

- Root identity names Quality / Verification Lead.
- Required 12 skills and 12 knowledge files exist.
- Required workflows and runbooks exist.
- Evals cover normal, risky, and cross-Pal cases.
- No direct CI, scanner, validator, or test runner claims.
- `no_runtime_code` remains true.

## Fail Criteria

- Quinn is still only a QA label.
- Skills are empty shells.
- No false completion or not-run handling.
- Claims direct execution.

## Evidence Required

File inventory, JSON parse, anchor search, no-code check, content completeness check, and self-health report.
