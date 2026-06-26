# Vega Research Capability Eval

## Purpose

Check whether Vega can act as Research / Intelligence Lead Pal instead of a simple source summarizer.

## Cases

| Case | Input | Expected behavior | Pass signal |
| --- | --- | --- | --- |
| vague research | "Research agent platforms" | Ask or infer bounded question, scope, source need, and output purpose. | Research intake and question frame exist. |
| latest facts | "Check the latest pricing" | Require Runtime web evidence and source access date. | Says web research needed if not run. |
| multi-source report | "Use these links and advise" | Build inventory, credibility notes, matrix, and synthesis. | Source IDs and confidence appear. |
| handoff | "Give Atlas what it needs" | Produce research handoff packet with evidence and implementation questions. | Atlas receives source IDs, constraints, and risks. |

## Failure conditions

- Unsupported current facts.
- No source inventory for multi-source work.
- Recommendation without confidence.
- Runtime execution claim without evidence.

