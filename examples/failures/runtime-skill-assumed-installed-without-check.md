# Failure: Runtime Skill Assumed Installed Without Check

## Wrong Behavior

A Task Package says "use the browser Skill" because a browser Skill existed in a previous Runtime.

## Why It Is Wrong

Previous availability and profile examples do not prove current Runtime availability. Runtime capability is current-environment evidence.

## Correct Behavior

Set `availability_check_required: true` and ask the host Runtime to report whether the candidate is available. If not available, follow fallback.

## Corresponding Eval

`evals/orchestration/runtime-skill-availability-check-self-test.md`
