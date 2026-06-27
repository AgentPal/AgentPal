# Runtime Skill-aware Coordination Example

## User Input

"Can you use the browser Skill to check the report page and remember if it works?"

## Mira Shape

Mira keeps Conductor responsibility and names candidates:

- owner/verifier Pal candidate: Quinn, because the deliverable is a verification result.
- host Runtime candidate: current Runtime.
- Runtime Skill candidate: browser inspection Skill, availability unknown.
- fallback: mark browser evidence `not-run` and provide a manual checklist or ask for a browser-capable Runtime.
- memory: Runtime Skill Usage Memory only after current evidence exists.

## Boundary

Mira does not call or scan Runtime Skills. Candidate does not mean fixed route.
