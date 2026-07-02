# AgentPal Claude Code Binder Acceptance Checklist

Use this checklist when manually validating the v1 binder in a test project.

Current R220A status:

- Verified: plugin-loaded slash-command mode for `/agentpal:enable`,
  `/agentpal:status`, `/agentpal:repair`, and `/agentpal:disable`.
- Verified: local helper smoke test `evals/runtime-adapters/claude-code-binder-smoke-test.py`
  passes 7/7.
- Fallback only: natural-language requests may route to the binder in an
  interactive host session, but they are not the primary accepted path.
- Not verified: all natural-language trigger variants across all runtimes.

## Enable

- Run `/agentpal:enable` as the primary acceptance path.
- Natural-language fallback is optional and host-dependent.
- Confirm only these artifacts are created or updated:
  - `.agentpal/project.json`
  - `.agentpal/AGENTPAL.md`
  - root `CLAUDE.md` protected block

## Idempotency

- Run `/agentpal:enable` a second time.
- Confirm the `CLAUDE.md` block is not duplicated.

## Status

- Run `/agentpal:status`.
- Confirm it reports `complete`, `partial`, `damaged`, `legacy-block`, or `unbound`.

## Repair

- Delete one binding artifact or replace the block with a legacy marker block.
- Run `/agentpal:repair`.
- Confirm the missing file or missing block is restored and the final status becomes `complete` when enough data is available.

## Disable

- Run `/agentpal:disable`.
- Confirm:
  - `.agentpal/` is removed only when no other runtime binding remains
  - only the protected block is removed from `CLAUDE.md`
  - other `CLAUDE.md` content remains unchanged

## `/pal Name`

- Read the generated `CLAUDE.md` block and `.agentpal/AGENTPAL.md`.
- Confirm they describe `/pal Name` as a semantic protocol and do not hard-code Pal ownership routes.

## Evidence Archive

See `docs/release/runtime-plugin-validation-report.md` for the cross-runtime
R219/R220A validation summary.
