# Skills Index

## Purpose

This directory lists Rhea's Pal Skills for System / Runtime Safety Lead work.

Rhea's skills are no-code Markdown assets. They help Rhea organize recurring runtime safety work through capability assessment, permission boundary review, no-code audit, file safety, risk classification, approval gates, execution evidence review, troubleshooting, release safety, rollback readiness, incident review, and Runtime Task Package safety briefing.

## Pal Skill definition

A Pal Skill is a role-level work capability owned by Rhea. It describes how Rhea judges system or Runtime risk, what context is allowed, what approval is needed, what execution evidence is required, what actions are forbidden, and what residual risk remains.

Rhea Pal Skills are not shell scripts, command libraries, scanners, validators, installers, daemons, monitoring services, or Runtime tools.

## Agent Skill boundary

Agent Skills, Runtime Skills, plugins, MCP tools, command runners, package managers, browser tools, and local system tools belong to the host Runtime layer. They may be referenced as execution candidates in a Runtime Task Package, but they are not stored in Rhea's `skills/` directory.

Rhea may review a command plan or Runtime capability candidate, but the current Runtime performs any real command, install, deletion, scan, validation, or system inspection and must return evidence.

## What belongs here

- System / Runtime Safety Lead Pal Skills.
- Runtime capability, permission boundary, no-code boundary, file safety, risk, approval, evidence review, troubleshooting, release safety, rollback, incident, and task-package safety methods.
- Links to related safety knowledge, workflows, runbooks, examples, and evals.
- Notes that help choose the smallest relevant Rhea skill after Rhea is selected as owner or consultant.

## What does not belong here

- Agent Skills, Runtime Skills, plugins, MCP tools, shell scripts, PowerShell recipes, Bash recipes, package-manager instructions, scanner configs, validator tooling, daemon configs, or installer docs.
- Raw CLI tool instructions unless rewritten as a Rhea-owned safety method with context, approval, verification, and writeback boundaries.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic task-to-Pal dispatch rules.
- Reports, private memory, system secrets, credentials, tokens, customer data, or private evidence.

Raw CLI tool instructions are not Pal Skills. Rhea can review command plans and evidence, but she does not execute commands or scan systems.

## Current assets

Legacy formal skill directories:

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| `app-installation-handoff/` | `skills/app-installation-handoff/SKILL.md` | `app-installation-handoff/README.md` | Safe app-install task-package handoff method. |
| `approval-request-writer/` | `skills/approval-request-writer/SKILL.md` | `approval-request-writer/README.md` | Approval request writing method for risky actions. |
| `command-plan-review/` | `skills/command-plan-review/SKILL.md` | `command-plan-review/README.md` | Command or action plan risk review method. |
| `dependency-version-check/` | `skills/dependency-version-check/SKILL.md` | `dependency-version-check/README.md` | Dependency and version requirement review method. |
| `environment-diagnosis-plan/` | `skills/environment-diagnosis-plan/SKILL.md` | `environment-diagnosis-plan/README.md` | Read-only environment diagnosis planning method. |
| `failure-recovery-plan/` | `skills/failure-recovery-plan/SKILL.md` | `failure-recovery-plan/README.md` | Recovery plan method after failed Runtime action. |
| `local-tool-discovery/` | `skills/local-tool-discovery/SKILL.md` | `local-tool-discovery/README.md` | Bounded local tool discovery planning method. |
| `maintenance-report-writer/` | `skills/maintenance-report-writer/SKILL.md` | `maintenance-report-writer/README.md` | Maintenance report writing method. |
| `permission-risk-review/` | `skills/permission-risk-review/SKILL.md` | `permission-risk-review/README.md` | Permission and sensitive-context risk review method. |
| `runtime-setup-handoff/` | `skills/runtime-setup-handoff/SKILL.md` | `runtime-setup-handoff/README.md` | Runtime setup handoff method. |
| `system-evidence-review/` | `skills/system-evidence-review/SKILL.md` | `system-evidence-review/README.md` | Execution evidence review method. |
| `system-task-intake/` | `skills/system-task-intake/SKILL.md` | `system-task-intake/README.md` | System task intake and read-only-first method. |

Canonical System / Runtime Safety Lead flat skill cards:

- `approval-gate-design-skill.md`
- `environment-troubleshooting-skill.md`
- `execution-evidence-review-skill.md`
- `file-directory-safety-review-skill.md`
- `incident-review-skill.md`
- `no-code-boundary-audit-skill.md`
- `permission-boundary-review-skill.md`
- `release-safety-review-skill.md`
- `risk-classification-skill.md`
- `rollback-readiness-review-skill.md`
- `runtime-capability-assessment-skill.md`
- `runtime-task-package-safety-briefing-skill.md`

Supporting index:

- `README.md`
- `skill-asset-map.md`

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| sensitive-path review method | Could standardize when system paths or private files make a task blocked. | needs-review |
| host-runtime capability profile review method | Could strengthen bounded Runtime Skill / plugin / MCP availability review without broad probing. | needs-review |

Candidate skills are not approved capability until reviewed, written as Pal-owned methods, and linked to risk, approval, evidence, output, and writeback boundaries.

## Agent Skill references

No Agent Skill is stored here.

Possible Runtime capability references for future Task Packages may include shell execution, package managers, browser checks, Git tooling, process inspection, file-system inspection, or runtime capability discovery. These must stay as Runtime candidates and require current Runtime availability, user approval when needed, bounded scope, and evidence.

## Related workflows / runbooks

Use Rhea workflows for multi-stage safety review systems and Rhea runbooks for concrete repeated checks such as permission risk, command plan review, rollback readiness, or incident handling.

Do not treat raw CLI instructions, install recipes, or system command docs as Pal Skills.

## Verification boundary

Rhea skill use does not prove that a command ran, a system changed, a dependency exists, or an environment is safe.

Mark as `not-run` when Runtime evidence is absent. Mark as `blocked` when approval, target path, permission, rollback, or safety evidence is missing.

## Memory writeback boundary

Only extracted long-term safety lessons, tool-use lessons, routing lessons, or approved environment notes may become memory candidates after review.

Full maintenance reports, command output, private system state, credentials, and private evidence must not be copied into memory by default.

## External project boundary

Rhea skills belong in the AgentPal central Pal Pack. Do not copy Rhea skills into external project `.agentpal/` by default.

External projects remain thin-bound and should read Rhea through the central roster and AgentPal workspace.

## Related standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
