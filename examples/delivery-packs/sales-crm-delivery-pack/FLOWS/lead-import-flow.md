# Lead Import Flow

## Purpose

Turn a manually provided, public-safe lead summary into a clean lead review table for downstream segmentation.

This flow does not import real CRM exports and does not connect to a CRM.

## Inputs

Allowed:

- lead source category;
- company size band;
- industry category;
- interest category;
- lifecycle stage;
- non-identifying notes;
- missing-field markers.

Forbidden:

- real customer names;
- real emails or phone numbers;
- real account IDs;
- real CRM export files;
- credentials or CRM connection details.

## Steps

1. Confirm source sensitivity.
2. Reject real CRM data from the reusable pack.
3. Normalize public-safe fields.
4. Mark missing evidence as `missing`.
5. Prepare a lead review table for human review.
6. Hand off private data handling to customer-private records when needed.

## Candidate Pals

- CRM Ops Pal
- Data Review Pal
- Compliance QA Pal

Candidate Pals are AI judgement inputs only.

## Output

A public-safe lead review table template with fictional or de-identified rows only.

## Human Review

Required before any real CRM data is used.
