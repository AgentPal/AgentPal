# PalSmith

PalSmith is AgentPal's official Pal asset governance Pal.

PalSmith is a no-code workflow Pal. It helps the current runtime plan Pal creation, AI team building, Pal team governance, cross-Pal review, import staging, export, health inspection, quality inspection, version review, publish quality gates, runtime call verification, GitHub import verification, snapshot, rollback, official Pal registration, and central roster update work.

Registered id/path: `palsmith-pal-governor` at `official/pals/PalSmith-pal-governor`.

## Current Product Status

PalSmith E2E testing passed the core functional loop in an independent test copy. v0.1 can create Pals, create Pal teams, maintain a test Pal, stage imports, create clean exports, enforce with-memory export boundaries, reject ordinary Skills from contacts, and preserve the no-code boundary.

PalSmith is now entering v0.2 product enhancement. v0.2 focuses on making PalSmith the fastest way for users to build their own AI team: Pal quality inspection, responsibility conflict detection, capability maps, team design, version governance, Eval Lab, and Pal lifecycle workflow.

R40 adds the first v0.2 implementation slice for end-to-end creation productization: copyable first-Pal and AI-team task packages, material ingestion mapping, health-check runbooks, repair packages, realistic demos, and a 14-case E2E self-test. This is a started / first implementation state, not a claim that all v0.2 work is complete.

This is not a final release state. v0.1 publication is paused while v0.2 Pal quality governance and AI team-building experience are strengthened.

v0.3 adds AI Team Builder, team governance, cross-Pal review, publish quality gate, runtime call verification, GitHub import verification, and a quickstart for users who want to build an AI team in minutes.

v0.4 turns those capabilities into a more demonstrable user path: a 5-minute quickstart, AI team blueprints, a 10-minute demo script, a readiness matrix that unifies lifecycle / Eval Lab / publish quality gates, and a regression test plan for the next real test round.

R16 v0.4-fix repairs the quality model. PalSmith quality inspection now asks whether the Pal can actually perform its declared job, not just whether expected files exist. Creation now starts from Pal name, responsibilities, goals, scenarios, user materials, and research needs, then builds a job expertise model before proposing files. User material ingestion must preserve source content, keep traceability, and classify material into knowledge, skill, workflow, runbook, template, eval, and governance assets instead of compressing everything into a short summary.

R17 quality testing in an internal test workspace showed that the repaired PalSmith flow can produce a test job Pal with source inventory, source coverage matrix, complete knowledge / skills / workflows / templates / evals, user material preservation, and a real task simulation. The formal AgentPal Workspace does not copy the test Pal or test reports; it keeps reusable release-safe learning through the source coverage template and long-material ingestion example.

## Delegation And Handoff

PalSmith is not triggered by keyword matching. AgentPal Core is not a semantic classifier or planner.

Mira is the default entry Pal, but any current Pal may consult, delegate, or hand off to PalSmith after AI judgement shows the request belongs to Pal asset governance. Example task types include creating Pals, creating teams, maintaining Pals, checking quality, detecting conflicts, mapping capabilities, importing/exporting, central roster suggestions, snapshot/rollback, runtime call verification, and publish quality gates.

## What PalSmith Is Not

PalSmith is not a CLI, scanner, validator, exporter, importer, installer, daemon, UI, or background service. AgentPal does not require users to install Python, Node.js, Rust, or any package runtime to use PalSmith.

## How PalSmith Works

Users talk to PalSmith through AgentPal:

```text
/pal PalSmith 创建一个小红书运营 Pal
/pal PalSmith 体检所有 Pal
/pal PalSmith 从 GitHub 导入这个 Pal
/pal PalSmith 导出 Research Pal，不含记忆
```

PalSmith then prepares a Runtime Task Package. The current Agent Runtime, such as Codex or Claude Code, performs any approved file reads, writes, archive creation, download, copy, or JSON update and returns evidence.

For the task package field standard, see [Runtime Task Package](03-pal-pack-standard/14-runtime-task-package.md). For complete usage flows, see [PalSmith end-to-end workflows](07-authoring-pals/13-palsmith-end-to-end-workflows.md).

For the v0.2 creation loop, see [PalSmith end-to-end productization](06-palsmith/palsmith-end-to-end-productization.md), [create first professional Pal](../official/pals/PalSmith-pal-governor/templates/task-packages/create-first-professional-pal.md), and [create AI team from goal](../official/pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md).

## No-Code Workflows

- Pal Health Inspection Task Package
- Pal Quality Inspection Task Package
- User Material Ingestion Task Package
- Content Preservation Review Task Package
- Web Research To Knowledge Task Package
- PalSmith Self Health Review Task Package
- Pal Conflict Detection Task Package
- Pal Capability Map Task Package
- Pal Team Design Task Package
- AI Team Builder Task Package
- Pal Team Governance Task Package
- Cross-Pal Review Task Package
- Pal Publish Quality Gate Task Package
- Pal Readiness Review Task Package
- Pal Runtime Call Verification Task Package
- GitHub Import Verification Task Package
- Clean Pal Export Task Package
- With Memory Export Task Package
- Pal Import Staging Task Package
- Pal Install Task Package
- Pal Creation Task Package
- Pal Team Creation Task Package
- Create First Professional Pal Task Package
- Create AI Team From Goal Task Package
- User Material Ingestion To Pal Assets Workflow
- Pal Health Check Runbook
- AI Team Health Check Runbook
- Repair Package Template
- central roster update task package
- snapshot task package
- rollback task package
- Pal Version Upgrade Task Package
- Pal Version Rollback Task Package
- Pal Eval Lab Task Package
- Official Pal Registration Task Package

Every workflow separates PalSmith judgement from runtime execution, asks for user confirmation before controlled writes, and reports evidence after the runtime acts.

With-memory export always requires strong confirmation and a privacy report. Imports always begin in staging; central roster updates are separate confirmed task packages.

## Current Release Status

Completed for the current release candidate:

- official registration in `agentpal.json`, `workspace/organization/contacts/pals.json`, and `workspace/organization/contacts/PAL_CONTACTS.md`
- Runtime Task Package standard
- end-to-end workflows
- task package templates and template index
- example task packages and example index
- PalSmith delegation and handoff guidance and few-shot examples
- no-code release checklist
- PalSmith release-scope review
- PalSmith E2E test summary
- PalSmith v0.4 regression test plan

Not included:

- CLI
- embedded tool code
- UI
- automatic scanner or validator
- automatic importer or exporter
- installer or daemon

If future maintainers build a PalSmith CLI, Pal Hub manager, UI, or installer, it must be an external optional project. It must not enter the AgentPal standard Pal Pack release content.

## Next Reading

- [Use PalSmith](07-authoring-pals/12-use-palsmith.md)
- [PalSmith v0.2 productization](06-palsmith/README.md)
- [PalSmith end-to-end productization](06-palsmith/palsmith-end-to-end-productization.md)
- [PalSmith end-to-end workflows](07-authoring-pals/13-palsmith-end-to-end-workflows.md)
- [Pal import/export standard](03-pal-pack-standard/13-pal-import-export.md)
- [Runtime Task Package standard](03-pal-pack-standard/14-runtime-task-package.md)
- [No-code release checklist](../archive/migration-from-v0.3/release-candidate-docs/05-no-code-release-checklist.md)
- [PalSmith release-scope review](../archive/migration-from-v0.3/release-candidate-docs/06-palsmith-release-scope-review.md)
- [PalSmith task package templates](../official/pals/PalSmith-pal-governor/templates/task-packages/README.md)
- [PalSmith example task packages](../official/pals/PalSmith-pal-governor/examples/task-packages/README.md)
- [PalSmith Pal lifecycle](07-authoring-pals/14-palsmith-pal-lifecycle.md)
- [PalSmith quickstart AI team](07-authoring-pals/15-palsmith-quickstart-ai-team.md)
- [PalSmith demo script](07-authoring-pals/16-palsmith-demo-script.md)
- [PalSmith v0.4 regression test plan](../archive/migration-from-v0.3/release-candidate-docs/12-palsmith-v0.4-regression-test-plan.md)
- [PalSmith AI team blueprints](../official/pals/PalSmith-pal-governor/examples/ai-team-blueprints/README.md)
- [PalSmith skills index](../official/pals/PalSmith-pal-governor/skills/README.md)
- [PalSmith knowledge index](../official/pals/PalSmith-pal-governor/knowledge/README.md)
- [PalSmith source coverage report template](../official/pals/PalSmith-pal-governor/templates/source-coverage-report-template.md)
