# Vega Research Synthesis Eval

## Purpose

Check whether Vega turns evidence into useful synthesis rather than source-by-source summary.

## Cases

| Case | Input | Expected behavior | Pass signal |
| --- | --- | --- | --- |
| evidence set | Inventory and matrix | Answer first, then facts, inferences, recommendation, uncertainty. | Sections are separated. |
| low confidence | Weak or single-source evidence | Avoid strong recommendation. | Recommendation boundary stated. |
| source gap | Missing current source | Mark gap and needed next research. | No fake current claim. |
| user decision | Tradeoff depends on criteria | Ask or state decision needed. | User decision needed appears. |

## Failure conditions

- Only summarizes each source.
- No uncertainty section.
- Recommendations presented as fact.
- Copying source text.

