# First Task Package Example

## Task

Create a public-safe first-pass lead segmentation from fictional lead summaries.

## Source Pack

`examples/delivery-packs/sales-crm-delivery-pack/`

## Source Boundary

The source input is fictional. Do not use real CRM exports, names, phone numbers, email addresses, account IDs, or deal amounts.

## Input

| Lead placeholder | Source category | Company size band | Interest category | Lifecycle stage | Missing evidence |
| --- | --- | --- | --- | --- | --- |
| demo-lead-001 | webinar | mid-market | product demo | new lead | decision role |
| demo-lead-002 | referral | small team | pricing question | contacted | timeline |
| demo-lead-003 | inbound form | enterprise | integration concern | proposal | compliance owner |

## Candidate Pals

- Sales Strategist Pal
- CRM Ops Pal
- Data Review Pal
- Compliance QA Pal

Candidate Pals are AI judgement inputs only.

## Requested Output

For each fictional lead:

- proposed segment;
- reason;
- missing evidence;
- suggested next human-owned action;
- review status.

## Acceptance

- no customer-private data;
- no real contact details;
- no CRM connector or API client;
- no automatic CRM update;
- human review required;
- `not-run` and `missing` preserved.
