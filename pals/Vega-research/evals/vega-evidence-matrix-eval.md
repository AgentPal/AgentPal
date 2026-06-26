# Vega Evidence Matrix Eval

## Purpose

Check whether Vega aligns claims with evidence, Source IDs, confidence, contradictions, open questions, and next research.

## Cases

| Case | Input | Expected behavior | Pass signal |
| --- | --- | --- | --- |
| recommendation draft | Draft claims plus sources | Convert to claim rows and attach Source IDs. | Required columns present. |
| unsupported claim | Claim with weak source | Mark low confidence or unsupported. | Claim downgraded or open. |
| contradiction | Sources conflict | Add contradiction and next research. | Conflict not hidden. |
| knowledge update | Research should become knowledge | Matrix supports writeback candidate. | Source IDs and owner Pal appear. |

## Failure conditions

- Claims without source IDs.
- Confidence without rationale.
- Contradictions omitted.
- Next research absent where evidence is insufficient.

