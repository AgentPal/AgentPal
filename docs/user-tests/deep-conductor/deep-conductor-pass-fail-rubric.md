# DeepConductor Pass / Fail Rubric

## Pass

Use `pass` when:

- The main natural-language request triggers DeepConductor.
- Team First Discovery happens before new-team creation.
- A fitting existing Team Pack is reused.
- Selected and rejected participants are explained.
- Every selected Pal has a Work Plan.
- Every selected Pal has Asset Preflight.
- Execution Trace maps work to owners.
- Owner Assignment Integrity Gate passes.
- Closure Gate passes.
- Quinn final verification is present.
- The final deliverable is directly usable.

## Pass With Notes

Use `pass_with_notes` when the content chain works, but one of these limits remains:

- host cannot prove strict project-bound thread loading;
- the run is a filesystem / evidence replay;
- no live GitHub outreach was performed;
- no live external user validation was performed;
- no real publication was authorized.

These notes must be visible and must not be hidden.

## Fail

Use `fail` if any of these happen:

- No Team First Discovery.
- A new team is created before checking existing Team Packs.
- A Pal is selected but has no participation record.
- Quinn is named as verifier but has no output.
- Pal Work Plan and actual execution do not match.
- Asset Preflight is mentioned but not used in execution.
- Faye is used for routine promotion execution and not corrected.
- Quinn is used for ordinary copywriting and not corrected.
- PalSmith is used for routine execution when an existing Team Pack fits.
- Closure Gate does not check required steps.
- Owner Assignment Integrity is missing.
- The final plan is not usable and does not say why.

## Blocked

Use `blocked` when AgentPal cannot be enabled, DeepConductor cannot be triggered at all, or required project-bound context is unavailable and no evidence replay is possible.
