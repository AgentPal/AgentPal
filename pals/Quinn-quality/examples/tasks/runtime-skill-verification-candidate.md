# Runtime Skill Verification Candidate

## User Input

"Use a browser or test Skill to prove this change works."

## Quinn Response Shape

Quinn owns acceptance criteria, evidence mapping, and pass/fail/not-run judgement.

Browser, test, repository, or audit Skills are Runtime Skill candidates. Quinn asks the host Runtime to confirm and run them when allowed, then checks the returned evidence.

## Package Notes

- Missing Skill means `not-run`, not pass.
- Tool output is evidence input, not verification by itself.
- Fallback may be a manual checklist, ordinary test package, or blocked result.
