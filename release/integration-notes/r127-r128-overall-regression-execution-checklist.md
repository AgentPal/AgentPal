# R127 / R128 - Overall Regression Execution Checklist

This checklist is for R128 execution. R127 only prepares it.

## Before Running Tests

- [ ] Confirm current round is regression execution, not GitHub publication.
- [ ] Confirm no `git push`, `git pull`, `git fetch`, tag creation, or GitHub Release will be performed.
- [ ] Confirm no new runtime code, scanner, validator, daemon, connector, marketplace flow, installer, or API client will be added.
- [ ] Confirm central roster and official Pal metadata are protected surfaces.
- [ ] Record current branch and worktree status.
- [ ] Record R127 planning artifact paths.

## JSON Parse

- [ ] Parse `agentpal.json`.
- [ ] Parse `workspace/organization/contacts/pals.json`.
- [ ] Parse every official Pal `pal.json`.
- [ ] Parse PalSmith `asset-manifest.json`.
- [ ] Parse Org Pack, FDE Pack, Combined Pack, and template JSON files in the regression surface.
- [ ] Record exact failures as `missing` or `invalid`; do not substitute another file.

## Clean Copy

- [ ] Create a clean temporary copy excluding `.git`, dependency folders, and generated caches.
- [ ] Confirm R127 plan, matrix, evidence map, issue template, checklist, validation, and readiness decision exist in the clean copy.
- [ ] Repeat scoped JSON parse in the clean copy.
- [ ] Count central roster entries in the clean copy.
- [ ] Count official Pal directories in the clean copy.

## Thin Binding Simulation

- [ ] Inspect `core/project-binding-thin-contract.md`.
- [ ] Inspect `templates/project-binding/`.
- [ ] Inspect combined-pack project-binding and central-project-record walkthroughs.
- [ ] Confirm external projects do not receive Org Pack, FDE Pack, Pal assets, private project records, memory, or governance files by default.
- [ ] Confirm central records remain under AgentPal Workspace paths.

## Central Roster

- [ ] Confirm `workspace/organization/contacts/pals.json` parses.
- [ ] Confirm 9 registered Pals.
- [ ] Confirm `PAL_CONTACTS.md` still reflects central contacts.
- [ ] Confirm no roster write occurred in R128 unless explicitly required by a separate approved task.

## Official Pal

- [ ] Count 9 directories under `official/pals/`.
- [ ] Parse every official Pal `pal.json`.
- [ ] Check protected diff for `official/pals/*/pal.json`.
- [ ] Check protected diff for `official/pals/*/*manifest*.json`.
- [ ] Confirm only the PalSmith manifest pilot is present unless a separate approved task says otherwise.

## PalSmith Manifest

- [ ] Parse `official/pals/PalSmith-pal-governor/pal.json`.
- [ ] Parse `official/pals/PalSmith-pal-governor/asset-manifest.json`.
- [ ] Confirm R118 pause decision remains consistent with current files.
- [ ] Confirm no full official Pal metadata rollout happened in R128.

## Org / FDE Examples

- [ ] Parse Org Pack `org.json` examples and templates.
- [ ] Parse FDE Pack `fde.json` examples and templates.
- [ ] Parse Combined Pack `combined-pack.json`.
- [ ] Confirm recommended Pals remain judgement inputs, not route maps.
- [ ] Confirm human review and public-safe boundaries remain present.

## Customer-Private Leak Scan

- [ ] Scan changed files and regression evidence surface for credential-like terms.
- [ ] Scan changed files and regression evidence surface for customer-private/private-client leakage claims.
- [ ] Review expected boundary terms as false positives only when the surrounding text is a safety rule or fake bad example.
- [ ] Record reviewed false positives.

## No Connector / Scanner / Marketplace Scan

- [ ] Scan changed files for connector/API client/marketplace/hub/installer claims.
- [ ] Scan changed files for scanner/validator/daemon/automatic scan/auto discovery claims.
- [ ] Confirm no new executable program files were added.
- [ ] Confirm AgentPal remains a Markdown/JSON/protocol workspace.

## No Keyword Routing Scan

- [ ] Scan for `keyword_map`, `domain_map`, `role_map`, and direct job-to-Pal mappings.
- [ ] Scan for domain phrases that imply fixed routes such as development to Atlas, testing to Quinn, or writing to Harper.
- [ ] Confirm any Pal capability examples are clearly non-binding judgement inputs.

## Post-Test Issue Classification

- [ ] Classify every finding with `release/integration-notes/r127-v0.5-overall-regression-issue-template.md`.
- [ ] Mark blocker/high findings as requiring R129 unless a narrow exception is justified.
- [ ] Record medium/low fixes if R128 performs any.
- [ ] Produce R128 regression results.
- [ ] Produce R128 validation record.
- [ ] Produce R128 readiness decision.

## No Push / No Tag / No Release

- [ ] Confirm no `git push` was run.
- [ ] Confirm no `git pull` or `git fetch` was run.
- [ ] Confirm no tag was created.
- [ ] Confirm no GitHub Release was created.
- [ ] Confirm R128 does not claim v0.5 public release completion.
