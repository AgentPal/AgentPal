# R202 Official Pal Adoption Gaps Summary

Status: gap summary for a spot-check, not a migration completion record.

## Summary

R202 checked the 10 official bundled Pals against the R198-R201 Pal Asset
Execution Contract. The roster is structurally strong: most Pals have identity,
knowledge, skills, workflows, memory placeholders, collaboration boundaries,
and quality or eval assets.

The common gap is adoption wiring. Most official Pals do not yet name the new
Asset Loading Gate, Task Asset Packet, Asset Use Summary, and Missing Asset
Plan in their sampled entry assets. PalSmith is the exception because it owns
Pal asset governance and was updated during R198-R201.

## Common Gaps

| Gap | Observed shape | Risk |
| --- | --- | --- |
| Identity exists but asset loading is implicit | Many Pals have rich `identity/` and `PAL.md` assets but no explicit Asset Loading Gate entry note. | A runtime may answer from role or persona without recording what assets shaped the work. |
| Skill entry exists but Task Asset Packet is absent | Most `SKILL.md` files define read order and task scope but do not require a Task Asset Packet for substantive work. | Tool-backed or complex work may not preserve pre-action evidence. |
| Workflow exists but Asset Use Summary is absent | Most Pals have workflows and runbooks but no post-work asset summary pattern. | Reviewers cannot tell whether the answer used Pal assets or generic model knowledge. |
| Tool boundary exists but tool-is-not-asset wording is uneven | Many Pals say they are not runtimes, scanners, validators, browsers, shells, or direct executors. | The boundary is strong, but not always connected to the R198-R201 contract language. |
| Eval assets exist but asset usage regression is not specific | Many Pals have self-tests or quality evals. | Existing evals do not automatically prove task asset usage. |
| Missing Asset Plan is mostly absent outside PalSmith | PalSmith documents Missing Asset Plans; other Pals generally do not expose the template. | Missing assets may become unsupported readiness claims instead of repair plans. |
| Faye has a compact structure | Faye has delivery assets but no `identity/` or `evals/` directory in this spot-check. | Faye should receive early Phase 1/2 adoption work because it is user-facing and central to business delivery. |

## Phased Migration Recommendation

### Phase 1: Entry Declaration

Add a short Pal-specific entry note to every official Pal explaining that
substantive work must pass the Asset Loading Gate or explicitly use the
lightweight path.

Minimum surface:

- `SKILL.md` or a Pal-owned core entry file;
- one link to `core/asset-loading-gate.md`;
- one link to `core/pal-asset-execution-contract.md`;
- no claim of verified readiness.

### Phase 2: Task Packet And Summary Patterns

For priority Pals, add Pal-specific Task Asset Packet and Asset Use Summary
examples.

Suggested order:

1. Faye, because delivery users need concrete Pack evidence.
2. Quinn, because Quinn reviews evidence and should model asset summaries.
3. Rhea, because no-code and runtime boundary claims are high risk.
4. Atlas, because development/release work is tool-backed.
5. Vega, Morgan, Harper, Nova, and Mira by common user workflow frequency.

### Phase 3: Representative Regression

Run one real or controlled host regression per official Pal task family:

- task request;
- required assets;
- loaded assets;
- host Runtime evidence if used;
- Asset Use Summary;
- Quinn review or equivalent quality gate.

Do not use old self-tests as a substitute unless they explicitly demonstrate
asset use under the R198-R201 contract.

### Phase 4: Readiness Label Review

Only after Phase 3 should a Pal be considered for `executable_pal` or
`verified_executable_pal` in the tested task family.

The label must include scope. Example:

```text
verified_executable_pal for documented delivery-pack drafting tasks
```

Do not use a universal label without representative evidence for the relevant
task family.

## No-Code Boundary

This summary does not add runtime code, CLI behavior, installer behavior,
scanner behavior, daemon behavior, connector behavior, backend services, or
Marketplace infrastructure. It also does not modify contacts, official roster
status, real user custom Pals, or the R200 controlled-write fixture.

## Decision

Decision: `adoption_gaps_identified_phase_plan_ready`.

Recommended next work:

```text
R203 - Phase 1 official Pal asset execution entry adoption
```
