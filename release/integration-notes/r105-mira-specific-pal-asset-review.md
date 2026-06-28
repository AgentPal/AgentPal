# R105 Mira-Specific Pal Asset Review

Date: 2026-06-28

## Purpose

R105 performs a Mira-specific review before adding or expanding public-safe
indexes for Mira `memory/` and `research/`.

This is a local Markdown / validation round. It is not a GitHub sync, tag,
release, `pal.json` metadata upgrade, or `asset-manifest.json` generation round.

## Source Of Truth

Mira was resolved from the central roster:

| Field | Value |
| --- | --- |
| roster path | `workspace/organization/contacts/pals.json` |
| id | `mira-main` |
| display name | `Mira` |
| status | `active` |
| role | `main-leader-conductor` |
| `is_main_pal` | `true` |
| `pack_path` | `official/pals/Mira-main` |

## Mira Root Entry Review

| Entry | Status | R105 action |
| --- | --- | --- |
| `README.md` | present | Read for public overview and team-leadership asset boundary. |
| `PAL.md` | present | Read for identity, owner boundary, project workgroup wording, and memory/knowledge notes. |
| `AGENTS.md` | present | Read for runtime-facing load order and Simple Pal Mode boundaries. |
| `SKILL.md` | present | Read for Pal Pack entry and Mira invocation boundary. |
| `pal.json` | present / parses | Read only; unchanged. |

## Directory Review

| Directory | Finding | R105 action |
| --- | --- | --- |
| `memory/` | Existing `README.md` was present but too thin for the v0.5 public-safe memory boundary. | Expanded `README.md` as documentation-only index. |
| `research/` | `source-inventory.md` and `source-coverage-matrix.md` existed; no README/index existed. | Added `README.md` as documentation-only index. |
| `knowledge/` | Existing stable Mira knowledge assets and `INDEX.md` existed. | Read by directory listing only; no content moves. |
| `reports/` | Handoff/task report placeholder directories existed. | Read placeholders; no content moves. |
| `state/` | Release-safe placeholder README existed. | Read placeholder; no state write. |

## Mira-Specific Findings

- Mira is the default Main Pal, Leader Pal, and Conductor, not a normal
  specialist Pal. Index backfill must preserve this special boundary.
- Mira may steward memory candidates and knowledge candidates, but specialist
  professional learning still belongs to the judged owner Pal.
- Mira `research/` contains source-context assets that support leader and
  conductor methods. They should remain research until reviewed and promoted.
- Existing root-entry wording about external project facts and `.agentpal/`
  should be treated as review-sensitive for a separate entry-file update. R105
  does not edit root entries.

## Changed Public Files

| File | Change type | Boundary |
| --- | --- | --- |
| `official/pals/Mira-main/memory/README.md` | expanded index | Documentation-only memory boundary. |
| `official/pals/Mira-main/research/README.md` | new index | Documentation-only research boundary. |
| `evals/palbench/pal-asset/r105-mira-specific-memory-research-boundary.md` | new eval | R105 acceptance gate. |
| `release/fresh-clone-checks/r105-local-mira-specific-memory-research-validation.md` | new validation | Local evidence record. |
| `release/integration-notes/r105-mira-specific-pal-asset-review.md` | new integration note | Review and scope record. |

## Forbidden Actions Confirmed

R105 does not:

- modify any official Pal `pal.json`;
- modify central contacts or registry files;
- generate a real `asset-manifest.json`;
- move, delete, rename, or reclassify existing Mira assets;
- copy reports into memory;
- promote research directly into knowledge;
- add a runtime Agent Skill under Mira `skills/`;
- create keyword, domain, role, or deterministic routing maps;
- create a CLI, Web App, Desktop App, scanner, validator, daemon, database,
  connector, marketplace, hub, auto-sync engine, or auto-execution engine;
- write Mira memory or research into an external project `.agentpal/`;
- push, pull, fetch, tag, or create a GitHub Release.

## Decision

Decision: pass with a follow-up warning.

The Mira memory and research indexes are safe to backfill because they document
directory responsibility, public safety, external project boundaries, and
promotion paths without changing Pal behavior. A separate future round should
review root-entry project memory wording if maintainers want the oldest
`.agentpal` language aligned with the current v0.3 thin-binding policy.
