# Acceptance Criteria

## Delivery Pack Completeness

- [ ] `delivery-pack.json` parses.
- [ ] Required files exist.
- [ ] Five flow files exist.
- [ ] Two task package files exist.
- [ ] `FAYE_BUILD_REQUEST.md` exists.
- [ ] `PAL_TEAM.md` exists.
- [ ] Integration notes are manual handoff profiles only.
- [ ] Report placeholders do not claim execution.

## Business Fit

- [ ] The pack covers lead intake, customer segmentation, follow-up copy, reminder planning, and deal review.
- [ ] Sales copy requires human review.
- [ ] Customer-private CRM data is excluded from the reusable pack.
- [ ] Missing CRM evidence remains `missing` or `not-run`.
- [ ] Compliance-sensitive content requires human confirmation.

## Public Safety

- [ ] No real customer names.
- [ ] No real CRM exports.
- [ ] No real phone numbers or emails.
- [ ] No real deal amounts.
- [ ] No credentials, tokens, cookies, API keys, webhooks, passwords, private keys, or connection strings.
- [ ] No internal system screenshots.

## Runtime Boundary

- [ ] No CRM connector.
- [ ] No API client.
- [ ] No automatic sync.
- [ ] No automatic reminder scheduling.
- [ ] No keyword routing, domain routing, role routing, or deterministic Pal assignment.
- [ ] Candidate Pals are AI judgement inputs only.

## Completion Terms

Use `pass`, `partial`, `missing`, `not-run`, `blocked`, and `requires-human-review`.

Do not convert `not-run`, `missing`, or `requires-human-review` into `pass`.
