# Schema Standards

This directory is the standards landing area for AgentPal JSON and Markdown schema notes.

Schemas document expected fields, boundary rules, and compatibility expectations for workspace files. They do not create validators, scanners, CLIs, or generated code.

Machine-readable workspace metadata currently lives in `agentpal.json`, central contacts live in `workspace/organization/contacts/`, and central project-record templates live in `workspace/projects/_template/`.

## Contact Capability Cards

- Schema: `contact-capability-card.schema.json`
- Template: `workspace/organization/contacts/templates/pal-capability-card.template.json`
- Cards: `workspace/organization/contacts/capability-cards/*.json`

Contact Capability Cards are v0.6 routing and collaboration judgement inputs.
They add positive capability fields and negative boundary fields to central Pal
contacts. They must not be used as keyword route maps.

Team Pack schemas:

- `team.schema.json` describes Team Pack metadata in `team.json`.
- `roster.schema.json` describes Team Pack roster references in `roster.json`.

Canonical Team Pack JSON examples:

- `templates/team-pack/standard-team-pack/team.json`
- `templates/team-pack/standard-team-pack/roster.json`
- `examples/team-packs/research-team/team.json`
- `examples/team-packs/research-team/roster.json`

Related v0.6 protocol records:

- Workflow Execution Contract: `templates/orchestration/workflow-execution-contract.md`
- Team Asset Preflight: `templates/team/team-asset-preflight.md`
- Pal Asset Preflight: `templates/pal/pal-asset-preflight.md`
- Closure Gate: `orchestration/workflow-closure-gate-protocol.md`
