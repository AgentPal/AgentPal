# AgentPal Documentation

This documentation set is the public entry point for AgentPal v0.2.0-rc.1.

AgentPal is a Pal layer and Pal Pack Standard practice for Markdown/JSON-capable agent runtimes. It is not an Agent layer, not a multi-agent runtime, and not an execution layer.

## Start Here

- [What is AgentPal?](00-overview/00-what-is-agentpal.md)
- [Current status](00-overview/01-current-status.md)
- [Repository map](00-overview/02-repository-map.md)
- [Why Pal?](01-concepts/07-why-pal.md)
- [Pal Teams, Multi-Pal Collaboration, and Deep Conductor](01-concepts/08-pal-teams-collaboration-and-deep-conductor.md)
- [Quick start](02-getting-started/00-quick-start.md)
- [Mira-first usage](02-getting-started/mira-first-usage.md)
- [Mira-first prompt cards](02-getting-started/mira-first-prompt-cards.md)
- [Multi-Pal collaboration prompt cards](02-getting-started/multi-pal-collaboration-prompt-cards.md)
- [Official Pal examples index](07-official-pals/official-pal-examples-index.md)
- [Use AgentPal with Claude Code](10-using-agentpal-with-claude-code.md)
- [Use AgentPal with generic CLI agents](11-using-agentpal-with-cli-agents.md)
- [Simple Pal Mode](01-concepts/05-simple-pal-mode.md)
- [Pal Pack Standard](03-pal-pack-standard/README.md)
- [Author your own Pal](07-authoring-pals/README.md)
- [Orchestration methodology](05-orchestration-methodology/README.md)
- [Pal Teams and Deep Conductor](05-orchestration-methodology/11-pal-teams-and-deep-conductor.md)
- [Capability Inventory minimal usable design](05-orchestration-methodology/capability-inventory-minimal-usable-design.md)
- [PalBench Light Suite](../evals/palbench-light/README.md)
- [PalBench Light suite plan](research/palbench-light-suite-plan.md)
- [Runtime Adapter stability guide](04-runtime-guides/runtime-adapter-stability-guide.md)
- [Runtime Adapter troubleshooting prompt cards](04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md)
- [v0.2 release readiness](09-roadmap/v0.2-release-readiness.md)
- [v0.2 public capability summary](09-roadmap/v0.2-public-capability-summary.md)
- [v0.2 integration test matrix](../evals/v0.2-integration/v0.2-integration-test-matrix.md)
- [v0.3 development plan](09-roadmap/v0.3-development-plan.md)
- [v0.3 task pool](09-roadmap/v0.3-task-pool.md)
- [v0.3 Deep Conductor readiness](09-roadmap/v0.3-deep-conductor-readiness.md)
- [v0.3 public capability summary](09-roadmap/v0.3-public-capability-summary.md)
- [v0.3 release checklist](09-roadmap/v0.3-release-checklist.md)
- [v0.3 Deep Conductor integration matrix](../evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md)
- [PalBench Collaboration coverage audit](research/palbench-collaboration-coverage-audit.md)
- [No-code future boundary](09-roadmap/no-code-future-boundary.md)
- [Deep Conductor master goal](05-orchestration-methodology/deep-conductor-master-goal.md)
- [Deep Conductor master loop usage guide](05-orchestration-methodology/deep-conductor-master-loop-usage-guide.md)
- [Deep Conductor E2E usage guide](05-orchestration-methodology/deep-conductor-e2e-usage-guide.md)
- [Deep Conductor real Runtime replay gap analysis](research/deep-conductor-real-runtime-replay-gap-analysis.md)
- [Cross-Runtime Pal Memory](05-orchestration-methodology/cross-runtime-pal-memory.md)
- [Project Conductor workflow](../orchestration/project-conductor-workflow.md)
- [Subagent / External Agent handoff boundary](../orchestration/subagent-external-agent-handoff-boundary.md)
- [Memory Boundary Protocol](../orchestration/memory-boundary-protocol.md)
- [Pal Skill vs Runtime Skill protocol](../orchestration/pal-skill-vs-runtime-skill-protocol.md)
- [Runtime-installed Skill Orchestration](05-orchestration-methodology/runtime-installed-skill-orchestration-guide.md)
- [Runtime Skill Candidate Decision Protocol](../orchestration/runtime-skill-candidate-decision-protocol.md)
- [Token / Cost-aware Deep Conductor](05-orchestration-methodology/token-cost-aware-deep-conductor.md)
- [Runtime Skill-aware Task Package](../templates/orchestration/runtime-skill-aware-task-package.md)
- [Runtime Skill Availability Check Package](../templates/orchestration/runtime-skill-availability-check-package.md)
- [Runtime Skill Fallback Package](../templates/orchestration/runtime-skill-fallback-package.md)
- [Cross-runtime Pal memory protocol](../memory/runtime/cross-runtime-pal-memory-protocol.md)
- [Pal Project Memory Snapshot template](../templates/memory/pal-project-memory-snapshot.md)
- [Routing Memory Record template](../templates/memory/routing-memory-record.md)
- [Runtime Skill Usage Memory Record template](../templates/memory/runtime-skill-usage-memory-record.md)
- [Cross-Runtime Continuation Task Package](../templates/orchestration/cross-runtime-continuation-task-package.md)
- [Token / Cost-aware Conductor policy](../orchestration/token-cost-aware-conductor-policy.md)
- [Context Budget Protocol](../orchestration/context-budget-protocol.md)
- [Prompt Shaping By Model And Reasoning](../orchestration/prompt-shaping-by-model-and-reasoning.md)
- [Context Usage Report template](../templates/orchestration/context-usage-report.md)
- [Context Packet usage guide](05-orchestration-methodology/context-packet-usage-guide.md)
- [Owner + Verifier usage guide](05-orchestration-methodology/owner-verifier-usage-guide.md)
- [Parallel Independent Review usage guide](05-orchestration-methodology/parallel-independent-review-usage-guide.md)
- [PalBench Collaboration Suite](../evals/palbench-collaboration/README.md)
- [Validation and evidence](06-validation-and-evidence/README.md)
- [v0.1.0-rc.1 release candidate](08-release-candidate/README.md)
- [v0.2 development plan](09-roadmap/v0.2-development-plan.md)
- [v0.2 task pool](09-roadmap/v0.2-task-pool.md)

## PalSmith Quick Links

- [PalSmith overview](PalSmith.md)
- [Use PalSmith](07-authoring-pals/12-use-palsmith.md)
- [PalSmith end-to-end workflows](07-authoring-pals/13-palsmith-end-to-end-workflows.md)
- [PalSmith Pal lifecycle](07-authoring-pals/14-palsmith-pal-lifecycle.md)
- [PalSmith quickstart AI team](07-authoring-pals/15-palsmith-quickstart-ai-team.md)
- [PalSmith demo script](07-authoring-pals/16-palsmith-demo-script.md)
- [PalSmith v0.4 regression test plan](08-release-candidate/12-palsmith-v0.4-regression-test-plan.md)
- [PalSmith v0.2 productization](06-palsmith/README.md)
- [PalSmith end-to-end productization](06-palsmith/palsmith-end-to-end-productization.md)
- [Create first professional Pal task package](../pals/PalSmith-pal-governor/templates/task-packages/create-first-professional-pal.md)
- [Create AI team from goal task package](../pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md)
- [Pal import/export standard](03-pal-pack-standard/13-pal-import-export.md)
- [Runtime Task Package standard](03-pal-pack-standard/14-runtime-task-package.md)
- [No-code release checklist](08-release-candidate/05-no-code-release-checklist.md)
- [PalSmith release-scope review](08-release-candidate/06-palsmith-release-scope-review.md)
- [PalSmith E2E test summary](08-release-candidate/11-palsmith-e2e-test-summary.md)
- [PalSmith Pal Pack](../pals/PalSmith-pal-governor/README.md)

## Mira Leader Quick Links

- [Mira Pal Pack](../pals/Mira-main/README.md)
- [Mira-first usage](02-getting-started/mira-first-usage.md)
- [Mira-first prompt cards](02-getting-started/mira-first-prompt-cards.md)
- [Mira first task intake template](../pals/Mira-main/templates/task-packages/mira-first-task-intake.md)
- [Mira composite deliverable template](../pals/Mira-main/templates/task-packages/mira-composite-deliverable-task-package.md)
- [Mira runtime brief template](../pals/Mira-main/templates/task-packages/mira-runtime-brief.md)
- [Mira leader skills](../pals/Mira-main/skills/index.md)
- [Mira leader knowledge](../pals/Mira-main/knowledge/INDEX.md)
- [Mira workflows](../pals/Mira-main/workflows/index.md)
- [Mira runbooks](../pals/Mira-main/runbooks/INDEX.md)
- [Mira evals](../pals/Mira-main/evals/README.md)
- [Mira self-health report](../pals/Mira-main/reports/mira-self-health-report.md)
- [PalSmith Mira Leader review](../pals/Mira-main/reports/palsmith-mira-leader-review.md)

## Official Pal Example Links

- [Official Pal examples index](07-official-pals/official-pal-examples-index.md)
- [Official Pal example library plan](07-official-pals/official-pal-example-library-plan.md)
- [Official Pal example library self-test](../evals/official-pals/official-pal-example-library-self-test.md)
- [Cross-Pal product/research/dev/QA/docs example](../examples/orchestration/cross-pal-product-research-dev-qa-docs.md)
- [Cross-Pal PalSmith AI team example](../examples/orchestration/cross-pal-palsmith-create-ai-team.md)
- [Cross-Pal release readiness example](../examples/orchestration/cross-pal-release-readiness-review.md)

## Capability Inventory Quick Links

- [Capability Inventory minimal usable design](05-orchestration-methodology/capability-inventory-minimal-usable-design.md)
- [Capability profiles index](../capabilities/README.md)
- [Runtime profiles](../capabilities/runtime-profiles/README.md)
- [Model profiles](../capabilities/model-profiles/README.md)
- [Reasoning profiles](../capabilities/reasoning-profiles/README.md)
- [Skill profiles](../capabilities/skill-profiles/README.md)
- [Pal capability profiles](../capabilities/pal-profiles/README.md)
- [Capability Inventory self-test](../evals/capability-inventory/capability-inventory-minimal-usable-self-test.md)
- [Capability Inventory task judgement example](../examples/orchestration/capability-inventory-task-judgement-example.md)

## PalBench Light Quick Links

- [PalBench Light suite plan](research/palbench-light-suite-plan.md)
- [PalBench Light eval index](../evals/palbench-light/task-index.md)
- [PalBench Light scoring rubric](../evals/palbench-light/scoring-rubric.md)
- [PalBench Light case template](../evals/palbench-light/case-template.md)
- [PalBench Light suite self-test](../evals/palbench-light/palbench-light-suite-self-test.md)

## v0.3 Orchestration Prototype Quick Links

- [v0.3 development plan](09-roadmap/v0.3-development-plan.md)
- [v0.3 task pool](09-roadmap/v0.3-task-pool.md)
- [v0.3 Deep Conductor readiness](09-roadmap/v0.3-deep-conductor-readiness.md)
- [v0.3 public capability summary](09-roadmap/v0.3-public-capability-summary.md)
- [v0.3 release checklist](09-roadmap/v0.3-release-checklist.md)
- [No-code future boundary](09-roadmap/no-code-future-boundary.md)
- [Deep Conductor master goal](05-orchestration-methodology/deep-conductor-master-goal.md)
- [Deep Conductor master loop usage guide](05-orchestration-methodology/deep-conductor-master-loop-usage-guide.md)
- [Deep Conductor E2E usage guide](05-orchestration-methodology/deep-conductor-e2e-usage-guide.md)
- [Cross-Runtime Pal Memory](05-orchestration-methodology/cross-runtime-pal-memory.md)
- [Project Conductor workflow](../orchestration/project-conductor-workflow.md)
- [Memory Boundary Protocol](../orchestration/memory-boundary-protocol.md)
- [Pal Skill vs Runtime Skill protocol](../orchestration/pal-skill-vs-runtime-skill-protocol.md)
- [Runtime-installed Skill Orchestration](05-orchestration-methodology/runtime-installed-skill-orchestration-guide.md)
- [Runtime Skill Candidate Decision Protocol](../orchestration/runtime-skill-candidate-decision-protocol.md)
- [Token / Cost-aware Deep Conductor](05-orchestration-methodology/token-cost-aware-deep-conductor.md)
- [Runtime Skill-aware Task Package](../templates/orchestration/runtime-skill-aware-task-package.md)
- [Runtime Skill Availability Check Package](../templates/orchestration/runtime-skill-availability-check-package.md)
- [Runtime Skill Fallback Package](../templates/orchestration/runtime-skill-fallback-package.md)
- [Project Conductor Task Map template](../templates/orchestration/project-conductor-task-map.md)
- [Deep Conductor Plan template](../templates/orchestration/deep-conductor-plan.md)
- [Deep Conductor E2E Package template](../templates/orchestration/deep-conductor-e2e-package.md)
- [Deep Conductor E2E Synthesis Report template](../templates/orchestration/deep-conductor-e2e-synthesis-report.md)
- [E2E user-facing short summary template](../templates/orchestration/e2e-user-facing-short-summary.md)
- [External Agent handoff package](../templates/orchestration/external-agent-handoff-package.md)
- [Subagent task package](../templates/orchestration/subagent-task-package.md)
- [Next-Round Runtime Task Package template](../templates/orchestration/next-round-runtime-task-package.md)
- [Conductor Decision Record template](../templates/orchestration/conductor-decision-record.md)
- [Cross-runtime Pal memory protocol](../memory/runtime/cross-runtime-pal-memory-protocol.md)
- [Pal Project Memory Snapshot template](../templates/memory/pal-project-memory-snapshot.md)
- [Routing Memory Record template](../templates/memory/routing-memory-record.md)
- [Runtime Skill Usage Memory Record template](../templates/memory/runtime-skill-usage-memory-record.md)
- [Cross-Runtime Continuation Task Package](../templates/orchestration/cross-runtime-continuation-task-package.md)
- [Token / Cost-aware Conductor policy](../orchestration/token-cost-aware-conductor-policy.md)
- [Context Budget Protocol](../orchestration/context-budget-protocol.md)
- [Prompt Shaping By Model And Reasoning](../orchestration/prompt-shaping-by-model-and-reasoning.md)
- [Context Budget Plan template](../templates/orchestration/context-budget-plan.md)
- [Context Usage Report template](../templates/orchestration/context-usage-report.md)
- [Context Packet usage guide](05-orchestration-methodology/context-packet-usage-guide.md)
- [Owner + Verifier usage guide](05-orchestration-methodology/owner-verifier-usage-guide.md)
- [Parallel Independent Review usage guide](05-orchestration-methodology/parallel-independent-review-usage-guide.md)
- [Multi-Pal collaboration prompt cards](02-getting-started/multi-pal-collaboration-prompt-cards.md)
- [Context Packet protocol](../orchestration/context-packet-protocol.md)
- [Mention and Direct Pal protocol](../orchestration/mention-and-direct-pal-protocol.md)
- [Owner + Verifier workflow](../orchestration/owner-verifier-workflow-protocol.md)
- [Verifier Context Packet template](../templates/orchestration/verifier-context-packet.md)
- [Verification Result Record template](../templates/orchestration/verification-result-record.md)
- [Parallel Independent Review workflow](../orchestration/parallel-independent-review-protocol.md)
- [Reviewer Context Packet template](../templates/orchestration/reviewer-context-packet.md)
- [Reviewer Final Report template](../templates/orchestration/reviewer-final-report.md)
- [Parallel Review Synthesis Summary template](../templates/orchestration/parallel-review-synthesis-summary.md)
- [Plan -> Execute -> Verify workflow](../orchestration/plan-execute-verify-protocol.md)
- [Routing Memory writeback protocol](../orchestration/routing-memory-writeback-protocol.md)
- [PalBench Collaboration suite plan](research/palbench-collaboration-suite-plan.md)
- [PalBench Collaboration coverage audit](research/palbench-collaboration-coverage-audit.md)
- [PalBench Collaboration eval index](../evals/palbench-collaboration/task-index.md)

## Atlas Developer Quick Links

- [Atlas Pal Pack](../pals/Atlas-developer/README.md)
- [Atlas skills](../pals/Atlas-developer/skills/index.md)
- [Atlas knowledge](../pals/Atlas-developer/knowledge/index.md)
- [Atlas workflows](../pals/Atlas-developer/workflows/index.md)
- [Atlas runbooks](../pals/Atlas-developer/runbooks/index.md)
- [Atlas evals](../pals/Atlas-developer/evals/README.md)
- [Atlas research inventory](../pals/Atlas-developer/research/source-inventory.md)
- [Atlas Developer gap report](08-release-candidate/atlas-developer-gap-report.md)
- [Atlas self-health report](08-release-candidate/atlas-self-health-report.md)

## Vega Research Quick Links

- [Vega Pal Pack](../pals/Vega-research/README.md)
- [Vega skills](../pals/Vega-research/skills/index.md)
- [Vega knowledge](../pals/Vega-research/knowledge/index.md)
- [Vega workflows](../pals/Vega-research/workflows/index.md)
- [Vega runbooks](../pals/Vega-research/runbooks/index.md)
- [Vega evals](../pals/Vega-research/evals/README.md)
- [Vega source inventory](../pals/Vega-research/research/source-inventory.md)
- [Vega Research gap report](08-release-candidate/vega-research-gap-report.md)
- [Vega self-health report](08-release-candidate/vega-self-health-report.md)

## Rhea Safety Quick Links

- [Rhea Pal Pack](../pals/Rhea-system/README.md)
- [Rhea skills](../pals/Rhea-system/skills/index.md)
- [Rhea knowledge](../pals/Rhea-system/knowledge/index.md)
- [Rhea workflows](../pals/Rhea-system/workflows/index.md)
- [Rhea runbooks](../pals/Rhea-system/runbooks/index.md)
- [Rhea evals](../pals/Rhea-system/evals/README.md)
- [Rhea source inventory](../pals/Rhea-system/research/source-inventory.md)
- [Rhea System / Runtime gap report](08-release-candidate/rhea-system-runtime-gap-report.md)
- [Rhea self-health report](08-release-candidate/rhea-self-health-report.md)

## Quinn Quality Quick Links

- [Quinn Pal Pack](../pals/Quinn-quality/README.md)
- [Quinn skills](../pals/Quinn-quality/skills/index.md)
- [Quinn knowledge](../pals/Quinn-quality/knowledge/index.md)
- [Quinn workflows](../pals/Quinn-quality/workflows/index.md)
- [Quinn runbooks](../pals/Quinn-quality/runbooks/index.md)
- [Quinn evals](../pals/Quinn-quality/evals/README.md)
- [Quinn source inventory](../pals/Quinn-quality/research/source-inventory.md)
- [Quinn Quality / Verification gap report](08-release-candidate/quinn-quality-verification-gap-report.md)
- [Quinn self-health report](08-release-candidate/quinn-self-health-report.md)

## Morgan Document Workflow Quick Links

- [Morgan Pal Pack](../pals/Morgan-document/README.md)
- [Morgan skills](../pals/Morgan-document/skills/index.md)
- [Morgan knowledge](../pals/Morgan-document/knowledge/index.md)
- [Morgan workflows](../pals/Morgan-document/workflows/index.md)
- [Morgan runbooks](../pals/Morgan-document/runbooks/index.md)
- [Morgan evals](../pals/Morgan-document/evals/README.md)
- [Morgan source inventory](../pals/Morgan-document/research/source-inventory.md)
- [Morgan Document / File Workflow gap report](08-release-candidate/morgan-document-workflow-gap-report.md)
- [Morgan self-health report](08-release-candidate/morgan-self-health-report.md)

## Harper Writing / Content Craft Quick Links

- [Harper Pal Pack](../pals/Harper-writing/README.md)
- [Harper skills](../pals/Harper-writing/skills/index.md)
- [Harper knowledge](../pals/Harper-writing/knowledge/index.md)
- [Harper workflows](../pals/Harper-writing/workflows/index.md)
- [Harper runbooks](../pals/Harper-writing/runbooks/index.md)
- [Harper evals](../pals/Harper-writing/evals/README.md)
- [Harper source inventory](../pals/Harper-writing/research/source-inventory.md)
- [Harper Writing / Content Craft gap report](08-release-candidate/harper-writing-content-gap-report.md)
- [Harper self-health report](08-release-candidate/harper-self-health-report.md)

## Nova Product / Strategy Quick Links

- [Nova Pal Pack](../pals/Nova-product/README.md)
- [Nova skills](../pals/Nova-product/skills/index.md)
- [Nova knowledge](../pals/Nova-product/knowledge/index.md)
- [Nova workflows](../pals/Nova-product/workflows/index.md)
- [Nova runbooks](../pals/Nova-product/runbooks/index.md)
- [Nova evals](../pals/Nova-product/evals/README.md)
- [Nova source inventory](../pals/Nova-product/research/source-inventory.md)
- [Nova Product / Strategy gap report](08-release-candidate/nova-product-strategy-gap-report.md)
- [Nova self-health report](08-release-candidate/nova-self-health-report.md)
- [PalSmith Nova review](../pals/Nova-product/reports/palsmith-nova-product-strategy-review.md)

## Documentation Map

| Area | Use it for |
| --- | --- |
| [00-overview](00-overview/00-what-is-agentpal.md) | Product definition, current status, repository map, and runtime boundary |
| [01-concepts](01-concepts/01-what-is-a-pal.md) | Pal, Pal Pack, Skill, Agent, Why Pal, Pal Team, multi-Pal collaboration, and Simple Pal Mode concepts |
| [02-getting-started](02-getting-started/00-quick-start.md) | Opening AgentPal, initializing Mira, and calling a Pal |
| [03-pal-pack-standard](03-pal-pack-standard/README.md) | Pal Pack structure, root files, import/export, public/private boundary, and checklist |
| [04-runtime-guides](04-runtime-guides/00-runtime-compatibility.md) | Runtime compatibility, Codex, Claude Code, thin binding stability, troubleshooting, and future adapters |
| [05-orchestration-methodology](05-orchestration-methodology/README.md) | Fast Route, Task Package, Context Slicing, Asset Loading Budget, Pal Teams, evidence records, and future orchestration boundaries |
| [06-palsmith](06-palsmith/README.md) | PalSmith v0.2 end-to-end productization path |
| [06-collaboration](06-collaboration/00-collaboration-overview.md) | Contacts, mention protocol, Context Packets, handoff, and project workgroups |
| [06-validation-and-evidence](06-validation-and-evidence/README.md) | PalBench meaning, limits, observed benefits, and future validation design |
| [evals/palbench-light](../evals/palbench-light/README.md) | v0.2 PalBench Light release regression suite |
| [evals/v0.2-integration](../evals/v0.2-integration/v0.2-integration-test-matrix.md) | v0.2 first-phase integrated readiness matrix |
| [07-authoring-pals](07-authoring-pals/README.md) | Designing, writing, testing, publishing, and governing Pal Packs with PalSmith |
| [07-memory-and-learning](07-memory-and-learning/00-memory-overview.md) | User memory, project memory, skill memory, and repeated-task learning |
| [08-release-and-maintenance](08-release-and-maintenance/00-release-process.md) | Release process, public-safety checks, versioning, and maintenance |
| [08-release-candidate](08-release-candidate/README.md) | v0.1.0-rc.1 scope, manifest, public-safe audit summary, tag process, and known limitations |
| [09-roadmap](09-roadmap/README.md) | v0.2 and v0.3 development plans, task pools, and release-readiness planning |
| [research](research/README.md) | Archived research notes only; not a primary docs entry point |
| [99-reference](99-reference/glossary.md) | Glossary, file index, official Pals, FAQ, and known limitations |

## Current v0.2.0-rc.1 Boundary

- Simple Pal Mode is the only active task-handling path.
- Mira is the default Main Pal, Leader Pal, and Conductor.
- `/pal Name` is a plain-text AgentPal direct-call protocol for a registered Pal by display name or alias; it does not require a native Runtime command.
- `contacts/` and `registry/` are the source of truth for Pal discovery.
- AgentPal does not execute actions by itself; the host runtime performs file reads, writes, commands, tool calls, publishing, and deletion.
- Future child workflow or subagent design material is not active in v0.2.0-rc.1.
- Research and orchestration methodology docs are design foundations. They do not enable Deep Conductor, external Agent calls, or Subagent Mode in v0.2.0-rc.1.

## Public-Safe Rule

Do not publish private user memory, private project state, real task reports, internal development notes, sensitive credentials, local absolute paths, customer data, or unauthorized third-party full text.

See [public/private boundary](03-pal-pack-standard/11-public-private-boundary.md) and [public-safe checklist](08-release-and-maintenance/02-public-safe-checklist.md).
