# R163 Docs Directory Restructure Summary

## Scope

R163 restructured the `docs/` directory so the main user path no longer carries validation reports, release-history docs, roadmap history, or research/evidence records.

This round did not rewrite the root README pair, did not add runtime code, and did not perform push, pull, fetch, tag, or GitHub Release operations.

## Main Result

The R161 `move_to_evidence_archive` set has been moved to:

```text
evals/palbench/v0.5/documentation/archive/docs/
```

The `docs/` top-level path now keeps user and integrator documentation:

- `00-overview/`
- `01-concepts/`
- `01-getting-started/`
- `02-concepts/`
- `02-getting-started/`
- `03-pal-pack-standard/`
- `03-user-guides/`
- `04-runtime-guides/`
- `04-usage-scenarios/`
- `05-orchestration-methodology/`
- `06-collaboration/`
- `06-palsmith/`
- `07-authoring-pals/`
- `07-memory-and-learning/`
- `07-official-pals/`
- `99-reference/`

## Counts

| Action | Count |
| --- | ---: |
| Moved from `docs/` to documentation archive | 39 |
| Deleted duplicate root runtime guide files | 2 |
| R161 move/archive candidates processed | 39 / 39 |
| R143-R160 key evidence deleted | 0 |
| Runtime code added | 0 |

## User Navigation

`docs/README.md` remains the user navigation entry. It links to current user docs and points maintainers to the evidence archive without exposing test流水 as the main path.

## Duplicate Runtime Guide Cleanup

Deleted duplicate root-level runtime docs:

- `docs/10-using-agentpal-with-claude-code.md`
- `docs/11-using-agentpal-with-cli-agents.md`

Current replacements:

- `docs/04-runtime-guides/02-use-with-claude-code.md`
- `docs/04-runtime-guides/03-use-with-generic-cli-agent.md`

## Decision

`ready_for_r164_docs_content_rewrite`

R164 can focus on rewriting remaining user-facing content inside the retained docs directories.

