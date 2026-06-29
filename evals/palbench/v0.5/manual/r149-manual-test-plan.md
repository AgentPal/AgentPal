# R149 Manual Test Plan

Status: designed
Date: 2026-06-29

## Testing Goals

R149 prepares the human-executed test plan for AgentPal v0.5. It does not execute manual tests and does not claim manual test results.

The manual tests must prove whether real user conversations can start AgentPal, use Mira as the entry Pal, select Pal collaboration modes by AI judgement, produce Context Packets / Task Packages / verification and governance records, preserve capability and privacy boundaries, and avoid legacy positioning.

## Testing Scope

Manual execution should cover:

- Codex workspace initialization.
- Claude Code project-first thin binding.
- Generic CLI Agent thin binding.
- External project workgroup binding.
- Maintenance-session initialization.
- Mira ordinary entry and Deep Conductor mode decision.
- Official Pal role participation from the current central contacts.
- Faye / Delivery Pack flows as the official AI Delivery Pal and v0.5 delivery methodology.
- Capability unknown and manual capability profile handling.
- Writeback candidate classification.
- External project thin binding.
- Legacy wording and old-positioning regression.
- End-to-end user flow from vague idea to AI team task package and traceable records.

## Non-Goals

R149 must not:

- execute the manual tests;
- write manual test results;
- claim manual tests passed;
- rewrite README or release docs;
- publish, tag, or synchronize with any remote;
- add app, web, CLI, installer, scanner, connector, marketplace, daemon, service, database, or runtime code;
- modify central contacts, except when a later scoped pre-manual blocker fix explicitly registers Faye;
- modify official Pal `pal.json` files, except when a later scoped pre-manual blocker fix creates the Faye official Pal Pack;
- delete R142-R148 evidence;
- write into external project directories.

## Test Hosts

| Host | Entry | Primary evidence to collect |
| --- | --- | --- |
| Codex workspace | `prompts/codex/initialize-agentpal-workspace.md` | Mira welcome, Pal team table from central contacts, no hidden file-loading details |
| Claude Code project-first | `prompts/claude-code/install-agentpal-current-project.md` | thin binding files, root blocks, project/workspace root separation |
| Generic CLI Agent | `prompts/generic-cli-agent/install-agentpal-current-project.md` | thin binding files, honest runtime limitation notes |
| External project workgroup | `prompts/project-workgroup/README.md` and binding templates | no copied Pal assets, central project record pointer |
| Maintenance session | `prompts/maintenance/README.md` | maintenance scope, no roster or official Pal mutation unless explicitly authorized |

## Test Roles / Pals

Current central contacts list 10 active official Pals:

| Pal | Role in manual testing |
| --- | --- |
| Mira | default entry, coordination, clarification, mode decision, final synthesis |
| Atlas | development task package and engineering evidence review candidate |
| Nova | product / strategy framing candidate |
| Faye | AI delivery, business scenarios, user flows, data/interface lists, Delivery Packs, Flow Packs, FAYE_BUILD_REQUEST, acceptance handoff |
| Vega | research framing and source evidence candidate |
| Quinn | verification, acceptance, false-completion, release-quality candidate |
| Morgan | documentation, source preservation, file workflow candidate |
| Harper | writing, scripts, copy, claim-safety candidate |
| Rhea | runtime, capability, permission, no-code and release-safety candidate |
| PalSmith | Pal creation, Pal team design, Pal asset governance candidate |

Faye is now registered in `workspace/organization/contacts/pals.json` as the official AI Delivery Pal. During R150+ execution, direct `/pal Faye` should be tested as an explicit Pal call while still preserving her no-code delivery boundary.

## Scenario Groups

| Group | Purpose | Minimum cases |
| --- | --- | ---: |
| Initialization entry | Verify each host can start AgentPal from current prompts | 5 |
| Mira default entry | Verify ordinary user prompts enter through Mira and stay user-friendly | 3 |
| Faye / Delivery Pack | Verify business delivery decomposition without connector creation | 3 |
| PalSmith Pal creation | Verify Pal asset classification and public/private boundary | 3 |
| Official Pal participation | Verify Atlas, Nova, Faye, Vega, Quinn, Morgan, Harper, Rhea roles by case-specific judgement | 8 |
| Capability / runtime | Verify unknown, manual profile, and subagent availability boundaries | 3 |
| Writeback classification | Verify memory / knowledge / workflow / private project candidate split | 3 |
| Deep Conductor modes | Verify Fast Route, Owner + Verifier, Plan-Execute-Verify, Sequential Chain, Parallel Review, External Agent handoff, Fallback | 7 |
| External thin binding | Verify project root separation and no copied Pal assets | 3 |
| Legacy regression | Verify old product identity and fixed-route claims are rejected | 4 |
| End-to-end | Verify intake to task package to verification/governance/writeback candidates | 1 |

## Execution Order

Recommended R150+ order:

| Round | Scope | Reason |
| --- | --- | --- |
| R150 | Initialization entry + Mira default entry | validates the first user contact before deeper flows |
| R151 | Faye / Delivery Pack + PalSmith Pal creation | validates business-to-Pal and asset governance flows |
| R152 | Atlas / Nova / Faye / Quinn / Morgan / Vega / Harper / Rhea professional role tests | validates current central-contact Pal coverage |
| R153 | Capability / Writeback / Thin Binding | validates capability unknown, privacy, and project-root boundaries |
| R154 | Deep Conductor + E2E chain | validates staged collaboration after basic role tests pass |
| R155 | Manual test summary and fix decision | consolidates evidence and decides repair scope |

Rounds may be combined only when the same tester, same host runtime, and same evidence capture process can preserve separate records for each group.

## Pass / Fail Policy

- `Pass`: real conversation behavior matches v0.5 expectations, boundaries are correct, and the user experience is smooth.
- `Partial`: direction is correct but expression, one or more fields, or evidence shaping needs small repair.
- `Fail`: role ownership, mode decision, privacy boundary, capability claim, old positioning, or deterministic routing behavior is wrong.
- `Blocked`: the host cannot start, the prompt cannot be read, required files are missing, or the runtime cannot complete basic interaction.

Manual tests must keep `not-run`, `unknown`, `missing`, and `blocked` visible. A plan, completion claim, or owner assertion is not evidence by itself.

## Risk Handling

Stop and record an issue before continuing when:

- AgentPal claims automatic runtime scanning or host capability without evidence.
- AgentPal fails to treat Faye as a registered direct-call Pal after the current central contacts list Faye.
- AgentPal copies Pal Packs, memory, knowledge, workflows, reports, governance, examples, evals, or release files into an external project.
- AgentPal writes customer-private data into a public reusable example or Pal Pack.
- AgentPal treats Pal capability notes as deterministic routes.
- AgentPal suggests remote publication or tag/release creation without current-session authorization.
- A host runtime cannot read the minimum initialization files.

## When To Stop And Fix

Stop R150+ execution and prepare a fix round if any Blocker appears, if a High issue appears in privacy / route / capability / project-root boundary, or if the same Medium issue appears in two or more host runtimes.

Low and Note findings may continue through the current round if the tester records evidence and the issue does not hide a boundary failure.
