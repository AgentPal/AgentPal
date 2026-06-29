# Glossary

## AgentPal

The AgentPal Workspace and Pal Pack Standard practice. AgentPal is a Pal layer, not an Agent layer, not a multi-agent runtime, and not an execution layer.

## Pal

A portable working companion for agent runtimes. A Pal packages identity, knowledge, skills, memory boundaries, workflows, context rules, output contracts, verification standards, and collaboration protocols.

## Pal Pack

The directory package for one Pal, usually under `official/pals/<Pal-Directory>/`.

## Simple Pal Mode

The lightweight day-to-day task path in AgentPal v0.5. Mira routes clear work to one owner Pal, or a user directly calls one Pal with `/pal Name`, and the selected Pal answers in the same response. Deep Conductor can still be used as a no-code collaboration and mode-decision protocol for complex work.

## Contacts

Current roster records under `workspace/organization/contacts/` define registered Pal contactability and aliases. Old root `contacts/` records were archived under `archive/migration-from-v0.3/root-legacy/contacts/`.

## Registry

Legacy registry records moved from old root `registry/` to `workspace/resources/registry/`. They are compatibility and historical navigation records, not the current Pal discovery source of truth.

## Output Contract

A Pal-owned file that defines what a valid response from that Pal must include.

## Related

- [What is a Pal?](../01-concepts/01-what-is-a-pal.md)
- [What is a Pal Pack?](../01-concepts/02-what-is-a-pal-pack.md)
- [Simple Pal Mode](../01-concepts/05-simple-pal-mode.md)
