# R161 Docs Directory Keep / Rewrite / Delete Matrix

## Summary Counts

| Category | Count |
| --- | ---: |
| keep_current | 62 |
| rewrite_required | 93 |
| move_to_evidence_archive | 39 |
| delete_obsolete | 0 |
| Total audited docs files | 194 |

## Directory Matrix

| Directory | File count | Category | Decision |
| --- | ---: | --- | --- |
| `docs/00-overview/` | 18 | rewrite_required | Rewrite as current v0.5 overview set. |
| `docs/01-concepts/` | 10 | rewrite_required | Merge or rewrite duplicated concept tracks. |
| `docs/01-getting-started/` | 3 | keep_current | Keep, then lightly align during R162. |
| `docs/02-concepts/` | 7 | rewrite_required | Resolve duplication with `01-concepts`. |
| `docs/02-getting-started/` | 10 | rewrite_required | Reconcile with `01-getting-started`. |
| `docs/03-pal-pack-standard/` | 17 | keep_current | Keep as Pal Pack standard body. |
| `docs/03-user-guides/` | 6 | keep_current | Keep as user guide base. |
| `docs/04-runtime-guides/` | 10 | rewrite_required | Tighten Codex-first and non-Codex evidence limits. |
| `docs/04-usage-scenarios/` | 1 | keep_current | Keep as scenario doc. |
| `docs/05-orchestration-methodology/` | 23 | rewrite_required | Keep methodology, but separate current no-code protocols from future/runtime claims. |
| `docs/06-collaboration/` | 7 | keep_current | Keep as collaboration docs. |
| `docs/06-palsmith/` | 2 | keep_current | Keep. |
| `evals/palbench/v0.5/documentation/archive/docs/06-validation-and-evidence/` | 7 | move_to_evidence_archive | Move away from first-entry user docs. |
| `docs/07-authoring-pals/` | 18 | keep_current | Keep as authoring docs. |
| `docs/07-memory-and-learning/` | 6 | keep_current | Keep, with future privacy wording pass. |
| `docs/07-official-pals/` | 2 | keep_current | Keep and align with 10-Pal current roster. |
| `evals/palbench/v0.5/documentation/archive/docs/08-release-and-maintenance/` | 7 | move_to_evidence_archive | Keep as maintenance/release evidence. |
| `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/` | 1 | move_to_evidence_archive | Archive or merge into release evidence. |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/` | 13 | move_to_evidence_archive | Keep as roadmap/history, not current behavior. |
| `docs/99-reference/` | 11 | rewrite_required | Rewrite or split reference vs historical compatibility. |
| `docs/archive/` | 5 | move_to_evidence_archive | Keep as archive. |
| `docs/` root files | 4 | rewrite_required | Normalize or move duplicate runtime docs. |
| `evals/palbench/v0.5/documentation/archive/docs/research/` | 6 | move_to_evidence_archive | Keep as research, not user-facing current docs. |

## R162 Restructure Principle

R162 should separate the docs tree into:

- current user docs
- authoring and Pal Pack standards
- runtime adapter guides with explicit evidence limits
- release/eval/history archive
- research/future design archive

