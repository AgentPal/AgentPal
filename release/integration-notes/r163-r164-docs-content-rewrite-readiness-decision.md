# R163 to R164 Docs Content Rewrite Readiness Decision

## Decision

`ready_for_r164_docs_content_rewrite`

## Basis

- The `docs/` user path was narrowed.
- R161's 39 evidence/archive docs candidates were moved to `evals/palbench/v0.5/documentation/archive/docs/`.
- Duplicate root runtime guides were deleted and references were moved to `docs/04-runtime-guides/`.
- `docs/README.md` now keeps evidence and validation records out of the main user path.
- No runtime code or remote publication action was added.

## R164 Should Focus On

- Rewriting retained current docs content for v0.5.
- Normalizing the duplicated concept/getting-started tracks.
- Tightening runtime guide wording across `docs/04-runtime-guides/`.
- Keeping archive/evidence links as maintainer references, not user onboarding.

## R164 Must Preserve

- Codex-first public path.
- Claude Code as limited/minimal handoff unless future full host evidence exists.
- OpenCode and Gemini as unavailable in current evidence.
- Plan Mode UI unavailable.
- Goal Mode limited.
- No connector / scanner / daemon / marketplace / app runtime claims.
- No public customer data or internal path leakage.

