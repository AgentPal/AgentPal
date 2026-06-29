# Public-Safe Checklist

Use this checklist before publishing AgentPal docs, root release files, examples, evals, templates, or Pal Packs.

AgentPal v0.1.0-rc.1 is a Markdown/JSON Pal Workspace for existing runtimes. It is not a desktop app, web app, marketplace, automation platform, execution engine, complete multi-agent runtime, daemon, scanner, validator, installer, or hosted service.

## 1. What Must Not Be Published

Do not publish:

- API keys, tokens, passwords, secrets, credentials, private keys, session IDs, or payment data
- private user memory, private project state, private preferences, or private collaboration history
- real customer data, proprietary user project data, regulated personal data, or confidential business material
- real task reports, verification reports, maintenance reports, internal development reports, or unauthorized raw logs
- local absolute paths, maintainer machine paths, private workspace paths, or private software inventories
- copied internal reference documents or private planning notes
- unauthorized third-party source code, copyrighted full text, paid content, or long documentation excerpts
- future design material described as active current behavior
- claims that AgentPal v0.1.0-rc.1 includes a Pal marketplace, desktop app, full automation runtime, OpenClaw deep adapter, Hermes deep adapter, or active Subagent Mode

## 2. What Can Be Published

Public release content may include:

- workspace-level Markdown and JSON instructions
- Pal Pack identity, skill entry, output contract, public knowledge, public runbooks, public workflows, public examples, and public evals
- synthetic examples, placeholder records, and sanitized templates
- central contacts and compatibility indexes for official Pals
- public-safe docs, release notes, checklists, and audit summaries
- license, third-party notices, and contribution rules

When in doubt, publish a template or placeholder instead of real runtime content.

## 3. Memory, State, And Reports Boundary

`memory/`, `state/`, and `reports/` are runtime-sensitive by default.

Public releases may include:

- `README.md` placeholders that explain the directory purpose
- empty or explicitly public-safe examples
- templates that tell users what not to store

Public releases must not include:

- user-specific memory
- project-specific private facts
- active session state
- real routing decisions tied to a private task
- real task reports or verification reports
- raw logs or private troubleshooting histories

Before release, check:

- `memory/`
- `state/`
- `reports/`
- `official/pals/*/memory/`
- `official/pals/*/state/`
- `official/pals/*/reports/`

Ignored local-only files can exist in a working copy, but they must not be included in the public release package.

## 4. Pal Pack Public Asset Rules

Each public Pal Pack may include:

- `PAL.md`
- `pal.json`
- `SKILL.md`
- `AGENTS.md`
- `README.md`
- `core/output-contract.md`
- public `knowledge/`, `skills/`, `runbooks/`, `workflows/`, `examples/`, `evals/`, and placeholder memory/state/report directories

Each public Pal Pack must avoid:

- real user data or private project data
- raw private logs
- production secrets
- private local paths
- unauthorized full-text source material
- claims that a missing runtime integration is active

Pal Packs are working assets, not independent agent runtimes. `official/pals/<Pal>/` is the official Pal Pack boundary; the root AgentPal Workspace is not itself one single Pal Pack.

## 5. Runtime State Exclusion Rules

`.gitignore` and release packaging should exclude:

- runtime-private memory and state files
- real reports
- raw imports and private imports
- temporary files
- OS/editor files
- logs and local backups

`.gitignore` should keep:

- public README placeholders
- public templates
- root release documents
- official Pal Pack public assets
- central contacts files

Do not rely on `.gitignore` alone. Review the release archive or GitHub diff before publishing.

## 6. Contributor Checklist

Before opening a contribution, confirm:

- [ ] The contribution does not contain secrets, credentials, tokens, passwords, or private keys.
- [ ] The contribution does not contain real user memory, private project state, or real customer data.
- [ ] Examples and evals are synthetic, placeholder, or explicitly authorized.
- [ ] Third-party content is summarized, cited when needed, and not copied as unauthorized full text.
- [ ] New Pal Pack contributions include the minimum public files listed in the Pal Pack Standard.
- [ ] Future or experimental features are labeled as future, experimental, or not active.
- [ ] Local paths use generic examples such as `<your-agentpal-directory>`.

## 7. Maintainer Release Audit Checklist

Before tagging a release, maintainers should:

- [ ] Run keyword scans for secrets, credentials, private data, local paths, internal reports, and future-feature claims.
- [ ] Validate root JSON, central contacts JSON, and official Pal `pal.json` files.
- [ ] Compare `workspace/organization/contacts/pals.json` and `workspace/organization/contacts/PAL_CONTACTS.md` for official Pal synchronization.
- [ ] Check `memory/`, `state/`, `reports/`, and Pal-local equivalents for non-placeholder content.
- [ ] Review public examples and evals for private or unauthorized material.
- [ ] Confirm release notes and GitHub release draft do not overclaim active capabilities.
- [ ] Record findings in the versioned release audit directory.
- [ ] Require maintainer sign-off for any ambiguous content.

## Related

- [Release process](00-release-process.md)
- [Release checklist](01-release-checklist.md)
- [Public/private boundary](../03-pal-pack-standard/11-public-private-boundary.md)
- [Known limitations](../99-reference/known-limitations.md)
- [Third-party notices](../../THIRD_PARTY_NOTICES.md)
