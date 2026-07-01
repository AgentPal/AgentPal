# PalSmith v0.5 Release Checklist

This checklist is for a local release-preparation review. It does not authorize remote publication.

## Required Local Checks

- [ ] `agentpal.json` parses as JSON.
- [ ] `official/pals/PalSmith-pal-governor/pal.json` parses as JSON.
- [ ] `workspace/resources/user-pals/FirstPrinciplesProductReviewer/pal.json` parses as JSON when the user custom Pal test artifact is in scope.
- [ ] `RESOURCE_INDEX.md` lists the PalSmith v0.5 user docs and evidence files.
- [ ] PalSmith release-prep docs are present.
- [ ] PalSmith R193 evidence files are present.
- [ ] Pal Asset Execution docs are linked from `docs/README.md` and PalSmith docs.
- [ ] Release notes include Pal Asset Execution Contract without overstating tool capability.
- [ ] Release notes distinguish representative host regression evidence from scoped certification.
- [ ] Markdown links in the added docs point to existing local files.
- [ ] `git diff --check` has no content errors.

## Boundary Checks

- [ ] Official Pal directory count remains 10.
- [ ] `workspace/organization/contacts/` has no unauthorized diff.
- [ ] `official/pals/` has no unauthorized roster or official Pal addition.
- [ ] User custom Pal remains `official: false`.
- [ ] User custom Pal remains private by default unless scoped authorization evidence says otherwise.
- [ ] Discovery, invocation, delegation, contacts registration, and Marketplace draft permissions remain separate.
- [ ] No AgentPal runtime backend, CLI, installer, scanner, daemon, connector, validator program, or app runtime is introduced.
- [ ] No Marketplace backend or public listing is claimed.
- [ ] User custom Pal, controlled-write fixture, and official Pal statuses are not mixed.
- [ ] R200 fixture is described as a test artifact, not a real user custom Pal upgrade.
- [ ] No release notes claim all official Pals have been individually migrated to the Pal Asset Execution Contract.
- [ ] No release notes claim official Pal task-family certification without a scoped certification record.

## Remote Publication Gate

Do not perform any remote action unless the user explicitly authorizes it in the current task.

Remote actions include:

- `git push`
- `git pull`
- `git fetch`
- tag creation
- tag push
- GitHub Release creation
- release asset upload

If a remote action is not authorized, the correct result is local readiness evidence only.

## Release Notes Gate

Before a public pre-release:

- [ ] Release notes say PalSmith is no-code Pal asset governance.
- [ ] Release notes say AgentPal is not an Agent Runtime.
- [ ] Release notes separate current features from future work.
- [ ] Release notes do not claim automatic discovery, Marketplace backend, scanner, daemon, connector, app runtime, or remote publication.
- [ ] Release notes state that tools are not Pal assets.
- [ ] Release notes keep Luma-style evidence as fixture/example evidence, not a real Luma change.
- [ ] Known limits are linked or summarized.

## Decision Values

Use one of these values:

- `release_prep_ready_for_user_review`
- `release_prep_ready_for_remote_authorization_decision`
- `blocked_by_missing_evidence`
- `blocked_by_boundary_overclaim`
- `blocked_by_unreviewed_file_change`

R193 target decision: `release_prep_ready_for_user_review`.
