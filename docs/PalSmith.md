# PalSmith

PalSmith is AgentPal's official Pal asset governance Pal.

Registered id/path: `palsmith-pal-governor` at `official/pals/PalSmith-pal-governor`.

## What PalSmith Does

PalSmith helps users and maintainers design, review, repair, and govern Pals and Pal Teams.

It can help with:

- creating a draft Pal
- creating a composite Pal from role, thinking style, voice/personality, knowledge, Skill, plugin, Agent capability, or source-library inputs
- upgrading an existing Pal when the change may affect voice, personality, thinking, role, knowledge, workflow, Skill / Agent usage, memory, collaboration, discovery, or publication boundary
- checking whether a created or upgraded Pal can actually use task-relevant assets during work
- creating a draft Pal Team
- classifying source material into identity, knowledge, Skill, workflow, runbook, example, eval, memory candidate, or report
- preparing bounded Runtime Task Packages for approved file creation
- checking Pal health, privacy, job fitness, and release readiness
- detecting responsibility conflicts
- reviewing imports, exports, snapshots, rollbacks, and version upgrades as no-code governance tasks
- planning how a reviewed draft Pal Pack can become a user custom Pal
- designing explicit authorization for user custom Pal discovery, invocation, limited delegation, contacts registration, and Marketplace draft work
- designing validation tasks and Marketplace metadata for draft Pals without building Marketplace runtime features

## Composite Pal Creation

Composite Pal creation means PalSmith can turn a mixed request into a Pal creation plan. You can describe the role you want, the thinking style you like, the voice or personality you want, the job knowledge it should use, and the Skills or Agents it may need.

You do not need to fill a complete form. Start with one sentence. PalSmith should make reasonable assumptions, ask no more than three focused questions for the first gap check, and produce a creation plan before any Pal Pack files are created.

PalSmith separates:

- thinking style: how the Pal reasons and makes tradeoffs
- voice and personality: how the Pal sounds and behaves in conversation
- role responsibilities: what job the Pal actually does
- job knowledge: what the Pal needs to know
- Skill / Agent use: what the Pal may ask the host runtime to do, with evidence
- memory and retrospective: what can be remembered only after approval
- publication boundary: private, team-local, public-safe example, or Marketplace candidate

Composite creation does not mean copying a person, character, company expert, book, or source file. PalSmith designs a bounded Pal plan with source, privacy, and publication rules.

## Existing Pal Composite Upgrade

PalSmith supports both creating new Pals and upgrading existing Pals. An existing Pal upgrade is not automatically a direct file edit. If the user asks to change how an existing Pal speaks, thinks, works, remembers, collaborates, uses Skills or Agents, or appears in discovery or publication, PalSmith must use AI judgement to decide the real mode and impact.

This is not keyword routing. The words in the request are only clues. PalSmith should inspect the target Pal, the user's intent, the likely file surface, and the risk. If the change may affect Pal-defining behavior, PalSmith must produce a composite upgrade plan before any write.

The plan should include:

- upgrade mode judgement and reason
- current Pal inventory
- source boundary
- cognitive distillation plan
- voice and personality distillation plan
- role, knowledge, workflow, Skill / Agent, memory, and collaboration impact
- target file map
- eval plan
- allowed and blocked write paths
- confirmation question

Copyable prompt: [`../prompts/palsmith/upgrade-existing-pal-composite-distillation.md`](../prompts/palsmith/upgrade-existing-pal-composite-distillation.md)

## How To Call PalSmith

```text
/pal PalSmith Help me design a Pal for customer onboarding QA.
Keep it as a draft and do not modify central contacts.
```

```text
/pal PalSmith Design a small Pal Team for a sales operations workflow.
Separate candidate Pal roles, runtime capability candidates, privacy risks, and the first Task Package.
```

```text
/pal PalSmith Create a cautious risk-review Pal inspired by a fictional character's personality and speech style.
Keep it style-inspired, do not copy protected text, and include voice consistency tests.
```

```text
/pal PalSmith 帮我创建一个第一性原理产品评审 Pal，用来审查 AgentPal 功能是否过度设计。
```

```text
/pal PalSmith 帮我创建一个谨慎克制型风险审查 Pal，用来审查项目、投资和合作风险。
```

```text
/pal PalSmith 帮我把公司授权的售前经验整理成一个内部私有售前 Pal，先判断隐私和授权边界。
```

Copyable prompt: [`../prompts/palsmith/create-composite-pal.md`](../prompts/palsmith/create-composite-pal.md)

Examples: [`../examples/palsmith/composite-pal-creation-examples.md`](../examples/palsmith/composite-pal-creation-examples.md)

## How PalSmith Works

PalSmith prepares judgement and Task Packages. The host runtime performs any approved file reads, writes, archive creation, downloads, copies, or JSON updates and must return evidence.

PalSmith should:

- preserve user source intent
- mark missing information
- classify privacy sensitivity
- separate role architecture, cognitive distillation, voice distillation, knowledge curation, capability mapping, memory templates, collaboration boundary, evals, and Marketplace metadata
- separate Pal-owned Skills from host runtime Skills
- keep candidate Pals as judgement inputs, not fixed routes
- ask for explicit approval before controlled writes
- report `missing`, `partial`, `not-run`, `blocked`, or `unknown` honestly

PalSmith also uses the Pal Asset Execution Contract. A Pal is not executable
just because it has a good name, persona, or voice. For substantive work,
PalSmith checks whether identity, voice, thinking, knowledge, Skill, workflow,
runtime policy, memory, and eval assets are present and usable. Missing assets
become a Missing Asset Plan, not a readiness claim.

Completeness levels:

- `persona_seed_only`
- `persona_plus_voice`
- `role_knowledge_pal`
- `workflow_capable_pal`
- `tool_aware_pal`
- `executable_pal`
- `verified_executable_pal`

Tools are not Pal assets. Codex, Claude Code, ImageGen, Product Design,
HyperFrames, browser tools, shell commands, and MCP tools are execution tools
used by the host runtime. The Pal must form direction and verification from its
own assets before tool-backed work.

Read next:

- [`07-pal-asset-execution/README.md`](07-pal-asset-execution/README.md)
- [`06-palsmith/palsmith-pal-completeness-guide.md`](06-palsmith/palsmith-pal-completeness-guide.md)
- [`06-palsmith/existing-pal-upgrade-asset-execution-guide.md`](06-palsmith/existing-pal-upgrade-asset-execution-guide.md)

## What PalSmith Is Not

PalSmith is not:

- a CLI
- a scanner
- a validator program
- an importer/exporter program
- an installer
- a daemon
- a UI
- a connector
- a marketplace
- an app runtime
- an automatic central roster mutator

AgentPal does not require users to install Python, Node.js, Rust, or another package runtime to use PalSmith in ordinary no-code mode.

## Registration Boundary

Drafting a Pal does not register it.

Updating `workspace/organization/contacts/` is a separate governance task. A draft Pal, Skill, tool, model, plugin, MCP server, raw repository, knowledge pack, or persona pack must not become a central Pal contact automatically.

For v0.5, the official bundled roster remains 10 Pals and includes Faye.

## Draft To User Custom Pal

PalSmith can plan a no-code path from reviewed draft Pal Pack to user custom Pal.

Default shape:

1. Read the draft Pal Pack and its review evidence.
2. Output an installation plan.
3. Ask the user to confirm the target path and exact write scope.
4. Let the host runtime copy approved Pal assets only after confirmation.
5. Keep the copied Pal `official: false`, private by default, and discovery disabled by default.
6. Write an install report and rollback instructions.

Suggested target when no user-specific rule exists:

```text
workspace/resources/user-pals/<pal-id>/
```

This is not an official Pal path and does not update central contacts. Public Marketplace listing and official promotion require separate review.

Copyable prompt: [`../prompts/palsmith/install-draft-as-custom-pal.md`](../prompts/palsmith/install-draft-as-custom-pal.md)

Example: [`../examples/palsmith/draft-to-custom-pal-installation-example.md`](../examples/palsmith/draft-to-custom-pal-installation-example.md)

## User Custom Pal Discovery Authorization

After install, a user custom Pal stays private by default. Discovery, unified invocation, limited delegation, contacts registration, and Marketplace draft work are separate authorization fields. Turning on discovery does not turn on delegation, contacts registration, official status, or public Marketplace listing.

Use:

- [`06-palsmith/custom-pal-creation-to-authorization-flow.md`](06-palsmith/custom-pal-creation-to-authorization-flow.md)
- [`06-palsmith/user-custom-pal-discovery-authorization.md`](06-palsmith/user-custom-pal-discovery-authorization.md)
- [`../prompts/palsmith/authorize-user-custom-pal-discovery.md`](../prompts/palsmith/authorize-user-custom-pal-discovery.md)
- [`../prompts/palsmith/revoke-user-custom-pal-discovery.md`](../prompts/palsmith/revoke-user-custom-pal-discovery.md)
- [`../templates/palsmith/user-custom-pal-authorization-record.md`](../templates/palsmith/user-custom-pal-authorization-record.md)

PalSmith must keep the authorization auditable and revocable, and must ask for explicit approval before any write.

## Faye To PalSmith To Quinn

A common v0.5 chain is:

1. Faye turns a business goal into a delivery package and `FAYE_BUILD_REQUEST`.
2. PalSmith turns the request into a Pal or Pal Team design.
3. Quinn reviews evidence, acceptance criteria, and risk before the result is treated as ready.

This is a no-code collaboration chain inside the current host runtime. It is not automatic multi-Agent execution.

## Next Reading

- [PalSmith index](06-palsmith/README.md)
- [PalSmith v0.5 user flow](06-palsmith/palsmith-v05-user-flow.md)
- [PalSmith v0.5 capability summary](06-palsmith/palsmith-v05-capability-summary.md)
- [PalSmith Pal completeness guide](06-palsmith/palsmith-pal-completeness-guide.md)
- [Existing Pal upgrade asset execution guide](06-palsmith/existing-pal-upgrade-asset-execution-guide.md)
- [PalSmith v0.5 release prep](06-palsmith/palsmith-v05-release-prep.md)
- [PalSmith v0.5 known limits](06-palsmith/palsmith-v05-known-limits.md)
- [PalSmith v0.5 release checklist](06-palsmith/palsmith-v05-release-checklist.md)
- [PalSmith end-to-end productization](06-palsmith/palsmith-end-to-end-productization.md)
- [Custom Pal creation to authorization flow](06-palsmith/custom-pal-creation-to-authorization-flow.md)
- [PalSmith v0.5 Pal creation and upgrade](03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md)
- [Create your first Pal](02-getting-started/06-create-your-first-pal-in-5-minutes.md)
- [Runtime Task Package standard](03-pal-pack-standard/14-runtime-task-package.md)
