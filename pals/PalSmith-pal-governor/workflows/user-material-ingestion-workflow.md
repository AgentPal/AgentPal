# User Material Ingestion Workflow

Status: R16 v0.4-fix no-code workflow.

Use this workflow when a user provides notes, transcripts, documents, SOPs, examples, product materials, or domain references for a Pal.

## Flow

1. Confirm the material scope, privacy level, allowed reads, and intended Pal target.
2. Create a source inventory with path or source label, owner, date if known, source type, sensitivity, and intended use.
3. Extract content with preservation notes: important terms, examples, decision rules, step sequences, edge cases, constraints, and quoted fragments that must remain close to the source.
4. Classify material into knowledge, skill, workflow, runbook, template, eval, output contract, governance note, and open question.
5. Produce proposed asset paths and explain why each asset type fits the source content.
6. Run a content preservation review before writing or publishing derived assets.
7. After Runtime writes assets, review evidence against the source inventory and report `done`, `missing`, `not-run`, and residual risk.

## Acceptance

- The output includes a source inventory and classification table.
- Important source content is traceable back to the source label.
- Long materials are split into appropriate assets rather than flattened into one brief summary.
- Sensitive or private material is not written into public release content without explicit approval.

## Boundary

The Runtime reads or writes only approved material and paths. PalSmith must not infer approval from the existence of an attached file.
