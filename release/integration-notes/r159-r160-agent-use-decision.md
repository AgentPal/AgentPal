# R159 to R160 Agent-use Decision

Status: decision-recorded
Date: 2026-06-29

## Decision

`codex_subagent_and_direct_tool_partial_pass_ready_for_r160_pack_evidence_tightening`

## Basis

- Real Codex background threads were created and returned merge-back evidence.
- One real Codex subagent was started and closed.
- R158 child-thread enum gap was corrected in R159 records: no actual result used `background_thread_review`.
- Explicit `pdf:pdf` and `product-design:audit` directives produced bounded direct-use evidence.
- Claude Code and CodeWhale produced minimal safe startup/handoff evidence.
- DeepSeek/DeepSeek-TUI remain version/help-only; OpenCode/Gemini remain unavailable.
- Plan Mode and Goal Mode remain recommendation-only in this run.

## R160 Direction

R160 should tighten evidence, not expand scope:

1. Add small public Delivery Pack fixtures for child review.
2. Add optional operator-captured Plan/Goal UI evidence if needed.
3. Keep non-Codex support claims tiered: minimal handoff, version/help-only, unavailable, or not-run.

## Release Boundary

No push, pull, fetch, tag, GitHub Release, external deploy, connector install, scanner, daemon, database, or marketplace workflow was performed in R159.

