# Sales Reminder Flow

## Purpose

Design a reusable reminder cadence for sales follow-up without scheduling anything automatically.

## Reminder Cadence Example

| Stage | Reminder idea | Review |
| --- | --- | --- |
| new lead | same-day review by sales owner | human owner confirms |
| contacted | follow-up planning after waiting period | human owner confirms |
| proposal | check missing decision criteria | human owner confirms |
| inactive | decide nurture or close loop | human owner confirms |

## Steps

1. Identify lifecycle stage.
2. Review last known public-safe activity summary.
3. Propose next reminder intent.
4. Mark missing evidence.
5. Ask a human sales owner to approve cadence.
6. Record as plan only.

## Candidate Pals

- CRM Ops Pal
- Sales Strategist Pal
- Data Review Pal

## Boundary

This flow does not create calendar events, send reminders, call CRM APIs, or run automatic scheduling.
