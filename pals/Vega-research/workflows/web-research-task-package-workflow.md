# web-research-task-package-workflow

## Trigger

Vega determines that external or current evidence is needed.

## Inputs

Question frame, source plan, search queries, source constraints, risk level, and output needs.

## Steps

1. State the research goal and subquestions.
2. List source classes and query clusters.
3. Define required metadata: title, URL, publisher, date, type, access date, and key points.
4. Ask Runtime to gather sources and avoid copying long source text.
5. Ask Runtime to include contradictions, stale-source risk, and source gaps.
6. Convert returned evidence into inventory, matrix, and synthesis.

## Decision points

- Are official or primary sources required?
- Is source freshness critical?
- Is the evidence enough for recommendation?
- Are connectors or private sources involved?

## Outputs

Runtime Task Package, source inventory, coverage matrix, and evidence matrix.

## Quality checks

Returned sources must map to subquestions and must not rely only on snippets.

## Required user confirmation

Private connectors, proprietary sources, paid sources, sensitive context, or regulated-domain advice.

## Evidence to return

Source inventory rows, access dates, coverage notes, contradictions, and confidence notes.

