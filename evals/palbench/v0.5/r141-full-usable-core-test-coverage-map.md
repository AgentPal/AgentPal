# R141 Full Usable-Core Test Coverage Map

Status: ready for R142 execution.

Date: 2026-06-29.

R142 should execute a full usable-core test, not a remote publication round and
not an app/runtime test. The test should prove the v0.5 no-code framework is
usable from public package, Pal, pack, workflow, and release-decision angles.

| test_group | target capabilities | evidence to read | test method | pass criteria | failure severity | should_run_in_R142 |
| --- | --- | --- | --- | --- | --- | --- |
| T01 Repository and shared navigation | C01, C23 | README, README.zh-CN, RESOURCE_INDEX, agentpal.json, repository-structure guide | Check links, index coverage, JSON parse, no stale current paths. | Required entries present; JSON parses; no stale public entry path. | high | yes |
| T02 Fresh-clone onboarding path | C02 | START_HERE, first-30-minutes, first walkthrough, FAQ, glossary, R140 evidence | Repeat clean-copy walk from first entry to walkthrough. | User can understand what AgentPal is, what it is not, and what to try safely. | high | yes |
| T03 Thin binding and central project record | C03, C21 | project-binding templates, bind guide, workspace project template | Simulate template inspection only; no real external project write. | Thin files only; central record separation clear. | high | yes |
| T04 Central roster and AI judgement routing | C04, C06 | central contacts, agentpal.json, routing protocols | Parse roster and scan route-map patterns; inspect direct call policy. | 9/9 active; AI judgement only; no keyword route map. | blocker | yes |
| T05 Official Pal readiness | C05 | official/pals, R141 Pal matrix | Verify root entries, `pal.json`, asset directories, public-safe status. | 9/9 usable; manifest gap classified correctly. | high | yes |
| T06 PalSmith and Pal Asset governance | C07, C08 | PalSmith files, standards/pal-asset, standards/palsmith, PalSmith manifest | Parse PalSmith metadata and check governance boundaries. | PalSmith pilot works as no-code governance, not runtime automation. | high | yes |
| T07 Org Pack / FDE / asset boundary | C09, C10, C11 | standards, templates, examples, asset-boundary docs | Check required files, sample boundaries, no private data. | Public-safe reusable assets remain separate from customer-private assets. | high | yes |
| T08 Combined Pack and workflow governance | C12, C13, C20 | combined-pack example and usage scenario | Follow reference chain through context packet, task package, verification, governance. | Example chain is coherent and no-code. | medium | yes |
| T09 Faye and Delivery Packs | C14-C18 | Faye standards, delivery template, Video Growth, Sales CRM, handoff standard | Test standard/template/example chain and handoff to PalSmith. | Faye works as delivery role/workflow; no official-Pal claim. | high | yes |
| T10 Deep Conductor governance loop | C19, C20 | standards/deep-conductor, templates, examples, routing-memory-record | Inspect no-code loop and `not-run`/missing evidence behavior. | Protocol assets are coherent without claiming runtime execution. | medium | yes |
| T11 Public safety and no program expansion | C06, C11, C22, C24 | full public repo scan | Scan internal paths, hidden release claims, credentials, customer-private data, connector/scanner/marketplace language. | 0 real leaks/expansions; raw boundary hits classified. | blocker | yes |
| T12 Release evidence and decision boundary | C23, C24 | R130-R141 release/eval evidence | Check local evidence chain and remote authorization boundary. | Local completion/preflight evidence is consistent; no remote publication claim. | high | yes |

## R142 Pass Criteria

R142 should pass only if all blocker/high groups pass and no medium issue blocks
user-facing usability under the no-code framework standard. If a blocker or
high issue appears, R142 should route to targeted fix. If all groups pass, R142
may support a final release decision.

