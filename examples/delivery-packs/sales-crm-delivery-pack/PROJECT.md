# Project Context

## Fake Business Scenario

A fictional B2B sales team wants AI assistance for lead organization, customer segmentation, follow-up message drafting, reminder planning, and deal review.

The team has a CRM, team chat, and email system, but this reusable pack does not connect to any of them. It describes manual handoff boundaries and reusable no-code workflows only.

## Fictional Inputs

Allowed public-safe demo inputs:

- lead source category, such as webinar, referral, inbound form, or partner list;
- generic company-size band, such as small, mid-market, or enterprise;
- generic interest category, such as product demo, pricing question, or renewal;
- fictional lifecycle stage, such as new lead, contacted, qualified, proposal, or inactive;
- non-identifying risk note, such as needs legal review or unclear budget.

Forbidden inputs in this reusable pack:

- real customer names;
- real account IDs;
- real CRM exports;
- real phone numbers or email addresses;
- real deal amounts;
- contracts, invoices, legal, tax, medical, or financial records;
- credentials, tokens, cookies, API keys, webhooks, or connection strings;
- screenshots of internal systems.

## Assumptions

- Sales data is provided as a manually prepared, de-identified summary.
- A human sales owner reviews every customer-facing message.
- Compliance QA reviews regulated or sensitive claims.
- Private CRM data stays in customer-private records.
- Integration profiles remain manual handoff notes.

## Success Criteria

- Leads can be mapped into public-safe segmentation categories.
- Follow-up copy can be drafted from generic context.
- Reminder cadence can be proposed without automatic scheduling.
- Deal reviews can identify missing evidence and next actions.
- The reusable pack remains free of customer-private data.

## Risk Register

| Risk | Boundary |
| --- | --- |
| Customer privacy leak | Keep real CRM data in customer-private records. |
| Overconfident sales claims | Human review required before use. |
| Compliance-sensitive messaging | Compliance QA candidate review and human confirmation required. |
| CRM integration confusion | Manual handoff only; no connector or API client. |
| Reminder automation confusion | Reminder plan only; no automatic scheduling. |
