# PalSmith Evals

These are Markdown evaluation cases for human or Runtime-assisted review. They are not scripts, tests, validators, or commands, and passing them requires current evidence from the host runtime.

- `official-registration-eval.md`: checks official Pal registration consistency.
- `registry-contacts-consistency-eval.md`: checks id/path/direct call consistency across PalSmith, registry, and contacts.
- `no-code-boundary-eval.md`: checks the no-code PalSmith boundary.
- `palsmith-release-scope-eval.md`: checks GitHub-ready release scope for PalSmith.
- `pal-quality-inspection-eval.md`: checks R16 job fitness, job expertise, and real work readiness inspection behavior.
- `user-material-ingestion-eval.md`: checks content-preserving user material ingestion into knowledge, skills, workflows, runbooks, templates, and evals.
- `content-preservation-eval.md`: checks source inventory, no over-compression, traceable extraction, and retention of important user-supplied content.
- `web-research-to-knowledge-eval.md`: checks optional web research planning, source attribution, freshness, uncertainty, and conversion into Pal knowledge assets.
- `palsmith-self-health-eval.md`: checks PalSmith's own skill/knowledge depth against its formal capability claims.
- `pal-conflict-detection-eval.md`: checks v0.2 conflict detection behavior.
- `pal-team-design-eval.md`: checks v0.2 team design before creation.
- `pal-version-governance-eval.md`: checks v0.2 version upgrade and rollback governance.
- `pal-eval-lab-eval.md`: checks v0.2 Pal Eval Lab behavior.
- `palsmith-v0.2-capability-eval.md`: checks the v0.2 capability file set and no-code boundary.
- `ai-team-builder-eval.md`: checks v0.3 AI Team Builder behavior.
- `pal-team-governance-eval.md`: checks v0.3 team governance behavior.
- `cross-pal-review-eval.md`: checks v0.3 independent review behavior.
- `pal-publish-quality-gate-eval.md`: checks v0.3 publish quality gate behavior.
- `pal-readiness-matrix-eval.md`: checks v0.4 lifecycle, Eval Lab, and publish readiness matrix behavior.
- `pal-runtime-call-verification-eval.md`: checks v0.3 direct-call verification levels.
- `github-import-verification-eval.md`: checks v0.3 GitHub import verification levels.
- `palsmith-v0.3-capability-eval.md`: checks the v0.3 capability file set, delegation wording, and no-code boundary.

## Evidence Style

Record concrete file paths inspected, JSON parse results, forbidden-file search results, forbidden-direction search results, and `not-run` items. Do not treat example task packages as proof that a real Runtime action has already happened.
