# Deep Conductor E2E Document Runtime Skill Example

## User input

Convert a source document into a reviewed PDF-style deliverable, preserving structure and evidence.

## Deep Conductor E2E Package

```yaml
schema: agentpal.deep-conductor-e2e-package.v0.3
package_id: e2e-document-runtime-skill-example
user_goal: document transformation with evidence
project_or_single_task: single_task
workflow_topology:
  selected: owner_verifier + plan_execute_verify
  reason: document transformation needs source preservation, host Runtime Skill availability, and verification
  not_a_fixed_route: true
context_usage_report_required: true
not_a_fixed_route: true
```

## Context Budget

- read document inventory and source summary first;
- full source read requires source-preservation, exact wording, layout, or verification reason;
- no unrelated user documents are read;
- private or sensitive material requires approval.

## Memory used

Runtime Skill Usage Memory may show that a host document Skill worked before, but current availability still must be checked. Pal memory does not contain raw private document content.

## Capability Inventory used

- Morgan profile for document workflow and source preservation;
- host Runtime profile for document/PDF/rendering capabilities;
- Quinn or Rhea profile for verification and file safety where needed.

## Topology selected

Owner + Verifier plus Plan -> Execute -> Verify. Morgan-like document ownership and verifier candidates are selected by current task judgement, not by filename alone.

## Context Packets

- document owner packet: purpose, audience, source boundary, output format;
- Runtime Skill packet: named document/PDF/render candidates, availability check, fallback;
- verifier packet: source preservation, rendered artifact evidence, not-run handling.

## Runtime Skill-aware packages

- document rendering Skill candidate;
- PDF inspection Skill candidate;
- fallback: Markdown-only transformation plan and manual review instructions;
- host Runtime must report availability before use.

## Verification plan

- source meaning preserved;
- output artifact path and render evidence reported by host Runtime;
- layout/accessibility checks run or marked `not-run`;
- private content excluded from public memory and examples.

## Synthesis report

```yaml
schema: agentpal.deep-conductor-e2e-synthesis-report.v0.3
report_id: e2e-document-runtime-skill-report-example
goal: document deliverable with preservation evidence
what_was_planned: source inventory, Runtime Skill check, transformation, verification
what_was_executed_by_runtime: document rendering/export only if host Runtime performs it
what_was_verified: source preservation, artifact evidence, layout checks, privacy boundary
agreement: [Runtime Skills are host capabilities, not Pal-owned Skills]
conflicts: []
risks: [unavailable rendering Skill, missing source approval]
missing_evidence: []
next_round_recommendation:
  action: use fallback package if Skill availability is blocked
  not_a_fixed_route: true
requires_user_decision:
  needed: true
  decisions: [approve source document handling]
```

## Routing Memory candidate

Record document task type, Runtime Skill availability, fallback, verification result, source preservation issues, and next-time recommendation without storing raw private document text.

## No-code boundary note

This example does not add converters, Office automation, PDF tools, scanners, validators, daemons, or services to AgentPal. It only prepares host Runtime task packages.
