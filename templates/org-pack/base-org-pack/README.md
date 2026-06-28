# Base Org Pack Template

This is a reusable no-code Org Pack template for AgentPal.

It is a template for organization assets, not a program, installer, marketplace package, connector, scanner, validator, daemon, database, auto sync engine, or auto execution engine.

Use this template to create a public-safe reusable organization package. Do not place real customer data, customer credentials, private project memory, or private evidence here.

## Files

- `ORG.md`
- `org.json`
- `memory-policy.md`
- `customer-private-assets-boundary.md`
- `governance/README.md`
- `workflows/README.md`
- `capability-inventory/README.md`
- `verification/README.md`

## Boundaries

- Do not copy the central Pal roster.
- Do not modify `workspace/organization/contacts/pals.json`.
- Do not store credentials or private tokens.
- Do not include real customer data.
- Do not write Org Pack assets into external project `.agentpal/` by default.
- Treat recommended Pals as AI judgement input only.
- Do not create keyword routing, domain routing, or role routing maps.
