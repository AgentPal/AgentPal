# Agent Skills Specification

## Source

- URL: https://github.com/agentskills/agentskills
- Resource type: Reference / Specification
- License / usage boundary: Apache-2.0, per R2 GitHub metadata check on 2026-06-22.
- Current handling: public-card, reference-only, convert-to-knowledge-card.

## Main Use

Reference for understanding Agent Skill package structure, metadata, progressive disclosure, and package boundaries.

## Useful For Vega

- Identifying whether a resource is a Skill package.
- Checking SKILL.md, README, manifest, examples, scripts, and bundled resources.
- Distinguishing Skill, tool, knowledge, persona, workflow, and Pal Pack.
- Designing public Skill Cards without importing source.

## Not Directly Used

- This is not a Vega formal Skill.
- It is not a Research Pal.
- It does not enter contacts.

## Risk Boundary

- A valid Skill package is not automatically safe or appropriate for AgentPal.
- License, security, privacy, execution actions, and source quality still require separate checks.

## Public Package Boundary

- Contains third-party source code: no.
- Contains long third-party text: no.
- Enters Pal contacts: no.

## Recommended Trigger

Use as a reference when evaluating whether a GitHub repository is a Skill package and whether it can be represented as a public Skill Card.

## Vega Handling

Vega may use this card to evaluate external Skill resources and decide whether they belong in `imports/`, `registry/`, `runbooks/`, `workflows/`, `knowledge/`, or formal `skills/`.

## Attribution

Original project: `agentskills/agentskills`. Third-party project remains under its original License.

