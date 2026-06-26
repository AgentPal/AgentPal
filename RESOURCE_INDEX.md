# AgentPal Resource Index

This index helps a runtime or maintainer find the right public AgentPal file without loading the whole workspace. It is navigation only, not a default context bundle.

Reading this file does not authorize loading every referenced file.

## Default Initialization Files

Use the short initialization path by default:

- `AGENTS.md`
- `prompts/codex/initialize-agentpal-workspace.md`
- `core/agentpal-core-gate.md`
- `core/first-pal-gate.md`
- `core/simple-pal-mode-runtime-contract.md`
- `core/deliverable-aware-task-judgement-gate.md`
- `core/main-pal-conductor-gate.md`
- `core/runtime-adapter-shared-contract.md`
- `contacts/pals.json`
- `registry/pal.index.json`
- `pals/Mira-main/PAL.md`
- `pals/Mira-main/core/output-contract.md`

If an external project is already bound to AgentPal, project-side `.agentpal/` binding files may be read first when they exist. They are binding context, not permission to treat the AgentPal Workspace as the user project.

## Index Exposure Is Not Content Reading

Directory listings, registry entries, and index files expose paths for navigation. Report those as `index_known_*`, not `content_read_*`.

Use:

- `index_known_count` for paths known through listings, indexes, or registries
- `content_read_count` for files actually opened and read
- `index_only_not_content_read` for known paths that were not opened

## Root Files

| Path | Purpose | When To Read |
| --- | --- | --- |
| `README.md` | English public introduction | onboarding, release checks, user questions |
| `README.zh-CN.md` | Chinese public introduction | Chinese onboarding or localization checks |
| `AGENTS.md` | project-level runtime instructions | initialization and context switches |
| `PAL.md` | AgentPal Workspace identity | workspace identity questions and initialization |
| `SKILL.md` | Workspace-level Skill entry | Skill-aware runtime entry |
| `prompts/codex/initialize-agentpal-workspace.md` | copyable initialization prompt | first run or re-initialization |
| `agentpal.json` | machine-readable workspace metadata | initialization, validation, release checks |
| `CHANGELOG.md` | public version history | release review |
| `RELEASE_NOTES.md` | user-facing release notes | release review or user onboarding |
| `GITHUB_RELEASE_DRAFT.md` | manual GitHub Release draft | release publishing |
| `RELEASE_CHECKLIST.md` | maintainer release checklist | release validation |
| `CONTRIBUTING.md` | contribution rules | contributor onboarding |
| `THIRD_PARTY_NOTICES.md` | license and third-party notice policy | release validation |
| `LICENSE` | MIT License | release validation |
| `.gitignore` | public-safe ignore rules | release validation |

## Core Gates

| Path | Purpose |
| --- | --- |
| `core/agentpal-core-gate.md` | shared first-read gate for Runtime adapters |
| `core/first-pal-gate.md` | First Pal task and composite deliverable gate |
| `core/simple-pal-mode-runtime-contract.md` | Simple Pal Mode and future-boundary contract |
| `core/deliverable-aware-task-judgement-gate.md` | shared deliverable-aware Task Judgement gate |
| `core/main-pal-conductor-gate.md` | Mira Main Pal / Conductor boundary |
| `core/runtime-adapter-shared-contract.md` | thin adapter contract for Codex, Claude Code, and generic CLI |
| `core/project-binding-thin-contract.md` | minimal external project binding contract |
| `core/runtime-response-gate.md` | core pointer to detailed response gate |

## Main Directories

| Directory | Purpose | Default Loading |
| --- | --- | --- |
| `pals/` | official and user-added Pal Pack pool | selected Pal only |
| `contacts/` | Pal contact source of truth | routing and discovery |
| `registry/` | Pal and resource indexes | routing and selected navigation |
| `core/` | shared AgentPal core gates | runtime adapter and project binding bootstrap |
| `orchestration/` | current protocols and future-design notes | selected current protocols only |
| `templates/` | reusable Context Packet, output, binding, and task templates | selected template only |
| `prompts/` | copyable maintenance and setup prompts | when running that prompt flow |
| `projects/` | external project workgroup binding templates | project binding only |
| `runtime/` | runtime-awareness notes | diagnostics or runtime documentation |
| `models/` | model-routing notes | model-routing documentation |
| `plugins/` | plugin-discovery notes | plugin documentation |
| `capabilities/` | capability-profile notes | diagnostics or capability documentation |
| `response-fingerprints/` | Pal response fingerprint references | selected Pal validation |
| `docs/` | user documentation and reference material | docs work or user questions |
| `docs/01-concepts/07-why-pal.md` | why AgentPal uses the Pal concept between Skills and Agent teams | concept questions and onboarding |
| `docs/05-orchestration-methodology/` | current AgentPal Pal orchestration methodology | methodology questions and docs navigation |
| `docs/09-roadmap/` | v0.2 roadmap and task pool | v0.2 planning and development sequencing |
| `docs/06-palsmith/README.md` | PalSmith v0.2 productization index | PalSmith creation and AI team productization work |
| `docs/06-palsmith/palsmith-end-to-end-productization.md` | PalSmith v0.2 end-to-end user path | PalSmith creation and AI team productization work |
| `pals/PalSmith-pal-governor/templates/task-packages/create-first-professional-pal.md` | Copyable first professional Pal creation task package | PalSmith v0.2 single-Pal creation work |
| `pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md` | Copyable AI team creation task package | PalSmith v0.2 AI team creation work |
| `pals/PalSmith-pal-governor/runbooks/pal-health-check.md` | Pal health check runbook | PalSmith v0.2 creation and repair checks |
| `pals/PalSmith-pal-governor/runbooks/ai-team-health-check.md` | AI team health check runbook | PalSmith v0.2 team readiness checks |
| `docs/02-getting-started/mira-first-usage.md` | Mira-first user path | onboarding and daily-use examples |
| `docs/02-getting-started/mira-first-prompt-cards.md` | Copyable Mira-first prompts | daily user prompts and direct `/pal Name` guidance |
| `pals/Mira-main/templates/task-packages/mira-first-task-intake.md` | Mira ordinary task intake template | Mira-first task organization |
| `pals/Mira-main/templates/task-packages/mira-composite-deliverable-task-package.md` | Mira composite deliverable template | staged Task Package creation |
| `pals/Mira-main/templates/task-packages/mira-owner-judgement-summary.md` | Mira owner judgement summary template | explaining Pal candidates and override paths |
| `pals/Mira-main/templates/task-packages/mira-runtime-brief.md` | Mira runtime brief template | Codex / Claude Code / generic CLI execution handoff |
| `pals/Mira-main/examples/mira-runtime-brief-example.md` | Mira runtime brief example | execution-layer evidence and project boundary example |
| `pals/Mira-main/evals/mira-first-usage-self-test.md` | Mira-first self-test | ordinary, composite, direct Pal, and release-check regression |
| `docs/07-official-pals/official-pal-examples-index.md` | Official 9 Pal real task examples index | official Pal examples and v0.2 R42 navigation |
| `docs/07-official-pals/official-pal-example-library-plan.md` | Official Pal example library plan | official Pal examples planning and R42 first implementation status |
| `evals/official-pals/official-pal-example-library-self-test.md` | Official Pal example library self-test | R42 example structure and boundary checks |
| `docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md` | Capability Inventory minimal usable design | v0.2 R43 manual profile design |
| `capabilities/README.md` | Capability Inventory profile index | runtime/model/reasoning/skill/plugin/MCP/Pal profile navigation |
| `capabilities/runtime-profiles/` | Runtime profile examples | runtime capability judgement inputs |
| `capabilities/model-profiles/` | Model profile examples | model tendency judgement inputs |
| `capabilities/reasoning-profiles/` | Reasoning strength profile examples | prompt-shaping judgement inputs |
| `capabilities/skill-profiles/` | Skill profile examples | Skill capability judgement inputs |
| `capabilities/plugin-profiles/` | Plugin profile notes | plugin capability judgement inputs |
| `capabilities/mcp-profiles/` | MCP profile notes | MCP capability judgement inputs |
| `capabilities/pal-profiles/` | Pal capability profile examples | Pal capability judgement inputs |
| `evals/capability-inventory/` | Capability Inventory self-tests | R43 profile structure, loading budget, and no fixed route checks |
| `examples/orchestration/capability-inventory-task-judgement-example.md` | Capability Inventory successful use example | profile-as-judgement-input example |
| `examples/failures/capability-profile-used-as-fixed-route.md` | Capability Inventory failure example | profile-as-route regression example |
| `docs/research/palbench-light-suite-plan.md` | PalBench Light suite plan | v0.2 R44 release regression suite design |
| `evals/palbench-light/README.md` | PalBench Light eval entry | v0.2 release regression suite navigation |
| `evals/palbench-light/task-index.md` | PalBench Light task index | R44 first 24 case index |
| `evals/palbench-light/scoring-rubric.md` | PalBench Light scoring rubric | 0 / 1 / 2 release regression scoring |
| `evals/palbench-light/palbench-light-suite-self-test.md` | PalBench Light suite self-test | R44 suite structure and boundary check |
| `docs/04-runtime-guides/runtime-adapter-stability-guide.md` | Runtime Adapter stability guide | R45 thin binding stability and cross-project troubleshooting |
| `docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md` | Runtime Adapter troubleshooting cards | R45 copyable bounded troubleshooting prompts |
| `docs/04-runtime-guides/upgrade-existing-binding-to-thin-binding.md` | existing binding upgrade runbook | R45 upgrade path for old copied bindings |
| `evals/runtime-adapters/runtime-adapter-regression-suite.md` | Runtime Adapter regression suite | R45 12-scenario adapter regression checklist |
| `docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md` | Pal Team, runtime-layer agent execution, and future Deep Conductor boundaries | Pal Team and orchestration questions |
| `docs/06-validation-and-evidence/` | current PalBench and evidence interpretation | validation, PalBench, and evidence questions |
| `docs/08-release-candidate/` | current v0.1.0-rc.1 release candidate notes | release candidate scope and evidence questions |
| `docs/research/` | archived research notes | historical traceability only; not a primary entry point |
| `examples/` | public-safe examples and failure examples | examples, evals, or regression checks |
| `evals/` | self-tests and release checks | eval or release validation only |
| `memory/` | public-safe memory placeholders | not ordinary task context |
| `state/` | public-safe state placeholders | not ordinary task context |
| `reports/` | public-safe report placeholders | not ordinary task context |
| `imports/` | import staging placeholders | not ordinary task context |

For user-facing documentation, start with `docs/README.md`. For root-level release asset navigation, use this file.

## Project Install Prompts

| Path | Purpose |
| --- | --- |
| `prompts/codex/initialize-agentpal-workspace.md` | Codex AgentPal Workspace initialization prompt |
| `prompts/codex/remove-agentpal-current-project.md` | remove AgentPal binding from the current external Codex project |
| `prompts/codex/remove-agentpal-workspace-from-codex.md` | stop using AgentPal Workspace in Codex without deleting files |
| `prompts/claude-code/install-agentpal-current-project.md` | one-prompt Claude Code project install from inside `<your-project>` |
| `prompts/claude-code/remove-agentpal-current-project.md` | remove AgentPal binding from a Claude Code project |
| `prompts/claude-code/verify-agentpal-current-project.md` | verify Claude Code project binding and `settings.local.json` |
| `prompts/generic-cli-agent/install-agentpal-current-project.md` | one-prompt generic CLI Agent project install |
| `prompts/generic-cli-agent/remove-agentpal-current-project.md` | remove generic CLI Agent project binding |

These prompts are Markdown instructions, not scripts or installers.

## Official Pal Packs

Official Pal Packs for v0.1.0-rc.1:

- `pals/Mira-main`
- `pals/Atlas-developer`
- `pals/Vega-research`
- `pals/Rhea-system`
- `pals/PalSmith-pal-governor`
- `pals/Quinn-quality`
- `pals/Morgan-document`
- `pals/Harper-writing`
- `pals/Nova-product`

Do not load all Pal directories by default. Load Mira for ordinary entry and the selected owner Pal for owned tasks.

## Current Protocols To Prefer

- `orchestration/runtime-response-gate.md`
- `orchestration/fast-route-protocol.md`
- `orchestration/ai-routing-judgement-protocol.md`
- `orchestration/pal-context-slicing-protocol.md`
- `orchestration/agent-instruction-file-loading-policy.md`
- `orchestration/pal-asset-loading-budget.md`
- `orchestration/context-packet-minimalism-protocol.md`
- `orchestration/memory-summary-loading-protocol.md`
- `orchestration/task-package-output-contract.md`
- `orchestration/pal-owned-skill-storage-protocol.md`
- `orchestration/specialist-pal-asset-loading-protocol.md`

## Methodology, Validation, Release Candidate, And Archive

Use the current docs directories as the public entry points. Archived research notes are kept only for traceability. None of these files activate Deep Conductor, Subagent Mode, or external Agent calls.

| Path | Purpose |
| --- | --- |
| `docs/05-orchestration-methodology/README.md` | current Pal Orchestration Methodology entry |
| `docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md` | v0.2 minimal manual Capability Inventory profile design |
| `docs/05-orchestration-methodology/00-methodology-overview.md` | current methodology overview |
| `docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md` | Pal Team and future Deep Conductor relationship |
| `docs/06-validation-and-evidence/README.md` | current validation and PalBench entry |
| `docs/06-validation-and-evidence/01-palbench-small-sample-report.md` | current R33 PalBench small-sample report |
| `docs/06-validation-and-evidence/05-future-palbench-design.md` | current future PalBench design notes |
| `docs/08-release-candidate/README.md` | current release candidate entry |
| `docs/08-release-candidate/02-release-manifest.md` | current release candidate manifest |
| `docs/research/README.md` | archive status note; not a primary docs entry |
| `docs/research/archive/` | historical research notes retained for traceability |
| `orchestration/fast-route-protocol.md` | current Simple Pal Mode clear-task handoff pattern |
| `orchestration/deep-conductor-protocol.md` | future complex-workflow orchestration design |
| `orchestration/capability-inventory-protocol.md` | runtime/model/skill/plugin/MCP/Pal profile design |
| `orchestration/task-judgement-protocol.md` | structured task judgement design |
| `orchestration/workflow-topology-protocol.md` | workflow topology design and v0.1/future boundary |
| `orchestration/context-access-list-protocol.md` | context access list design |
| `orchestration/pal-isolation-and-shared-memory-protocol.md` | isolation and shared memory design |
| `orchestration/routing-reward-memory-protocol.md` | routing outcome memory design |
| `capabilities/` | capability profile notes and illustrative examples |
| `templates/orchestration/` | task judgement, workflow, access list, routing, and verification templates |
| `templates/capabilities/` | profile templates |
| `templates/research/` | PalBench result template |
| `evals/palbench/` | PalBench evaluation drafts |
| `evals/palbench-light/` | v0.2 PalBench Light regression suite |
| `evals/palbench-light/task-index.md` | R44 PalBench Light first implementation index |
| `evals/palbench-light/scoring-rubric.md` | R44 PalBench Light shared scoring protocol |
| `evals/orchestration/` | orchestration boundary and protocol self-tests |
| `examples/orchestration/` | orchestration examples |

## Deliverable-Aware Task Judgement References

| Path | Purpose |
| --- | --- |
| `examples/orchestration/deliverable-aware-task-judgement-example.md` | staged Task Package example for composite deliverables |
| `examples/failures/domain-only-owner-handoff.md` | regression example for domain-only owner handoff |
| `evals/orchestration/deliverable-aware-task-judgement-self-test.md` | self-test for Mira, direct Atlas, and direct Vega composite task handling |

## Runtime Adapter Thin Binding References

| Path | Purpose |
| --- | --- |
| `examples/runtime-adapters/thin-binding-project-example.md` | expected thin project binding shape |
| `examples/runtime-adapters/core-gate-shared-by-codex-claude-generic.md` | shared core gate example across adapters |
| `examples/failures/stale-project-copied-pal-list.md` | failure example for copied Pal rosters |
| `examples/failures/runtime-adapter-rule-drift.md` | failure example for adapter rule drift |
| `evals/runtime-adapters/thin-binding-core-gate-self-test.md` | thin binding self-test |
| `evals/runtime-adapters/core-gate-update-propagation-self-test.md` | core gate propagation self-test |
| `evals/runtime-adapters/no-stale-pal-list-in-project-binding-self-test.md` | stale Pal list self-test |
| `evals/runtime-adapters/claude-code-thin-binding-self-test.md` | Claude Code thin binding self-test |
| `evals/runtime-adapters/generic-cli-thin-binding-self-test.md` | Generic CLI thin binding self-test |
| `docs/04-runtime-guides/runtime-adapter-stability-guide.md` | thin binding stability guide |
| `docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md` | troubleshooting prompt cards |
| `docs/04-runtime-guides/upgrade-existing-binding-to-thin-binding.md` | upgrade old bindings to thin binding |
| `evals/runtime-adapters/runtime-adapter-regression-suite.md` | 12-scenario Runtime Adapter regression suite |
| `examples/failures/runtime-opened-in-wrong-directory.md` | failure example for wrong working directory |
| `examples/failures/stale-pal-list-after-agentpal-update.md` | failure example for stale Pal list |
| `examples/failures/claude-settings-local-not-refreshed.md` | failure example for Claude Code session refresh |
| `examples/failures/active-project-root-confused-with-agentpal-root.md` | failure example for root confusion |

## Mira Conductor References

| Path | Purpose |
| --- | --- |
| `pals/Mira-main/PAL.md` | Mira Main Pal / Leader Pal / Conductor identity |
| `pals/Mira-main/AGENTS.md` | Mira runtime instructions |
| `pals/Mira-main/SKILL.md` | Mira Pal Pack skill entry |
| `pals/Mira-main/core/output-contract.md` | Mira output shapes, Fast Route, CAL, Task Package, and future-design boundaries |

## R32 PalBench And Orchestration Additions

| Path | Purpose |
| --- | --- |
| `evals/palbench/fast-route-vs-direct-agent.md` | Fast Route comparison eval |
| `evals/palbench/deep-conductor-design-simulation.md` | future Deep Conductor design simulation eval |
| `evals/palbench/context-access-list-vs-full-context.md` | CAL versus full-context eval |
| `evals/palbench/pal-isolation-vs-group-chat.md` | isolation versus group-chat eval |
| `evals/palbench/single-entry-mira-vs-manual-selection.md` | Mira single-entry eval |
| `examples/orchestration/fast-route-vs-deep-conductor.md` | current/future scheduling example |
| `examples/orchestration/mira-as-conductor-example.md` | Mira conductor example |
| `examples/orchestration/intra-workflow-pal-isolation-example.md` | isolation example |
| `examples/orchestration/shared-memory-across-workflows-example.md` | cleaned shared memory example |
| `examples/orchestration/single-entry-mira-example.md` | Mira single-entry example |
| `examples/orchestration/palbench-small-sample-dev-prompt.md` | R33 dev prompt smoke sample |
| `examples/orchestration/palbench-small-sample-false-completion.md` | R33 false completion smoke sample |
| `examples/orchestration/palbench-small-sample-context-access-list.md` | R33 context access smoke sample |

## Runtime Guides

- `docs/10-using-agentpal-with-claude-code.md`
- `docs/11-using-agentpal-with-cli-agents.md`
- `docs/04-runtime-guides/runtime-adapter-stability-guide.md`
- `docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md`
- `docs/04-runtime-guides/upgrade-existing-binding-to-thin-binding.md`

## Do Not Load By Default

- all Pal Packs
- all project files
- all Pal knowledge directories
- all memory
- all state
- all reports
- all imports
- all examples
- all evals
- future design docs
- subagent templates

## Navigation Method

1. Start from the user goal.
2. Resolve whether the active context is the AgentPal Workspace or an external user project.
3. Resolve Mira or the selected owner Pal through contacts and registry.
4. Read the smallest relevant index.
5. Select one to three relevant files.
6. If more context is needed, explain why before expanding.
