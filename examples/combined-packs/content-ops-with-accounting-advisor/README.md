# Content Ops With Accounting Advisor Combined Pack

This is a public-safe combined Org Pack + FDE Pack example for AgentPal v0.5.

It shows how a reusable content operations Org Pack can reference a reusable
accounting advisor FDE Pack without copying customer-private evidence, Pal
bodies, central contacts, connector settings, credentials, marketplace logic,
scanner logic, validator programs, or keyword routing into the combined pack.

## References

- Org Pack: `examples/org-packs/content-ops-org-pack/`
- FDE Pack: `examples/fde-packs/accounting-advisor-fde-pack/`
- Asset boundary: `standards/asset-boundary/reusable-vs-customer-private-assets.md`
- PalSmith classification: `standards/palsmith/palsmith-asset-classification-standard.md`
- PalSmith review status: `approved_for_r123_integration_with_human_review_retained`

## Files

- `combined-pack.json`
- `ORG-FDE-COMPOSITION.md`
- `recommended-pals.md`
- `reusable-assets-map.md`
- `customer-private-boundary.md`
- `thin-binding-relationship.md`
- `verification-checklist.md`
- `palsmith-audit-note.md`

## Boundary

- This combined pack is no-code documentation and governance.
- The Org Pack reference provides reusable content operations structure.
- The FDE Pack reference provides reusable accounting advisor delivery assets.
- Recommended Pals are AI judgement inputs only.
- Customer-private accounting, tax, finance, content, and project evidence stays
  in approved private project records.
- External projects remain thin-bound and do not receive copied Org/FDE/Pals
  directories by default.
