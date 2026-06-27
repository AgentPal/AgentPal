# AgentPal Release Notes

## v0.3.0-rc.1

AgentPal v0.3.0-rc.1 is a release candidate for the no-code orchestration prototype line.

It strengthens Deep Conductor, Multi-Pal Collaboration, Context Packet handoff, evidence-based verification, Runtime Skill-aware task packaging, cross-runtime memory continuity, and qualitative release regression coverage.

This is not a stable release. The GitHub Release should be marked as a pre-release.

## What This Release Is

AgentPal remains a Markdown / JSON / protocol workspace for host Agent Runtimes. It is a Pal layer and Pal Pack Standard practice, not an Agent runtime, multi-agent runtime, app, CLI, service, or execution layer.

Deep Conductor in v0.3.0-rc.1 is a no-code orchestration protocol and task-package system. Host Runtimes perform real file reads, writes, commands, tool calls, rendering, browsing, publishing, and Skill/plugin/MCP use, and must return evidence.

## What Is New In v0.3.0-rc.1

- Deep Conductor E2E package and synthesis report.
- Deep Conductor Master Loop and Project Conductor workflow.
- Context Packet and Context Access boundaries for controlled Pal handoff.
- `/pal Name` and `@Pal` collaboration protocols as plain-text AgentPal behavior.
- Owner + Verifier workflow with independent evidence checks.
- Parallel Independent Review workflow with isolated reviewer packets.
- Cross-Runtime Pal Memory, Routing Memory, Runtime Skill Usage Memory, and continuation packages.
- Runtime-installed Skill Orchestration packages with availability checks, fallback, verification, and usage-memory records.
- Token / Cost-aware Context Budget, Context Usage Report, and prompt-shaping guidance.
- Deep Conductor real host Runtime replay report and replay gap repair.
- PalBench Collaboration expanded to 87 qualitative no-code regression cases.
- v0.3 readiness, public capability summary, release checklist, integration matrix, and coverage audit.

## What Remains No-Code / Host-Runtime-Dependent

- Deep Conductor produces plans, Context Packets, Runtime Skill-aware packages, verification plans, synthesis reports, and next-round recommendations.
- AgentPal does not execute those packages by itself.
- Runtime-installed Skills are host Runtime capabilities. AgentPal may name them as candidates, but the current host Runtime must prove availability and execute them if authorized.
- Subagent and external Agent handoff remains unavailable, unknown, blocked, or host-dependent unless a host Runtime explicitly supports and permits it.
- Context Budget is qualitative unless the host Runtime provides exact token or cost metering evidence.
- Routing Memory is a writeback candidate and judgement input, not an automatic database or fixed route table.

## What This Release Does Not Include

- No stable `v0.3.0` release.
- No desktop app, web app, CLI runtime, daemon, service, scanner, validator, installer, database, token meter, or cost calculator.
- No automatic Deep Conductor background executor.
- No automatic Subagent launch or external Agent calls by AgentPal.
- No automatic scan of all Runtime Skills, plugins, or MCP tools.
- No claim that Runtime Skills are installed or available in a user's current Runtime.
- No statistical benchmark proof or foundation-model performance comparison from PalBench.
- No replacement for Codex, Claude Code, OpenCode, OpenHands, Gemini CLI, or another host Runtime.

## How To Try It

1. Open the AgentPal Workspace in a Markdown/JSON-capable host Runtime.
2. Start from `docs/README.md` or `RESOURCE_INDEX.md`.
3. For v0.3 concepts, read `docs/09-roadmap/v0.3-public-capability-summary.md`.
4. For Deep Conductor, read `docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md`.
5. For release evidence, read `docs/09-roadmap/v0.3-deep-conductor-readiness.md` and `evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md`.
6. Use the host Runtime to perform any real execution and report evidence.

## Known Limitations

- Runtime Skill execution quality is not proven unless the current host Runtime runs the named Skill and returns evidence.
- Browser/render verification, publishing, and external calls remain host Runtime tasks.
- Subagent / external Agent execution is not an AgentPal capability.
- PalBench Collaboration is qualitative regression coverage, not a statistical benchmark.
- Cross-runtime memory freshness still needs future replay after time passes.
- Release publication requires a separate tag / push / GitHub Release operation after maintainer approval.

## Validation Summary

- R63 recommended entering `v0.3.0-rc.1` release preparation.
- v0.3 integration matrix records pass / partial / unavailable boundaries.
- PalBench Collaboration task index contains 87 cases.
- R61 real host Runtime replay and R62 gap repair preserve partial, unavailable, blocked, and not-run outcomes.
- R64 release preparation should verify JSON, no-runtime, no-program-future, no-hardcoded-routing, no-future-as-current, public safety, PalBench count, public entry links, and Git state before tag / push work.

## Next Steps

Create the GitHub release from tag `v0.3.0-rc.1`, use `GITHUB_RELEASE_DRAFT.md` as the release body, and mark it as a pre-release rather than a stable release.
