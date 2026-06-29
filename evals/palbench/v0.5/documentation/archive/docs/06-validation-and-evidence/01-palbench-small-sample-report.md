# R33 PalBench Small-Sample Report

R33 PalBench is a small-sample smoke validation for AgentPal v0.1.0-rc.1.

It evaluated six qualitative scenarios that are relevant to the current AgentPal working method. The comparison was between agent usage workflows, not between underlying models.

## Scope

- Sample count: 6.
- Validation type: smoke validation.
- Measurement style: qualitative observation.
- Runtime behavior covered: Simple Pal Mode and future-boundary documentation.
- Runtime behavior not covered: active Deep Conductor execution, active subagent orchestration, external agent calls, installers, daemons, services, or UI behavior.

## Method Summary

Each sample recorded:

- baseline condition or prompt shape
- AgentPal-style condition
- observed criteria
- judge notes
- result

The score scale used in the archived report is qualitative:

| Score | Meaning |
| --- | --- |
| 0 | Not shown. |
| 1 | Partially shown. |
| 2 | Clearly shown. |

These scores are smoke-test observations. They are not statistical measurements.

## Observed Direction

Across the six samples, the AgentPal-style condition showed observed benefits in:

- clearer Task Packages for handoff
- stronger evidence checks for release verification
- reduced broad context-scope risk through Context Access Lists
- lower user burden from using Mira as the single entry point
- reusable routing notes for similar later tasks
- clearer separation between current Fast Route behavior and future Deep Conductor design

## Archive Relationship

The earlier research note is preserved in [Archived R33 PalBench small-sample smoke validation](../research/archive/palbench-r33-small-sample-report.md).

This page is the current public validation entry and keeps the same conservative boundary.
