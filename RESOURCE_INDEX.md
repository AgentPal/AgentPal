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
| `evals/palbench/v0.5/documentation/archive/docs/08-release-and-maintenance/v0.4-local-completion-summary.md` | archived v0.4 local completion summary | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.5-local-development-scope.md` | archived v0.5 local development scope freeze | evidence/history lookup |
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
| `docs/release/v0.5-release-candidate-preflight.md` | local v0.5 release candidate preflight | user-authorized release decision; not release completion |
| `docs/release/v0.5-user-authorization-decision.md` | local v0.5 user authorization decision | choose push / tag / GitHub Release scope; not release execution |
| `docs/release/v0.5-release-notes-draft.md` | draft v0.5 release notes | user review before release publication; not published release notes |
| `docs/release/v0.5-release-readiness-checklist.md` | R211 v0.5 release readiness checklist | release package preparation checks; not remote authorization |
| `docs/release/v0.5-known-limits.md` | R211 v0.5 known limits | release package boundary notes |
| `docs/release/v0.5-release-authorization-decision.md` | R211 v0.5 release authorization decision | ready_with_notes for release package preparation only |
| `docs/release/v0.5-release-package-manifest.md` | R212 v0.5 release package manifest | local release package contents and exclusions |
| `docs/release/v0.5-release-notes.md` | R212 final prepared v0.5 release notes | local final release notes; not published |
| `docs/release/v0.5-release-preflight-checklist.md` | R212 v0.5 release preflight checklist | local preflight before any user-authorized remote operation |
| `docs/release/v0.5-remote-operation-authorization-guide.md` | R212 remote operation authorization guide | future push/tag/release authorization boundary |
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
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/` | archived roadmap and task pool docs | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.2-release-readiness.md` | archived v0.2 release readiness assessment | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.2-public-capability-summary.md` | archived v0.2 public capability summary | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/no-code-future-boundary.md` | archived no-code future boundary | evidence/history lookup |
| `docs/00-overview/capability-inventory-migration-plan.md` | capability/runtime/model/plugin migration plan | R77 high-risk reference directory planning |
| `docs/00-overview/orchestration-migration-plan.md` | orchestration migration plan | R77 high-risk protocol surface planning |
| `docs/00-overview/prompts-migration-plan.md` | prompts migration plan | R77 copyable prompt family planning |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-development-plan.md` | archived v0.3 no-code orchestration prototype plan | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-task-pool.md` | archived v0.3 execution task pool | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-deep-conductor-readiness.md` | archived v0.3 Deep Conductor readiness | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-public-capability-summary.md` | archived v0.3 public capability summary | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-release-checklist.md` | archived v0.3 release preparation checklist | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-release-preparation-audit.md` | archived v0.3 release preparation audit | evidence/history lookup |
| `evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md` | v0.3 Deep Conductor integration matrix | integrated pass / partial / unavailable readiness matrix |
| `docs/05-orchestration-methodology/deep-conductor-master-goal.md` | Deep Conductor master goal | no-code 12-step conductor loop and executor boundary |
| `docs/05-orchestration-methodology/deep-conductor-master-loop-usage-guide.md` | Deep Conductor master loop usage guide | project goal to task map, Runtime packages, verification, synthesis, and memory writeback |
| `docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md` | Deep Conductor E2E usage guide | full no-code loop from goal through memory, capability, context budget, topology, Runtime Skill-aware packages, verification, synthesis, routing memory, and next-round recommendation |
| `evals/palbench/v0.5/documentation/archive/docs/research/deep-conductor-real-runtime-replay-gap-analysis.md` | archived Deep Conductor real replay gap analysis | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/research/deep-conductor-real-runtime-replay-report.md` | archived Deep Conductor real Runtime replay report | evidence/history lookup |
| `docs/05-orchestration-methodology/cross-runtime-pal-memory.md` | Cross-Runtime Pal Memory usage guide | no-code continuity across Codex, Claude Code, generic CLI, and other host Runtimes |
| `docs/05-orchestration-methodology/runtime-installed-skill-orchestration-guide.md` | Runtime-installed Skill Orchestration guide | no-code Runtime Skill candidate selection, availability checks, fallback, verification, and usage memory |
| `docs/05-orchestration-methodology/token-cost-aware-deep-conductor.md` | Token / Cost-aware Deep Conductor guide | no-code Context Budget, read tier, prompt shaping, verification cost, and usage report guidance |
| `docs/05-orchestration-methodology/context-packet-usage-guide.md` | Context Packet usage guide | user and maintainer guide for `/pal`, `@Pal`, consult, handoff, review, owner transfer, privacy, and runtime adapter usage |
| `docs/05-orchestration-methodology/owner-verifier-usage-guide.md` | Owner + Verifier usage guide | no-code owner/verifier workflow, independent evidence context, result records, and repair package guidance |
| `docs/05-orchestration-methodology/parallel-independent-review-usage-guide.md` | Parallel Independent Review usage guide | no-code isolated reviewer workflow, reviewer packets, final reports, synthesis, and group-chat collapse prevention |
| `docs/02-getting-started/multi-pal-collaboration-prompt-cards.md` | Multi-Pal prompt cards | copyable user prompts for Mira, `/pal`, `@Pal`, Context Packet, review, handoff, and summary paths |
| `evals/v0.2-integration/v0.2-integration-test-matrix.md` | v0.2 integration matrix | R46 integrated readiness test matrix |
| `docs/06-palsmith/README.md` | PalSmith v0.5 user index | PalSmith creation, Pal Team design, Task Package, and governance work |
| `docs/06-palsmith/palsmith-v05-user-flow.md` | PalSmith v0.5 user flow | external user path for creation, draft, custom Pal, authorization, revocation, and review |
| `docs/06-palsmith/palsmith-v05-capability-summary.md` | PalSmith v0.5 capability summary | PalSmith v0.5 capability and readiness summary |
| `docs/06-palsmith/palsmith-pal-completeness-guide.md` | PalSmith Pal completeness guide | persona seed to verified executable Pal readiness ladder |
| `docs/06-palsmith/existing-pal-upgrade-asset-execution-guide.md` | Existing Pal upgrade asset execution guide | plan-first upgrade boundary and asset execution evidence |
| `docs/07-pal-asset-execution/official-pal-adoption-spot-check.md` | Official Pal adoption spot-check | R202 official Pal Asset Execution adoption route and limits |
| `docs/06-palsmith/palsmith-v05-release-prep.md` | PalSmith v0.5 release prep | local release-preparation scope and publication boundary |
| `docs/06-palsmith/palsmith-v05-known-limits.md` | PalSmith v0.5 known limits | current limits for user custom Pal discovery, runtime, evidence, and publication claims |
| `docs/06-palsmith/palsmith-v05-release-checklist.md` | PalSmith v0.5 release checklist | local checks before remote authorization decisions |
| `docs/06-palsmith/palsmith-end-to-end-productization.md` | PalSmith v0.5 end-to-end user path | PalSmith creation and Pal Team productization work |
| `official/pals/PalSmith-pal-governor/templates/task-packages/create-first-professional-pal.md` | Copyable first professional Pal creation task package | PalSmith single-Pal creation work |
| `official/pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md` | Copyable AI team creation task package | PalSmith Pal Team creation work |
| `official/pals/PalSmith-pal-governor/runbooks/pal-health-check.md` | Pal health check runbook | PalSmith creation and repair checks |
| `official/pals/PalSmith-pal-governor/runbooks/ai-team-health-check.md` | AI team health check runbook | PalSmith team readiness checks |
| `docs/02-getting-started/mira-first-usage.md` | Mira-first user path | onboarding and daily-use examples |
| `docs/02-getting-started/mira-first-prompt-cards.md` | Copyable Mira-first prompts | daily user prompts and direct `/pal Name` guidance |
| `official/pals/Mira-main/templates/task-packages/mira-first-task-intake.md` | Mira ordinary task intake template | Mira-first task organization |
| `official/pals/Mira-main/templates/task-packages/mira-composite-deliverable-task-package.md` | Mira composite deliverable template | staged Task Package creation |
| `official/pals/Mira-main/templates/task-packages/mira-owner-judgement-summary.md` | Mira owner judgement summary template | explaining Pal candidates and override paths |
| `official/pals/Mira-main/templates/task-packages/mira-runtime-brief.md` | Mira runtime brief template | Codex / Claude Code / generic CLI execution handoff |
| `official/pals/Mira-main/examples/mira-runtime-brief-example.md` | Mira runtime brief example | execution-layer evidence and project boundary example |
| `official/pals/Mira-main/evals/mira-first-usage-self-test.md` | Mira-first self-test | ordinary, composite, direct Pal, and release-check regression |
| `docs/07-official-pals/official-pal-examples-index.md` | Official 10 Pal real task examples index | official Pal examples and v0.5 navigation |
| `docs/07-official-pals/official-pal-example-library-plan.md` | Official Pal example library plan | official 10 Pal examples planning and boundary rules |
| `docs/07-pal-asset-execution/README.md` | Pal Asset Execution adoption guide | user-readable guide for asset-grounded Pal work |
| `docs/07-pal-asset-execution/scoped-certification-plan.md` | Scoped Pal Asset Execution certification plan | certification levels, evidence gates, and R209 planning |
| `docs/07-pal-asset-execution/scoped-certification-checklist.md` | Scoped certification checklist | copyable checklist for Pal plus task-family certification review |
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
| `evals/palbench/v0.5/documentation/archive/docs/research/palbench-light-suite-plan.md` | archived PalBench Light suite plan | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/research/palbench-collaboration-suite-plan.md` | archived PalBench Collaboration suite plan | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/research/palbench-collaboration-coverage-audit.md` | archived PalBench Collaboration coverage audit | evidence/history lookup |
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
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.2-release-readiness.md` | v0.2 release readiness assessment | R46 integrated readiness conclusion |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.2-public-capability-summary.md` | v0.2 public capability summary | public-safe capability summary |
| `evals/v0.2-integration/v0.2-integration-test-matrix.md` | v0.2 integration matrix | first-phase integration test matrix |
| `docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md` | Pal Team, runtime-layer agent execution, and future Deep Conductor boundaries | Pal Team and orchestration questions |
| `evals/palbench/v0.5/documentation/archive/docs/06-validation-and-evidence/` | archived PalBench and evidence interpretation docs | evidence/history lookup |
| `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/README.md` | archived historical release-candidate pointer | evidence/history lookup |
| `archive/migration-from-v0.3/release-candidate-docs/` | historical v0.3 release-candidate documents | historical traceability only |
| `evals/palbench/v0.5/documentation/archive/docs/research/` | archived research notes | historical traceability only; not a primary entry point |
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
| `prompts/cli-agent/README.md` | compatibility entry for CLI Agent prompts, pointing to generic CLI Agent prompts |
| `prompts/generic-cli-agent/install-agentpal-current-project.md` | one-prompt generic CLI Agent project install |
| `prompts/generic-cli-agent/remove-agentpal-current-project.md` | remove generic CLI Agent project binding |
| `prompts/test-codex-subagent-mode.md` | diagnostic prompt for Codex child workflow availability; not evidence of automatic subagent execution |

These prompts are Markdown instructions, not scripts or installers.

## Official Pal Packs

Official Pal Packs for current v0.5 local pre-manual readiness:

- `official/pals/Mira-main`
- `official/pals/Atlas-developer`
- `official/pals/Vega-research`
- `official/pals/Rhea-system`
- `official/pals/PalSmith-pal-governor`
- `official/pals/Quinn-quality`
- `official/pals/Morgan-document`
- `official/pals/Harper-writing`
- `official/pals/Nova-product`
- `official/pals/Faye-delivery`

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
| `evals/palbench/v0.5/documentation/archive/docs/08-release-and-maintenance/v0.4-local-completion-summary.md` | R96 user-facing v0.4 local completion summary |
| `evals/palbench/v0.4/r96-v0.4-completion-evidence-review.md` | R96 evidence review for v0.4 local completion |
| `release/fresh-clone-checks/r96-v0.4-local-completion-validation.md` | R96 local completion validation record |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.5-local-development-scope.md` | R97 v0.5 local development scope and no-code boundary freeze |
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
| `core/pal-asset-execution-contract.md` | R198 global no-code Pal Asset Execution Contract |
| `core/asset-loading-gate.md` | R198 global Asset Loading Gate |
| `templates/pal/task-asset-packet.md` | R198 Task Asset Packet template |
| `templates/pal/asset-use-summary.md` | R198 Asset Use Summary template |
| `templates/pal/missing-asset-plan.md` | R198 Missing Asset Plan template |
| `templates/pal/scoped-certification-record.md` | R208 scoped certification record template |
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
| `official/pals/PalSmith-pal-governor/core/composite-pal-distillation-protocol.md` | R168 PalSmith composite Pal creation protocol |
| `official/pals/PalSmith-pal-governor/core/existing-pal-composite-upgrade-protocol.md` | R196 existing Pal composite upgrade protocol using AI judgement, not keyword routing |
| `official/pals/PalSmith-pal-governor/core/custom-pal-installation-protocol.md` | R179 PalSmith draft-to-user-custom Pal installation protocol |
| `official/pals/PalSmith-pal-governor/core/user-custom-pal-discovery-authorization-protocol.md` | R185 user custom Pal discovery authorization protocol |
| `official/pals/PalSmith-pal-governor/skills/composite-pal-distillation-skill.md` | R168 PalSmith composite Pal distillation Skill |
| `official/pals/PalSmith-pal-governor/templates/composite-pal-creation-plan.md` | R168 composite Pal creation plan template |
| `official/pals/PalSmith-pal-governor/templates/existing-pal-composite-upgrade-plan.md` | R196 existing Pal composite upgrade plan template |
| `official/pals/PalSmith-pal-governor/evals/composite-pal-distillation-eval.md` | R168 composite Pal distillation eval |
| `official/pals/PalSmith-pal-governor/evals/existing-pal-composite-upgrade-eval.md` | R196 existing Pal composite upgrade AI judgement eval |
| `evals/palbench/v0.5/palsmith/r169-composite-creation-real-task-tests.md` | R169 PalSmith composite creation real-task test summary |
| `evals/palbench/v0.5/palsmith/r169-quinn-review.md` | R169 Quinn / QA review for PalSmith composite creation tests |
| `evals/palbench/v0.5/palsmith/r170-docs-and-examples-closure.md` | R170 PalSmith docs and examples closure evidence note |
| `evals/palbench/v0.5/palsmith/r171-palsmith-host-dialogue.md` | R171 PalSmith real host dialogue evidence |
| `evals/palbench/v0.5/palsmith/r171-quinn-host-review.md` | R171 Quinn host review evidence |
| `evals/palbench/v0.5/palsmith/r171-manual-host-acceptance-script.md` | R171 manual real-host acceptance script |
| `examples/palsmith/composite-pal-creation-examples.md` | R170 user-facing composite Pal creation examples |
| `prompts/palsmith/create-composite-pal.md` | R170 copyable PalSmith composite Pal creation prompt |
| `prompts/palsmith/upgrade-existing-pal-composite-distillation.md` | R196 copyable PalSmith existing Pal composite upgrade prompt |
| `prompts/palsmith/create-or-upgrade-pal-asset-execution.md` | R198 copyable PalSmith Pal asset execution readiness prompt |
| `docs/06-palsmith/palsmith-pal-completeness-guide.md` | R201 PalSmith completeness adoption guide |
| `docs/06-palsmith/existing-pal-upgrade-asset-execution-guide.md` | R201 existing Pal upgrade asset execution guide |
| `examples/palsmith/draft-to-custom-pal-installation-example.md` | R179 draft Pal Pack to user custom Pal installation example |
| `prompts/palsmith/install-draft-as-custom-pal.md` | R179 copyable PalSmith draft-to-custom installation prompt |
| `evals/palbench/v0.5/palsmith/draft-pal-packs/FirstPrinciplesProductReviewer/` | R174 non-official draft Pal Pack test artifact |
| `evals/palbench/v0.5/palsmith/r174-draft-pal-pack-creation.md` | R174 PalSmith draft Pal Pack creation evidence |
| `evals/palbench/v0.5/palsmith/r174-quinn-draft-pal-pack-review.md` | R174 draft Pal Pack file-level QA review |
| `evals/palbench/v0.5/palsmith/r175-draft-pal-pack-quality-regression.md` | R175 PalSmith draft Pal Pack quality regression and commit readiness evidence |
| `evals/palbench/v0.5/palsmith/r177-draft-pal-loading-regression.md` | R177 draft Pal loading and identity regression evidence |
| `evals/palbench/v0.5/palsmith/r177-draft-pal-product-review-task.md` | R177 draft Pal product review task evidence |
| `evals/palbench/v0.5/palsmith/r177-draft-pal-boundary-pressure-test.md` | R177 draft Pal boundary pressure test evidence |
| `evals/palbench/v0.5/palsmith/r177-quinn-draft-usage-review.md` | R177 Quinn read-only draft usage review |
| `evals/palbench/v0.5/palsmith/r177-draft-pal-usage-regression-summary.md` | R177 draft Pal usage regression summary |
| `evals/palbench/v0.5/palsmith/r179-draft-to-custom-pal-installation-flow.md` | R179 draft Pal Pack to user custom Pal no-code flow evidence |
| `workspace/resources/user-pals/README.md` | R181 local user custom Pal index |
| `workspace/resources/user-pals/FirstPrinciplesProductReviewer/` | R181 non-official user custom Pal test artifact |
| `evals/palbench/v0.5/palsmith/r181-palsmith-draft-to-custom-plan.md` | R181 PalSmith draft-to-custom enablement plan evidence |
| `evals/palbench/v0.5/palsmith/r181-draft-to-custom-install-result.md` | R181 draft-to-custom placement result evidence |
| `evals/palbench/v0.5/palsmith/r181-quinn-draft-to-custom-review.md` | R181 Quinn draft-to-custom file-level QA review |
| `evals/palbench/v0.5/palsmith/r181-draft-to-custom-real-host-summary.md` | R181 draft-to-custom real host rehearsal summary |
| `evals/palbench/v0.5/palsmith/r183-user-custom-pal-explicit-invocation.md` | R183 user custom Pal explicit invocation regression evidence |
| `evals/palbench/v0.5/palsmith/r183-discovery-refusal-regression.md` | R183 default discovery refusal regression evidence |
| `evals/palbench/v0.5/palsmith/r183-contacts-registration-refusal.md` | R183 central contacts registration refusal evidence |
| `evals/palbench/v0.5/palsmith/r183-unauthorized-delegation-refusal.md` | R183 unauthorized delegation refusal evidence |
| `evals/palbench/v0.5/palsmith/r183-quinn-user-custom-pal-discovery-review.md` | R183 Quinn review for user custom Pal invocation and discovery boundaries |
| `evals/palbench/v0.5/palsmith/r183-user-custom-pal-invocation-discovery-summary.md` | R183 user custom Pal invocation and discovery refusal summary |
| `docs/06-palsmith/user-custom-pal-discovery-authorization.md` | R185 user custom Pal discovery authorization user guide |
| `docs/06-palsmith/user-custom-pal-discovery-authorization-protocol.md` | R191 user-docs entry for the PalSmith user custom Pal authorization protocol |
| `prompts/palsmith/authorize-user-custom-pal-discovery.md` | R185 copyable PalSmith authorization prompt |
| `templates/palsmith/user-custom-pal-authorization-record.md` | R185 user custom Pal authorization record template |
| `templates/palsmith/user-custom-pal-discovery-policy.md` | R185 user custom Pal discovery policy template |
| `evals/palbench/v0.5/palsmith/r185-user-custom-pal-discovery-authorization-design.md` | R185 discovery authorization design evidence |
| `evals/palbench/v0.5/palsmith/r185-user-custom-pal-authorization-boundary-cases.md` | R185 authorization boundary cases evidence |
| `evals/palbench/v0.5/palsmith/r185-quinn-authorization-flow-review.md` | R185 Quinn review for user custom Pal authorization flow |
| `evals/palbench/v0.5/palsmith/r186-user-custom-pal-authorization-quality-regression.md` | R186 user custom Pal authorization quality regression |
| `evals/palbench/v0.5/palsmith/r186-authorization-boundary-pressure-tests.md` | R186 authorization boundary pressure tests |
| `evals/palbench/v0.5/palsmith/r186-quinn-authorization-regression-review.md` | R186 Quinn authorization regression review |
| `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-host-dialogue.md` | R188 real Codex host thread custom Pal authorization dialogue |
| `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-record-sample.md` | R188 custom Pal authorization and revocation record samples |
| `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-boundary-results.md` | R188 custom Pal authorization boundary results |
| `evals/palbench/v0.5/palsmith/r188-quinn-authorization-e2e-review.md` | R188 Quinn custom Pal authorization E2E review |
| `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-e2e-summary.md` | R188 custom Pal authorization E2E summary |
| `evals/palbench/v0.5/palsmith/r189-custom-pal-authorization-e2e-quality-regression.md` | R189 custom Pal authorization E2E quality regression |
| `evals/palbench/v0.5/palsmith/r189-quinn-custom-pal-authorization-e2e-quality-review.md` | R189 Quinn custom Pal authorization E2E quality review |
| `docs/06-palsmith/custom-pal-creation-to-authorization-flow.md` | R190 PalSmith custom Pal creation to authorization flow |
| `prompts/palsmith/revoke-user-custom-pal-discovery.md` | R190 copyable custom Pal discovery authorization revocation prompt |
| `evals/palbench/v0.5/palsmith/r190-palsmith-custom-pal-creation-authorization-integrated-matrix.md` | R190 PalSmith custom Pal creation and authorization integrated closeout matrix |
| `evals/palbench/v0.5/palsmith/r190-quinn-palsmith-custom-pal-authorization-closeout-review.md` | R190 Quinn closeout review for PalSmith custom Pal authorization |
| `evals/palbench/v0.5/palsmith/r191-custom-pal-revocation-host-regression.md` | R191 custom Pal revocation real-host and file-level regression evidence |
| `evals/palbench/v0.5/palsmith/r191-custom-pal-revocation-boundary-results.md` | R191 custom Pal revocation boundary result matrix |
| `evals/palbench/v0.5/palsmith/r191-external-user-readability-review.md` | R191 external user readability review for custom Pal creation and authorization |
| `evals/palbench/v0.5/palsmith/r191-quinn-revocation-and-readability-review.md` | R191 Quinn QA review for revocation and readability |
| `evals/palbench/v0.5/palsmith/r191-custom-pal-revocation-readability-summary.md` | R191 custom Pal revocation and readability summary |
| `evals/palbench/v0.5/palsmith/r192-palsmith-phase-evidence-audit-matrix.md` | R192 PalSmith phase evidence audit matrix |
| `evals/palbench/v0.5/palsmith/r192-resource-index-consistency-review.md` | R192 PalSmith resource index consistency review |
| `evals/palbench/v0.5/palsmith/r192-no-code-boundary-audit.md` | R192 PalSmith no-code boundary audit |
| `evals/palbench/v0.5/palsmith/r192-quinn-phase-closeout-review.md` | R192 Quinn PalSmith phase closeout review |
| `docs/06-palsmith/palsmith-v05-release-prep.md` | R193 PalSmith v0.5 release-prep note |
| `docs/06-palsmith/palsmith-v05-known-limits.md` | R193 PalSmith v0.5 known limits |
| `docs/06-palsmith/palsmith-v05-release-checklist.md` | R193 PalSmith v0.5 release checklist |
| `evals/palbench/v0.5/palsmith/r193-release-prep-package-review.md` | R193 PalSmith release-prep package review |
| `evals/palbench/v0.5/palsmith/r193-release-boundary-pressure-tests.md` | R193 PalSmith release boundary pressure tests |
| `evals/palbench/v0.5/palsmith/r193-quinn-release-prep-review.md` | R193 Quinn release-prep review |
| `evals/palbench/v0.5/palsmith/r196-existing-pal-upgrade-routing-regression.md` | R196 existing Pal upgrade routing regression |
| `evals/palbench/v0.5/palsmith/r196-luma-upgrade-regression.md` | R196 Luma upgrade regression scenario |
| `evals/palbench/v0.5/palsmith/r196-quinn-existing-pal-upgrade-review.md` | R196 Quinn review for existing Pal composite upgrade |
| `evals/palbench/v0.5/palsmith/r197-existing-pal-upgrade-host-plan.md` | R197 real Codex host existing Pal upgrade plan rehearsal |
| `evals/palbench/v0.5/palsmith/r197-ai-judgement-no-keyword-routing-check.md` | R197 AI semantic judgement and no-keyword-routing host check |
| `evals/palbench/v0.5/palsmith/r197-simple-edit-contrast-check.md` | R197 simple existing Pal edit contrast host check |
| `evals/palbench/v0.5/palsmith/r197-quinn-existing-pal-upgrade-host-review.md` | R197 Quinn review for existing Pal upgrade real-host rehearsal |
| `evals/palbench/v0.5/palsmith/r198-palsmith-pal-completeness-regression.md` | R198 PalSmith completeness level regression |
| `evals/palbench/v0.5/palsmith/r213-primary-function-acceptance.md` | R213 PalSmith primary function acceptance summary |
| `evals/palbench/v0.5/palsmith/r213-mia-crossborder-coach-creation-result.md` | R213 Mia CrossBorder Coach composite creation result |
| `evals/palbench/v0.5/palsmith/r213-draft-to-custom-functional-result.md` | R213 draft-to-custom functional result |
| `evals/palbench/v0.5/palsmith/r213-authorization-revocation-functional-result.md` | R213 discovery authorization and revocation functional result |
| `evals/palbench/v0.5/palsmith/r213-quinn-primary-function-review.md` | R213 Quinn primary function review |
| `evals/palbench/v0.5/palsmith/r213-functional-fixtures/` | R213 controlled MiaCrossBorderCoach draft and user custom Pal fixtures |
| `evals/palbench/v0.5/palsmith/r214-fresh-copy-primary-function-test.md` | R214 PalSmith fresh copy primary function test summary |
| `evals/palbench/v0.5/palsmith/r214-fresh-copy-mia-creation-result.md` | R214 fresh copy Mia creation result |
| `evals/palbench/v0.5/palsmith/r214-fresh-copy-draft-to-custom-result.md` | R214 fresh copy draft-to-custom result |
| `evals/palbench/v0.5/palsmith/r214-fresh-copy-authorization-revocation-result.md` | R214 fresh copy authorization and revocation result |
| `evals/palbench/v0.5/palsmith/r214-quinn-fresh-copy-primary-function-review.md` | R214 Quinn fresh copy primary function review |
| `evals/palbench/v0.5/palsmith/r214-fresh-copy-test/` | R214 fresh copy MiaCrossBorderCoach test fixtures |
| `templates/palsmith/minimal-pal-generation-checklist.md` | Minimal Pal generation checklist |
| `templates/palsmith/standard-pal-generation-checklist.md` | Standard Pal generation checklist |
| `templates/palsmith/pal-asset-classification-result-template.json` | Pal asset classification result JSON template |
| `templates/palsmith/existing-pal-upgrade-report-template.md` | existing Pal upgrade report template |
| `evals/palbench/palsmith/r98c-palsmith-v0.5-asset-generation-boundary.md` | R98-C PalSmith boundary eval |
| `release/fresh-clone-checks/r98c-local-palsmith-v0.5-template-validation.md` | R98-C local validation |
| `docs/03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md` | PalSmith v0.5 user guide |
| `docs/07-pal-asset-execution/README.md` | R201 Pal Asset Execution adoption guide |

## Pal Asset Usage Regression

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/asset-usage/r198-pal-asset-execution-contract.md` | R198 Pal Asset Execution Contract eval |
| `evals/palbench/v0.5/asset-usage/r198-luma-style-design-asset-usage-regression.md` | R198 Luma-style design task asset usage regression fixture |
| `evals/palbench/v0.5/asset-usage/r198-generic-pal-asset-usage-regression.md` | R198 generic Pal asset usage regression matrix |
| `evals/palbench/v0.5/asset-usage/r198-quinn-asset-execution-review.md` | R198 Quinn review for Pal asset execution contract |
| `evals/palbench/v0.5/asset-usage/r199-user-custom-pal-product-review-host-rehearsal.md` | R199 real host user custom Pal product review rehearsal |
| `evals/palbench/v0.5/asset-usage/r199-no-blind-tool-call-design-host-rehearsal.md` | R199 real host no blind tool call design rehearsal |
| `evals/palbench/v0.5/asset-usage/r199-palsmith-completeness-host-rehearsal.md` | R199 real host PalSmith completeness rehearsal |
| `evals/palbench/v0.5/asset-usage/r199-lightweight-path-contrast-host-rehearsal.md` | R199 real host lightweight path contrast rehearsal |
| `evals/palbench/v0.5/asset-usage/r199-quinn-pal-asset-execution-host-review.md` | R199 Quinn review for real host Pal asset execution rehearsal |
| `evals/palbench/v0.5/asset-usage/controlled-write-fixtures/FirstPrinciplesProductReviewerControlledWrite/` | R200 controlled write test artifact fixture; not official, not user-installed, not contacts-registered |
| `evals/palbench/v0.5/asset-usage/r200-controlled-write-asset-inventory.md` | R200 controlled write fixture asset inventory |
| `evals/palbench/v0.5/asset-usage/r200-palsmith-controlled-write-plan.md` | R200 PalSmith plan-first controlled write evidence |
| `evals/palbench/v0.5/asset-usage/r200-controlled-write-result.md` | R200 controlled write result evidence |
| `evals/palbench/v0.5/asset-usage/r200-controlled-write-fixture-execution-regression.md` | R200 controlled write fixture execution regression |
| `evals/palbench/v0.5/asset-usage/r200-controlled-write-boundary-pressure-tests.md` | R200 controlled write negative boundary pressure tests |
| `evals/palbench/v0.5/asset-usage/r200-quinn-controlled-write-review.md` | R200 Quinn controlled write review |
| `evals/palbench/v0.5/asset-usage/r201-asset-execution-adoption-guide-review.md` | R201 Pal Asset Execution adoption guide review |
| `evals/palbench/v0.5/asset-usage/r201-release-readiness-update-review.md` | R201 release readiness update review |
| `evals/palbench/v0.5/asset-usage/r201-quinn-adoption-guide-review.md` | R201 Quinn adoption guide review |
| `evals/palbench/v0.5/asset-usage/r202-official-pal-asset-execution-adoption-matrix.md` | R202 official Pal Asset Execution adoption spot-check matrix |
| `evals/palbench/v0.5/asset-usage/r202-official-pal-adoption-gaps-summary.md` | R202 official Pal adoption gaps and phase plan |
| `evals/palbench/v0.5/asset-usage/r202-quinn-official-pal-adoption-review.md` | R202 Quinn review for official Pal adoption spot-check |
| `evals/palbench/v0.5/asset-usage/r203-official-pal-entry-adoption-matrix.md` | R203 official Pal Phase 1 entry adoption matrix |
| `evals/palbench/v0.5/asset-usage/r203-official-pal-entry-adoption-before-after.md` | R203 official Pal entry adoption before / after summary |
| `evals/palbench/v0.5/asset-usage/r203-quinn-official-pal-entry-adoption-review.md` | R203 Quinn review for official Pal entry adoption |
| `evals/palbench/v0.5/asset-usage/r204-high-priority-pal-task-asset-packet-examples-matrix.md` | R204 high-priority Pal Task Asset Packet examples matrix |
| `evals/palbench/v0.5/asset-usage/r204-task-asset-packet-example-quality-review.md` | R204 quality review for Task Asset Packet examples |
| `evals/palbench/v0.5/asset-usage/r204-quinn-phase-2-example-review.md` | R204 Quinn review for Phase 2 examples |
| `evals/palbench/v0.5/asset-usage/r205-mira-release-readiness-host-regression.md` | R205 Mira representative host regression |
| `evals/palbench/v0.5/asset-usage/r205-palsmith-existing-pal-upgrade-host-regression.md` | R205 PalSmith representative host regression |
| `evals/palbench/v0.5/asset-usage/r205-atlas-development-task-package-host-regression.md` | R205 Atlas representative host regression |
| `evals/palbench/v0.5/asset-usage/r205-quinn-completion-report-review-host-regression.md` | R205 Quinn representative host regression |
| `evals/palbench/v0.5/asset-usage/r205-nova-product-privacy-boundary-host-regression.md` | R205 Nova representative host regression |
| `evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md` | R205 Quinn summary review for high-priority host regressions |
| `evals/palbench/v0.5/asset-usage/r205-high-priority-host-regression-summary.md` | R205 high-priority representative host regression summary |
| `evals/palbench/v0.5/asset-usage/r206-official-pal-representative-regression-coverage-matrix.md` | R206 official Pal representative regression coverage matrix |
| `evals/palbench/v0.5/asset-usage/r206-remaining-official-pal-regression-plan.md` | R206 remaining official Pal regression plan |
| `evals/palbench/v0.5/asset-usage/r206-r207-execution-package.md` | R206 R207 execution package for remaining official Pals |
| `evals/palbench/v0.5/asset-usage/r206-quinn-phase-3-plan-review.md` | R206 Quinn review for Phase 3 plan |
| `evals/palbench/v0.5/asset-usage/r207-faye-delivery-host-regression.md` | R207 Faye representative host regression |
| `evals/palbench/v0.5/asset-usage/r207-harper-writing-host-regression.md` | R207 Harper representative host regression |
| `evals/palbench/v0.5/asset-usage/r207-morgan-document-host-regression.md` | R207 Morgan representative host regression |
| `evals/palbench/v0.5/asset-usage/r207-rhea-system-boundary-host-regression.md` | R207 Rhea representative host regression |
| `evals/palbench/v0.5/asset-usage/r207-vega-research-host-regression.md` | R207 Vega representative host regression |
| `evals/palbench/v0.5/asset-usage/r207-quinn-remaining-official-pal-host-regression-review.md` | R207 Quinn review for remaining official Pal host regressions |
| `evals/palbench/v0.5/asset-usage/r207-remaining-official-pal-host-regression-summary.md` | R207 remaining official Pal representative host regression summary |
| `evals/palbench/v0.5/asset-usage/r207-official-pal-representative-regression-coverage-matrix.md` | R207 10-Pal scoped representative regression coverage matrix |
| `docs/07-pal-asset-execution/scoped-certification-plan.md` | R208 scoped certification plan |
| `docs/07-pal-asset-execution/scoped-certification-checklist.md` | R208 scoped certification checklist |
| `templates/pal/scoped-certification-record.md` | R208 scoped certification record template |
| `evals/palbench/v0.5/asset-usage/r208-scoped-certification-candidate-matrix.md` | R208 scoped certification candidate matrix |
| `evals/palbench/v0.5/asset-usage/r208-r209-scoped-certification-execution-package.md` | R208 R209 scoped certification execution package |
| `evals/palbench/v0.5/asset-usage/r208-quinn-scoped-certification-plan-review.md` | R208 Quinn review for scoped certification plan |
| `evals/palbench/v0.5/asset-usage/r209-mira-main-scoped-certification-review.md` | R209 Mira scoped certification review |
| `evals/palbench/v0.5/asset-usage/r209-palsmith-governor-scoped-certification-review.md` | R209 PalSmith scoped certification review |
| `evals/palbench/v0.5/asset-usage/r209-atlas-developer-scoped-certification-review.md` | R209 Atlas scoped certification review |
| `evals/palbench/v0.5/asset-usage/r209-quinn-quality-scoped-certification-review.md` | R209 Quinn scoped certification review |
| `evals/palbench/v0.5/asset-usage/r209-nova-product-scoped-certification-review.md` | R209 Nova scoped certification review |
| `evals/palbench/v0.5/asset-usage/r209-scoped-certification-review-matrix.md` | R209 scoped certification review matrix |
| `evals/palbench/v0.5/asset-usage/r209-quinn-scoped-certification-review.md` | R209 Quinn scoped certification review |
| `evals/palbench/v0.5/asset-usage/certifications/r209-mira-main-release-readiness-coordination-scoped-certification-record.md` | R209 Mira release readiness coordination scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r209-palsmith-governor-existing-pal-composite-upgrade-planning-scoped-certification-record.md` | R209 PalSmith existing Pal composite upgrade planning scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r209-atlas-developer-docs-first-development-task-package-scoped-certification-record.md` | R209 Atlas docs-first development task package scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r209-quinn-quality-completion-report-false-completion-review-scoped-certification-record.md` | R209 Quinn completion report / false completion review scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r209-nova-product-privacy-authorization-boundary-decision-scoped-certification-record.md` | R209 Nova product privacy and authorization boundary scoped certification record |
| `evals/palbench/v0.5/asset-usage/r210-faye-delivery-scoped-certification-review.md` | R210 Faye delivery handoff scoped certification review |
| `evals/palbench/v0.5/asset-usage/r210-harper-writing-scoped-certification-review.md` | R210 Harper README writing scoped certification review |
| `evals/palbench/v0.5/asset-usage/r210-morgan-document-scoped-certification-review.md` | R210 Morgan document package scoped certification review |
| `evals/palbench/v0.5/asset-usage/r210-rhea-system-scoped-certification-review.md` | R210 Rhea no-code risk scoped certification review |
| `evals/palbench/v0.5/asset-usage/r210-vega-research-scoped-certification-review.md` | R210 Vega source-policy scoped certification review |
| `evals/palbench/v0.5/asset-usage/r210-scoped-certification-review-matrix.md` | R210 remaining Pal task-family scoped certification review matrix |
| `evals/palbench/v0.5/asset-usage/r210-combined-scoped-certification-coverage-matrix.md` | R210 combined R209-R210 scoped representative task-family coverage matrix |
| `evals/palbench/v0.5/asset-usage/r210-quinn-scoped-certification-review.md` | R210 Quinn review for remaining scoped certification records |
| `evals/palbench/v0.5/asset-usage/certifications/r210-faye-delivery-handoff-user-facing-summary-scoped-certification-record.md` | R210 Faye delivery handoff scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r210-harper-writing-readme-style-revision-scoped-certification-record.md` | R210 Harper README writing scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r210-morgan-document-release-notes-package-scoped-certification-record.md` | R210 Morgan document package scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r210-rhea-system-no-code-risk-review-scoped-certification-record.md` | R210 Rhea no-code risk scoped certification record |
| `evals/palbench/v0.5/asset-usage/certifications/r210-vega-research-source-policy-skill-to-pal-evaluation-scoped-certification-record.md` | R210 Vega source-policy scoped certification record |

## Official Pal Asset Audit

| Path | Purpose |
| --- | --- |
| `evals/palbench/pal-asset/r98b-official-pal-asset-audit.md` | R98-B historical pre-Faye asset audit; current roster is 10 |
| `evals/palbench/pal-asset/r98b-official-pal-upgrade-gap-table.md` | R98-B official Pal upgrade gap table |
| `release/integration-notes/r98b-official-pal-upgrade-plan.md` | R98-B official Pal upgrade plan |
| `release/fresh-clone-checks/r98b-local-official-pal-asset-audit-validation.md` | R98-B local validation |
| `docs/03-user-guides/official-pal-asset-upgrade-plan.md` | official Pal asset upgrade plan guide |
| `docs/07-pal-asset-execution/official-pal-adoption-spot-check.md` | R202 official Pal Asset Execution adoption spot-check guide |
| `evals/palbench/v0.5/asset-usage/r203-official-pal-entry-adoption-matrix.md` | R203 Phase 1 official Pal entry adoption evidence |
| `official/pals/Mira-main/evals/asset-execution-example.md` | R204 Mira Task Asset Packet example |
| `official/pals/PalSmith-pal-governor/evals/asset-execution-example.md` | R204 PalSmith Task Asset Packet example |
| `official/pals/Atlas-developer/evals/asset-execution-example.md` | R204 Atlas Task Asset Packet example |
| `official/pals/Quinn-quality/evals/asset-execution-example.md` | R204 Quinn Task Asset Packet example |
| `official/pals/Nova-product/evals/asset-execution-example.md` | R204 Nova Task Asset Packet example |
| `evals/palbench/v0.5/asset-usage/r205-high-priority-host-regression-summary.md` | R205 representative host regression summary for five high-priority official Pals |
| `docs/07-pal-asset-execution/phase-3-official-pal-regression-plan.md` | R206 Phase 3 official Pal regression plan guide |
| `evals/palbench/v0.5/asset-usage/r206-official-pal-representative-regression-coverage-matrix.md` | R206 10-Pal representative regression coverage matrix |
| `evals/palbench/v0.5/asset-usage/r207-official-pal-representative-regression-coverage-matrix.md` | R207 10-Pal scoped representative regression coverage matrix |
| `evals/palbench/v0.5/asset-usage/r207-remaining-official-pal-host-regression-summary.md` | R207 representative host regression summary for remaining five official Pals |
| `docs/07-pal-asset-execution/scoped-certification-plan.md` | R208 scoped certification plan for official Pal task-family reviews |
| `evals/palbench/v0.5/asset-usage/r208-scoped-certification-candidate-matrix.md` | R208 candidate matrix for official Pal task-family scoped certification review |
| `evals/palbench/v0.5/asset-usage/r209-scoped-certification-review-matrix.md` | R209 selected high-priority Pal task-family scoped certification review matrix |
| `evals/palbench/v0.5/asset-usage/r209-quinn-scoped-certification-review.md` | R209 Quinn review for selected high-priority scoped certification records |
| `evals/palbench/v0.5/asset-usage/r210-scoped-certification-review-matrix.md` | R210 remaining Pal task-family scoped certification review matrix |
| `evals/palbench/v0.5/asset-usage/r210-combined-scoped-certification-coverage-matrix.md` | R210 combined scoped representative task-family coverage matrix |
| `evals/palbench/v0.5/asset-usage/r210-quinn-scoped-certification-review.md` | R210 Quinn review for remaining scoped certification records |

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
| `official/pals/Faye-delivery/` | R149 official Faye AI Delivery Pal Pack |
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
| `evals/palbench/v0.5/behavior/r148-prompt-initialization-v0-5-alignment-results.md` | R148 AgentPal v0.5 prompt initialization alignment results |
| `release/fresh-clone-checks/r148-local-prompt-initialization-v0-5-validation.md` | R148 local validation for prompt initialization v0.5 alignment |
| `release/integration-notes/r148-r149-readiness-decision.md` | R148 readiness decision for R149 manual test plan preparation |
| `evals/palbench/v0.5/cleanup/r148-legacy-entry-wording-file-audit.md` | R148 full legacy entry / wording / file audit |
| `evals/palbench/v0.5/cleanup/r148-legacy-entry-wording-file-cleanup-summary.md` | R148 legacy entry / wording cleanup summary |
| `evals/palbench/v0.5/cleanup/r148-legacy-entry-wording-file-deletion-manifest.md` | R148 deletion manifest for legacy cleanup |
| `evals/palbench/v0.5/cleanup/r148-legacy-entry-wording-file-residual-review-list.md` | R148 residual review list for ambiguous legacy files |
| `release/fresh-clone-checks/r148-local-legacy-cleanup-validation.md` | R148 local validation for legacy cleanup |
| `evals/palbench/v0.5/manual/r149-manual-test-plan.md` | R149 manual test goals, scope, hosts, roles, scenario groups, order, policy, and risk handling |
| `evals/palbench/v0.5/manual/r149-manual-test-scripts.md` | R149 copyable manual test prompts, expected behavior, fail conditions, and recording notes |
| `evals/palbench/v0.5/manual/r149-manual-test-record-template.md` | R149 single-test record, round summary, issue, and evidence templates |
| `evals/palbench/v0.5/manual/r149-manual-test-scoring-rubric.md` | R149 pass/partial/fail/blocked, issue severity, user experience, and v0.5 boundary scoring rubric |
| `release/fresh-clone-checks/r149-local-manual-test-plan-validation.md` | R149 local validation for manual test planning artifacts |
| `evals/palbench/v0.5/readiness/r149-pre-manual-readiness-audit.md` | R149 pre-manual blocker audit and Faye registration readiness |
| `evals/palbench/v0.5/readiness/r149-faye-official-pal-registration-results.md` | R149 Faye official Pal registration and behavior smoke results |
| `evals/palbench/v0.5/readiness/r149-pre-manual-blocking-fix-summary.md` | R149 pre-manual blocking fix summary |
| `evals/palbench/v0.5/readiness/r149-pre-manual-residual-risk-list.md` | R149 residual risk list before manual execution |
| `release/fresh-clone-checks/r149-local-pre-manual-readiness-validation.md` | R149 local validation for Faye registration and pre-manual readiness |
| `release/integration-notes/r149-r150-readiness-decision.md` | R149 readiness decision for R150 manual test execution |

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
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-deep-conductor-readiness.md` | v0.3 Deep Conductor readiness assessment for rc.1 preparation |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-public-capability-summary.md` | public-safe v0.3 capability summary |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-release-checklist.md` | v0.3 release preparation checklist |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-release-preparation-audit.md` | R64 release preparation audit |
| `evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md` | v0.3 integration readiness matrix |
| `docs/05-orchestration-methodology/cross-runtime-pal-memory.md` | Cross-Runtime Pal Memory guide for preserving Pal/project/routing continuity across host Runtimes |
| `docs/05-orchestration-methodology/token-cost-aware-deep-conductor.md` | Token / Cost-aware Deep Conductor guide for qualitative Context Budget planning |
| `docs/05-orchestration-methodology/00-methodology-overview.md` | current methodology overview |
| `docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md` | Pal Team and future Deep Conductor relationship |
| `evals/palbench/v0.5/documentation/archive/docs/06-validation-and-evidence/README.md` | current validation and PalBench entry |
| `evals/palbench/v0.5/documentation/archive/docs/06-validation-and-evidence/01-palbench-small-sample-report.md` | current R33 PalBench small-sample report |
| `evals/palbench/v0.5/documentation/archive/docs/06-validation-and-evidence/05-future-palbench-design.md` | current future PalBench design notes |
| `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/README.md` | historical release-candidate pointer |
| `archive/migration-from-v0.3/release-candidate-docs/02-release-manifest.md` | historical release-candidate manifest |
| `evals/palbench/v0.5/documentation/archive/docs/research/README.md` | archive status note; not a primary docs entry |
| `evals/palbench/v0.5/documentation/archive/docs/research/archive/` | historical research notes retained for traceability |
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

- `docs/04-runtime-guides/runtime-adapter-stability-guide.md`
- `docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md`
- `docs/04-runtime-guides/upgrade-existing-binding-to-thin-binding.md`

## R156 Agent Use Partner Evidence

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/agent-use/r156-agent-use-partner-real-task-test-plan.md` | R156 real host Agent-use partner test plan and scoring policy |
| `evals/palbench/v0.5/agent-use/r156-agent-use-partner-real-task-results.md` | R156 real Codex thread results with 18 final answers and 16 pass / 2 partial |
| `evals/palbench/v0.5/agent-use/r156-agent-use-partner-issues.md` | R156 issue list: mode-label gap, Host Capability Snapshot gap, latency note, non-Codex host status |
| `evals/palbench/v0.5/agent-use/r156-codex-mode-skill-plugin-trigger-matrix.md` | R156 trigger matrix with correct/partial actual trigger observations |
| `evals/palbench/v0.5/agent-use/r156-claude-code-real-call-results.md` | R156 Claude Code minimal real-call evidence |
| `evals/palbench/v0.5/agent-use/r156-agent-use-optimization-backlog.md` | R156 follow-up backlog for Agent-use partner behavior |
| `release/fresh-clone-checks/r156-local-agent-use-partner-validation.md` | R156 local validation record |
| `release/integration-notes/r156-r157-agent-use-decision.md` | R156 to R157 decision record |

## R157 Agent-use Decision Protocol Evidence

| Path | Purpose |
| --- | --- |
| `standards/agent-use/` | R157 Agent-use no-code standards for Decision Cards, invocation records, modes, model/reasoning, subthreads, Claude Code handoff, and pre-execution checklist |
| `templates/agent-use/` | R157 Agent-use templates |
| `standards/capability-inventory/host-capability-snapshot.md` | bounded Host Capability Snapshot protocol |
| `templates/capability-inventory/host-capability-snapshot-template.json` | Host Capability Snapshot JSON template |
| `standards/deep-conductor/agent-use-mode-decision-protocol.md` | Deep Conductor bridge to R157 Agent-use mode decisions |
| `evals/palbench/v0.5/agent-use/r157-agent-use-decision-protocol-enhancement-summary.md` | R157 enhancement summary |
| `evals/palbench/v0.5/agent-use/r157-agent-use-decision-protocol-check-results.md` | R157 protocol check results |
| `evals/palbench/v0.5/agent-use/r157-agent-use-decision-protocol-issues.md` | R157 issue record |
| `release/fresh-clone-checks/r157-local-agent-use-decision-protocol-validation.md` | R157 local validation |
| `release/integration-notes/r157-r158-real-invocation-readiness-decision.md` | R157 to R158 readiness decision |

## R158 Real Skill / Plugin / Mode Invocation Evidence

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/agent-use/r158-real-skill-plugin-mode-invocation-plan.md` | R158 bounded real invocation test plan and scoring policy |
| `evals/palbench/v0.5/agent-use/r158-real-skill-plugin-mode-invocation-results.md` | R158 16-case real/dry-run/handoff invocation results |
| `evals/palbench/v0.5/agent-use/r158-skill-plugin-invocation-records.md` | R158 per Skill/plugin invocation records |
| `evals/palbench/v0.5/agent-use/r158-codex-mode-invocation-results.md` | R158 Codex mode and background-thread evidence |
| `evals/palbench/v0.5/agent-use/r158-claude-code-handoff-acceptance-results.md` | R158 Claude Code minimal-call result and full-host boundary |
| `evals/palbench/v0.5/agent-use/r158-real-invocation-issues.md` | R158 issue list, including child-thread enum gap |
| `evals/palbench/v0.5/agent-use/r158-agent-use-next-optimization-backlog.md` | R158 next optimization backlog for R159 |
| `evals/palbench/v0.5/agent-use/fixtures/r158/` | R158 public-safe local fixtures and evidence outputs |
| `release/fresh-clone-checks/r158-local-real-invocation-validation.md` | R158 local validation record |
| `release/integration-notes/r158-r159-real-invocation-decision.md` | R158 to R159 decision record |

## R159 Codex Subagent / External Agent / Explicit Tool Evidence

| Path | Purpose |
| --- | --- |
| `standards/agent-use/child-thread-decision-card.md` | R159 child/background thread decision-card standard and enum compliance guard |
| `templates/agent-use/child-thread-decision-card-template.md` | R159 child/background thread decision-card template |
| `standards/agent-use/explicit-tool-directive-rule.md` | R159 explicit Skill/plugin/tool/external-agent directive rule |
| `templates/agent-use/explicit-tool-directive-record-template.md` | R159 explicit directive record template |
| `standards/agent-use/codex-expert-usage-guide.md` | R159 Codex expert usage guide for all official Pals |
| `evals/palbench/v0.5/agent-use/r159-codex-subagent-external-agent-test-plan.md` | R159 bounded real-host test plan |
| `evals/palbench/v0.5/agent-use/r159-codex-subagent-external-agent-results.md` | R159 14-case results for Codex child/background threads, subagent, external agents, and direct-use Skills |
| `evals/palbench/v0.5/agent-use/r159-child-thread-decision-records.md` | R159 child/background thread and subagent decision records |
| `evals/palbench/v0.5/agent-use/r159-explicit-tool-directive-records.md` | R159 explicit Skill/plugin/tool/external-agent directive records |
| `evals/palbench/v0.5/agent-use/r159-claude-code-minimal-handoff-results.md` | R159 Claude Code minimal handoff result; not full host acceptance |
| `evals/palbench/v0.5/agent-use/r159-each-pal-codex-expert-smoke-results.md` | R159 each-Pal Codex expert smoke results |
| `evals/palbench/v0.5/agent-use/r159-agent-use-issues.md` | R159 issue list and non-blocking notes |
| `evals/palbench/v0.5/agent-use/r159-next-optimization-backlog.md` | R159 to R160 evidence-tightening backlog |
| `evals/palbench/v0.5/agent-use/fixtures/r159/` | R159 public-safe local fixture and evidence outputs |
| `release/fresh-clone-checks/r159-local-codex-subagent-external-agent-validation.md` | R159 local validation record |
| `release/integration-notes/r159-r160-agent-use-decision.md` | R159 to R160 decision record |

## R160 Final Real Host Gap Closure Evidence

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/agent-use/r160-final-real-host-gap-closure-results.md` | R160 final real-host gap closure results and 6-case summary |
| `evals/palbench/v0.5/agent-use/r160-plan-goal-mode-manual-evidence.md` | R160 Plan Mode / Goal Mode evidence, limitations, and copyable manual scripts |
| `evals/palbench/v0.5/agent-use/r160-claude-code-host-acceptance-results.md` | R160 Claude Code minimal handoff and budget-blocked full-host attempt |
| `evals/palbench/v0.5/agent-use/r160-subagent-child-thread-regression-results.md` | R160 Codex child-thread enum regression evidence |
| `evals/palbench/v0.5/agent-use/r160-capability-status-classification.md` | R160 final capability status classification table |
| `evals/palbench/v0.5/agent-use/r160-release-claim-guard.md` | R160 public claim guard with claimable and forbidden wording |
| `evals/palbench/v0.5/agent-use/r160-final-gap-issues.md` | R160 remaining low/note limitations |
| `evals/palbench/v0.5/agent-use/fixtures/r160/` | R160 public-safe local fixture and evidence outputs |
| `release/fresh-clone-checks/r160-local-final-real-host-gap-validation.md` | R160 local validation record |
| `release/integration-notes/r160-r161-release-evidence-readiness-decision.md` | R160 to R161 readiness decision |

## R161 Documentation Governance Evidence

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/documentation/r161-documentation-governance-audit.md` | R161 documentation governance audit summary |
| `evals/palbench/v0.5/documentation/r161-root-docs-keep-rewrite-delete-matrix.md` | R161 root keep / rewrite / archive / delete matrix |
| `evals/palbench/v0.5/documentation/r161-docs-directory-keep-rewrite-delete-matrix.md` | R161 docs-directory keep / rewrite / archive / delete matrix |
| `evals/palbench/v0.5/documentation/r161-obsolete-file-deletion-candidates.md` | R161 obsolete deletion and archive candidates |
| `evals/palbench/v0.5/documentation/r161-readme-v0.5-rewrite-requirements.md` | R161 README rewrite requirements for v0.5 |
| `evals/palbench/v0.5/documentation/r161-docs-restructure-plan.md` | R161 docs restructure plan for R162 |
| `release/fresh-clone-checks/r161-local-documentation-governance-validation.md` | R161 local documentation governance validation |
| `release/integration-notes/r161-r162-documentation-rewrite-readiness-decision.md` | R161 to R162 rewrite readiness decision |

## R162 Public Docs Rewrite Evidence

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/documentation/r162-public-docs-rewrite-summary.md` | R162 public README and docs navigation rewrite summary |
| `evals/palbench/v0.5/documentation/r162-readme-claim-guard.md` | R162 public README claim guard |
| `release/fresh-clone-checks/r162-local-public-docs-validation.md` | R162 local public docs validation |
| `release/integration-notes/r162-r163-docs-restructure-readiness-decision.md` | R162 to R163 docs restructure readiness decision |

## R163 Docs Restructure Evidence

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/documentation/archive/docs/` | R163 archived docs evidence/history tree moved out of the user docs path |
| `evals/palbench/v0.5/documentation/r163-docs-directory-restructure-summary.md` | R163 docs restructure summary |
| `evals/palbench/v0.5/documentation/r163-docs-move-manifest.md` | R163 docs move manifest |
| `evals/palbench/v0.5/documentation/r163-docs-restructure-deletion-manifest.md` | R163 deletion manifest |
| `evals/palbench/v0.5/documentation/r163-docs-link-and-claim-check.md` | R163 link and claim check |
| `release/fresh-clone-checks/r163-local-docs-restructure-validation.md` | R163 local docs restructure validation |
| `release/integration-notes/r163-r164-docs-content-rewrite-readiness-decision.md` | R163 to R164 docs content rewrite readiness decision |

## R164 User Docs Content Rewrite Evidence

| Path | Purpose |
| --- | --- |
| `evals/palbench/v0.5/documentation/r164-docs-content-rewrite-summary.md` | R164 user docs content rewrite summary |
| `evals/palbench/v0.5/documentation/r164-docs-claim-consistency-check.md` | R164 docs claim consistency check |
| `evals/palbench/v0.5/documentation/r164-docs-link-check.md` | R164 docs link check |
| `evals/palbench/v0.5/documentation/r164-docs-remaining-work.md` | R164 docs remaining work |
| `release/fresh-clone-checks/r164-local-docs-content-validation.md` | R164 local docs content validation |
| `release/integration-notes/r164-r165-release-docs-readiness-decision.md` | R164 to R165 release docs readiness decision |
| `evals/palbench/v0.5/documentation/r165-release-docs-final-review.md` | R165 release docs final review |
| `evals/palbench/v0.5/documentation/r165-public-package-docs-scope.md` | R165 public package docs scope |
| `evals/palbench/v0.5/documentation/r165-final-claim-guard.md` | R165 final public claim guard |
| `evals/palbench/v0.5/documentation/r165-user-path-walkthrough.md` | R165 user documentation path walkthrough |
| `release/fresh-clone-checks/r165-local-release-docs-validation.md` | R165 local release docs validation |
| `release/integration-notes/r165-r166-release-candidate-readiness-decision.md` | R165 to R166 release candidate readiness decision |
| `release/fresh-clone-checks/r166-local-release-candidate-preflight.md` | R166 local release candidate preflight |
| `release/integration-notes/r166-v0.5-release-candidate-scope.md` | R166 v0.5 release candidate scope |
| `release/integration-notes/r166-v0.5-release-candidate-claim-guard.md` | R166 v0.5 release candidate claim guard |
| `release/integration-notes/r166-v0.5-release-candidate-evidence-summary.md` | R166 v0.5 release candidate evidence summary |
| `release/integration-notes/r166-r167-release-preparation-readiness-decision.md` | R166 to R167 release preparation readiness decision |
| `evals/palbench/v0.5/documentation/r166-release-candidate-docs-final-check.md` | R166 release candidate docs final check |
| `docs/release/v0.5-release-candidate-preflight.md` | R194 local AgentPal v0.5 release candidate preflight |
| `evals/palbench/v0.5/release/r194-agentpal-v05-release-candidate-preflight.md` | R194 full-workspace release candidate preflight evidence |
| `evals/palbench/v0.5/release/r194-release-boundary-scan.md` | R194 release/runtime/Marketplace/contacts boundary scan |
| `evals/palbench/v0.5/release/r194-external-readability-spot-check.md` | R194 external readability spot check |
| `evals/palbench/v0.5/release/r194-quinn-release-candidate-review.md` | R194 Quinn release candidate review |
| `docs/release/v0.5-user-authorization-decision.md` | R195 user authorization decision for GitHub sync / tag / GitHub Release |
| `docs/release/v0.5-release-notes-draft.md` | R195 draft release notes for user review; not published |
| `evals/palbench/v0.5/release/r195-release-authorization-decision-package.md` | R195 release authorization decision package evidence |
| `evals/palbench/v0.5/release/r195-release-notes-draft-review.md` | R195 release notes draft review |
| `evals/palbench/v0.5/release/r195-quinn-release-authorization-review.md` | R195 Quinn release authorization review |
| `docs/release/v0.5-release-readiness-checklist.md` | R211 v0.5 release readiness checklist |
| `docs/release/v0.5-known-limits.md` | R211 v0.5 known limits |
| `docs/release/v0.5-release-authorization-decision.md` | R211 v0.5 release authorization decision |
| `evals/palbench/v0.5/release/r211-subagent-a-palsmith-readiness-audit.md` | R211 PalSmith readiness audit role output |
| `evals/palbench/v0.5/release/r211-subagent-b-official-pal-certification-readiness-audit.md` | R211 official Pal scoped certification readiness audit role output |
| `evals/palbench/v0.5/release/r211-subagent-c-no-code-boundary-audit.md` | R211 no-code/runtime/Marketplace/contacts boundary audit role output |
| `evals/palbench/v0.5/release/r211-subagent-d-release-docs-audit.md` | R211 release docs audit role output |
| `evals/palbench/v0.5/release/r211-subagent-e-integrity-audit.md` | R211 integrity audit role output |
| `evals/palbench/v0.5/release/r211-quinn-v05-release-authorization-review.md` | R211 Quinn release authorization review |
| `evals/palbench/v0.5/release/r211-v05-release-authorization-gate-review.md` | R211 v0.5 release authorization gate review |
| `evals/palbench/v0.5/release/r211-v05-release-boundary-scan.md` | R211 v0.5 release boundary scan |
| `evals/palbench/v0.5/release/r211-v05-release-integrity-review.md` | R211 v0.5 release integrity review |
| `evals/palbench/v0.5/release/r211-v05-release-readiness-verdict.md` | R211 v0.5 release readiness verdict |
| `docs/release/v0.5-release-package-manifest.md` | R212 v0.5 release package manifest |
| `docs/release/v0.5-release-notes.md` | R212 final prepared v0.5 release notes |
| `docs/release/v0.5-release-preflight-checklist.md` | R212 v0.5 release preflight checklist |
| `docs/release/v0.5-remote-operation-authorization-guide.md` | R212 remote operation authorization guide |
| `evals/palbench/v0.5/release/r212-release-package-manifest-review.md` | R212 release package manifest review |
| `evals/palbench/v0.5/release/r212-release-notes-known-limits-review.md` | R212 release notes and known limits review |
| `evals/palbench/v0.5/release/r212-release-preflight-checklist-review.md` | R212 release preflight checklist review |
| `evals/palbench/v0.5/release/r212-remote-operation-authorization-boundary-review.md` | R212 remote operation authorization boundary review |
| `evals/palbench/v0.5/release/r212-quinn-release-package-review.md` | R212 Quinn release package review |

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
