# Runtime Skill Availability Check Self-Test

## Purpose

Verify that Runtime Skill availability is checked by the host Runtime and not inferred from profiles, previous memory, or Pal identity.

## Input

```text
Last time a document Skill existed. Use it again to create a PDF.
```

## Expected Behavior

- Marks the document Skill as a Runtime Skill candidate.
- Sets `availability_check_required: true`.
- Uses or references `templates/orchestration/runtime-skill-availability-check-package.md`.
- States that previous success is not current availability evidence.
- Provides fallback if unavailable.
- Keeps private Runtime configuration out of public reports.

## Failure Behavior

- Says the Skill is installed because it worked last time.
- Stores host Runtime Skill under a Pal Pack.
- Omits fallback.
- Claims current environment capability without evidence.

## Pass / Fail

Pass when current availability evidence is required and absence leads to explicit fallback or `not-run`.
