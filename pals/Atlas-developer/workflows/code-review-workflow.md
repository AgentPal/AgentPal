# Code Review Workflow

## Trigger

Runtime returns changes, a patch, a pull request, or a completion report needing engineering review.

## Inputs

- Original task package.
- Diff or changed files.
- Test/build/check evidence.
- Project instructions.
- Runtime report and not-run items.

## Steps

1. Read the objective and acceptance criteria.
2. Inspect changed files or diff evidence.
3. Check behavior against the original task.
4. Check file boundary and out-of-scope changes.
5. Check tests, manual evidence, and not-run items.
6. Identify findings by severity.
7. If no findings, state remaining risk and test gaps.

## Decision points

- Is the evidence strong enough to review?
- Are any changes outside allowed scope?
- Are missing tests acceptable or blocking?
- Should Quinn, Rhea, or PalSmith review a stage?

## Outputs

Code review report with findings first, then open questions, verification state, and summary.

## Quality checks

- Findings are grounded in evidence.
- Severity is clear.
- Scope creep is visible.
- No completion claim without checks.

## Required user confirmation

Required before approving risky exceptions, release promotion, or accepting missing evidence for high-risk work.

## Evidence to return

Return file paths, changed-file list, test output summary, not-run checks, and residual risk.
