# Design Tool Selection Skill

## Purpose

Choose the right runtime, model, reasoning strength, Skill, plugin, MCP, or external tool combination for a design task.

## Method

1. Classify the task: brand, logo, UI, page, poster, social, video, review, prototype, or production.
2. Identify required outputs and evidence.
3. Check current host capability evidence or mark `unknown`.
4. Select candidate tools and fallback.
5. State model/reasoning needs.
6. Preserve tool references as candidates, not routes.

## Output

Compact Agent-use style decision:

- owner Pal;
- verifier Pal;
- runtime/tool candidates;
- capability source;
- selected mode;
- evidence required;
- authorization needed;
- fallback.

## Boundary

No plugin, MCP, paid tool, API, Figma, Product Design, ImageGen, or external Agent invocation is claimed unless it actually happened.
