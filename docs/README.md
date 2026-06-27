# AgentPal Documentation

This documentation set is the public entry point for AgentPal v0.3.0-rc.1.

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
- [Bind an external project](01-getting-started/bind-external-project.md)
- [Central project record](02-concepts/central-project-record.md)
- [Project memory in AgentPal](02-concepts/project-memory-in-agentpal.md)
- [Source map and derived knowledge](02-concepts/source-map-and-derived-knowledge.md)
- [Project memory user guide](03-user-guides/project-memory.md)
- [Using user project docs](03-user-guides/using-user-project-docs.md)
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
- [v0.3 release preparation audit](09-roadmap/v0.3-release-preparation-audit.md)
- [v0.3 Deep Conductor integration matrix](../evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md)
- [PalBench Collaboration coverage audit](research/palbench-collaboration-coverage-audit.md)
- [No-code future boundary](09-roadmap/no-code-future-boundary.md)
- [Deep Conductor master goal](05-orchestration-methodology/deep-conductor-master-goal.md)
- [Deep Conductor master loop usage guide](05-orchestration-methodology/deep-conductor-master-loop-usage-guide.md)
- [Deep Conductor E2E usage guide](05-orchestration-methodology/deep-conductor-e2e-usage-guide.md)
- [Deep Conductor real Runtime replay report](research/deep-conductor-real-runtime-replay-report.md)
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
- [Historical release-candidate pointer](08-release-candidate/README.md)
- [v0.2 development plan](09-roadmap/v0.2-development-plan.md)
- [v0.2 task pool](09-roadmap/v0.2-task-pool.md)

## PalSmith Quick Links

- [PalSmith overview](PalSmith.md)
- [Use PalSmith](07-authoring-pals/12-use-palsmith.md)
- [PalSmith end-to-end workflows](07-authoring-pals/13-palsmith-end-to-end-workflows.md)
- [PalSmith Pal lifecycle](07-authoring-pals/14-palsmith-pal-lifecycle.md)
- [PalSmith quickstart AI team](07-authoring-pals/15-palsmith-quickstart-ai-team.md)
- [PalSmith demo script](07-authoring-pals/16-palsmith-demo-script.md)
- [PalSmith v0.4 regression test plan](../archive/migration-from-v0.3/release-candidate-docs/12-palsmith-v0.4-regression-test-plan.md)
- [PalSmith v0.2 productization](06-palsmith/README.md)
- [PalSmith end-to-end productization](06-palsmith/palsmith-end-to-end-productization.md)
- [Create first professional Pal task package](../official/pals/PalSmith-pal-governor/templates/task-packages/create-first-professional-pal.md)
- [Create AI team from goal task package](../official/pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md)
- [Pal import/export standard](03-pal-pack-standard/13-pal-import-export.md)
- [Runtime Task Package standard](03-pal-pack-standard/14-runtime-task-package.md)
- [No-code release checklist](../archive/migration-from-v0.3/release-candidate-docs/05-no-code-release-checklist.md)
- [PalSmith release-scope review](../archive/migration-from-v0.3/release-candidate-docs/06-palsmith-release-scope-review.md)
- [PalSmith E2E test summary](../archive/migration-from-v0.3/release-candidate-docs/11-palsmith-e2e-test-summary.md)
- [PalSmith Pal Pack](../official/pals/PalSmith-pal-governor/README.md)

## Mira Leader Quick Links

- [Mira Pal Pack](../official/pals/Mira-main/README.md)
- [Mira-first usage](02-getting-started/mira-first-usage.md)
- [Mira-first prompt cards](02-getting-started/mira-first-prompt-cards.md)
- [Mira first task intake template](../official/pals/Mira-main/templates/task-packages/mira-first-task-intake.md)
- [Mira composite deliverable template](../official/pals/Mira-main/templates/task-packages/mira-composite-deliverable-task-package.md)
- [Mira runtime brief template](../official/pals/Mira-main/templates/task-packages/mira-runtime-brief.md)
- [Mira leader skills](../official/pals/Mira-main/skills/index.md)
- [Mira leader knowledge](../official/pals/Mira-main/knowledge/INDEX.md)
- [Mira workflows](../official/pals/Mira-main/workflows/index.md)
- [Mira runbooks](../official/pals/Mira-main/runbooks/INDEX.md)
- [Mira evals](../official/pals/Mira-main/evals/README.md)
- [Mira self-health report archive](../archive/migration-from-v0.3/official-pal-history/official/pals/Mira-main/reports/mira-self-health-report.md)
- [PalSmith Mira Leader review archive](../archive/migration-from-v0.3/official-pal-history/official/pals/Mira-main/reports/palsmith-mira-leader-review.md)

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
- [v0.3 release preparation audit](09-roadmap/v0.3-release-preparation-audit.md)
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

- [Atlas Pal Pack](../official/pals/Atlas-developer/README.md)
- [Atlas skills](../official/pals/Atlas-developer/skills/index.md)
- [Atlas knowledge](../official/pals/Atlas-developer/knowledge/index.md)
- [Atlas workflows](../official/pals/Atlas-developer/workflows/index.md)
- [Atlas runbooks](../official/pals/Atlas-developer/runbooks/index.md)
- [Atlas evals](../official/pals/Atlas-developer/evals/README.md)
- [Atlas research inventory](../official/pals/Atlas-developer/research/source-inventory.md)
- [Atlas Developer gap report](../archive/migration-from-v0.3/release-candidate-docs/atlas-developer-gap-report.md)
- [Atlas self-health report](../archive/migration-from-v0.3/release-candidate-docs/atlas-self-health-report.md)

## Vega Research Quick Links

- [Vega Pal Pack](../official/pals/Vega-research/README.md)
- [Vega skills](../official/pals/Vega-research/skills/index.md)
- [Vega knowledge](../official/pals/Vega-research/knowledge/index.md)
- [Vega workflows](../official/pals/Vega-research/workflows/index.md)
- [Vega runbooks](../official/pals/Vega-research/runbooks/index.md)
- [Vega evals](../official/pals/Vega-research/evals/README.md)
- [Vega source inventory](../official/pals/Vega-research/research/source-inventory.md)
- [Vega Research gap report](../archive/migration-from-v0.3/release-candidate-docs/vega-research-gap-report.md)
- [Vega self-health report](../archive/migration-from-v0.3/release-candidate-docs/vega-self-health-report.md)

## Rhea Safety Quick Links

- [Rhea Pal Pack](../official/pals/Rhea-system/README.md)
- [Rhea skills](../official/pals/Rhea-system/skills/index.md)
- [Rhea knowledge](../official/pals/Rhea-system/knowledge/index.md)
- [Rhea workflows](../official/pals/Rhea-system/workflows/index.md)
- [Rhea runbooks](../official/pals/Rhea-system/runbooks/index.md)
- [Rhea evals](../official/pals/Rhea-system/evals/README.md)
- [Rhea source inventory](../official/pals/Rhea-system/research/source-inventory.md)
- [Rhea System / Runtime gap report](../archive/migration-from-v0.3/release-candidate-docs/rhea-system-runtime-gap-report.md)
- [Rhea self-health report](../archive/migration-from-v0.3/release-candidate-docs/rhea-self-health-report.md)

## Quinn Quality Quick Links

- [Quinn Pal Pack](../official/pals/Quinn-quality/README.md)
- [Quinn skills](../official/pals/Quinn-quality/skills/index.md)
- [Quinn knowledge](../official/pals/Quinn-quality/knowledge/index.md)
- [Quinn workflows](../official/pals/Quinn-quality/workflows/index.md)
- [Quinn runbooks](../official/pals/Quinn-quality/runbooks/index.md)
- [Quinn evals](../official/pals/Quinn-quality/evals/README.md)
- [Quinn source inventory](../official/pals/Quinn-quality/research/source-inventory.md)
- [Quinn Quality / Verification gap report](../archive/migration-from-v0.3/release-candidate-docs/quinn-quality-verification-gap-report.md)
- [Quinn self-health report](../archive/migration-from-v0.3/release-candidate-docs/quinn-self-health-report.md)

## Morgan Document Workflow Quick Links

- [Morgan Pal Pack](../official/pals/Morgan-document/README.md)
- [Morgan skills](../official/pals/Morgan-document/skills/index.md)
- [Morgan knowledge](../official/pals/Morgan-document/knowledge/index.md)
- [Morgan workflows](../official/pals/Morgan-document/workflows/index.md)
- [Morgan runbooks](../official/pals/Morgan-document/runbooks/index.md)
- [Morgan evals](../official/pals/Morgan-document/evals/README.md)
- [Morgan source inventory](../official/pals/Morgan-document/research/source-inventory.md)
- [Morgan Document / File Workflow gap report](../archive/migration-from-v0.3/release-candidate-docs/morgan-document-workflow-gap-report.md)
- [Morgan self-health report](../archive/migration-from-v0.3/release-candidate-docs/morgan-self-health-report.md)

## Harper Writing / Content Craft Quick Links

- [Harper Pal Pack](../official/pals/Harper-writing/README.md)
- [Harper skills](../official/pals/Harper-writing/skills/index.md)
- [Harper knowledge](../official/pals/Harper-writing/knowledge/index.md)
- [Harper workflows](../official/pals/Harper-writing/workflows/index.md)
- [Harper runbooks](../official/pals/Harper-writing/runbooks/index.md)
- [Harper evals](../official/pals/Harper-writing/evals/README.md)
- [Harper source inventory](../official/pals/Harper-writing/research/source-inventory.md)
- [Harper Writing / Content Craft gap report](../archive/migration-from-v0.3/release-candidate-docs/harper-writing-content-gap-report.md)
- [Harper self-health report](../archive/migration-from-v0.3/release-candidate-docs/harper-self-health-report.md)

## Nova Product / Strategy Quick Links

- [Nova Pal Pack](../official/pals/Nova-product/README.md)
- [Nova skills](../official/pals/Nova-product/skills/index.md)
- [Nova knowledge](../official/pals/Nova-product/knowledge/index.md)
- [Nova workflows](../official/pals/Nova-product/workflows/index.md)
- [Nova runbooks](../official/pals/Nova-product/runbooks/index.md)
- [Nova evals](../official/pals/Nova-product/evals/README.md)
- [Nova source inventory](../official/pals/Nova-product/research/source-inventory.md)
- [Nova Product / Strategy gap report](../archive/migration-from-v0.3/release-candidate-docs/nova-product-strategy-gap-report.md)
- [Nova self-health report](../archive/migration-from-v0.3/release-candidate-docs/nova-self-health-report.md)
- [PalSmith Nova review archive](../archive/migration-from-v0.3/official-pal-history/official/pals/Nova-product/reports/palsmith-nova-product-strategy-review.md)

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
| [08-release-candidate](08-release-candidate/README.md) | historical pointer to archived release-candidate documents |
| [09-roadmap](09-roadmap/README.md) | v0.2 and v0.3 development plans, task pools, and release-readiness planning |
| [research](research/README.md) | Archived research notes only; not a primary docs entry point |
| [99-reference](99-reference/glossary.md) | Glossary, file index, official Pals, FAQ, and known limitations |

## Current v0.3.0-rc.1 Boundary

- Simple Pal Mode is the only active task-handling path.
- Mira is the default Main Pal, Leader Pal, and Conductor.
- `/pal Name` is a plain-text AgentPal direct-call protocol for a registered Pal by display name or alias; it does not require a native Runtime command.
- `workspace/organization/contacts/` is the source of truth for Pal discovery; legacy `contacts/` and `registry/` remain compatibility references.
- AgentPal does not execute actions by itself; the host runtime performs file reads, writes, commands, tool calls, publishing, and deletion.
- Deep Conductor is available as no-code protocols, templates, task packages, examples, evals, and replay reports; it is not automatic execution.
- Subagent / external Agent execution remains unavailable, unknown, blocked, or host-dependent unless the host Runtime proves support and permission.

## Public-Safe Rule

Do not publish private user memory, private project state, real task reports, internal development notes, sensitive credentials, local absolute paths, customer data, or unauthorized third-party full text.

See [public/private boundary](03-pal-pack-standard/11-public-private-boundary.md) and [public-safe checklist](08-release-and-maintenance/02-public-safe-checklist.md).
