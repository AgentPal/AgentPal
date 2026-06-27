# Deep Conductor E2E Verification Self-Test

## Purpose

Verify that E2E planning preserves evidence review and not-run reporting.

## Passing criteria

- `verification_plan` names acceptance criteria, evidence required, not-run reporting, blocked reporting, and verification owner or owner gap.
- Owner + Verifier or Plan -> Execute -> Verify is used when evidence separation is needed.
- Runtime output is not accepted as proof without evidence mapping.
- Runtime Skill output requires verification against original acceptance criteria.
- Synthesis report includes `what_was_verified`, `missing_evidence`, `risks`, and `requires_user_decision`.
- Cost or context pressure does not remove necessary verification.
- No private paths or secrets appear in public evidence examples.

## Failing patterns

- Owner completion text is treated as verification.
- A generated artifact is accepted without file/path/render/source evidence.
- Not-run checks are hidden.

## Related failure example

- `examples/failures/deep-conductor-e2e-no-verification.md`

## Shared E2E regression checklist

Every Deep Conductor E2E self-test must also check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory, not fixed route language, and no internal path leakage.
