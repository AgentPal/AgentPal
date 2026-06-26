# Example: User Material Ingestion

This is an example only and contains no real private user material.

## User Goal

User wants to create a Customer Support Pal from a support SOP, reply examples, escalation rules, and tone guide.

## Material Ingestion Plan

- Read approved files only.
- Inventory each source.
- Classify sections.
- Preserve examples and escalation rules.
- Split output into knowledge, runbook, templates, and evals.

## Source Inventory

| Source | Sections | Privacy | Use |
| --- | --- | --- | --- |
| `support-sop.md` | intake, refund, escalation | private until cleaned | knowledge/runbook |
| `reply-examples.md` | tone examples | private until cleaned | templates/examples |
| `risk-rules.md` | forbidden promises | public-safe after review | boundary/eval |

## Classification Table

| Section | Classification | Target |
| --- | --- | --- |
| refund policy | Knowledge | `knowledge/refund-policy.md` |
| escalation steps | Runbook | `runbooks/escalation.md` |
| reply examples | Template / Example | `templates/reply-patterns.md` |
| forbidden promises | Boundary / Eval | `evals/risky-promises.md` |

## Content Preservation Checklist

- source anchors preserved: yes
- examples preserved: yes
- steps preserved: yes
- edge cases preserved: yes
- unclassified material: none in this example
- private data removed from public targets: required before clean export

## Runtime Task Package

Use `User Material Ingestion Task Package`. Runtime writes only after the user confirms target paths.
