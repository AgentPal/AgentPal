# source-inventory-knowledge

## Concept Explanation

A source inventory is a structured record of sources, metadata, trust level, key points, relevance, target asset, and coverage status.

## Judgement Standards

- Each source gets a stable Source ID.
- Access date is required for web evidence.
- Source type and trust level must be explicit.
- Each source maps to at least one research question, claim, or asset target.
- Gaps are recorded instead of hidden.

## Examples

- SRC-10 supports source metadata and citations for deep research workflows.
- SRC-13 supports competitive research criteria.

## Counterexamples

- A list of links with no dates.
- A report with citations but no source coverage.

## Scope

Use for multi-source research, handoff, and knowledge distillation.

## How This Becomes Skill, Workflow, Or Eval

Skill: source-inventory-building. Workflow: source-inventory. Eval: evidence matrix and source credibility evals.

## Common Mistakes

Copying source content into the inventory, missing coverage, and using unstable source labels.

## Source Refs Or Local Notes

Based on SRC-02 and SRC-10 plus `research/source-inventory.md`.

