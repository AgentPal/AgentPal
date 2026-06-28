# R140 Fresh-Clone Usability Simulation Setup

Status: pass.

Simulation date: 2026-06-29.

This setup record covers a local clean-copy usability simulation for the R139
new-user onboarding path. It is local-only evidence and does not perform remote
publication.

## Scope

| Item | Result |
| --- | --- |
| source commit | `50d3ba1` |
| clean-copy method | local repository copy with VCS/runtime cache folders excluded |
| public clean-copy path record | withheld from public records |
| clean-copy file count | 3607 |
| starting entry file | `START_HERE.md` |
| remote operation | not performed |

## Required Entry Files

| Path | Result |
| --- | --- |
| `START_HERE.md` | present |
| `docs/00-overview/what-is-agentpal.md` | present |
| `docs/01-getting-started/first-30-minutes.md` | present |
| `examples/walkthroughs/first-agentpal-team/README.md` | present |
| `docs/01-getting-started/faq.md` | present |
| `docs/00-overview/glossary.md` | present |
| `release/current/v0.5-fresh-clone-usability-checklist.md` | present |

## Setup Checks

| Check | Result |
| --- | --- |
| required R140 onboarding paths missing | pass; 0 |
| required R140 evidence paths missing after report creation | pass; 0 |
| JSON parse in clean copy | pass; 105 / 105 parsed |
| Delivery Pack JSON parse | pass; 4 / 4 parsed |
| routing-memory-record JSON parse | pass; 1 / 1 parsed |
| README START_HERE link | pass |
| README.zh-CN START_HERE link | pass |
| central roster | pass; 9 registered / 9 active |
| official Pal dirs | pass; 9 |
| official Pal `pal.json` parse | pass; 9 / 9 |
| official manifest count | pass; 1, PalSmith only |
| internal path leak | pass; 0 |
| hidden positive release claim | pass; 0 real positive claims |

## Boundary

The clean-copy path is intentionally not recorded as an absolute local path in
public files. A final clean-copy pass after creating the R140 evidence confirmed
that required R140 evidence paths were present. No GitHub API, push, pull,
fetch, tag operation, GitHub Release, release automation, connector, scanner,
validator, daemon, database, installer, marketplace, keyword router, central
roster update, official Pal update, real customer data, or real external
project `.agentpal/` write was used.
