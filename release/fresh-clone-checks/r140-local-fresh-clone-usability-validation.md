# R140 Local Fresh-Clone Usability Validation

Status: pass.

Validation date: 2026-06-29.

This validation covers the R140 local clean-copy usability simulation. It does
not prove or perform remote publication.

## Required R140 Artifacts

| Artifact | Result |
| --- | --- |
| setup record | pass |
| START_HERE walkthrough result | pass |
| first-30-minutes walkthrough result | pass |
| first AgentPal team walkthrough result | pass |
| usability issues file | pass |
| evidence review | pass |
| R141 readiness decision | pass |

## Structured Validation

| Check | Result |
| --- | --- |
| JSON parse | pass; 105 / 105 parsed |
| Delivery Pack JSON parse | pass; 4 / 4 parsed |
| routing-memory-record JSON parse | pass; 1 / 1 parsed |
| `agentpal.json` parse | pass |
| clean-copy pass | pass |
| required R140 paths missing | pass; 0 |
| required R140 evidence paths missing in final clean copy | pass; 0 |
| markdown link check on entry path | pass; 0 broken links |
| internal path leak | pass; 0 hits |
| hidden positive release claim | pass; 0 real positive claims; 1 historical negative raw hit reviewed |
| central roster | pass; 9 registered / 9 active |
| official Pal dirs | pass; 9 |
| official Pal `pal.json` parse | pass; 9 / 9 |
| official manifest count | pass; 1, PalSmith only |
| no keyword routing | pass |
| no connector / scanner / marketplace program | pass; 0 real expansions |
| no credential leak | pass; 0 real leaks |
| no customer-private leak | pass; 0 real leaks |
| no executable code added | pass; 0 executable changed files |
| no external project `.agentpal/delivery-pack` write | pass; 0 writes |
| no remote operation | pass |

## Clean-Copy Notes

The local clean-copy absolute path is withheld from public records. The final
clean copy included 3607 files and was checked from `START_HERE.md` through the
first-30-minutes guide, the first AgentPal team walkthrough, and the R140
evidence files.

## Scan Classification Notes

- The hidden release raw hit is an older validation line that says a historical
  tag operation was not performed. It is not a positive release claim.
- Route / program raw hits are boundary language, negative examples, or
  metadata flags. No real connector, scanner, marketplace, daemon, runtime, or
  keyword-router expansion was added.
- Credential-shaped raw hits are examples or boundary warnings. No real
  credential was found.
- Customer-private raw hits are boundary language. No real customer-private
  material was found.
- External `.agentpal` raw hits are boundary statements. No real external
  project `.agentpal` write target was created.

## Not Performed

- no `git push`;
- no `git pull`;
- no `git fetch`;
- no tag operation;
- no GitHub Release creation or modification;
- no remote publication;
- no GitHub API call;
- no release automation;
- no CLI, Web App, Desktop App, installer, scanner, validator, daemon,
  database, background service, connector, API client, marketplace, hub
  program, or keyword router addition;
- no central roster change;
- no official Pal change;
- no official manifest addition;
- no real external project `.agentpal` creation.

## Decision

R140 local fresh-clone usability simulation passes.
