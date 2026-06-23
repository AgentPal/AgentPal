# Prompt Shaping Policy

Prompt detail depends on model and runtime capability.

AgentPal v0.1 uses Simple Pal Mode only. Prompt shaping must not include instructions to probe, call, or narrate separate runtime workflows.

## Strong Model

Give goal, context, constraints, open tradeoffs, risk analysis, and verification strategy.

## Medium Model

Give explicit file or task scope, expected output, constraints, and acceptance checks.

## Weaker Or Lower-Cost Model

Give exact steps, strict boundaries, forbidden changes, acceptance commands, and final report format. Avoid broad architecture or product judgment.

Mira should use runtime-awareness notes to compensate for weaker models with clearer prompts.

## Specialist Prompts

When shaping a prompt for a specialist Pal, include:

- owner Pal
- consultant Pal(s)
- reviewer Pal(s)
- case-specific AI routing judgement
- task family
- specialist assets used
- Knowledge gap
- fallback allowed
- fallback method
- repeated task record
- execution layer
- evidence review

If specialist assets are missing, say fallback method is allowed only when reported. Do not let Mira own specialist learning; domain learning belongs to the specialist Pal.

No hard-coded semantic routing. The selected owner, consultants, and reviewers must come from case-by-case judgement, not keyword triggers or task-domain tables. Pal capability reference is not a route map.

Use clearer prompts for lower-cost or weaker models, especially for safety, evidence, and permission boundaries.

