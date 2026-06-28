# R103-C PalSmith Runbooks README Policy Pilot Summary

## Summary

R103-C adds a policy README for `official/pals/PalSmith-pal-governor/runbooks/`.

The README explains:

- runbooks are concrete operating manuals and exception-handling guides;
- runbooks are not workflows;
- runbooks are not Pal Skills;
- runbooks do not save credentials;
- runbooks do not auto-execute;
- runbooks do not create keyword routes;
- runbooks may identify `blocked` states and human review triggers;
- PalSmith runbooks are not copied into external project `.agentpal/` by default.

## Files Added

- `official/pals/PalSmith-pal-governor/runbooks/README.md`
- `evals/palbench/pal-asset/r103c-palsmith-runbooks-readme-policy-boundary.md`
- `release/fresh-clone-checks/r103c-local-palsmith-runbooks-readme-policy-validation.md`

## Boundary

This pilot does not:

- modify PalSmith `pal.json`;
- generate `asset-manifest.json`;
- move, delete, or rename existing runbooks;
- modify central contacts or registry;
- modify other official Pals;
- add connector, scanner, validator, installer, daemon, marketplace, hub, or auto execution behavior;
- perform remote Git operations.

## Current Runbooks

- `ai-team-health-check.md`
- `classify-user-materials.md`
- `pal-health-check.md`
