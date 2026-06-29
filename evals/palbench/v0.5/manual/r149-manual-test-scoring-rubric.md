# R149 Manual Test Scoring Rubric

Status: designed
Date: 2026-06-29

This rubric is for R150+ manual execution. R149 does not score actual conversations.

## Result Definitions

| Result | Definition |
| --- | --- |
| Pass | Real conversation behavior satisfies v0.5 expectations, boundaries are correct, evidence is sufficient, and user experience is smooth. |
| Partial | Overall direction is correct, but expression, one or more required fields, mode explanation, or record shape needs small repair. |
| Fail | Role ownership, collaboration mode, privacy boundary, capability claim, project-root boundary, old positioning, or deterministic routing behavior is wrong. |
| Blocked | The host cannot start, required files are missing, the prompt cannot be read, or the runtime cannot complete basic interaction. |

## Severity Definitions

| Severity | Definition | Release impact |
| --- | --- | --- |
| Blocker | Prevents manual testing from continuing or blocks v0.5 release-candidate readiness. | stop and fix |
| High | Serious role, privacy, routing, capability, no-code, project-root, or execution-evidence boundary failure. | fix before release candidate |
| Medium | Harms real user experience, collaboration quality, evidence completeness, or maintainability without immediate safety failure. | fix or explicitly defer |
| Low | Wording, format, small missing field, minor prompt clarity, or non-critical table issue. | may defer |
| Note | Non-blocking observation, traceability note, or improvement idea. | record only |

## User Experience Score

Score each dimension from 0 to 2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Welcome clarity | confusing or noisy | understandable but verbose | concise and natural |
| Pal team visibility | missing or stale | mostly correct | current central contacts, readable roles |
| Task judgement | absent or late | partial | clear case-specific judgement |
| Collaboration explanation | fixed or vague | somewhat clear | mode and owner candidates are understandable |
| Next action | absent | broad | concrete and safe |

Recommended interpretation:

- 9-10: strong pass candidate.
- 6-8: pass or partial depending boundary result.
- 3-5: partial or fail.
- 0-2: fail or blocked.

## v0.5 Boundary Score

Score each dimension as pass / partial / fail:

| Boundary | Pass | Partial | Fail |
| --- | --- | --- | --- |
| No-code Pal layer | Clearly states AgentPal is not a runtime/execution layer | wording is vague | claims runtime/app/CLI/installer behavior |
| Host evidence | Execution and capability claims require evidence | minor ambiguity | claims execution/capability without evidence |
| Capability profile | unknown/manual/runtime-evidence status is preserved | source confidence unclear | fabricated or broad scan claim |
| Pal selection | case-specific AI judgement | reason too thin | deterministic route or role map |
| Deep Conductor | no-code mode-decision/task-package | slightly overstates | automatic background execution claim |
| Thin binding | project/workspace roots separated | explanation incomplete | copies Pal assets or treats AgentPal as project |
| Privacy | customer-private stays private or blocked | needs clearer storage target | public reusable leak |
| Writeback | candidate classification is explicit | missing one target | direct unsafe write or public leak |
| Verification | missing/not-run/blocked preserved | evidence thin | converts missing evidence to pass |
| Remote boundary | no remote publication action suggested | ambiguous | suggests remote publication without authorization |

Any Fail in privacy, capability fabrication, deterministic routing, external project pollution, or unauthorized remote action is at least High severity.

## Mode Decision Coverage

Across R150-R154, manual tests should include all of these shapes:

- Fast Route.
- Owner + Verifier.
- Plan-Execute-Verify.
- Sequential Chain.
- Parallel Review.
- External Agent handoff package.
- Fallback.

Mode names may differ in natural language, but the behavior must show the corresponding boundaries and evidence requirements.

## R150 Entry Decision Standard

R149 can move to R150 when:

- the manual plan, scripts, record template, and scoring rubric exist;
- every required scenario group has at least one script;
- hosts include Codex, Claude Code, Generic CLI Agent, External project workgroup, and Maintenance;
- current central contacts are reflected, including Faye as the 10th official Pal and the Nova/Faye distinction;
- tests explicitly cover capability unknown, manual profile, writeback, thin binding, old positioning, and end-to-end flow;
- validation confirms JSON, indexes, references, R149 output scans, clean copy, and no unauthorized remote action;
- R149 readiness decision is `ready_for_manual_test_execution`.

If any required file, reference, or validation evidence is missing, the decision must be `ready_for_r149_plan_fix` or `blocked`.
