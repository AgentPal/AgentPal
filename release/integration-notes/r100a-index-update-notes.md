# R100-A Index Update Notes

Date: 2026-06-28

## Purpose

This note records shared-entry update suggestions for R100-A. R100-A does not
modify `README.md`, `RESOURCE_INDEX.md`, `agentpal.json`, central roster files,
or `official/pals/**`.

## Added Artifacts

- `standards/pal-asset/pal-json-v0.5-standard.md`
- `standards/pal-asset/asset-manifest-standard.md`
- `standards/schemas/pal.schema.json`
- `standards/schemas/pal-asset-manifest.schema.json`
- `templates/pal-asset/pal-json-template.json`
- `templates/pal-asset/asset-manifest-template.json`
- `evals/palbench/pal-asset/r100a-pal-metadata-schema-boundary.md`
- `release/fresh-clone-checks/r100a-local-pal-metadata-schema-validation.md`

## Suggested Future Shared Entry Updates

When a later integration round is allowed to edit shared public entry points,
consider adding these references to the Pal Asset / metadata sections:

- Pal JSON v0.5 standard:
  `standards/pal-asset/pal-json-v0.5-standard.md`
- Asset manifest standard:
  `standards/pal-asset/asset-manifest-standard.md`
- Pal schema:
  `standards/schemas/pal.schema.json`
- Pal asset manifest schema:
  `standards/schemas/pal-asset-manifest.schema.json`
- Pal JSON template:
  `templates/pal-asset/pal-json-template.json`
- Asset manifest template:
  `templates/pal-asset/asset-manifest-template.json`
- R100-A boundary eval:
  `evals/palbench/pal-asset/r100a-pal-metadata-schema-boundary.md`
- R100-A validation:
  `release/fresh-clone-checks/r100a-local-pal-metadata-schema-validation.md`

## Boundary Notes

- Do not treat the schemas as runtime validators or scanners.
- Do not modify official Pal manifests during index integration.
- Do not modify central contacts during index integration.
- Keep `keyword_routing_allowed=false`.
- Keep `external_project_write_allowed_by_default=false`.
- Keep `credentials_allowed=false`.
- Preserve legacy Pal manifest compatibility until an explicit official Pal
  metadata upgrade round is approved.
