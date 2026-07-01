# Scoped Pal Asset Execution Certification Plan

Status: R208 plan, not certification execution.

## Why This Exists

R205 and R207 together show that the 10 official bundled Pals each have one
representative real host regression for Pal Asset Execution adoption.

That is important evidence, but it is still not certification. A representative
host regression proves one Pal can use its assets for one task family in one
bounded host setting. It does not prove every task family, every tool path,
every environment, every missing-asset path, or release readiness.

R208 defines how a future review may grant a scoped certification only for a
specific Pal and task family, with explicit evidence and limits.

## Terms

### Representative Host Regression

A representative host regression is evidence that one Pal, in one task family,
used Asset Loading Gate, Task Asset Packet, and Asset Use Summary in a real
host thread or controlled execution setting.

It proves:

- the Pal had current behavior evidence for that task family;
- the Pal used task-relevant assets;
- the result had a visible boundary and quality check.

It does not prove:

- every task family for that Pal;
- every tool or runtime path;
- every environment;
- full release readiness;
- certification.

### Scoped Certification

Scoped certification is a limited review result for exactly one Pal plus one
task family, under a named evidence set, version or commit, review date, and
boundary.

It must include:

- `pal_id`
- `task_family`
- evidence IDs and paths
- host thread IDs
- asset coverage
- tool / runtime boundary evidence
- missing-asset handling
- known limits
- certification level
- valid scope
- invalid scope
- review date and version

### Full Certification

Full certification would cover a Pal's main task families, common tool paths,
important boundary cases, and regression set. AgentPal v0.5 does not grant full
certification without a separate evidence package.

## Certification Levels

| Level | Meaning |
| --- | --- |
| `uncertified` | No current entry adoption or task-family evidence. |
| `entry_adopted` | Entry files tell the Pal to use the Asset Loading Gate and Task Asset Packet for substantive work. |
| `representative_regression_passed` | At least one representative host regression has passed for a task family. |
| `scoped_certification_candidate` | Evidence appears sufficient to run a formal scoped certification review, but no final certification is granted yet. |
| `scoped_certified` | A formal review certifies one Pal plus one task family under explicit evidence and limits. |
| `full_certified` | Reserved for broad evidence across main task families and boundaries. Do not use by default in v0.5. |

## Evidence Gate

A Pal plus task family can receive `scoped_certified` only when the record has:

1. Phase 1 entry adoption.
2. Task Asset Packet example or equivalent documented task plan.
3. Real host representative regression.
4. Asset Loading Gate evidence.
5. Task Asset Packet evidence.
6. Asset Use Summary evidence.
7. Tool / runtime boundary evidence.
8. Missing Asset Plan handling, or a clear reason it was not needed.
9. No-code boundary scan result.
10. Quinn or equivalent QA review pass.
11. JSON, Markdown, and index checks for the evidence package.
12. Known limits.
13. No overclaim in docs, release notes, or indexes.

If any required item is missing, keep the level at
`representative_regression_passed` or `scoped_certification_candidate`.

## Certification Record Format

Use [`../../templates/pal/scoped-certification-record.md`](../../templates/pal/scoped-certification-record.md).

Each record must be task-family specific. Do not write one broad record that
implicitly covers a whole Pal, the official roster, or all future tasks.

## Downgrade And Revoke Conditions

Downgrade or revoke a scoped certification when:

- the Pal entry assets change materially;
- the task family changes;
- the evidence path is deleted or contradicted;
- host behavior changes and the old thread is no longer representative;
- the Pal fails a later regression for the certified scope;
- missing assets become material;
- a doc or release note expands the scope beyond the record;
- contacts, runtime, discovery, or publication boundaries change.

The downgraded level should usually be `representative_regression_passed` until
a new review is completed.

## Release Notes Guard

Release notes may say:

```text
The 10 official bundled Pals have representative task-family host regression
evidence for Pal Asset Execution adoption.
```

Release notes must not say that the official roster is broadly certified, that
every task family is covered, or that AgentPal gained runtime / backend /
publication behavior.

## R209 Recommended Execution Path

Recommended path:

```text
R209 - Scoped certification review for high-priority official Pal task families
```

Start with the R205 high-priority set because these five Pals have Phase 1
entry adoption, Phase 2 examples, representative host regressions, and Quinn
review:

- Mira-main: release readiness coordination
- PalSmith-pal-governor: existing Pal composite upgrade planning
- Atlas-developer: docs-first development task package
- Quinn-quality: completion report / false completion review
- Nova-product: product privacy and authorization-boundary decision

Alternative path: review all 10 official Pals for certification readiness, but
write one decision per Pal plus task family and keep non-ready items at
`representative_regression_passed`.
