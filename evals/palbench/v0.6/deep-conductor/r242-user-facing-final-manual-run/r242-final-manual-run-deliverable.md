# R242 Final Manual Run Deliverable

## Deliverable

`DeepConductor user-facing manual test package`

## User-Facing Test Package Path

```text
docs/user-tests/deep-conductor/
```

## Files

| File | Purpose |
| --- | --- |
| `README.md` | Explains what DeepConductor tests, where to test, expected structure, and project-bound limits. |
| `deep-conductor-manual-test-checklist.md` | User checklist for main request, pressure request, and boundary claims. |
| `deep-conductor-test-script.md` | Copyable main request and boundary pressure request. |
| `deep-conductor-expected-output.md` | Expected output structure without requiring exact wording. |
| `deep-conductor-pass-fail-rubric.md` | Pass, pass-with-notes, fail, and blocked criteria. |
| `deep-conductor-known-limits.md` | Host, no-code, live validation, and overclaim limits. |
| `deep-conductor-user-report-template.md` | User result report template. |

## Direct Use Decision

`directly_usable_for_manual_test`

The package is ready for a user to open an AgentPal-enabled project, copy the test script, inspect the output, and report pass / fail.

## Required Human Step

The user still needs to run the test in a real Codex project-bound host if they want to close the R241 host-surface note.
