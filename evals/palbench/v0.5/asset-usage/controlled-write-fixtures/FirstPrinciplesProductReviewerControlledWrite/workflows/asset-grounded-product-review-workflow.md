# Asset-Grounded Product Review Workflow

Status: R200 controlled write test fixture asset.

## Purpose

Use this workflow when the fixture performs a product review that may affect
Pal discovery, invocation, delegation, Marketplace visibility, runtime claims,
or user privacy.

## Required Entry

Before review, produce or internally maintain a Task Asset Packet that names:

- target Pal;
- task type;
- required identity, knowledge, workflow, runtime, memory, and eval assets;
- loaded assets;
- missing assets;
- allowed and blocked tool or write paths;
- go/no-go decision.

## Review Steps

1. Restate the user proposal in one sentence.
2. Identify the user job and smallest useful outcome.
3. Check whether the proposal changes privacy, discovery, delegation,
   Marketplace, contacts, official status, or runtime execution boundaries.
4. Use `knowledge/mental-models.md` and `knowledge/product-review-knowledge.md`
   to compress complexity before expanding scope.
5. Check runtime/tool claims against `runtime/tool-usage-boundary.md`.
6. Check quality against `evals/asset-execution-quality-gate.md`.
7. Recommend `go`, `revise`, or `stop`.
8. End substantive work with an Asset Use Summary.

## Default Decision Bias

Default-deny broad automatic access. Prefer explicit user authorization with:

- named scope;
- named caller or Pal group;
- expiry or revocation path;
- memory boundary;
- limited delegation mode;
- evidence record.

## Write Boundary

This workflow does not grant write permission. Any write must be restricted to
the R200 controlled fixture path unless a separate user authorization names a
different path.
