# Model Routing Policy

## Core Rule

Use the strongest available model for understanding, planning, prompt shaping, and final verification only when needed.

Use lower-cost models or non-Pal runtimes for clear, bounded execution tasks.

## Routing factors

- task complexity maps to model tier
- task risk maps to reasoning strength
- task ambiguity maps to prompt detail
- cost requirements may favor lower-cost execution
- context complexity may require a stronger model to compress and supervise

## Weak model prompt shaping

When using weaker or lower-cost models:

- provide exact objective
- provide file boundaries
- provide required documents
- provide forbidden changes
- provide acceptance commands
- require final report with changed files, verification, risks, and blockers
- avoid broad product or architecture judgment

## AI Routing Judgement Boundary

Model routing is separate from Pal owner selection. It may inform prompt detail, reasoning strength, verification depth, and cost tradeoff, but it must not become a semantic task-to-Pal map.

No hard-coded semantic routing. AI routing judgement is case-by-case. Pal capability reference is not a route map.

## Explainability

When the user asks why a task was routed this way, explain the task type, available runtime facts, model strength, cost/quality tradeoff, prompt-shaping approach, and verification plan.


