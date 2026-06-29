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
- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `workspace/projects/README.md`
- `workspace/projects/projects.index.json`
- `official/pals/Mira-main/PAL.md`
- `official/pals/Mira-main/core/output-contract.md`

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
| `START_HERE.md` | first fresh-clone onboarding entry | new users and v0.5 first-use walkthrough |
| `AGENTS.md` | project-level runtime instructions | initialization and context switches |
| `INIT_PROMPT.md` | short AgentPal Workspace initialization prompt | direct workspace initialization by Markdown/JSON-capable runtimes |
| `PAL.md` | AgentPal Workspace identity | workspace identity questions and initialization |
| `SKILL.md` | Workspace-level Skill entry | Skill-aware runtime entry |
| `prompts/codex/initialize-agentpal-workspace.md` | copyable initialization prompt | first run or re-initialization |
| `agentpal.json` | machine-readable workspace metadata | initialization, validation, release checks |
| `docs/00-overview/repository-structure.md` | visual repository structure and thin-binding map | repository orientation, local structure checks |
| `docs/00-overview/what-is-agentpal.md` | concise new-user AgentPal explanation | first-time orientation |
| `docs/01-getting-started/first-30-minutes.md` | first 30 minutes walkthrough guide | fresh-clone onboarding |
| `examples/walkthroughs/first-agentpal-team/` | public-safe first AI team walkthrough | new-user walkthrough |
| `docs/01-getting-started/faq.md` | new-user FAQ | onboarding questions |
| `docs/00-overview/glossary.md` | new-user glossary | terms and concepts |
| `release/current/v0.5-fresh-clone-usability-checklist.md` | v0.5 fresh-clone usability checklist | onboarding validation |
| `release/current/v0.4-local-completion-report.md` | v0.4 local completion report | local completion review; not remote release proof |
| `release/current/v0.4-local-completion-evidence-index.md` | v0.4 local completion evidence index | evidence lookup for local completion |
| `docs/08-release-and-maintenance/v0.4-local-completion-summary.md` | user-facing v0.4 local completion summary | contributor and user orientation |
| `docs/09-roadmap/v0.5-local-development-scope.md` | v0.5 local development scope freeze | v0.5 planning and boundary checks |
| `standards/org-pack/org-pack-standard.md` | Org Pack standard | reusable no-code organization package work |
| `templates/org-pack/base-org-pack/` | base Org Pack template | creating public-safe reusable organization packages |
| `examples/org-packs/base-agentpal-org-pack/` | public-safe base Org Pack example | examples and Org Pack boundary checks |
| `docs/00-overview/pal-asset-and-org-pack-relationship.md` | Pal Asset and Org Pack relationship guide | v0.5 Pal Asset / Org Pack integration |
| `standards/pal-asset/` | Pal Asset standards | Pal Asset, Pal Skill, loading order, and resolver standard work |
| `docs/00-overview/pal-metadata-v0.5-upgrade-path.md` | Pal Metadata v0.5 upgrade path | pal.json v0.5, asset-manifest, official Pal preflight, and R101 navigation |
| `standards/palsmith/` | PalSmith v0.5 standards | no-code Pal creation, classification, and upgrade standards |
| `docs/03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md` | PalSmith v0.5 user guide | Pal creation and upgrade orientation |
| `docs/03-user-guides/official-pal-asset-upgrade-plan.md` | official Pal asset upgrade plan guide | official Pal upgrade planning |
| `CHANGELOG.md` | public version history | release review |
| `RELEASE_NOTES.md` | user-facing release notes | release review or user onboarding |
| `GITHUB_RELEASE_DRAFT.md` | manual GitHub Release draft | release publishing |
| `RELEASE_CHECKLIST.md` | maintainer release checklist | release validation |
| `CONTRIBUTING.md` | contribution rules | contributor onboarding |
| `THIRD_PARTY_NOTICES.md` | license and third-party notice policy | release validation |
| `LICENSE` | MIT License | release validation |
| `.gitignore` | public-safe ignore rules | release validation |

## Foundation Directories

| Directory | Purpose | When To Read |
| --- | --- | --- |
| `standards/` | public governance standards for boundaries, project binding, central assets, and routing | repository governance, release checks, binding questions |
| `official/` | official AgentPal assets, including bundled Pal Packs | selected official Pal or team asset work |
| `workspace/` | central organization workspace, contacts, project records, resources, and state placeholders | central roster, central project records, project governance, workspace-private records |
| `templates/` | reusable project-binding, Pal Pack, organization, governance, org-pack, and prompt templates | selected template work or external project binding |
| `docs/` | user and contributor documentation | user-facing docs and public orientation |
| `archive/migration-from-v0.3/` | migration maps and compatibility notes | path migration and cleanup work |

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
| `official/pals/` | official bundled Pal Pack pool | selected Pal only |
| `workspace/organization/contacts/` | central Pal contact source of truth | routing and discovery |
| `workspace/projects/` | central project records and `_template/` | external project binding, project memory, source-map, derived-knowledge, governance |
| `templates/project-binding/` | thin external project binding templates | install/update/remove AgentPal workgroups in external projects |
| `docs/00-overview/repository-structure.md` | visible v0.4/v0.5 directory structure guide | explaining root directories and compatibility pointers |
| `core/` | shared AgentPal core gates | runtime adapter and project binding bootstrap |
| `orchestration/` | current protocols and future-design notes | selected current protocols only |
| `templates/` | reusable Context Packet, output, binding, and task templates | selected template only |
| `prompts/` | copyable maintenance and setup prompts | when running that prompt flow |
| `standards/project-binding/` | external project binding standards and removal protocol | project binding governance |
| `workspace/resources/registry/` | legacy registry records moved from root during R76 | compatibility and selected navigation |
| `archive/migration-from-v0.3/root-legacy/` | old root compatibility paths moved during R76 | migration audits and old-path questions |
| `standards/capability-inventory/` | capability profile standards, policies, protocols, and matrices | capability inventory governance and release checks |
| `workspace/organization/capability-inventory/` | central organization capability inventory records and usage-memory placeholders | current public-safe organization capability records |
| `workspace/projects/_template/capability-inventory/` | project-level capability inventory record template | central project record template work |
| `examples/capability-inventory/` | illustrative capability profile examples | examples and regression checks |
| `templates/capability-inventory/` | copyable Capability Inventory JSON profile templates | selected template work |
| `standards/capability-inventory/business-system-profile-standard.md` | Business System profile standard and boundaries | business-system profile governance, project record relationship checks |
| `standards/capability-inventory/business-system-profile-review-flow.md` | Business System profile review flow standard | project usage memory to organization profile review boundary checks |
| `standards/capability-inventory/business-system-profile-manual-update-evidence-pack.md` | Business System profile manual update evidence pack standard | approved review to manual writeback evidence, rollback, and second verification boundary checks |
| `standards/capability-inventory/business-system-profile-manual-writeback-replay-record.md` | Business System profile manual writeback replay record standard | completed manual writeback audit, rollback record, and second verification boundary checks |
| `standards/capability-inventory/business-system-profile-audit-trail-index.md` | Business System profile audit trail index standard | organization-level review / evidence / replay / rollback / verification index boundary checks |
| `standards/capability-inventory/business-system-profile-governance-decision-record.md` | Business System profile governance decision record standard | human governance decision, retained unknown / not-run / missing evidence, and manual update boundary checks |
| `standards/capability-inventory/business-system-profile-change-ledger.md` | Business System profile change ledger standard | field-level manual change history, old/new summary, second verification, rollback, and next manual review boundary checks |
| `templates/capability-inventory/business-system-profile-template.json` | Business System capability profile template for external system governance boundaries | business-system profile template work or release checks |
| `templates/capability-inventory/business-system-profile-review-packet.md` | Business System profile review packet template | no-code organization profile review proposals |
| `templates/capability-inventory/business-system-profile-manual-update-evidence-pack.md` | Business System profile manual update evidence pack template | approved-review evidence pack preparation without automatic profile writeback |
| `templates/capability-inventory/business-system-profile-manual-writeback-replay-record.md` | Business System profile manual writeback replay record template | completed manual writeback audit without execution or automatic rollback |
| `templates/capability-inventory/business-system-profile-audit-trail-index.md` | Business System profile audit trail index template | manual no-code audit trail summaries without automatic actions |
| `templates/capability-inventory/business-system-profile-governance-decision-record.md` | Business System profile governance decision record template | human decision record without automatic approval or execution |
| `templates/capability-inventory/business-system-profile-change-ledger.md` | Business System profile change ledger template | field-level manual change ledger without automatic writeback or scheduled automation |
| `examples/capability-inventory/business-system-profiles/` | public-safe Business System profile examples | example shape and no-connector boundary checks |
| `examples/capability-inventory/business-system-profile-reviews/` | public-safe Business System profile review examples | no-code review flow examples that do not auto-update organization truth |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-manual-update-evidence.example.md` | public-safe Notion read access manual update evidence example | approved-review premise, rollback note, second verification not-run, and no auto writeback |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-manual-writeback-replay.example.md` | public-safe Notion read access manual writeback replay example | completed manual writeback premise, rollback record, second verification not-run, and no auto rollback |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-audit-trail-index.example.md` | public-safe Notion read access audit trail index example | review / evidence / replay / rollback / verification summary with no automatic action |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-governance-decision.example.md` | public-safe Notion read access governance decision example | `needs_second_verification` decision with manual update still blocked |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-change-ledger.example.md` | public-safe Notion read access change ledger example | field-level `read_access` old/new summary with second verification not-run and missing evidence retained |
| `examples/project-records/business-system-profile-references/` | public-safe project record examples that reference Business System profiles | central project record relationship examples, not real private project records |
| `examples/capability-inventory/business-system-profiles/manual-github-profile-walkthrough.md` | manual GitHub Business System walkthrough | end-to-end user-confirmed facts to organization and project records |
| `examples/capability-inventory/business-system-profiles/manual-notion-profile-walkthrough.md` | manual Notion Business System walkthrough | non-code user-confirmed facts, unknown fields, not-run checks, and missing evidence |
| `examples/capability-inventory/business-system-profiles/unknown-not-run-missing-examples.md` | `unknown`, `not-run`, and `missing` examples | evidence-state clarification |
| `examples/capability-inventory/business-system-profiles/non-verifiable-business-system-fields.md` | non-verifiable Business System field notes | access, permission, API, export, role, and evidence boundary checks |
| `examples/failures/business-system-profile-as-connector.md` | forbidden failure example for treating a profile as a connector | boundary regression and anti-pattern review |
| `docs/03-user-guides/manual-capability-profile.md` | manual Capability Inventory profile guide | adding no-code manual or semi-manual capability profiles |
| `docs/03-user-guides/project-usage-memory-boundary.md` | project usage memory boundary guide | project memory is not organization truth |
| `evals/palbench/capability-inventory/r82-manual-profile-guide-compliance.md` | Manual Profile Guide compliance regression | Capability Inventory boundary checks |
| `evals/palbench/capability-inventory/r83-project-record-relationship-boundary.md` | Business System project relationship regression | organization/project record and thin binding boundary checks |
| `evals/palbench/capability-inventory/r84-business-system-manual-walkthrough-boundary.md` | Business System manual walkthrough regression | walkthrough, failure example, and evidence-state boundary checks |
| `evals/palbench/capability-inventory/r85-non-github-business-system-boundary.md` | Non-GitHub Business System regression | Notion, CRM, non-code walkthrough, non-verifiable fields, and no-connector boundary checks |
| `evals/palbench/capability-inventory/r86-project-record-business-system-reference-boundary.md` | project record Business System reference regression | content-ops and sales-ops examples, project usage memory, central roster, thin binding, and no-connector boundary checks |
| `evals/palbench/capability-inventory/r87-business-system-profile-review-flow-boundary.md` | Business System profile review flow regression | review packet, project usage memory upgrade, central roster, thin binding, and no-connector boundary checks |
| `evals/palbench/capability-inventory/r88-business-system-profile-manual-update-evidence-boundary.md` | Business System profile manual update evidence regression | evidence pack, rollback, second verification, central roster, thin binding, and no-connector boundary checks |
| `evals/palbench/capability-inventory/r89-business-system-profile-manual-writeback-replay-boundary.md` | Business System profile manual writeback replay regression | replay record, rollback record, second verification, central roster, thin binding, and no-connector boundary checks |
| `evals/palbench/capability-inventory/r90-business-system-profile-audit-trail-index-boundary.md` | Business System profile audit trail index regression | audit trail index, next manual actions, missing evidence, central roster, thin binding, external API, and no-connector boundary checks |
| `evals/palbench/capability-inventory/r91-business-system-profile-governance-decision-boundary.md` | Business System profile governance decision regression | human decision record, second verification blocking, missing evidence, central roster, thin binding, and no-connector boundary checks |
| `evals/palbench/capability-inventory/r92-business-system-profile-change-ledger-boundary.md` | Business System profile change ledger regression | field-level old/new summary, second verification, missing evidence, next manual review, central roster, thin binding, and no-connector boundary checks |
| `release/fresh-clone-checks/r90-local-business-system-profile-audit-trail-index-validation.md` | R90 local clean-copy validation record | audit trail index validation and local no-code boundary evidence |
| `release/fresh-clone-checks/r91-local-business-system-profile-governance-decision-validation.md` | R91 local clean-copy validation record | governance decision validation and local no-code boundary evidence |
| `release/fresh-clone-checks/r92-local-business-system-profile-change-ledger-validation.md` | R92 local clean-copy validation record | change ledger validation and local no-code boundary evidence |
| `archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/` | archived R78 root compatibility pointers | legacy path questions and migration audits |
| `workspace/resources/imports/` | public-safe import staging placeholders | import/resource boundary work |
| `workspace/organization/memory/` | public-safe organization memory placeholders and examples | memory protocol or placeholder work |
| `workspace/resources/response-fingerprints/` | Pal response fingerprint references | selected Pal validation |
| `docs/` | user documentation and reference material | docs work or user questions |
| `docs/01-concepts/07-why-pal.md` | why AgentPal uses the Pal concept between Skills and Agent teams | concept questions and onboarding |
| `docs/05-orchestration-methodology/` | current AgentPal Pal orchestration methodology | methodology questions and docs navigation |
| `docs/09-roadmap/` | v0.2 roadmap and task pool | v0.2 planning and development sequencing |
| `docs/09-roadmap/v0.2-release-readiness.md` | v0.2 release readiness assessment | R46 first-phase integrated readiness and rc preparation recommendation |
| `docs/09-roadmap/v0.2-public-capability-summary.md` | v0.2 public capability summary | restrained public claims for v0.2 first phase |
| `docs/09-roadmap/no-code-future-boundary.md` | no-code future boundary | default v0.3/v0.4/v0.5 boundary: AgentPal remains Pal layer, not runtime program |
| `docs/00-overview/capability-inventory-migration-plan.md` | capability/runtime/model/plugin migration plan | R77 high-risk reference directory planning |
| `docs/00-overview/orchestration-migration-plan.md` | orchestration migration plan | R77 high-risk protocol surface planning |
| `docs/00-overview/prompts-migration-plan.md` | prompts migration plan | R77 copyable prompt family planning |
| `docs/09-roadmap/v0.3-development-plan.md` | v0.3 no-code orchestration prototype plan | Multi-Pal Collaboration, Deep Conductor prototype, Context Packet, Owner + Verifier, Plan -> Execute -> Verify, Parallel Review, and Routing Memory planning |
| `docs/09-roadmap/v0.3-task-pool.md` | v0.3 execution task pool | P0/P1/P2 task packages for collaboration protocol work |
| `docs/09-roadmap/v0.3-deep-conductor-readiness.md` | v0.3 Deep Conductor readiness | R63 readiness decision for entering v0.3.0-rc.1 release preparation |
| `docs/09-roadmap/v0.3-public-capability-summary.md` | v0.3 public capability summary | public-safe current capability and forbidden claim summary |
| `docs/09-roadmap/v0.3-release-checklist.md` | v0.3 release preparation checklist | checks before tag, push, or GitHub Release work |
| `docs/09-roadmap/v0.3-release-preparation-audit.md` | v0.3 release preparation audit | R64 release-facing package audit before tag / push / release work |
| `evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md` | v0.3 Deep Conductor integration matrix | integrated pass / partial / unavailable readiness matrix |
| `docs/05-orchestration-methodology/deep-conductor-master-goal.md` | Deep Conductor master goal | no-code 12-step conductor loop and executor boundary |
| `docs/05-orchestration-methodology/deep-conductor-master-loop-usage-guide.md` | Deep Conductor master loop usage guide | project goal to task map, Runtime packages, verification, synthesis, and memory writeback |
| `docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md` | Deep Conductor E2E usage guide | full no-code loop from goal through memory, capability, context budget, topology, Runtime Skill-aware packages, verification, synthesis, routing memory, and next-round recommendation |
| `docs/research/deep-conductor-real-runtime-replay-gap-analysis.md` | Deep Conductor real replay gap analysis | R61 real host replay pass / partial / unavailable / fail classification and R62 repair targets |
| `docs/research/deep-conductor-real-runtime-replay-report.md` | Deep Conductor real Runtime replay report | R61 manual host Runtime replay report and boundary evidence |
| `docs/05-orchestration-methodology/cross-runtime-pal-memory.md` | Cross-Runtime Pal Memory usage guide | no-code continuity across Codex, Claude Code, generic CLI, and other host Runtimes |
| `docs/05-orchestration-methodology/runtime-installed-skill-orchestration-guide.md` | Runtime-installed Skill Orchestration guide | no-code Runtime Skill candidate selection, availability checks, fallback, verification, and usage memory |
| `docs/05-orchestration-methodology/token-cost-aware-deep-conductor.md` | Token / Cost-aware Deep Conductor guide | no-code Context Budget, read tier, prompt shaping, verification cost, and usage report guidance |
| `docs/05-orchestration-methodology/context-packet-usage-guide.md` | Context Packet usage guide | user and maintainer guide for `/pal`, `@Pal`, consult, handoff, review, owner transfer, privacy, and runtime adapter usage |
| `docs/05-orchestration-methodology/owner-verifier-usage-guide.md` | Owner + Verifier usage guide | no-code owner/verifier workflow, independent evidence context, result records, and repair package guidance |
| `docs/05-orchestration-methodology/parallel-independent-review-usage-guide.md` | Parallel Independent Review usage guide | no-code isolated reviewer workflow, reviewer packets, final reports, synthesis, and group-chat collapse prevention |
| `docs/02-getting-started/multi-pal-collaboration-prompt-cards.md` | Multi-Pal prompt cards | copyable user prompts for Mira, `/pal`, `@Pal`, Context Packet, review, handoff, and summary paths |
| `evals/v0.2-integration/v0.2-integration-test-matrix.md` | v0.2 integration matrix | R46 integrated readiness test matrix |
| `docs/06-palsmith/README.md` | PalSmith v0.2 productization index | PalSmith creation and AI team productization work |
| `docs/06-palsmith/palsmith-end-to-end-productization.md` | PalSmith v0.2 end-to-end user path | PalSmith creation and AI team productization work |
| `official/pals/PalSmith-pal-governor/templates/task-packages/create-first-professional-pal.md` | Copyable first professional Pal creation task package | PalSmith v0.2 single-Pal creation work |
| `official/pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md` | Copyable AI team creation task package | PalSmith v0.2 AI team creation work |
| `official/pals/PalSmith-pal-governor/runbooks/pal-health-check.md` | Pal health check runbook | PalSmith v0.2 creation and repair checks |
| `official/pals/PalSmith-pal-governor/runbooks/ai-team-health-check.md` | AI team health check runbook | PalSmith v0.2 team readiness checks |
| `docs/02-getting-started/mira-first-usage.md` | Mira-first user path | onboarding and daily-use examples |
| `docs/02-getting-started/mira-first-prompt-cards.md` | Copyable Mira-first prompts | daily user prompts and direct `/pal Name` guidance |
| `official/pals/Mira-main/templates/task-packages/mira-first-task-intake.md` | Mira ordinary task intake template | Mira-first task organization |
| `official/pals/Mira-main/templates/task-packages/mira-composite-deliverable-task-package.md` | Mira composite deliverable template | staged Task Package creation |
| `official/pals/Mira-main/templates/task-packages/mira-owner-judgement-summary.md` | Mira owner judgement summary template | explaining Pal candidates and override paths |
| `official/pals/Mira-main/templates/task-packages/mira-runtime-brief.md` | Mira runtime brief template | Codex / Claude Code / generic CLI execution handoff |
| `official/pals/Mira-main/examples/mira-runtime-brief-example.md` | Mira runtime brief example | execution-layer evidence and project boundary example |
| `official/pals/Mira-main/evals/mira-first-usage-self-test.md` | Mira-first self-test | ordinary, composite, direct Pal, and release-check regression |
| `docs/07-official-pals/official-pal-examples-index.md` | Official 9 Pal real task examples index | official Pal examples and v0.2 R42 navigation |
| `docs/07-official-pals/official-pal-example-library-plan.md` | Official Pal example library plan | official Pal examples planning and R42 first implementation status |
| `evals/official-pals/official-pal-example-library-self-test.md` | Official Pal example library self-test | R42 example structure and boundary checks |
| `docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md` | Capability Inventory minimal usable design | v0.2 R43 manual profile design |
| `docs/03-user-guides/manual-capability-profile.md` | Manual Capability Profile Guide | no-code manual or semi-manual capability profile creation |
| `docs/00-overview/capability-inventory-navigation.md` | Capability Inventory standards / records / examples / templates navigation | R80 template and runtime example path clarification |
| `standards/capability-inventory/README.md` | Capability Inventory profile index | runtime/model/reasoning/skill/plugin/MCP/Pal profile navigation |
| `examples/capability-inventory/runtime-profiles/` | Runtime profile examples | runtime capability judgement inputs |
| `examples/capability-inventory/model-profiles/` | Model profile examples | model tendency judgement inputs |
| `examples/capability-inventory/reasoning-profiles/` | Reasoning strength profile examples | prompt-shaping judgement inputs |
| `examples/capability-inventory/skill-profiles/` | Skill profile examples | Skill capability judgement inputs |
| `examples/capability-inventory/plugin-profiles/` | Plugin profile notes | plugin capability judgement inputs |
| `examples/capability-inventory/mcp-profiles/` | MCP profile notes | MCP capability judgement inputs |
| `examples/capability-inventory/pal-profiles/` | Pal capability profile examples | Pal capability judgement inputs |
| `evals/capability-inventory/` | Capability Inventory self-tests | R43 profile structure, loading budget, and no fixed route checks |
| `examples/orchestration/capability-inventory-task-judgement-example.md` | Capability Inventory successful use example | profile-as-judgement-input example |
| `examples/failures/capability-profile-used-as-fixed-route.md` | Capability Inventory failure example | profile-as-route regression example |
| `docs/research/palbench-light-suite-plan.md` | PalBench Light suite plan | v0.2 R44 release regression suite design |
| `docs/research/palbench-collaboration-suite-plan.md` | PalBench Collaboration suite plan | v0.3 qualitative regression suite for no-code multi-Pal collaboration |
| `docs/research/palbench-collaboration-coverage-audit.md` | PalBench Collaboration coverage audit | R63 coverage audit for 87 v0.3 no-code regression cases |
| `evals/palbench-light/README.md` | PalBench Light eval entry | v0.2 release regression suite navigation |
| `evals/palbench-light/task-index.md` | PalBench Light task index | R44 first 24 case index |
| `evals/palbench-light/scoring-rubric.md` | PalBench Light scoring rubric | 0 / 1 / 2 release regression scoring |
| `evals/palbench-light/palbench-light-suite-self-test.md` | PalBench Light suite self-test | R44 suite structure and boundary check |
| `evals/palbench-collaboration/README.md` | PalBench Collaboration eval entry | v0.3 collaboration regression suite navigation |
| `evals/palbench-collaboration/task-index.md` | PalBench Collaboration task index | collaboration cases for direct Pal, mention consult, Owner + Verifier, Parallel Independent Review, Context Packet privacy, missing fields, and failure cases |
| `docs/04-runtime-guides/runtime-adapter-stability-guide.md` | Runtime Adapter stability guide | R45 thin binding stability and cross-project troubleshooting |
| `docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md` | Runtime Adapter troubleshooting cards | R45 copyable bounded troubleshooting prompts |
| `docs/04-runtime-guides/upgrade-existing-binding-to-thin-binding.md` | existing binding upgrade runbook | R45 upgrade path for old copied bindings |
| `evals/runtime-adapters/runtime-adapter-regression-suite.md` | Runtime Adapter regression suite | R45 12-scenario adapter regression checklist |
| `docs/09-roadmap/v0.2-release-readiness.md` | v0.2 release readiness assessment | R46 integrated readiness conclusion |
| `docs/09-roadmap/v0.2-public-capability-summary.md` | v0.2 public capability summary | public-safe capability summary |
| `evals/v0.2-integration/v0.2-integration-test-matrix.md` | v0.2 integration matrix | first-phase integration test matrix |
| `docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md` | Pal Team, runtime-layer agent execution, and future Deep Conductor boundaries | Pal Team and orchestration questions |
| `docs/06-validation-and-evidence/` | current PalBench and evidence interpretation | validation, PalBench, and evidence questions |
| `docs/08-release-candidate/README.md` | pointer to archived historical release-candidate documents | legacy release-candidate path questions |
| `archive/migration-from-v0.3/release-candidate-docs/` | historical v0.3 release-candidate documents | historical traceability only |
| `docs/research/` | archived research notes | historical traceability only; not a primary entry point |
| `examples/` | public-safe examples and failure examples | examples, evals, or regression checks |
| `evals/` | self-tests and release checks | eval or release validation only |
| `workspace/organization/memory/` | public-safe memory placeholders | not ordinary task context |
| `archive/migration-from-v0.3/root-legacy/state/` | legacy public-safe state placeholder | migration traceability only |
| `archive/migration-from-v0.3/root-legacy/reports/` | legacy public-safe report placeholders | migration traceability only |
| `workspace/resources/imports/` | import staging placeholders | not ordinary task context |

For user-facing documentation, start with `docs/README.md`. For root-level release asset navigation, use this file.

## Capability Inventory Navigation

Capability Inventory is a no-code profile layer. It is not an automatic scanner, automatic validator, automatic discovery service, automatic execution engine, or keyword router.

### Capability Inventory Standards

| Path | Purpose |
| --- | --- |
| `standards/capability-inventory/` | standards, matrices, protocols, and profile rules |
| `standards/capability-inventory/business-system-profile-standard.md` | Business System profile standard for external system governance boundaries |
| `standards/capability-inventory/business-system-profile-review-flow.md` | Business System profile review flow standard for project usage memory to organization profile review |
| `standards/capability-inventory/business-system-profile-change-ledger.md` | Business System profile change ledger standard for manual field-level organization profile change history |
| `standards/capability-inventory/business-system-profile-change-review-note.md` | Business System profile change review note standard for periodic manual reconciliation |
| `docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md` | minimal usable design for manual profile records |

### Capability Inventory Templates

| Path | Purpose |
| --- | --- |
| `templates/capability-inventory/` | copyable JSON templates only, not current facts |
| `templates/capability-inventory/business-system-profile-template.json` | copyable Business System profile template for external system governance notes, not a connector |
| `templates/capability-inventory/business-system-profile-review-packet.md` | copyable no-code Business System profile review packet template |
| `templates/capability-inventory/business-system-profile-change-ledger.md` | copyable no-code Business System profile change ledger template |
| `templates/capability-inventory/business-system-profile-change-review-note.md` | copyable no-code Business System profile change review note template |

### Capability Inventory Examples

| Path | Purpose |
| --- | --- |
| `examples/capability-inventory/` | illustrative examples only, not proof of current availability |
| `examples/capability-inventory/business-system-profiles/` | public-safe Business System profile examples, not connectors or credentials |
| `examples/capability-inventory/business-system-profile-reviews/` | public-safe Business System profile review examples, not organization truth updates |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-change-ledger.example.md` | public-safe Business System profile change ledger example, not an automatic writeback |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-change-review-note.example.md` | public-safe Business System profile change review note example, not scheduled automation |
| `examples/capability-inventory/business-system-profiles/github-public-governance-profile.example.json` | GitHub governance example using placeholder `example-org/example-repo` |
| `examples/capability-inventory/business-system-profiles/notion-public-governance-profile.example.json` | Notion governance example with unknown workspace, database, write, and API access |
| `examples/capability-inventory/business-system-profiles/generic-crm-public-governance-profile.example.json` | Generic CRM governance example with unknown account, customer-data, export, write, and API access |
| `examples/capability-inventory/business-system-profiles/manual-github-profile-walkthrough.md` | manual walkthrough from confirmed facts to organization profile and project record |
| `examples/capability-inventory/business-system-profiles/manual-notion-profile-walkthrough.md` | non-code Notion walkthrough from possible use to central records without external `.agentpal/` copies |
| `examples/capability-inventory/business-system-profiles/github-project-record-reference.example.md` | central project record reference example |
| `examples/project-records/business-system-profile-references/content-ops-demo/` | public-safe central project record example referencing the Notion profile; not a real `workspace/projects/<project-id>` record |
| `examples/project-records/business-system-profile-references/sales-ops-demo/` | public-safe central project record example referencing the Generic CRM profile; not a real `workspace/projects/<project-id>` record |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-review.example.md` | public-safe review packet example with `blocked_missing_evidence` and no organization profile auto-update |
| `examples/capability-inventory/business-system-profiles/unknown-not-run-missing-examples.md` | evidence-state examples for `unknown`, `not-run`, and `missing` |
| `examples/capability-inventory/business-system-profiles/non-verifiable-business-system-fields.md` | fields that require user confirmation, host Runtime evidence, UI/export evidence, or admin confirmation |
| `examples/failures/business-system-profile-as-connector.md` | forbidden failure example for connector, credential, auto scan, and keyword route misuse |

### Organization Capability Records

| Path | Purpose |
| --- | --- |
| `workspace/organization/capability-inventory/` | public-safe organization-level capability records and placeholders |

### Project Capability Record Template

| Path | Purpose |
| --- | --- |
| `workspace/projects/_template/capability-inventory/` | project-level record template; real records live under `workspace/projects/<project-id>/capability-inventory/` and are private by default |
| `docs/03-user-guides/manual-capability-profile.md` | manual flow for choosing a profile type, copying a template, marking source/confidence, and saving to the right central record |
| `docs/03-user-guides/project-usage-memory-boundary.md` | project usage memory boundary guide; project memory is not organization truth and does not update central roster |
| `standards/capability-inventory/business-system-profile-review-flow.md` | review flow for project usage memory to organization Business System profile review |
| `templates/capability-inventory/business-system-profile-review-packet.md` | no-code review packet template for manual organization profile review |
| `evals/palbench/capability-inventory/r82-manual-profile-guide-compliance.md` | compliance regression for manual profiles, Business System profile boundary, project record relationship, and no auto scan / no keyword routing rules |
| `evals/palbench/capability-inventory/r83-project-record-relationship-boundary.md` | regression for organization/project record relationship, thin binding, no connector, no credentials, and no keyword routing |
| `evals/palbench/capability-inventory/r84-business-system-manual-walkthrough-boundary.md` | regression for walkthrough, evidence-state examples, forbidden failure example, and thin-binding boundary |
| `evals/palbench/capability-inventory/r85-non-github-business-system-boundary.md` | regression for Notion / CRM examples, non-code walkthrough, non-verifiable fields, and no connector / no keyword route |
| `evals/palbench/capability-inventory/r86-project-record-business-system-reference-boundary.md` | regression for project record Business System profile references and project usage memory boundary |
| `evals/palbench/capability-inventory/r87-business-system-profile-review-flow-boundary.md` | regression for Business System profile review flow and project usage memory upgrade boundary |
| `evals/palbench/capability-inventory/r93a-business-system-profile-change-review-note-boundary.md` | regression for Business System profile change review note boundary and manual reconciliation |
| `evals/palbench/v0.4/r93b-v0.4-real-usage-regression-test-plan.md` | R93-B v0.4 real-usage regression plan |
| `evals/palbench/v0.4/r93b-v0.4-test-matrix.md` | R93-B v0.4 regression test matrix |
| `evals/palbench/project-binding/r93c-thin-binding-simulation-results.md` | R93-C generic / Claude thin-binding temporary-project simulation results |
| `evals/palbench/v0.4/r93d-central-asset-integrity-audit.md` | R93-D central asset integrity audit |
| `release/fresh-clone-checks/r94-r93-parallel-integration-validation.md` | R94 validation for R93 parallel-result integration and shared-entry closure |

### Historical Migration Notes

| Path | Purpose |
| --- | --- |
| `docs/00-overview/capability-inventory-navigation.md` | current source map and legacy path notes |
| `docs/00-overview/capability-inventory-migration-plan.md` | migration plan and completed R78/R79/R80 path decisions |
| `archive/migration-from-v0.3/root-legacy/capability-inventory/` | historical migration evidence and archived root pointers |

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

Official Pal Packs for v0.3.0-rc.1:

- `official/pals/Mira-main`
- `official/pals/Atlas-developer`
- `official/pals/Vega-research`
- `official/pals/Rhea-system`
- `official/pals/PalSmith-pal-governor`
- `official/pals/Quinn-quality`
- `official/pals/Morgan-document`
- `official/pals/Harper-writing`
- `official/pals/Nova-product`

Do not load all Pal directories by default. Load Mira for ordinary entry and the selected owner Pal for owned tasks.

## Current Protocols To Prefer

- `orchestration/runtime-response-gate.md`
- `orchestration/fast-route-protocol.md`
- `orchestration/ai-routing-judgement-protocol.md`
- `orchestration/pal-context-slicing-protocol.md`
- `orchestration/agent-instruction-file-loading-policy.md`
- `orchestration/pal-asset-loading-budget.md`
- `orchestration/context-packet-minimalism-protocol.md`
- `orchestration/context-packet-protocol.md`
- `orchestration/mention-and-direct-pal-protocol.md`
- `orchestration/owner-verifier-workflow-protocol.md`
- `orchestration/parallel-independent-review-protocol.md`
- `orchestration/memory-summary-loading-protocol.md`
- `orchestration/task-package-output-contract.md`
- `orchestration/deep-conductor-protocol.md`
- `orchestration/project-conductor-workflow.md`
- `orchestration/memory-boundary-protocol.md`
- `orchestration/pal-skill-vs-runtime-skill-protocol.md`
- `orchestration/runtime-skill-candidate-decision-protocol.md`
- `orchestration/token-cost-aware-conductor-policy.md`
- `orchestration/context-budget-protocol.md`
- `orchestration/prompt-shaping-by-model-and-reasoning.md`
- `workspace/organization/memory/runtime/cross-runtime-pal-memory-protocol.md`
- `orchestration/pal-owned-skill-storage-protocol.md`
- `orchestration/specialist-pal-asset-loading-protocol.md`

## Methodology, Validation, Release Candidate, And Archive

Use the current docs directories as the public entry points. Archived research notes are kept only for traceability. None of these files activate Deep Conductor, Subagent Mode, or external Agent calls.

| Path | Purpose |
| --- | --- |
| `docs/05-orchestration-methodology/README.md` | current Pal Orchestration Methodology entry |
| `docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md` | v0.2 minimal manual Capability Inventory profile design |
| `standards/capability-inventory/business-system-profile-standard.md` | Business System profile standard for no-code external system governance |
| `standards/capability-inventory/business-system-profile-review-flow.md` | Business System profile review flow standard for no-code organization profile review |
| `standards/capability-inventory/business-system-profile-manual-update-evidence-pack.md` | Business System profile manual update evidence pack standard for approved-review evidence, rollback, and second verification |
| `standards/capability-inventory/business-system-profile-manual-writeback-replay-record.md` | Business System profile manual writeback replay record standard for completed manual writeback audit and rollback record |
| `standards/capability-inventory/business-system-profile-audit-trail-index.md` | Business System profile audit trail index standard for review / evidence / replay / rollback / verification summaries |
| `standards/capability-inventory/business-system-profile-governance-decision-record.md` | Business System profile governance decision record standard for human decisions after audit trail review |
| `standards/capability-inventory/business-system-profile-change-ledger.md` | Business System profile change ledger standard for manual field-level change history |
| `standards/capability-inventory/business-system-profile-change-review-note.md` | Business System profile change review note standard for manual periodic reconciliation |
| `examples/capability-inventory/business-system-profiles/github-public-governance-profile.example.json` | public-safe GitHub Business System profile example using `example-org/example-repo` |
| `examples/capability-inventory/business-system-profiles/notion-public-governance-profile.example.json` | public-safe Notion Business System profile example with unknown access and no connector |
| `examples/capability-inventory/business-system-profiles/generic-crm-public-governance-profile.example.json` | public-safe generic CRM Business System profile example with unknown customer-data and write access |
| `examples/project-records/business-system-profile-references/content-ops-demo/` | public-safe content operations project record example referencing the Notion Business System profile |
| `examples/project-records/business-system-profile-references/sales-ops-demo/` | public-safe sales operations project record example referencing the Generic CRM Business System profile |
| `templates/capability-inventory/business-system-profile-review-packet.md` | Business System profile review packet template |
| `templates/capability-inventory/business-system-profile-manual-update-evidence-pack.md` | Business System profile manual update evidence pack template |
| `templates/capability-inventory/business-system-profile-manual-writeback-replay-record.md` | Business System profile manual writeback replay record template |
| `templates/capability-inventory/business-system-profile-audit-trail-index.md` | Business System profile audit trail index template |
| `templates/capability-inventory/business-system-profile-governance-decision-record.md` | Business System profile governance decision record template |
| `templates/capability-inventory/business-system-profile-change-ledger.md` | Business System profile change ledger template |
| `templates/capability-inventory/business-system-profile-change-review-note.md` | Business System profile change review note template |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-review.example.md` | public-safe Notion read access review example blocked by missing evidence |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-manual-update-evidence.example.md` | public-safe Notion read access manual update evidence example with second verification not-run |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-manual-writeback-replay.example.md` | public-safe Notion read access manual writeback replay example with rollback record and second verification not-run |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-audit-trail-index.example.md` | public-safe Notion read access audit trail index example with next manual actions and missing evidence preserved |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-governance-decision.example.md` | public-safe Notion read access governance decision example with manual update blocked until second verification |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-change-ledger.example.md` | public-safe Notion read access change ledger example with old/new summary and second verification not-run |
| `examples/capability-inventory/business-system-profile-reviews/notion-read-access-change-review-note.example.md` | public-safe Notion read access change review note example with manual reconciliation and no scheduled automation |
| `evals/palbench/capability-inventory/r83-project-record-relationship-boundary.md` | Business System profile relationship and thin-binding regression |
| `examples/capability-inventory/business-system-profiles/manual-github-profile-walkthrough.md` | manual Business System walkthrough from user facts to central records |
| `examples/capability-inventory/business-system-profiles/manual-notion-profile-walkthrough.md` | manual Notion Business System walkthrough from user facts to central records |
| `examples/capability-inventory/business-system-profiles/unknown-not-run-missing-examples.md` | examples for preserving unknown, not-run, and missing evidence states |
| `examples/capability-inventory/business-system-profiles/non-verifiable-business-system-fields.md` | notes for non-verifiable access, permission, API, export, role, and evidence fields |
| `examples/failures/business-system-profile-as-connector.md` | forbidden connector misuse failure example |
| `evals/palbench/capability-inventory/r84-business-system-manual-walkthrough-boundary.md` | R84 walkthrough and boundary regression |
| `evals/palbench/capability-inventory/r85-non-github-business-system-boundary.md` | R85 non-GitHub Business System boundary regression |
| `evals/palbench/capability-inventory/r86-project-record-business-system-reference-boundary.md` | R86 project record Business System reference boundary regression |
| `release/fresh-clone-checks/r86-local-project-record-business-system-reference-validation.md` | R86 local clean-copy validation record |
| `evals/palbench/capability-inventory/r87-business-system-profile-review-flow-boundary.md` | R87 Business System profile review flow boundary regression |
| `release/fresh-clone-checks/r87-local-business-system-profile-review-flow-validation.md` | R87 local clean-copy validation record |
| `evals/palbench/capability-inventory/r88-business-system-profile-manual-update-evidence-boundary.md` | R88 Business System profile manual update evidence boundary regression |
| `release/fresh-clone-checks/r88-local-business-system-profile-manual-update-evidence-validation.md` | R88 local clean-copy validation record |
| `evals/palbench/capability-inventory/r89-business-system-profile-manual-writeback-replay-boundary.md` | R89 Business System profile manual writeback replay boundary regression |
| `release/fresh-clone-checks/r89-local-business-system-profile-manual-writeback-replay-validation.md` | R89 local clean-copy validation record |
| `evals/palbench/capability-inventory/r90-business-system-profile-audit-trail-index-boundary.md` | R90 Business System profile audit trail index boundary regression |
| `release/fresh-clone-checks/r90-local-business-system-profile-audit-trail-index-validation.md` | R90 local clean-copy validation record |
| `evals/palbench/capability-inventory/r91-business-system-profile-governance-decision-boundary.md` | R91 Business System profile governance decision boundary regression |
| `release/fresh-clone-checks/r91-local-business-system-profile-governance-decision-validation.md` | R91 local clean-copy validation record |
| `evals/palbench/capability-inventory/r92-business-system-profile-change-ledger-boundary.md` | R92 Business System profile change ledger boundary regression |
| `release/fresh-clone-checks/r92-local-business-system-profile-change-ledger-validation.md` | R92 local clean-copy validation record |
| `evals/palbench/capability-inventory/r93a-business-system-profile-change-review-note-boundary.md` | R93-A Business System profile change review note boundary regression |
| `release/fresh-clone-checks/r93a-local-business-system-profile-change-review-note-validation.md` | R93-A local clean-copy validation record |
| `evals/palbench/v0.4/r93b-v0.4-real-usage-regression-test-plan.md` | R93-B v0.4 real-usage regression test plan |
| `evals/palbench/v0.4/r93b-v0.4-test-matrix.md` | R93-B v0.4 regression test matrix |
| `release/fresh-clone-checks/r93b-v0.4-regression-test-plan-validation.md` | R93-B local validation record |
| `evals/palbench/project-binding/r93c-thin-binding-simulation-results.md` | R93-C thin-binding temporary-project simulation results |
| `release/fresh-clone-checks/r93c-local-thin-binding-simulation-validation.md` | R93-C local validation record |
| `evals/palbench/v0.4/r93d-central-asset-integrity-audit.md` | R93-D central asset integrity audit |
| `release/fresh-clone-checks/r93d-local-central-asset-integrity-validation.md` | R93-D local validation record |
| `release/integration-notes/r93d-path-fix-suggestions.md` | R93-D stale release path fix suggestion record |
| `release/integration-notes/r94-r93-parallel-integration-summary.md` | R94 summary for integrated R93 parallel outputs |
| `release/fresh-clone-checks/r94-r93-parallel-integration-validation.md` | R94 R93 parallel-result integration validation record |
| `evals/palbench/v0.4/r95-v0.4-real-usage-regression-results.md` | R95 v0.4 real-usage regression results |
| `evals/palbench/v0.4/r95-v0.4-regression-issues.md` | R95 v0.4 regression issue log |
| `release/fresh-clone-checks/r95-v0.4-full-regression-validation.md` | R95 full regression validation record |
| `release/current/v0.4-local-completion-report.md` | R96 v0.4 local completion report |
| `release/current/v0.4-local-completion-evidence-index.md` | R96 v0.4 local completion evidence index |
| `docs/08-release-and-maintenance/v0.4-local-completion-summary.md` | R96 user-facing v0.4 local completion summary |
| `evals/palbench/v0.4/r96-v0.4-completion-evidence-review.md` | R96 evidence review for v0.4 local completion |
| `release/fresh-clone-checks/r96-v0.4-local-completion-validation.md` | R96 local completion validation record |
| `docs/09-roadmap/v0.5-local-development-scope.md` | R97 v0.5 local development scope and no-code boundary freeze |
| `standards/org-pack/org-pack-standard.md` | R97 Org Pack standard |
| `templates/org-pack/base-org-pack/` | R97 base Org Pack template |
| `examples/org-packs/base-agentpal-org-pack/` | R97 public-safe base AgentPal Org Pack example |
| `evals/palbench/org-pack/r97-org-pack-foundation-boundary.md` | R97 Org Pack foundation boundary eval |
| `release/fresh-clone-checks/r97-local-org-pack-foundation-validation.md` | R97 local Org Pack foundation validation record |

## Pal Asset Standards

| Path | Purpose |
| --- | --- |
| `standards/pal-asset/README.md` | Pal Asset standards index |
| `standards/pal-asset/pal-asset-standard.md` | R98-A Pal Asset Standard |
| `standards/pal-asset/pal-skill-vs-agent-skill-standard.md` | R98-A Pal Skill vs Agent Skill boundary |
| `standards/pal-asset/pal-asset-directory-standard.md` | R98-A Pal asset directory responsibilities |
| `standards/pal-asset/pal-root-entry-standard.md` | R98-A Pal root entry responsibilities |
| `standards/pal-asset/pal-loading-order-standard.md` | R98-D Pal loading order standard |
| `standards/pal-asset/pal-asset-resolver-standard.md` | R98-D no-code Pal Asset Resolver standard |
| `templates/pal-asset/README.md` | Pal Asset template index |
| `evals/palbench/pal-asset/r98a-pal-asset-standard-boundary.md` | R98-A Pal Asset boundary eval |
| `release/fresh-clone-checks/r98a-local-pal-asset-standard-validation.md` | R98-A local validation |

## Pal Metadata v0.5

| Path | Purpose |
| --- | --- |
| `standards/pal-asset/pal-json-v0.5-standard.md` | R100-A pal.json v0.5 metadata standard |
| `standards/pal-asset/asset-manifest-standard.md` | R100-A optional asset-manifest standard |
| `standards/schemas/pal.schema.json` | R100-A pal.json schema |
| `standards/schemas/pal-asset-manifest.schema.json` | R100-A asset-manifest schema |
| `templates/pal-asset/pal-json-template.json` | R100-A pal.json template |
| `templates/pal-asset/asset-manifest-template.json` | R100-A asset-manifest template |
| `docs/00-overview/pal-metadata-v0.5-upgrade-path.md` | R101 public upgrade path and navigation |
| `evals/palbench/pal-asset/r100a-pal-metadata-schema-boundary.md` | R100-A metadata schema boundary eval |
| `release/fresh-clone-checks/r100a-local-pal-metadata-schema-validation.md` | R100-A metadata schema validation |
| `release/integration-notes/r100a-index-update-notes.md` | R100-A index update notes |

## Official Pal Metadata Upgrade Preparation

| Path | Purpose |
| --- | --- |
| `release/integration-notes/r100b-official-pal-metadata-upgrade-batch-plan.md` | R100-B official Pal metadata batch plan |
| `release/integration-notes/r100b-official-pal-safe-index-file-plan.md` | R100-B safe index file plan |
| `release/integration-notes/r100b-official-pal-asset-manifest-preview-plan.md` | R100-B asset-manifest preview plan |
| `evals/palbench/pal-asset/r100b-official-pal-metadata-preflight.md` | R100-B official Pal metadata preflight eval |
| `release/fresh-clone-checks/r100b-local-official-pal-metadata-preflight-validation.md` | R100-B preflight validation |
| `evals/palbench/pal-asset/r100d-pal-metadata-upgrade-compatibility-gate.md` | R100-D compatibility gate |
| `evals/palbench/pal-asset/r100d-pal-manifest-backward-compatibility-cases.md` | R100-D backward compatibility cases |
| `release/fresh-clone-checks/r100d-local-pal-metadata-upgrade-gate-validation.md` | R100-D gate validation |
| `release/integration-notes/r100d-official-pal-upgrade-gate-notes.md` | R100-D official upgrade gate notes |

## Pal Asset Index Templates

| Path | Purpose |
| --- | --- |
| `templates/pal-asset/index-templates/README.md` | R100-C index template package README |
| `templates/pal-asset/index-templates/skills-index-template.md` | Pal skills index template |
| `templates/pal-asset/index-templates/workflows-index-template.md` | Pal workflows index template |
| `templates/pal-asset/index-templates/runbooks-index-template.md` | Pal runbooks index template |
| `templates/pal-asset/index-templates/knowledge-index-template.md` | Pal knowledge index template |
| `templates/pal-asset/index-templates/memory-index-template.md` | Pal memory index template |
| `templates/pal-asset/index-templates/learning-index-template.md` | Pal learning index template |
| `templates/pal-asset/index-templates/evals-index-template.md` | Pal evals index template |
| `templates/pal-asset/index-templates/examples-index-template.md` | Pal examples index template |
| `templates/pal-asset/index-templates/research-index-template.md` | Pal research index template |
| `templates/pal-asset/safe-index-backfill-guide.md` | R100-C safe index backfill guide |
| `evals/palbench/pal-asset/r100c-pal-index-template-boundary.md` | R100-C index template boundary eval |
| `release/fresh-clone-checks/r100c-local-pal-index-template-validation.md` | R100-C template validation |
| `release/integration-notes/r100c-index-update-notes.md` | R100-C index update notes |

## PalSmith v0.5

| Path | Purpose |
| --- | --- |
| `standards/palsmith/palsmith-v0.5-creation-standard.md` | R98-C PalSmith creation standard |
| `standards/palsmith/palsmith-asset-classification-standard.md` | R98-C PalSmith asset classification standard |
| `templates/palsmith/minimal-pal-generation-checklist.md` | Minimal Pal generation checklist |
| `templates/palsmith/standard-pal-generation-checklist.md` | Standard Pal generation checklist |
| `templates/palsmith/pal-asset-classification-result-template.json` | Pal asset classification result JSON template |
| `templates/palsmith/existing-pal-upgrade-report-template.md` | existing Pal upgrade report template |
| `evals/palbench/palsmith/r98c-palsmith-v0.5-asset-generation-boundary.md` | R98-C PalSmith boundary eval |
| `release/fresh-clone-checks/r98c-local-palsmith-v0.5-template-validation.md` | R98-C local validation |
| `docs/03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md` | PalSmith v0.5 user guide |

## Official Pal Asset Audit

| Path | Purpose |
| --- | --- |
| `evals/palbench/pal-asset/r98b-official-pal-asset-audit.md` | R98-B official 9 Pal asset audit |
| `evals/palbench/pal-asset/r98b-official-pal-upgrade-gap-table.md` | R98-B official Pal upgrade gap table |
| `release/integration-notes/r98b-official-pal-upgrade-plan.md` | R98-B official Pal upgrade plan |
| `release/fresh-clone-checks/r98b-local-official-pal-asset-audit-validation.md` | R98-B local validation |
| `docs/03-user-guides/official-pal-asset-upgrade-plan.md` | official Pal asset upgrade plan guide |

## Pal Asset / Org Pack Integration

| Path | Purpose |
| --- | --- |
| `docs/00-overview/pal-asset-and-org-pack-relationship.md` | Pal Asset / Org Pack relationship guide |
| `examples/pal-asset/pal-asset-resolver-task-package.example.md` | public-safe Pal Asset Resolver task package example |
| `evals/palbench/pal-asset/r98d-pal-asset-resolver-thin-binding-boundary.md` | R98-D resolver and thin-binding boundary eval |
| `release/fresh-clone-checks/r98d-local-pal-asset-resolver-validation.md` | R98-D local validation |
| `evals/palbench/pal-asset/r99-pal-asset-v0.5-integration-boundary.md` | R99 Pal Asset v0.5 integration boundary eval |
| `release/fresh-clone-checks/r99-r98-parallel-integration-validation.md` | R99 R98 parallel integration validation |

## Org Pack v0.5

| Path | Purpose |
| --- | --- |
| `standards/org-pack/org-pack-standard.md` | Org Pack standard |
| `standards/org-pack/org-pack-practical-structure.md` | R119-A practical Org Pack structure |
| `templates/org-pack/base-org-pack/` | base Org Pack template |
| `templates/org-pack/practical-org-pack/` | R119-A practical Org Pack template |
| `examples/org-packs/base-agentpal-org-pack/` | public-safe base AgentPal Org Pack example |
| `examples/org-packs/content-ops-org-pack/` | R119-A public-safe content operations Org Pack example |
| `evals/palbench/org-pack/r119a-org-pack-practical-structure-boundary.md` | R119-A practical Org Pack boundary eval |
| `release/fresh-clone-checks/r119a-local-org-pack-practical-structure-validation.md` | R119-A local validation |

## FDE / Expert Delivery Pack

| Path | Purpose |
| --- | --- |
| `standards/fde-pack/fde-pack-standard.md` | R119-B FDE Pack standard |
| `standards/fde-pack/expert-delivery-boundary.md` | R119-B expert delivery boundary |
| `templates/fde-pack/base-fde-pack/` | R119-B base FDE Pack template |
| `examples/fde-packs/accounting-advisor-fde-pack/` | R119-B public-safe accounting advisor FDE example |
| `evals/palbench/fde-pack/r119b-fde-pack-standard-boundary.md` | R119-B FDE Pack boundary eval |
| `release/fresh-clone-checks/r119b-local-fde-pack-standard-validation.md` | R119-B local validation |

## Asset Boundary

| Path | Purpose |
| --- | --- |
| `standards/asset-boundary/reusable-vs-customer-private-assets.md` | R119-C reusable vs customer-private asset standard |
| `standards/asset-boundary/asset-classification-matrix.md` | R119-C asset classification matrix |
| `standards/asset-boundary/deidentification-standard.md` | R119-C de-identification standard |
| `templates/asset-boundary/asset-classification-result-template.json` | R119-C asset classification result template |
| `templates/asset-boundary/customer-private-boundary-template.md` | R119-C customer-private boundary template |
| `examples/asset-boundary/reusable-vs-private-classification-examples.md` | R119-C public-safe classification examples |
| `examples/asset-boundary/bad-examples-customer-private-leak.md` | R119-C fake bad examples for boundary regression |
| `evals/palbench/asset-boundary/r119c-reusable-private-asset-boundary.md` | R119-C reusable/private asset boundary eval |
| `release/fresh-clone-checks/r119c-local-reusable-private-asset-boundary-validation.md` | R119-C local validation |

## Org / FDE Integration

| Path | Purpose |
| --- | --- |
| `evals/palbench/org-pack/r119d-org-fde-integration-gate.md` | R119-D Org Pack / FDE integration gate |
| `release/fresh-clone-checks/r119d-local-org-fde-integration-gate-validation.md` | R119-D local gate validation |
| `release/integration-notes/r119d-org-fde-integration-checklist.md` | R119-D integration checklist |
| `release/integration-notes/r119d-org-fde-integration-issue-template.md` | R119-D integration issue template |
| `release/integration-notes/r119d-r120-integration-plan.md` | R119-D R120 integration plan |
| `docs/00-overview/org-pack-fde-asset-boundary-overview.md` | R120 Org Pack / FDE / Asset Boundary overview |
| `release/integration-notes/r120-r119-org-fde-integration-summary.md` | R120 R119 integration summary |
| `evals/palbench/org-pack/r120-org-fde-asset-boundary-integrated-boundary.md` | R120 integrated boundary eval |
| `release/fresh-clone-checks/r120-local-org-fde-asset-boundary-integration-validation.md` | R120 local integration validation |
| `release/integration-notes/r120-r121-readiness-decision.md` | R120 R121 readiness decision |

## Combined Pack Examples

| Path | Purpose |
| --- | --- |
| `examples/combined-packs/content-ops-with-accounting-advisor/` | R121 public-safe Org Pack + FDE Pack combined example |
| `examples/combined-packs/content-ops-with-accounting-advisor/combined-pack.json` | machine-readable combined pack metadata and false safety flags |
| `examples/combined-packs/content-ops-with-accounting-advisor/ORG-FDE-COMPOSITION.md` | Org/FDE reference composition notes |
| `examples/combined-packs/content-ops-with-accounting-advisor/palsmith-audit-note.md` | public-safe PalSmith audit note |
| `release/integration-notes/r122-combined-pack-palsmith-review-report.md` | R122 PalSmith-style review report |
| `release/integration-notes/r122-combined-pack-reusable-private-classification-review.md` | R122 reusable/private classification review |
| `release/integration-notes/r122-combined-pack-approval-checklist.md` | R122 approval checklist for shared-entry integration |
| `evals/palbench/org-pack/r123-combined-pack-shared-entry-integration-boundary.md` | R123 shared-entry integration boundary eval |
| `release/fresh-clone-checks/r123-local-combined-pack-shared-entry-integration-validation.md` | R123 local shared-entry integration validation |

## Usage Scenarios

| Path | Purpose |
| --- | --- |
| `docs/04-usage-scenarios/org-fde-combined-pack-usage-scenario.md` | R124 Org Pack + FDE Pack combined usage scenario |
| `examples/combined-packs/content-ops-with-accounting-advisor/usage-walkthrough.md` | R124 combined example usage walkthrough |
| `examples/combined-packs/content-ops-with-accounting-advisor/project-binding-walkthrough.md` | R124 thin project binding walkthrough |
| `examples/combined-packs/content-ops-with-accounting-advisor/central-project-record-walkthrough.md` | R124 central project record walkthrough |
| `examples/combined-packs/content-ops-with-accounting-advisor/workflow-usage-example.md` | R125 workflow usage example |
| `examples/combined-packs/content-ops-with-accounting-advisor/context-packet.example.md` | R125 context packet example |
| `examples/combined-packs/content-ops-with-accounting-advisor/task-package.example.md` | R125 task package example |
| `examples/combined-packs/content-ops-with-accounting-advisor/governance-record.example.md` | R125 governance record example |
| `examples/combined-packs/content-ops-with-accounting-advisor/verification-result.example.md` | R125 verification result example |
| `evals/palbench/org-pack/r124-org-fde-combined-pack-usage-scenario-boundary.md` | R124 usage scenario boundary eval |
| `release/fresh-clone-checks/r124-local-org-fde-combined-pack-usage-scenario-validation.md` | R124 local usage scenario validation |
| `release/integration-notes/r124-r125-readiness-decision.md` | R124 R125 readiness decision |
| `evals/palbench/org-pack/r125-org-fde-workflow-governance-example-boundary.md` | R125 workflow/governance example boundary eval |
| `release/fresh-clone-checks/r125-local-org-fde-workflow-governance-example-validation.md` | R125 local workflow/governance validation |
| `release/integration-notes/r125-r126-readiness-decision.md` | R125 R126 readiness decision |

## v0.5 Overall Regression Planning

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/r127-v0.5-overall-regression-plan.md` | R127 v0.5 overall regression plan for R128 execution |
| `evals/palbench/v0.5/r127-v0.5-overall-regression-test-matrix.md` | R127 12-group v0.5 regression test matrix |
| `release/integration-notes/r127-v0.5-overall-regression-evidence-map.md` | R127 evidence map for v0.4 baseline and v0.5 modules |
| `release/integration-notes/r127-v0.5-overall-regression-issue-template.md` | R127 issue template for R128 findings |
| `release/integration-notes/r127-r128-overall-regression-execution-checklist.md` | R128 execution checklist and safety gates |
| `release/fresh-clone-checks/r127-local-v0.5-overall-regression-planning-validation.md` | R127 local planning validation record |
| `release/integration-notes/r127-r128-readiness-decision.md` | R127 readiness decision for R128 regression execution |
| `evals/palbench/v0.5/r128-v0.5-overall-regression-results.md` | R128 executed v0.5 overall regression results |
| `evals/palbench/v0.5/r128-v0.5-overall-regression-issues.md` | R128 issue table and severity classification |
| `release/fresh-clone-checks/r128-local-v0.5-overall-regression-validation.md` | R128 local validation record |
| `release/integration-notes/r128-r129-readiness-decision.md` | R128 readiness decision for R129 fix round |
| `release/integration-notes/r129-v0.5-regression-medium-issue-fix-plan.md` | R129 fix plan for R128 medium issues |
| `evals/palbench/v0.5/r129-v0.5-targeted-fix-rerun-results.md` | R129 targeted rerun results |
| `release/fresh-clone-checks/r129-local-v0.5-medium-issue-fix-validation.md` | R129 local validation record |
| `release/integration-notes/r129-r130-readiness-decision.md` | R129 readiness decision for v0.5 local completion report |
| `release/current/v0.5-local-completion-report.md` | R130 v0.5 local completion report; not remote publication proof |
| `release/current/v0.5-local-completion-evidence-index.md` | R130 v0.5 local completion evidence index |
| `release/current/v0.5-release-not-published.md` | R130 statement that no push, tag, or GitHub Release was performed |
| `evals/palbench/v0.5/r130-v0.5-completion-evidence-review.md` | R130 completion evidence review eval |
| `release/fresh-clone-checks/r130-local-v0.5-completion-validation.md` | R130 local v0.5 completion validation |
| `release/integration-notes/r130-r131-readiness-decision.md` | R130 readiness decision for local-only v0.5 release preflight |
| `release/current/v0.5-local-release-preflight.md` | R131 local-only v0.5 release preflight; not remote publication proof |
| `release/current/v0.5-public-package-checklist.md` | R131 public package checklist for release decision |
| `release/current/v0.5-release-notes-draft.md` | R131 draft release notes; not published release notes |
| `release/current/v0.5-public-artifact-inventory.md` | R131 public artifact inventory for v0.5 package review |
| `release/current/v0.5-remote-publication-decision-required.md` | R131 decision gate before remote publication |
| `release/fresh-clone-checks/r131-local-v0.5-release-preflight-validation.md` | R131 local v0.5 release preflight validation |
| `evals/palbench/v0.5/r131-v0.5-release-preflight-evidence-review.md` | R131 release preflight evidence review eval |
| `release/integration-notes/r131-r132-readiness-decision.md` | R131 readiness decision for explicit R132 publication choice |
| `docs/00-overview/faye-delivery-pack-deep-conductor-overview.md` | R133 overview for Faye, Delivery Packs, examples, and Deep Conductor governance |
| `standards/faye-delivery-pal/faye-ai-delivery-pal-standard.md` | R132-A Faye / AI Delivery Pal standard |
| `standards/faye-delivery-pal/delivery-pack-standard.md` | R132-A Delivery Pack standard |
| `standards/faye-delivery-pal/faye-palsmith-handoff-standard.md` | R132-A Faye to PalSmith handoff standard |
| `templates/delivery-pack/base-delivery-pack/` | R132-A base Delivery Pack template |
| `examples/delivery-packs/base-faye-delivery-pack-example/` | R132-A public-safe Faye Delivery Pack example shell |
| `examples/delivery-packs/video-growth-delivery-pack/` | R132-B near-runnable video growth Delivery Pack example |
| `examples/delivery-packs/sales-crm-delivery-pack/` | R132-C near-runnable sales CRM Delivery Pack example |
| `standards/deep-conductor/faye-deep-conductor-protocol.md` | R132-D Faye Deep Conductor no-code protocol |
| `standards/deep-conductor/delivery-pack-governance-loop.md` | R132-D Delivery Pack governance loop protocol |
| `standards/deep-conductor/context-access-list-for-delivery-pack.md` | R132-D Context Access List standard for Delivery Packs |
| `templates/deep-conductor/` | R132-D Deep Conductor templates |
| `examples/deep-conductor/` | R132-D public-safe Deep Conductor examples |
| `evals/palbench/faye-delivery/r132a-faye-delivery-pal-standard-boundary.md` | R132-A boundary eval |
| `evals/palbench/faye-delivery/r132b-video-growth-delivery-pack-boundary.md` | R132-B boundary eval |
| `evals/palbench/faye-delivery/r132c-sales-crm-delivery-pack-boundary.md` | R132-C boundary eval |
| `evals/palbench/deep-conductor/r132d-faye-deep-conductor-boundary.md` | R132-D boundary eval |
| `release/fresh-clone-checks/r132a-local-faye-delivery-pal-standard-validation.md` | R132-A local validation |
| `release/fresh-clone-checks/r132b-local-video-growth-delivery-pack-validation.md` | R132-B local validation |
| `release/fresh-clone-checks/r132c-local-sales-crm-delivery-pack-validation.md` | R132-C local validation |
| `release/fresh-clone-checks/r132d-local-faye-deep-conductor-validation.md` | R132-D local validation |
| `release/integration-notes/r133-r132-faye-delivery-integration-summary.md` | R133 R132 parallel-result integration summary |
| `evals/palbench/faye-delivery/r133-faye-delivery-integration-boundary.md` | R133 Faye Delivery integration boundary eval |
| `release/fresh-clone-checks/r133-local-faye-delivery-integration-validation.md` | R133 local integration validation |
| `release/integration-notes/r133-r134-readiness-decision.md` | R133 readiness decision for R134 review gate |
| `release/integration-notes/r134-faye-delivery-pack-review-issues.md` | R134 Faye Delivery Pack review issue table and safe fix record |
| `release/fresh-clone-checks/r134-local-faye-delivery-pack-review-gate-validation.md` | R134 local review-gate validation |
| `release/integration-notes/r134-r135-readiness-decision.md` | R134 readiness decision for R135 scope integration |
| `release/current/v0.5-faye-extension-scope-update.md` | R135 v0.5 Faye extension scope update |
| `release/current/v0.5-completion-status-after-faye-extension.md` | R135 v0.5 completion status after Faye extension |
| `release/current/v0.5-faye-extension-evidence-index.md` | R135 Faye extension evidence index |
| `evals/palbench/v0.5/r135-r136-faye-extension-targeted-regression-plan.md` | R135 R136 targeted regression plan for Faye extension |
| `evals/palbench/v0.5/r135-r136-faye-extension-targeted-regression-matrix.md` | R135 R136 eight-group targeted regression matrix |
| `release/integration-notes/r135-r136-faye-extension-regression-execution-checklist.md` | R135 R136 execution checklist |
| `release/fresh-clone-checks/r135-local-faye-extension-scope-update-validation.md` | R135 local scope-update validation |
| `release/integration-notes/r135-r136-readiness-decision.md` | R135 readiness decision for R136 targeted regression |
| `evals/palbench/v0.5/r136-faye-extension-targeted-regression-results.md` | R136 executed Faye extension targeted regression results |
| `evals/palbench/v0.5/r136-faye-extension-targeted-regression-issues.md` | R136 Faye extension targeted regression issue table |
| `release/fresh-clone-checks/r136-local-faye-extension-targeted-regression-validation.md` | R136 local targeted regression validation |
| `release/integration-notes/r136-r137-readiness-decision.md` | R136 readiness decision for R137 completion refresh |
| `release/current/v0.5-local-completion-report-after-faye-extension.md` | R137 refreshed v0.5 local completion report after Faye extension |
| `release/current/v0.5-local-completion-evidence-index-after-faye-extension.md` | R137 refreshed v0.5 completion evidence index after Faye extension |
| `release/current/v0.5-local-release-preflight-after-faye-extension.md` | R137 refreshed local-only release preflight after Faye extension |
| `release/current/v0.5-public-package-checklist-after-faye-extension.md` | R137 refreshed public package checklist after Faye extension |
| `release/current/v0.5-release-notes-draft-after-faye-extension.md` | R137 refreshed draft release notes after Faye extension; not published release notes |
| `release/fresh-clone-checks/r137-local-v0.5-completion-refresh-after-faye-extension-validation.md` | R137 local validation for refreshed completion after Faye extension |
| `evals/palbench/v0.5/r137-v0.5-completion-refresh-evidence-review.md` | R137 completion-refresh evidence review eval |
| `release/integration-notes/r137-r138-readiness-decision.md` | R137 readiness decision for final local release preflight after Faye extension |
| `release/current/v0.5-final-local-release-preflight-after-faye-extension.md` | R138 final local release preflight after Faye extension |
| `release/current/v0.5-final-public-package-readiness-review.md` | R138 final public package readiness review |
| `release/fresh-clone-checks/r138-final-local-release-blocker-scan.md` | R138 final local release blocker scan |
| `evals/palbench/v0.5/r138-final-local-release-preflight-evidence-review.md` | R138 final local release preflight evidence review |
| `release/fresh-clone-checks/r138-local-final-release-preflight-after-faye-extension-validation.md` | R138 local final release preflight validation after Faye extension |
| `release/current/v0.5-final-local-release-status.md` | R138 final local release status note |
| `release/integration-notes/r138-r139-readiness-decision.md` | R138 readiness decision for user choice in R139 |
| `START_HERE.md` | R139 fresh-clone onboarding entry |
| `docs/00-overview/what-is-agentpal.md` | R139 concise what-is overview |
| `docs/01-getting-started/first-30-minutes.md` | R139 first 30 minutes guide |
| `examples/walkthroughs/first-agentpal-team/` | R139 public-safe first AgentPal team walkthrough |
| `release/current/v0.5-fresh-clone-usability-checklist.md` | R139 fresh-clone usability checklist |
| `docs/00-overview/glossary.md` | R139 glossary |
| `docs/01-getting-started/faq.md` | R139 FAQ |
| `release/fresh-clone-checks/r139-local-new-user-onboarding-validation.md` | R139 local onboarding validation |
| `evals/palbench/v0.5/r139-new-user-onboarding-evidence-review.md` | R139 onboarding evidence review |
| `release/integration-notes/r139-r140-readiness-decision.md` | R139 readiness decision for fresh-clone usability simulation |
| `release/fresh-clone-checks/r140-fresh-clone-usability-simulation-setup.md` | R140 clean-copy usability simulation setup |
| `evals/palbench/v0.5/r140-start-here-walkthrough-results.md` | R140 START_HERE walkthrough result |
| `evals/palbench/v0.5/r140-first-30-minutes-walkthrough-results.md` | R140 first-30-minutes walkthrough result |
| `evals/palbench/v0.5/r140-first-agentpal-team-walkthrough-results.md` | R140 first AgentPal team walkthrough result |
| `evals/palbench/v0.5/r140-fresh-clone-usability-issues.md` | R140 fresh-clone usability issue summary |
| `release/fresh-clone-checks/r140-local-fresh-clone-usability-validation.md` | R140 local fresh-clone usability validation |
| `evals/palbench/v0.5/r140-fresh-clone-usability-evidence-review.md` | R140 fresh-clone usability evidence review |
| `release/integration-notes/r140-r141-readiness-decision.md` | R140 readiness decision for user remote-publication decision |
| `evals/palbench/v0.5/r141-v0.5-core-capability-inventory.md` | R141 v0.5 core capability inventory |
| `evals/palbench/v0.5/r141-official-pal-readiness-matrix.md` | R141 official Pal readiness matrix |
| `evals/palbench/v0.5/r141-faye-readiness-note.md` | R141 Faye readiness note |
| `release/current/v0.5-completeness-scorecard.md` | R141 v0.5 completeness scorecard |
| `evals/palbench/v0.5/r141-full-usable-core-test-coverage-map.md` | R141 full usable-core test coverage map |
| `release/current/v0.5-release-readiness-interpretation.md` | R141 release readiness interpretation |
| `release/fresh-clone-checks/r141-local-core-capability-pal-readiness-audit-validation.md` | R141 local core capability / Pal readiness audit validation |
| `release/integration-notes/r141-r142-readiness-decision.md` | R141 readiness decision for R142 full usable-core test |
| `evals/palbench/v0.5/r142-pal-behavior-deep-conductor-full-test-plan.md` | R142 behavior / Deep Conductor full test design plan |
| `evals/palbench/v0.5/r142-pal-conversation-asset-use-test-matrix.md` | R142 Pal conversation and asset-use test matrix |
| `evals/palbench/v0.5/r142-capability-inventory-agent-model-skill-test-matrix.md` | R142 capability inventory / Agent / model / Skill / plugin matrix |
| `evals/palbench/v0.5/r142-memory-knowledge-skill-workflow-writeback-test-matrix.md` | R142 memory / knowledge / Skill / workflow writeback matrix |
| `evals/palbench/v0.5/r142-deep-conductor-decision-test-matrix.md` | R142 Deep Conductor decision test matrix |
| `evals/palbench/v0.5/r142-end-to-end-human-use-scenarios.md` | R142 end-to-end human-use scenario design |
| `evals/palbench/v0.5/r142-behavior-test-scoring-rubric.md` | R142 behavior test scoring rubric |
| `release/integration-notes/r142-r143-to-r146-behavior-test-execution-plan.md` | R142 staged behavior test execution plan for R143-R146 |
| `release/fresh-clone-checks/r142-local-pal-behavior-deep-conductor-test-design-validation.md` | R142 local behavior test design validation |
| `release/integration-notes/r142-r143-readiness-decision.md` | R142 readiness decision for R143 Mira / PalSmith / Faye behavior tests |
| `evals/palbench/v0.5/behavior/r143-mira-auto-behavior-results.md` | R143 executed Mira core entry behavior test results |
| `evals/palbench/v0.5/behavior/r143-palsmith-auto-behavior-results.md` | R143 executed PalSmith core entry behavior test results |
| `evals/palbench/v0.5/behavior/r143-faye-auto-behavior-results.md` | R143 executed Faye role/workflow behavior test results |
| `evals/palbench/v0.5/behavior/r143-mira-palsmith-faye-auto-behavior-summary.md` | R143 Mira / PalSmith / Faye behavior test summary |
| `evals/palbench/v0.5/behavior/r143-mira-palsmith-faye-auto-behavior-issues.md` | R143 Mira / PalSmith / Faye behavior issue table |
| `release/fresh-clone-checks/r143-local-mira-palsmith-faye-auto-behavior-validation.md` | R143 local validation for Mira / PalSmith / Faye auto behavior tests |
| `release/integration-notes/r143-r144-readiness-decision.md` | R143 readiness decision for R144 official Pal asset behavior tests |
| `evals/palbench/v0.5/behavior/r144-official-pal-asset-results/` | R144 executed official Pal asset behavior result files |
| `evals/palbench/v0.5/behavior/r144-official-pal-asset-behavior-summary.md` | R144 official Pal asset behavior test summary |
| `evals/palbench/v0.5/behavior/r144-official-pal-asset-behavior-issues.md` | R144 official Pal asset behavior issue table |
| `release/fresh-clone-checks/r144-local-official-pal-asset-behavior-validation.md` | R144 local validation for official Pal asset behavior tests |
| `release/integration-notes/r144-r145-readiness-decision.md` | R144 readiness decision for R145 capability writeback behavior tests |
| `evals/palbench/v0.5/behavior/r145-capability-agent-model-skill-results.md` | R145 capability / Agent / model / Skill / plugin behavior test results |
| `evals/palbench/v0.5/behavior/r145-writeback-classification-results.md` | R145 writeback classification behavior test results |
| `evals/palbench/v0.5/behavior/r145-capability-writeback-regression-results.md` | R145 capability / writeback regression behavior test results |
| `evals/palbench/v0.5/behavior/r145-capability-writeback-behavior-summary.md` | R145 capability / writeback behavior test summary |
| `evals/palbench/v0.5/behavior/r145-capability-writeback-behavior-issues.md` | R145 capability / writeback behavior issue table |
| `release/fresh-clone-checks/r145-local-capability-writeback-behavior-validation.md` | R145 local validation for capability / writeback behavior tests |
| `release/integration-notes/r145-r146-readiness-decision.md` | R145 readiness decision for R146 Deep Conductor E2E behavior tests |
| `evals/palbench/v0.5/behavior/r146-deep-conductor-mode-decision-results.md` | R146 Deep Conductor mode decision behavior test results |
| `evals/palbench/v0.5/behavior/r146-context-task-governance-verification-results.md` | R146 Context Packet / Task Package / Governance / Verification behavior test results |
| `evals/palbench/v0.5/behavior/r146-end-to-end-human-use-results.md` | R146 end-to-end human-use behavior test results |
| `evals/palbench/v0.5/behavior/r146-deep-conductor-e2e-behavior-summary.md` | R146 Deep Conductor / E2E behavior test summary |
| `evals/palbench/v0.5/behavior/r146-deep-conductor-e2e-behavior-issues.md` | R146 Deep Conductor / E2E behavior issue table |
| `release/fresh-clone-checks/r146-local-deep-conductor-e2e-behavior-validation.md` | R146 local validation for Deep Conductor / E2E behavior tests |
| `release/integration-notes/r146-r147-readiness-decision.md` | R146 readiness decision for R147 automatic test summary and fix decision |
| `evals/palbench/v0.5/behavior/r147-auto-behavior-test-summary.md` | R147 automatic behavior test summary across R142-R146 |
| `evals/palbench/v0.5/behavior/r147-auto-behavior-test-issue-rollup.md` | R147 automatic behavior test issue rollup and R148 input |
| `release/integration-notes/r147-auto-test-fix-decision.md` | R147 decision on whether an R148 targeted fix round is required |
| `release/fresh-clone-checks/r147-local-auto-test-summary-validation.md` | R147 local validation for automatic test summary and fix decision |
| `release/integration-notes/r147-r149-readiness-decision.md` | R147 readiness decision for R149 manual test plan preparation |

## R101 Integration

| Path | Purpose |
| --- | --- |
| `release/integration-notes/r101-official-pal-upgrade-gate-freeze.md` | R101 frozen preflight gate for official Pal metadata upgrades |
| `release/integration-notes/r101-next-official-pal-index-backfill-candidate.md` | R101 next safe official Pal index backfill candidate |
| `evals/palbench/pal-asset/r101-pal-metadata-v0.5-integration-boundary.md` | R101 Pal Metadata v0.5 integration boundary eval |
| `release/fresh-clone-checks/r101-r100-parallel-integration-validation.md` | R101 R100 parallel integration validation |

| `docs/05-orchestration-methodology/deep-conductor-master-goal.md` | Deep Conductor master goal and no-code 12-step loop |
| `docs/05-orchestration-methodology/deep-conductor-master-loop-usage-guide.md` | Deep Conductor usage guide for project-level no-code coordination |
| `docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md` | Deep Conductor E2E usage guide for integrated no-code project-level closure |
| `docs/09-roadmap/v0.3-deep-conductor-readiness.md` | v0.3 Deep Conductor readiness assessment for rc.1 preparation |
| `docs/09-roadmap/v0.3-public-capability-summary.md` | public-safe v0.3 capability summary |
| `docs/09-roadmap/v0.3-release-checklist.md` | v0.3 release preparation checklist |
| `docs/09-roadmap/v0.3-release-preparation-audit.md` | R64 release preparation audit |
| `evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md` | v0.3 integration readiness matrix |
| `docs/05-orchestration-methodology/cross-runtime-pal-memory.md` | Cross-Runtime Pal Memory guide for preserving Pal/project/routing continuity across host Runtimes |
| `docs/05-orchestration-methodology/token-cost-aware-deep-conductor.md` | Token / Cost-aware Deep Conductor guide for qualitative Context Budget planning |
| `docs/05-orchestration-methodology/00-methodology-overview.md` | current methodology overview |
| `docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md` | Pal Team and future Deep Conductor relationship |
| `docs/06-validation-and-evidence/README.md` | current validation and PalBench entry |
| `docs/06-validation-and-evidence/01-palbench-small-sample-report.md` | current R33 PalBench small-sample report |
| `docs/06-validation-and-evidence/05-future-palbench-design.md` | current future PalBench design notes |
| `docs/08-release-candidate/README.md` | historical release-candidate pointer |
| `archive/migration-from-v0.3/release-candidate-docs/02-release-manifest.md` | historical release-candidate manifest |
| `docs/research/README.md` | archive status note; not a primary docs entry |
| `docs/research/archive/` | historical research notes retained for traceability |
| `orchestration/fast-route-protocol.md` | current Simple Pal Mode clear-task handoff pattern |
| `orchestration/deep-conductor-protocol.md` | no-code Deep Conductor complex-workflow pattern |
| `orchestration/project-conductor-workflow.md` | project-level no-code conductor workflow |
| `orchestration/subagent-external-agent-handoff-boundary.md` | no-code boundary for host Runtime subagent / external Agent handoff packages |
| `orchestration/memory-boundary-protocol.md` | memory sharing, privacy, Git, Context Packet, and runtime-switch boundary |
| `orchestration/pal-skill-vs-runtime-skill-protocol.md` | Pal-owned Skill and Runtime-installed Skill separation |
| `orchestration/runtime-skill-candidate-decision-protocol.md` | Runtime Skill candidate decision, availability, fallback, verification, and usage memory protocol |
| `orchestration/token-cost-aware-conductor-policy.md` | token, cost, context, profile, memory, model, and verification policy |
| `orchestration/context-budget-protocol.md` | qualitative Context Budget Plan, read tiers, escalation, stop / ask-user conditions, and usage reporting |
| `orchestration/prompt-shaping-by-model-and-reasoning.md` | no-code prompt shaping guidance for strong, medium, and economy / weak model or reasoning candidates |
| `workspace/organization/memory/runtime/cross-runtime-pal-memory-protocol.md` | cross-runtime Pal memory continuity protocol |
| `orchestration/capability-inventory-protocol.md` | runtime/model/skill/plugin/MCP/Pal profile design |
| `orchestration/task-judgement-protocol.md` | structured task judgement design |
| `orchestration/workflow-topology-protocol.md` | workflow topology design and v0.1/future boundary |
| `orchestration/context-access-list-protocol.md` | context access list design |
| `orchestration/context-packet-protocol.md` | v0.3 Context Packet handoff protocol |
| `orchestration/mention-and-direct-pal-protocol.md` | v0.3 `/pal Name` and `@Pal` collaboration protocol |
| `orchestration/owner-verifier-workflow-protocol.md` | v0.3 Owner + Verifier staged workflow |
| `orchestration/parallel-independent-review-protocol.md` | v0.3 isolated independent review workflow |
| `orchestration/plan-execute-verify-protocol.md` | v0.3 Plan -> Execute -> Verify staged workflow |
| `orchestration/routing-memory-writeback-protocol.md` | v0.3 manual routing memory writeback protocol |
| `orchestration/pal-isolation-and-shared-memory-protocol.md` | isolation and shared memory design |
| `orchestration/routing-reward-memory-protocol.md` | routing outcome memory design |
| `standards/capability-inventory/` | capability profile standards and matrices |
| `workspace/organization/capability-inventory/` | current organization capability records |
| `workspace/projects/_template/capability-inventory/` | project capability record template, not real project data |
| `examples/capability-inventory/` | capability profile examples |
| `templates/capability-inventory/` | capability profile JSON templates |
| `templates/capability-inventory/business-system-profile-template.json` | Business System profile template |
| `docs/03-user-guides/manual-capability-profile.md` | manual no-code profile creation guide |
| `evals/palbench/capability-inventory/r82-manual-profile-guide-compliance.md` | Manual Profile Guide compliance regression |
| `archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/` | archived R78 capability inventory root pointers |
| `templates/orchestration/` | task judgement, workflow, access list, project conductor task map, Deep Conductor plan, next-round runtime package, cross-runtime continuation package, conductor decision record, Runtime Skill-aware task package, context budget plan, context usage report, verifier context packet, reviewer context packet, final report, synthesis, result record, routing, and verification templates |
| `templates/orchestration/deep-conductor-e2e-package.md` | complete Deep Conductor E2E package template |
| `templates/orchestration/deep-conductor-e2e-synthesis-report.md` | complete Deep Conductor E2E synthesis report template |
| `templates/orchestration/e2e-user-facing-short-summary.md` | short user-facing summary for E2E synthesis |
| `templates/orchestration/external-agent-handoff-package.md` | manual external Agent handoff package template |
| `templates/orchestration/subagent-task-package.md` | host Runtime subagent task package template |
| `templates/memory/` | Pal Project Memory Snapshot, Routing Memory Record, and Runtime Skill Usage Memory Record templates |
| `templates/capability-inventory/` | capability profile JSON templates under the templates tree, not a facts source |
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
| `examples/runtime-adapters/README.md` | runtime adapter and thin-binding examples navigation |
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
| `docs/02-concepts/central-project-record.md` | central project record concept |
| `docs/02-concepts/project-memory-in-agentpal.md` | project memory boundary |
| `docs/02-concepts/source-map-and-derived-knowledge.md` | source-map and derived-knowledge boundary |
| `docs/01-getting-started/bind-external-project.md` | external project binding quick start |
| `docs/03-user-guides/project-memory.md` | project memory user guide |
| `docs/03-user-guides/project-usage-memory-boundary.md` | project usage memory boundary guide |
| `docs/03-user-guides/using-user-project-docs.md` | user project docs to central records guide |
| `standards/capability-inventory/business-system-profile-review-flow.md` | Business System profile review flow standard |
| `templates/capability-inventory/business-system-profile-review-packet.md` | Business System profile review packet template |
| `workspace/projects/_template/` | central project record template |
| `examples/project-records/business-system-profile-references/` | public-safe central project record examples; not real project records |
| `evals/runtime-adapters/runtime-adapter-regression-suite.md` | 12-scenario Runtime Adapter regression suite |
| `evals/palbench/project-binding/r93c-thin-binding-simulation-results.md` | R93-C thin-binding simulation result for generic Codex and Claude Code templates |
| `examples/failures/runtime-opened-in-wrong-directory.md` | failure example for wrong working directory |
| `examples/failures/stale-pal-list-after-agentpal-update.md` | failure example for stale Pal list |
| `examples/failures/claude-settings-local-not-refreshed.md` | failure example for Claude Code session refresh |
| `examples/failures/active-project-root-confused-with-agentpal-root.md` | failure example for root confusion |

## Mira Conductor References

| Path | Purpose |
| --- | --- |
| `official/pals/Mira-main/PAL.md` | Mira Main Pal / Leader Pal / Conductor identity |
| `official/pals/Mira-main/AGENTS.md` | Mira runtime instructions |
| `official/pals/Mira-main/SKILL.md` | Mira Pal Pack skill entry |
| `official/pals/Mira-main/core/output-contract.md` | Mira output shapes, Fast Route, CAL, Task Package, and future-design boundaries |

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
