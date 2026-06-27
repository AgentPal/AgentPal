# Deep Conductor E2E Research To HTML Report Example

## User input

Research a current topic, write a detailed report, and create a polished HTML page.

## Deep Conductor E2E Package

```yaml
schema: agentpal.deep-conductor-e2e-package.v0.3
package_id: e2e-research-html-example
user_goal: research plus HTML deliverable
project_or_single_task: mixed
workflow_topology:
  selected: project_conductor + plan_execute_verify
  reason: the work has research, writing/document, implementation-shaped, and verification stages
  not_a_fixed_route: true
context_usage_report_required: true
not_a_fixed_route: true
```

## Context Budget

- start with source inventory, research questions, and existing approved summaries;
- read full sources only for claims, contradictions, freshness, or citation quality;
- read design or implementation files only if the final artifact requires them;
- do not read unrelated project files.

## Memory used

Approved research/project memory may reduce repeated source discovery. Missing or stale memory is reported, not replaced with guesses.

## Capability Inventory used

- research capability profile for source planning;
- writing/document profile for report structure;
- host Runtime profile for browser, file edit, or screenshot capability;
- verification profile for source and artifact checks.

## Topology selected

Project Conductor with Plan -> Execute -> Verify. Stage candidates are selected for this deliverable shape and may change with evidence.

## Context Packets

- research packet: questions, source boundary, freshness need, source inventory output;
- content packet: report audience, evidence matrix, writing constraints;
- artifact packet: allowed HTML file, assets, accessibility and responsive checks;
- verification packet: source mapping, artifact render evidence, not-run items.

## Runtime Skill-aware packages

- web research Skill candidate if available in the host Runtime;
- browser screenshot/render candidate if available;
- repository/file edit candidate if the artifact must be written locally;
- fallback: manual source list and static file review when Skills are unavailable.

## Verification plan

- source inventory exists;
- major claims map to source IDs or are labeled inference/uncertainty;
- HTML artifact path and changed files are reported by the host Runtime;
- render/screenshot checks are run when available or marked `not-run`;
- no unsupported current-fact claims.

## Synthesis report

```yaml
schema: agentpal.deep-conductor-e2e-synthesis-report.v0.3
report_id: e2e-research-html-report-example
goal: research plus polished HTML page
what_was_planned: research, report, artifact, verification stages
what_was_executed_by_runtime: file writes and browser checks only if the host Runtime performs them
what_was_verified: source coverage, claim support, artifact existence, render evidence
agreement: [evidence must precede current claims]
conflicts: [conflicting sources are preserved]
risks: [stale sources, missing render evidence]
missing_evidence: []
next_round_recommendation:
  action: update source set or artifact based on verifier gaps
  not_a_fixed_route: true
requires_user_decision:
  needed: false
  decisions: []
```

## Routing Memory candidate

Store whether memory reuse reduced reads, which host Runtime Skills were available, verification result, and rework count. Do not store paid source text or private project facts.

## No-code boundary note

The package can request an HTML artifact from the host Runtime, but AgentPal does not run a website builder, browser automation service, or hidden executor.
