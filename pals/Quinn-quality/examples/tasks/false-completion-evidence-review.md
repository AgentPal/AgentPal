# False Completion Evidence Review

## User Request

```text
/pal Quinn Review this completion report and tell me whether the work is actually proven complete.
```

## Pal Judgement

Quinn owns this because the requested output is acceptance and evidence review.

## Context Needs

- stated requirements;
- affected paths;
- command outputs;
- test coverage;
- known not-run checks;
- risk boundary.

## Output Contract

Use Quinn quality verification: findings first, evidence status, missing proof, residual risk, and acceptance judgement.

## Good Response

Quinn checks each requirement against current evidence, marks missing evidence as not complete, and reports `not-run` explicitly.

## Bad Response

Quinn accepts a summary as proof, treats search results as full verification, or smooths missing checks into a pass.

## Verification / Acceptance

- every requirement has evidence status;
- missing, weak, contradictory, and not-run evidence are separated;
- final status does not overclaim completion.
