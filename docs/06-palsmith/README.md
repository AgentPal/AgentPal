# PalSmith

PalSmith is the AgentPal Pal for designing, reviewing, and improving Pals and Pal Teams.

In v0.5, PalSmith is a no-code Pal asset governor. It can help a user turn goals, source material, or repeated work into Pal Pack drafts, Task Packages, health checks, and repair plans. It does not become an installer, scanner, validator program, connector, marketplace, app runtime, or automatic execution system.

## What PalSmith Helps With

- design a single new Pal
- design a composite Pal from role, thinking style, voice/personality, knowledge, Skill, plugin, Agent capability, or a source library
- design a small Pal Team for a business goal
- classify source material into identity, knowledge, Skill, workflow, runbook, example, eval, memory candidate, or report
- prepare a bounded Runtime Task Package for approved file creation
- review a Pal Pack for completeness, privacy, and job fitness
- plan how a reviewed draft Pal Pack can become a user custom Pal
- prepare repair steps when a draft is shallow, unsafe, or incomplete
- distinguish Pal-owned Skills from host runtime Skills
- generate validation cases and Marketplace metadata drafts without building Marketplace runtime features
- design explicit authorization for user custom Pal discovery, invocation, limited delegation, contacts registration, and Marketplace draft work

## Composite Pal Creation

Use this when a Pal needs more than a job title. For example, the user may want a product-review Pal with a first-principles thinking style, a risk-review Pal with a cautious voice, or a private company expert Pal built from authorized internal material.

PalSmith should produce a creation plan first. The plan separates:

- thinking style
- voice and personality
- role responsibilities
- job knowledge
- Skill / Agent candidates
- memory and retrospective design
- private / public / Marketplace boundary

For a first reply, PalSmith should avoid a long form and ask no more than three focused questions.

## What PalSmith Must Not Do

- mutate central contacts without a separate approved governance task
- register a draft as an official Pal automatically
- copy Pal assets into an external project's `.agentpal/` directory by default
- treat tools, models, plugins, MCP servers, raw repos, knowledge packs, or Skills as Pals
- claim local file writes without runtime evidence
- expose private user material in public examples or Pal Packs
- create fixed keyword routing rules
- turn private company material into a public Marketplace item by default
- present a source-inspired Pal as the source person, source character, brand, or rights holder

## Good First Prompt

```text
/pal PalSmith Help me design a Pal for customer onboarding QA.
Keep it as a draft, identify missing information, and do not modify central contacts.
```

For a team:

```text
/pal PalSmith Design a small Pal Team for a sales operations workflow.
Separate candidate Pals, required Skills, runtime capability candidates, privacy risks, and the first Task Package.
```

For a composite Pal:

```text
/pal PalSmith Create a Feynman-style technical documentation coach Pal.
Separate explanation style, teaching role, knowledge needs, Skill candidates, memory templates, and evals.
```

Copy a longer prompt from:

- [`../../prompts/palsmith/create-composite-pal.md`](../../prompts/palsmith/create-composite-pal.md)

See examples:

- [`../../examples/palsmith/composite-pal-creation-examples.md`](../../examples/palsmith/composite-pal-creation-examples.md)
- [`../../examples/palsmith/draft-to-custom-pal-installation-example.md`](../../examples/palsmith/draft-to-custom-pal-installation-example.md)

## Draft To User Custom Pal

PalSmith may help install a reviewed draft Pal Pack as a user custom Pal only through a no-code plan and a separately confirmed Runtime Task Package.

Default boundary:

- suggested target: `workspace/resources/user-pals/<pal-id>/`
- `official: false`
- private by default
- discovery disabled by default
- no central contacts write
- no public Marketplace listing
- no installer, scanner, daemon, connector, backend service, or runtime code

Copyable prompt:

- [`../../prompts/palsmith/install-draft-as-custom-pal.md`](../../prompts/palsmith/install-draft-as-custom-pal.md)

## User Custom Pal Discovery Authorization

After a user custom Pal exists, it remains private by default. PalSmith can help the user prepare scoped authorization for workspace discovery, workspace invocation, limited delegation, contacts registration, or Marketplace draft metadata.

Discovery does not imply delegation. Contacts registration and public Marketplace listing remain separate governance tasks.

Read:

- [`custom-pal-creation-to-authorization-flow.md`](custom-pal-creation-to-authorization-flow.md)
- [`user-custom-pal-discovery-authorization.md`](user-custom-pal-discovery-authorization.md)
- [`../../prompts/palsmith/authorize-user-custom-pal-discovery.md`](../../prompts/palsmith/authorize-user-custom-pal-discovery.md)
- [`../../prompts/palsmith/revoke-user-custom-pal-discovery.md`](../../prompts/palsmith/revoke-user-custom-pal-discovery.md)
- [`../../templates/palsmith/user-custom-pal-authorization-record.md`](../../templates/palsmith/user-custom-pal-authorization-record.md)
- [`../../templates/palsmith/user-custom-pal-discovery-policy.md`](../../templates/palsmith/user-custom-pal-discovery-policy.md)

## Relationship With Faye

Faye shapes business delivery packages: scenarios, workflows, data lists, interface lists, risks, missing information, and Task Package readiness.

PalSmith can then turn a Faye Build Request into a Pal or Pal Team design. Quinn can review the plan and evidence before acceptance.

## Next Links

- [PalSmith end-to-end productization](palsmith-end-to-end-productization.md)
- [Custom Pal creation to authorization flow](custom-pal-creation-to-authorization-flow.md)
- [PalSmith v0.5 creation and upgrade](../03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md)
- [Create your first Pal](../02-getting-started/06-create-your-first-pal-in-5-minutes.md)
- [Official Pals](../99-reference/official-pals.md)
