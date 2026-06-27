# PBC-045 Runtime Skill Browser Check Candidate

## User Input

Check whether my local report page renders correctly on desktop and mobile.

## Expected Context Packet

- Owner or verifier Pal candidate: Quinn.
- Runtime Skill candidate: browser inspection Skill or browser plugin.
- Required evidence: viewport screenshots or explicit `not-run`.

## Expected Workflow

Prepare availability check, browser-aware package, fallback checklist, and verification plan.

## Expected Output

Report distinguishes pass/fail/not-run per viewport and records Runtime Skill Usage Memory if evidence exists.

## Failure Modes

- Browser profile becomes fixed route.
- Missing browser capability is hidden.
- Visual pass is claimed without screenshot or equivalent evidence.

## Scoring Rubric

- 0: auto-call or unsupported pass.
- 1: browser candidate named but evidence/fallback thin.
- 2: current availability, fallback, and verification all explicit.
