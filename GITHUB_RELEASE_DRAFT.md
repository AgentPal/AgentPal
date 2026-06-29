# AgentPal v0.3.0-rc.1

AgentPal v0.3.0-rc.1 is a release candidate for the v0.3 no-code orchestration prototype line.

This release should be marked as a pre-release. It should not be marked as a stable `v0.3.0` release.

## Highlights

- Deep Conductor E2E no-code package and synthesis report.
- Deep Conductor Master Loop and Project Conductor workflow.
- Context Packet and `/pal Name` / `@Pal` collaboration protocols.
- Owner + Verifier workflow for evidence-based verification.
- Parallel Independent Review workflow with reviewer isolation.
- Cross-Runtime Pal Memory and Routing Memory continuity packages.
- Runtime-installed Skill Orchestration with availability checks, fallback, verification, and usage-memory records.
- Token / Cost-aware Context Budget and Context Usage Report.
- Real host Runtime replay report and replay gap repair.
- PalBench Collaboration expanded to 87 qualitative no-code regression cases.

## Deep Conductor Boundary

Deep Conductor is a no-code orchestration protocol and task-package system.

AgentPal does not automatically execute Deep Conductor packages, launch Subagents, call external Agents, scan all Runtime Skills, run tools, publish releases, meter tokens, or calculate cost. Host Agent Runtimes perform real execution and must return evidence.

## How To Start

- Documentation home: `docs/README.md`
- Resource index: `RESOURCE_INDEX.md`
- Public v0.3 capability summary: `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-public-capability-summary.md`
- Deep Conductor E2E guide: `docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md`
- v0.3 readiness: `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-deep-conductor-readiness.md`
- v0.3 integration matrix: `evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md`
- PalBench Collaboration: `evals/palbench-collaboration/README.md`

## Validation

- R63 readiness recommendation: enter `v0.3.0-rc.1` release preparation.
- v0.3 integration matrix: pass / partial / unavailable status preserved.
- PalBench Collaboration: 87 qualitative no-code cases.
- R61 / R62 replay reports: real host Runtime replay and gap repair completed.
- Release-preparation checks should pass before tag / push / GitHub Release work.

## Known Limitations

- This is a release candidate, not stable.
- Runtime Skill availability and output quality are host Runtime evidence issues.
- Subagent and external Agent execution are unavailable / unknown / blocked unless the host Runtime explicitly supports and permits them.
- Context Budget is qualitative unless the host Runtime provides exact metering evidence.
- PalBench Collaboration is qualitative regression coverage, not statistical benchmark proof.
- GitHub publication is complete only after the intended commit and tag are pushed and this draft is used to create a GitHub pre-release.

## Not Included

- No desktop app, web app, CLI runtime, daemon, service, scanner, validator, installer, database, token meter, or cost calculator.
- No automatic Deep Conductor background executor.
- No automatic Subagent launch or external Agent calls by AgentPal.
- No automatic Runtime Skill detection.
- No stable `v0.3.0` claim.

## Release Notes

Use `RELEASE_NOTES.md` for the full release notes and `RELEASE_MANIFEST.md` for the release package manifest.
