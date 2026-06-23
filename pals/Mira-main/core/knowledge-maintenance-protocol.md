# Knowledge Maintenance Protocol

Mira may maintain public, release-safe AgentPal knowledge.

## Suitable knowledge

- AgentPal usage guidance
- Pal Pack rules
- `/pal Name` protocol
- project workgroup rules
- runtime-awareness concepts
- safety and troubleshooting guidance

## Not suitable

- private user facts
- private project details
- internal development notes
- copied long third-party documentation
- secrets or credentials
- specialist domain advice that belongs in another Pal

## Update flow

1. Identify the source.
2. Check whether it is public and release-safe.
3. Summarize; do not copy long source text.
4. Mark stale or uncertain context.
5. Write a knowledge candidate when review is needed.
6. Update indexes only after deciding the static/runtime boundary.

## Specialist Knowledge Gaps

Mira should not own specialist learning.

Specialist knowledge gaps belong to the specialist Pal.

If a specialist Pal lacks a dedicated Skill, Knowledge Card, Runbook, or Workflow, the owner Pal may use fallback method and should record the gap under its own `learning/knowledge-gaps.md`.

If the user explicitly asks to save a Skill, or similar operations happen more than 3 times, the owner Pal must create the formal Skill under its own `skills/` directory:

- formal Skill path: `pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md`
- human notes path: `pals/<Owner-Pal-Directory>/skills/<skill-id>/README.md`
- index update: `pals/<Owner-Pal-Directory>/skills/index.md`

Fallback results are not formal knowledge until reviewed. Do not write them into public knowledge as if they were approved specialist doctrine.

