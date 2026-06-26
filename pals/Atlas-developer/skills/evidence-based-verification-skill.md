# Evidence Based Verification Skill

## Purpose

Ensure Atlas judges completion from evidence rather than runtime summaries or confidence.

## When to use

Use after any execution-backed development task, review, test, release check, or Pal asset change.

## Inputs

- Original objective.
- Acceptance criteria.
- Runtime report.
- Changed files.
- Test/build/check output.
- Artifacts, screenshots, logs, or not-run explanations.

## Required context

Read the objective, task package, changed-file evidence, and verification output. If evidence is missing, do not infer success.

## Process

1. Map each acceptance criterion to evidence.
2. Check changed files against allowed scope.
3. Check required commands or manual checks.
4. Classify each item as proven, contradicted, incomplete, weak, missing, or not-run.
5. Identify risks and next evidence required.
6. Only mark completion when evidence proves every required item.

## Output

An evidence review with criterion-by-criterion result and final judgement.

## Quality bar

Completion must be proven, not assumed. A completion report is input evidence only when backed by verifiable details.

## User confirmation points

Ask before accepting missing evidence for high-risk work or before declaring release readiness.

## No-code boundary

This skill reviews evidence. It does not run commands or produce artifacts.

## Common mistakes

- Treating "tests passed" without command output as enough.
- Using narrow tests to prove broad scope.
- Ignoring not-run checks.
- Marking complete because no obvious issue was found.

## Example

Runtime says a bug is fixed but gives no changed files or test output. Atlas returns "needs evidence" and asks for diff summary, command output, and reproduction result.
