# R97 Org Pack Foundation Boundary Eval

Date: 2026-06-28

Owner Pal: Quinn

## Scope

This eval checks the first v0.5 local Org Pack foundation. It is a Markdown boundary regression, not an executable validator and not a marketplace certification.

## Checks

| Check | Expected |
| --- | --- |
| Org Pack standard exists | `standards/org-pack/org-pack-standard.md` exists. |
| Base Org Pack template exists | `templates/org-pack/base-org-pack/` exists with `ORG.md`, `org.json`, `README.md`, governance, workflows, capability-inventory, verification, memory policy, and customer-private boundary files. |
| Base Org Pack example exists | `examples/org-packs/base-agentpal-org-pack/` exists with public-safe example files. |
| `org.json` files parse | Template and example JSON parse. |
| No credentials | Org Pack template and example do not contain real credentials or private secrets. |
| No connector | Org Pack template and example do not include connector behavior or API client behavior. |
| No scanner / validator | Org Pack template and example do not include scanner or validator programs. |
| No marketplace program | Org Pack template and example do not include a marketplace or hub program. |
| No keyword routing | Org Pack template and example do not include active `keyword_map`, `domain_map`, `role_map`, deterministic route tables, or task-domain-to-Pal assignment. |
| No copied central roster | Org Pack template and example reference central contacts but do not copy `workspace/organization/contacts/pals.json`. |
| No external project `.agentpal/org-pack` write | Org Pack docs state that external projects remain thin-bound and Org Pack assets are not written into external `.agentpal/org-pack/` by default. |
| Recommended Pals are judgement inputs | Example recommended Pals are labeled AI judgement input only. |
| Customer-private boundary exists | Template and example separate reusable and customer-private assets. |

## Prohibited Active Behaviors

This eval fails if R97 introduces:

- installer
- marketplace or hub program
- daemon
- database
- connector
- API client
- credential store
- auto sync engine
- auto execution engine
- scanner
- validator
- keyword router
- copied central roster
- external project `.agentpal/org-pack/` default write
- real customer-private data in public examples

## Expected Decision

R97 passes when the standard, template, example, eval, validation, and index updates exist; JSON parsing succeeds; and boundary searches classify hits as forbidden, boundary, example, eval, or historical contexts with no active implementation.
