# Pal Root Entry Standard

Date: 2026-06-28
Standard id: `agentpal-pal-root-entry-standard.v0.5`

## Purpose

This standard defines root entry files for a Pal Pack. Root entries make a Pal
discoverable to humans, machine-readable to AgentPal, and understandable to host
runtimes without requiring full asset loading.

## `README.md`

`README.md` is the human-facing Pal overview.

It should contain:

- who the Pal is
- what the Pal is useful for
- major responsibilities
- major boundaries
- typical interaction examples
- directory overview
- collaboration notes

It should not contain:

- full protocol bodies
- raw research
- private memory
- transient state
- task logs

## `PAL.md`

`PAL.md` is the Pal identity and collaboration statement.

It should contain:

- Pal identity
- role and mission
- responsibilities
- explicit non-responsibilities
- inbound collaboration policy
- outbound collaboration policy
- context sharing policy
- approval boundary
- reporting style

It should answer who the Pal is, what the Pal owns, what the Pal refuses or
escalates, and how other Pals or runtimes should interact with it.

## `pal.json`

`pal.json` is the machine-readable manifest.

It should contain stable metadata such as:

- schema
- id
- display name
- role
- type
- version
- asset standard reference
- root entry paths
- asset directory paths
- collaboration settings
- public-safe capability summaries

It should not contain large natural-language knowledge bodies, task logs, full
reports, private memory, credentials, or transient state.

## `AGENTS.md`

`AGENTS.md` is the host-runtime instruction entry for working as or with this
Pal Pack.

It should explain:

- that this directory is a Pal Pack, not a normal code project
- what root entries and core files should be read first
- how to preserve central roster and thin-binding boundaries
- how to prepare task packages for runtime execution
- how to avoid copying Pal assets into external projects
- how to report evidence, `not-run`, `missing`, and `blocked`

It should not claim that the Pal directly executes filesystem, system, network,
publishing, or external API actions.

## `SKILL.md`

`SKILL.md` is the Pal Pack compatible Skill entry. It exists so host runtimes and
skill-like ecosystems can discover the Pal Pack.

`SKILL.md` is not a single runtime Agent Skill. It should say that loading it
means loading the Pal Pack entry and then selecting relevant Pal assets by
context. If a user needs a concrete runtime tool capability, the runtime should
use its Agent Skill registry or tool system separately.

## `asset-manifest.json`

`asset-manifest.json` is an optional asset index for generated, upgraded, or
audited Pal Packs.

It may contain:

- asset standard id
- asset list by directory
- asset type
- status
- owner Pal
- public/private classification
- verification references
- deprecation or migration notes

It should not be required for old Pal Packs to remain readable. If present, it
can guide more precise asset loading. If absent, the runtime may fall back to
directory conventions and report `missing` for manifest-specific evidence.

## Compatibility

Existing official Pal Packs that already expose root entries and the standard
asset directories are compatible with this standard as v0.5 upgrade targets.
Future upgrades may add indexes and manifests without breaking current reads.
