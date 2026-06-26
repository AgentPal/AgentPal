# Rhea System / Runtime Safety Lead Gap Report

Access date: 2026-06-26
Inspection method: PalSmith-style job fitness inspection using PalSmith quality inspection, web-research-to-knowledge, and content preservation rules. Runtime execution was used only for file reads, web research, Markdown/JSON edits, and verification evidence.

## PalSmith-Style Fitness Conclusion

Rhea already has a strong safety instinct: it warns about permissions, direct command execution, deletion, install actions, PATH changes, and evidence requirements. The gap is job depth and release-safe framing. Current assets still describe Rhea as a "System Pal" or "system and app steward", with legacy capability names such as app installation and runtime setup. Those are useful historical assets, but for the official default Pal set Rhea needs to become the System / Runtime Safety Lead Pal: runtime capability awareness, permission boundary review, least privilege, no-code boundary guarding, file/directory safety, risk classification, approval gate design, execution evidence review, environment troubleshooting, release safety, rollback readiness, and incident review.

## Current Positioning Problems

- Role Fit: Rhea is currently framed around system maintenance, app installation handoff, and runtime setup rather than System / Runtime Safety Lead.
- System / Runtime Expertise Depth: existing knowledge covers command risk, approval actions, PATH/version checks, and evidence format, but lacks a complete safety-lead job model.
- Runtime Capability Awareness: current assets mention runtime awareness but do not provide a canonical capability-assessment skill.
- Permission Boundary Understanding: permission-risk-review exists, but least privilege and approval gates need stronger knowledge and eval coverage.
- No-Code Boundary Guarding: no canonical no-code-boundary-audit skill exists for AgentPal release assets.
- File / Directory Safety Review: current assets cover deletion risk generally, but not a dedicated file/directory safety review skill.
- Risk Classification: existing risk levels need a canonical low / medium / high / critical / blocked scale tied to confirmation rules.
- Execution Evidence Review: existing system-evidence-review is useful, but this round requires required fields: what ran, where, executor, exit status or observable result, changed files, not-run items, risks, next action.
- Release Safety: currently underdeveloped for release preflight, rollback readiness, ignored outputs, and runtime artifacts.
- Incident / Failure Review: failure recovery exists; incident review and post-failure learning need their own assets.
- Collaboration Fit: current collaboration files are generic; Rhea needs explicit default-Pal boundaries for Mira, PalSmith, Atlas, Vega, Quinn, Morgan, Harper, and Nova.

## Existing Skills

Existing formal skills: system-task-intake, environment-diagnosis-plan, runtime-setup-handoff, app-installation-handoff, dependency-version-check, permission-risk-review, command-plan-review, failure-recovery-plan, local-tool-discovery, approval-request-writer, system-evidence-review, and maintenance-report-writer.

These are usable compatibility assets, but they do not fully cover System / Runtime Safety Lead responsibilities.

## Missing Skills

P0 missing canonical skills: runtime-capability-assessment-skill, permission-boundary-review-skill, no-code-boundary-audit-skill, file-directory-safety-review-skill, risk-classification-skill, approval-gate-design-skill, execution-evidence-review-skill, environment-troubleshooting-skill, release-safety-review-skill, rollback-readiness-review-skill, incident-review-skill, and runtime-task-package-safety-briefing-skill.

## Existing Knowledge

Existing knowledge covers system maintenance principles, risk levels, runtime setup basics, agent-runtime boundary, development environment basics, path/version checks, command risk, approval-required actions, system evidence format, and collaboration with code/risk review.

## Missing Knowledge

P0 missing canonical knowledge: system-runtime-role-knowledge, runtime-capability-knowledge, permission-boundary-knowledge, least-privilege-knowledge, no-code-boundary-knowledge, file-directory-safety-knowledge, risk-classification-knowledge, approval-gate-knowledge, evidence-based-operations-knowledge, environment-troubleshooting-knowledge, release-safety-knowledge, incident-review-knowledge, and rollback-readiness-knowledge.

## Missing Workflows And Runbooks

P0 workflows: runtime safety intake, no-code boundary review, high-risk operation approval, environment troubleshooting, release safety review, evidence review, incident review, and default-Pal collaboration.

P0 runbooks: no-code boundary check, runtime capability check, file operation risk review, release preflight risk, rollback readiness, and not-run evidence reporting.

## Web Research Needed

Rhea needed source-backed knowledge from SRE, security, incident management, least privilege, DevSecOps, GitHub workflow security, rollback, and change management sources. This research was run live and recorded in `pals/Rhea-system/research/source-inventory.md`.

## Evals Needed

P0 evals: system runtime capability, no-code boundary, risk approval, evidence review, release safety, incident review, and self-health.

## Priority Plan

P0:

- Rewrite Rhea identity and metadata to System / Runtime Safety Lead Pal.
- Add the 12 required skill cards.
- Add the 13 required knowledge cards.
- Add live research inventory and coverage matrix.
- Add default-Pal collaboration boundary and workflow.
- Add dedicated evals and self-health report.

P1:

- Add workflows and runbooks so the skills are operational.
- Update indexes, README files, contacts, registry, and `agentpal.json`.
- Align formal skill count and skill list with actual skill inventory.

P2:

- Keep existing directory skills as compatibility assets.
- Later pass can consolidate legacy install/setup language after release review.

## PalSmith-Style Upgrade Task Package

Goal: Upgrade Rhea into AgentPal's official System / Runtime Safety Lead Pal without turning AgentPal into a code package, command runner, installer, scanner, daemon, or validation app.

Owner Pal: Rhea for system/runtime safety assets. PalSmith-style governance is used for gap review and final fitness review. Atlas is only the Runtime execution layer for file edits in this round.

Runtime role: read current files, run live web research, edit Markdown and JSON, run checks, and report evidence. Runtime must not add code, tools, installers, scanners, daemons, validators, or UI.

Files to update:

- `pals/Rhea-system/PAL.md`
- `pals/Rhea-system/SKILL.md`
- `pals/Rhea-system/AGENTS.md`
- `pals/Rhea-system/pal.json`
- `pals/Rhea-system/README.md`
- `pals/Rhea-system/identity/*`
- `pals/Rhea-system/skills/*.md`
- `pals/Rhea-system/knowledge/*.md`
- `pals/Rhea-system/workflows/*.md`
- `pals/Rhea-system/runbooks/*.md`
- `pals/Rhea-system/evals/*.md`
- `pals/Rhea-system/research/*.md`
- `README.md`, `docs/README.md`, `contacts/pals.json`, `registry/pal.index.json`, `agentpal.json`

Acceptance criteria:

- Rhea identity says System / Runtime Safety Lead Pal.
- Every required skill has Purpose, When to use, Inputs, Required context, Process, Output, Quality bar, User confirmation points, No-code boundary, Common mistakes, and Example.
- Every required knowledge file has concept explanation, judgement standards, examples, counterexamples, scope, conversion to skill/workflow/eval, common mistakes, and source notes.
- Every workflow and runbook has Trigger, Inputs, Steps, Decision points, Outputs, Quality checks, Required user confirmation, and Evidence to return.
- Source inventory records source ID, title, URL, publisher, access date, source type, trust level, key points, relevance, target artifact, file path, and coverage status.
- JSON files parse.
- Required anchors are searchable.
- No code files, tool directories, scanner, validation tooling, installer, UI, daemon, crawler, or downloader are added.
- Forbidden role expressions appear only in negative boundary examples if present.

