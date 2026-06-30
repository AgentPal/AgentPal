# R191 External User Readability Review

## Review Perspective

Reviewer perspective: a new external user who did not participate in R168-R190.

Files reviewed:

- `docs/06-palsmith/README.md`
- `docs/06-palsmith/custom-pal-creation-to-authorization-flow.md`
- `docs/06-palsmith/user-custom-pal-discovery-authorization.md`
- `docs/06-palsmith/user-custom-pal-discovery-authorization-protocol.md`
- `prompts/palsmith/authorize-user-custom-pal-discovery.md`
- `prompts/palsmith/revoke-user-custom-pal-discovery.md`
- `templates/palsmith/user-custom-pal-authorization-record.md`
- `templates/palsmith/user-custom-pal-discovery-policy.md`

## Findings

| Question | Result | Note |
| --- | --- | --- |
| Can the user understand what PalSmith can create? | pass | `docs/06-palsmith/README.md` and `docs/PalSmith.md` describe Pal creation, Pal Team design, and governance work. |
| Can the user understand draft Pal Pack vs user custom Pal? | pass | The flow document separates draft review artifacts from installed user custom Pals. |
| Can the user find the draft-to-custom path? | pass | The flow document and README link to `install-draft-as-custom-pal.md`. |
| Can the user understand why custom Pal discovery is off by default? | pass | The authorization guide states private-by-default and disabled defaults. |
| Can the user understand how to enable discovery? | pass | The authorization prompt and guide explain scoped authorization. |
| Can the user understand discovery is not delegation? | pass | The guide and protocol now repeat that discovery does not allow automatic delegation. |
| Can the user understand contacts registration is not default? | pass | Contacts registration is listed as a separate governance task. |
| Can the user understand Marketplace draft is not listing? | pass | The guide distinguishes draft metadata from public listing and backend capability. |
| Can the user understand how to revoke authorization? | pass | R191 strengthens the revocation prompt and links it from the flow and docs index. |
| Can the user tell no-code flow from runtime implementation? | pass | Docs and prompts explicitly deny runtime, CLI, scanner, daemon, connector, backend, and Marketplace backend claims. |

## Minimal Fixes Applied

R191 applied these readability fixes:

- added `docs/06-palsmith/user-custom-pal-discovery-authorization-protocol.md` as a docs-side entry pointing to the canonical PalSmith protocol;
- linked the protocol and revocation prompt from user-facing docs;
- strengthened `prompts/palsmith/revoke-user-custom-pal-discovery.md` with explicit revocation record shape and post-revocation state;
- strengthened `templates/palsmith/user-custom-pal-authorization-record.md` with audit-preserving post-revocation fields.

## Readability Result

`readability_result: pass`

The flow is understandable after R191 minimal fixes. Remaining improvement is optional: a one-page quick card could reduce reading time for non-technical users.
