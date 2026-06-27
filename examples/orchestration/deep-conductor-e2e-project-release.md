# Deep Conductor E2E Project Release Example

## User input

Prepare this public AgentPal release candidate, verify boundaries, and produce a final release readiness summary.

## Deep Conductor E2E Package

```yaml
schema: agentpal.deep-conductor-e2e-package.v0.3
package_id: e2e-project-release-example
user_goal: prepare public release readiness summary
project_or_single_task: project
workflow_topology:
  selected: owner_verifier + plan_execute_verify
  reason: release work needs owner planning, runtime evidence, and independent quality/safety review
  not_a_fixed_route: true
context_usage_report_required: true
not_a_fixed_route: true
```

## Context Budget

- read tier: targeted full reads for release checklist, manifest, changelog, docs index, and changed files;
- allowed context: release docs, public docs, registry, contacts, selected Pal boundary notes;
- forbidden context: private reports, raw user memory, local absolute paths, credentials;
- escalation: only when a release claim lacks evidence.

## Memory used

- routing memory: previous release checks can inform likely gaps;
- release memory: use only public-safe summaries;
- if missing, report `missing` instead of inventing readiness history.

## Capability Inventory used

- Pal profiles: Mira for synthesis, Rhea for safety, Quinn for evidence review, Atlas for repository handoff if edits are needed;
- Runtime profile: current host Runtime file/Git capability;
- Skill profiles: optional repository or JSON tools as host Runtime candidates only.

## Topology selected

Owner + Verifier with Plan -> Execute -> Verify. The selected owner and verifier are candidates chosen for this release case, not a permanent rule.

## Context Packets

- release owner packet: scope, files allowed, release claims, evidence required;
- safety review packet: no-code boundary, public/private boundary, publishing risk;
- quality packet: acceptance criteria, not-run handling, release-readiness verdict.

## Runtime Skill-aware packages

- JSON parse package if host Runtime has JSON tooling;
- Git status package if host Runtime has repository access;
- docs link review package if host Runtime can inspect changed docs.

## Verification plan

- JSON validity for release-critical JSON files;
- public-safe scan for secrets and private paths;
- no runtime program files introduced;
- no hard-coded routing in operational docs;
- Git state and release action evidence;
- not-run items must remain visible.

## Synthesis report

```yaml
schema: agentpal.deep-conductor-e2e-synthesis-report.v0.3
report_id: e2e-project-release-report-example
goal: release readiness summary
what_was_planned: release owner/verifier package plus runtime evidence checks
what_was_executed_by_runtime: evidence-producing checks only after package approval
what_was_verified: JSON, public-safety, no-code, routing, Git evidence
agreement: [release claims require evidence]
conflicts: []
risks: [unverified publish action remains not-run]
missing_evidence: []
next_round_recommendation:
  action: publish only after current GitHub release evidence exists
  not_a_fixed_route: true
requires_user_decision:
  needed: true
  decisions: [whether to publish]
```

## Routing Memory candidate

Record task type, topology, owner/verifier candidates, Runtime evidence used, verification result, not-run items, and user acceptance. Do not record private release notes or local paths.

## No-code boundary note

This example does not create a release tool, CLI, validator, scanner, or publisher. It only defines a package a host Runtime can follow with evidence.
