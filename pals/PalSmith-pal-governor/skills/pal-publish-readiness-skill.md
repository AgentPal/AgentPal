# Pal Publish Readiness Skill

## Purpose

Decide whether a Pal or team is ready for public sharing or should remain draft, testing, or stable.

## When To Use

Use when the user asks if something can publish, enter publish-ready, be shared, or become stable.

## Inputs

- target Pal/team
- release intent
- eval evidence
- export evidence
- registry/contacts evidence
- user confirmation for read/write scope

## Required Context

Read readiness matrix, publish quality gate protocol/template, quality inspection, Eval Lab evidence, export policy, and target Pal files.

## Process

1. Run readiness matrix review.
2. Run or reference job fitness inspection.
3. Check Eval Lab coverage.
4. Check clean export safety.
5. Check public/private boundary.
6. Check registry/contacts consistency when discoverability is requested.
7. Recommend the lowest state proven by evidence.
8. List must-fix, should-fix, acceptable risk, and not-run items.

## Output

- publish readiness report
- readiness matrix
- must-fix and should-fix list
- recommended state
- next Runtime Task Package

## Quality Bar

The skill must refuse unsupported `publish-ready` claims. Missing evidence blocks the state.

## User Confirmation Points

- read private or report directories
- write readiness report
- change lifecycle status
- publish or export

## No-Code Boundary

PalSmith does not publish or create releases. Runtime actions require confirmation and evidence.

## Common Mistakes

- saying yes too early
- treating local completeness as public readiness
- skipping clean export review
- ignoring with-memory export risk

## Example

A team with governance and eval plan but no full clean export is `testing` or `stable`, not `publish-ready`.
