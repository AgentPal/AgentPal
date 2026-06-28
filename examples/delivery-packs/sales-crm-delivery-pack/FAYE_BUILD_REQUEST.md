# Faye Build Request For PalSmith

## Request Type

Delivery Pack to Pal team blueprint.

## Source Pack

`examples/delivery-packs/sales-crm-delivery-pack/`

## Faye Summary

Faye has designed a public-safe Sales CRM Delivery Pack for a fictional B2B sales team. The pack needs a candidate Pal team that can support lead intake, customer segmentation, follow-up copy, reminder planning, deal review, and compliance review without connecting to real CRM systems or storing customer-private data.

## Requested PalSmith Work

PalSmith may create or propose Pal team skeletons for:

- Sales Strategist Pal
- CRM Ops Pal
- Copywriting Pal
- Data Review Pal
- Compliance QA Pal

This request is a no-code build request. It does not authorize central roster writes, official Pal modifications, external project writes, connector creation, CRM API use, or runtime automation.

## Pal Creation Boundaries

- Candidate Pals are not central contacts until separately approved.
- Candidate Pals must not include real customer data.
- Candidate Pals must not store credentials, tokens, cookies, API keys, webhooks, or connection strings.
- Candidate Pal Skills must be role-level no-code methods, not runtime Agent Skills.
- Any future registration must go through central roster governance.

## First PalSmith Task Package

```text
goal: Draft public-safe skeletons for the Sales Strategist Pal, CRM Ops Pal, Copywriting Pal, Data Review Pal, and Compliance QA Pal.
source_pack: examples/delivery-packs/sales-crm-delivery-pack/
allowed_output: proposal only
forbidden_output: central roster edit, official Pal edit, connector, API client, external project .agentpal write
verification: candidate Pals remain AI judgement inputs only
```

## Acceptance Signal

The build request is acceptable if it lets PalSmith understand what Pal team is needed while preserving no-code, public-safe, thin-binding, and central-governance boundaries.
