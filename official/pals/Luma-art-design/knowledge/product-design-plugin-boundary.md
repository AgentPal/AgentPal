# Product Design Plugin Boundary

Source: local Codex Product Design plugin skills inspected during Luma creation.

## What Product Design Is Good For

- Gathering and confirming a design brief before UI work.
- Product-flow audit from captured screenshots.
- Visual ideation with exactly three image-based options after a confirmed brief.
- Image-to-code implementation from a selected visual target.
- URL-to-code or prototype workflows when the plugin route supports them.
- Design QA for coded Product Design prototypes.

## Important Boundaries

- `get-context` is mandatory before Product Design ideation, prototyping, redesign, image-to-code, or product UI work when the brief is not already confirmed.
- `ideate` generates visual alternatives and stops for selection before build.
- `image-to-code` requires a selected image, screenshot, mockup, or ImageGen result; a written brief alone is not enough.
- `audit` requires captured screenshots and evidence; it is not a loose opinion.
- The Product Design plugin does not replace Luma's design judgement, brand memory, logo thinking, tool selection, or collaboration with other Pals.

## Luma Use

Luma should choose Product Design when the task needs product UI exploration, prototype generation, screenshot-based audit, or faithful code implementation from a visual target.

For logo, brand identity, poster, cover, social image, or broad art direction, Luma may use ImageGen or a specialized design tool first, then use Product Design only if UI/prototype work follows.
