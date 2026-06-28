# Customer Segmentation Flow

## Purpose

Classify leads into reusable, public-safe priority bands and follow-up categories.

## Segmentation Bands

Example bands:

- priority A: high-fit, clear need, recent engagement;
- priority B: possible fit, missing decision context;
- nurture: low urgency or education needed;
- hold: incomplete information or risk note;
- exclude: not a fit or compliance concern.

These are fictional categories, not customer-specific scoring rules.

## Steps

1. Review public-safe lead fields.
2. Identify missing evidence.
3. Apply generic segmentation criteria.
4. Flag compliance or privacy concerns.
5. Ask a human sales owner to confirm final segment.
6. Store customer-private details outside the reusable pack.

## Candidate Pals

- Sales Strategist Pal
- CRM Ops Pal
- Data Review Pal
- Compliance QA Pal

## Output

A segmentation recommendation table with:

- lead placeholder id;
- segment;
- reason;
- missing evidence;
- human review status.

## Boundary

Segmentation recommendations are not automated CRM updates.
