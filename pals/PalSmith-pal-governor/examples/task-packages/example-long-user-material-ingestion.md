# Example: Long User Material Ingestion

This example is synthetic and public-safe. It demonstrates how PalSmith should handle a long user-provided document without compressing it into a shallow card.

## User Goal

The user provides a 10,000-word operations manual and says:

```text
Use this to create a Customer Support Escalation Pal. Keep the examples, escalation thresholds, exception cases, and response templates.
```

## PalSmith First Questions

- Which source files may the Runtime read?
- Is the material private, team-local, or public-share candidate?
- Which sections must remain close to the original wording?
- Which examples, numbers, thresholds, names, or exceptions are critical?
- Should the output be a new Pal, a repair to an existing Pal, or only a material ingestion report?

## Source Inventory

| Source ID | Source label | Section | Privacy | Intended use |
| --- | --- | --- | --- | --- |
| U01 | support-ops-manual.md | escalation policy | private | workflow and runbook |
| U02 | support-ops-manual.md | refund examples | private | knowledge and template |
| U03 | support-ops-manual.md | exception table | private | eval and risk boundary |
| U04 | support-ops-manual.md | tone examples | private | persona / voice |

## Classification Table

| Source detail | Keep because | Target asset | Preservation rule |
| --- | --- | --- | --- |
| escalation thresholds | drives routing and approval | `runbooks/escalation-review-runbook.md` | preserve numbers and owners |
| refund examples | teaches judgement | `knowledge/refund-policy-knowledge.md` | preserve contrasting examples |
| exception cases | prevents unsafe automation | `evals/escalation-risk-eval.md` | preserve edge cases |
| approved reply templates | becomes reusable output | `templates/customer-reply-template.md` | keep structure, improve wording only |
| tone examples | guides Pal voice | `identity/voice.md` | preserve style constraints |

## Content Preservation Checklist

- source inventory exists
- classification table exists
- examples preserved
- parameters preserved
- limits and exceptions preserved
- unclear sections retained as review items
- summaries used only as navigation
- no long section replaced by a short capability card

## Split Plan

| Target type | Proposed files |
| --- | --- |
| knowledge | policy knowledge, escalation criteria, exception knowledge |
| skill | escalation triage skill, response drafting skill |
| workflow | customer issue intake workflow, escalation workflow |
| runbook | refund escalation runbook, safety escalation runbook |
| template | reply template, escalation report template |
| eval | policy judgement eval, exception handling eval |

## Source Coverage Requirement

After writing assets, PalSmith should use `templates/source-coverage-report-template.md`.

Required standard:

- critical points 100% covered
- important points at least 85% covered
- optional points tracked with reasons if missing

## Bad Output Pattern

Do not write only:

```text
The support Pal should know escalation rules and respond politely.
```

That loses the actual operational content.

## Good Output Pattern

Write source-linked assets with preserved examples, thresholds, exception cases, and templates. If the current context cannot hold the full document, process it in batches and report remaining sections as `not-run`.
