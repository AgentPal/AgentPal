# Vega Source Credibility Eval

## Purpose

Check whether Vega reviews source quality instead of accepting links at face value.

## Cases

| Case | Input | Expected behavior | Pass signal |
| --- | --- | --- | --- |
| official source | Vendor docs plus current date | Mark strong for vendor's own claims, limited for competitor claims. | Source type and usable claims separated. |
| marketing source | Product landing page | Identify bias and evidence limits. | Trust not marked high for broad claims. |
| stale source | Old article on changing API | Mark freshness risk. | Confidence downgraded. |
| conflicting sources | Two sources disagree | Record contradiction and next research. | Conflict visible in matrix. |

## Failure conditions

- Popularity treated as proof.
- No access date.
- No bias note.
- No cross-check request for important claim.

