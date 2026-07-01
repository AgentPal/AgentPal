# R215 Real Host User Walkthrough

## Verdict

`palsmith_primary_function_ready_with_notes`

## Summary

R215 attempted one real Codex host thread against the R214 fresh AgentPal copy:

```text
thread_id: 019f1cae-8165-7031-9e57-39861efefabf
fresh_copy: J:\开发\AgentPal_dcos\测试记录\R214-fresh-agentpal-copy\
thread_target: projectless
projectless_output_directory: C:\Users\Administrator\Documents\Codex\2026-07-01\r215-palsmith-real-host-walkthrough\outputs
```

The fresh copy was not registered in `codex_app.list_projects`, and creating a project-scoped thread with the fresh copy path failed with:

```text
Unknown projectId: J:\开发\AgentPal_dcos\测试记录\R214-fresh-agentpal-copy. Call list_projects to find available projects.
```

A single successful projectless Codex thread was then created and instructed to operate only on the fresh copy absolute path. The thread confirmed that the fresh copy was reachable, loaded central contacts and PalSmith protocols, created the allowed R215 walkthrough fixture evidence, and returned a final `partial` verdict. The limitation is that the host thread was projectless because the fresh copy was not registered in Codex `list_projects`.

## Real Host Evidence Observed

| Item | Result | Evidence |
| --- | --- | --- |
| One real Codex thread created | pass | `019f1cae-8165-7031-9e57-39861efefabf` |
| Fresh copy reachable | pass | Thread visible message: fresh copy is reachable |
| Fresh copy registered as Codex project | fail | `list_projects` did not include the R214 fresh copy |
| Project-scoped fresh-copy thread | fail | `Unknown projectId` |
| Projectless fallback thread | pass with limitation | Thread created with absolute fresh-copy path constraint |
| Thread final verdict returned | pass | Thread returned `partial` |
| R215 fixture files created by thread | pass | Draft, user-custom, authorization, revocation, walkthrough, and verification fixture files were written |
| Source workspace modified by thread | not observed | Thread prompt prohibited `J:\开发\AgentPal`; source status checked separately |

## Case Results

| Case | Result | Notes |
| --- | --- | --- |
| Case 1: user can find PalSmith | pass | Mira routes the ordinary creation question to PalSmith, not generic Codex. |
| Case 2: create MiaCrossBorderCoach | pass | PalSmith asks for missing key business inputs and produces a draft Pal plan. |
| Case 3: draft Pal Pack fixture | pass | Non-official draft fixture files written under the allowed R215 directory. |
| Case 4: draft-to-custom fixture | pass | Fixture-only user custom Pal copy written under the allowed R215 directory. |
| Case 5: explicit invocation shape | pass | `/pal MiaCrossBorderCoach` shape documented without claiming central discovery. |
| Case 6: discovery authorization | pass | Fixture-only authorization record written under `authorization-fixtures/`. |
| Case 7: discovery revocation | pass | Fixture-only revocation record written under `authorization-fixtures/`. |

## Fresh Copy Files Observed

The real thread created the following evidence files under the R214 fresh copy, mirrored in this repository under `evals/palbench/v0.5/palsmith/r215-real-host-walkthrough/`:

```text
R215_REAL_HOST_WALKTHROUGH.md
R215_VERIFICATION.md
MiaCrossBorderCoachDraft/PAL.md
MiaCrossBorderCoachDraft/README.md
MiaCrossBorderCoachDraft/SKILL.md
MiaCrossBorderCoachDraft/pal.json
MiaCrossBorderCoachDraft/core/output-contract.md
MiaCrossBorderCoachDraft/evals/basic-invocation.md
MiaCrossBorderCoachDraft/identity/voice.md
MiaCrossBorderCoachDraft/knowledge/listing-diagnosis.md
MiaCrossBorderCoachDraft/metadata-draft.md
MiaCrossBorderCoachDraft/workflows/launch-checklist.md
user-pals/MiaCrossBorderCoach/PAL.md
user-pals/MiaCrossBorderCoach/README.md
user-pals/MiaCrossBorderCoach/SKILL.md
user-pals/MiaCrossBorderCoach/pal.json
user-pals/MiaCrossBorderCoach/INSTALL_REPORT.md
authorization-fixtures/MiaCrossBorderCoach-discovery-authorization.fixture.json
authorization-fixtures/MiaCrossBorderCoach-discovery-authorization.md
authorization-fixtures/MiaCrossBorderCoach-discovery-revocation.fixture.json
authorization-fixtures/MiaCrossBorderCoach-discovery-revocation.md
```

## Boundary Checks

- central contacts modification: no, protected hash unchanged
- `official/pals` modification: no, protected aggregate unchanged
- real `workspace/resources/user-pals/` creation or modification: no, protected aggregate unchanged
- remote Git operation: not run
- GitHub Release / tag / push / pull / fetch: not run
- runtime / backend / CLI / installer / scanner / daemon / connector / Marketplace backend: not introduced

## Issues

| Severity | Issue | Status |
| --- | --- | --- |
| note | The fresh copy is not available as a Codex project target, so the host thread had to run projectless. | open |
| note | No separate live AgentPal app/runtime surface was used or claimed. | recorded |
| note | The thread reported one attempted temporary hash snapshot in the projectless workspace and stated it was removing it; no file was observed in that workspace during closeout inspection. | recorded |

## Decision

R215 is a real host partial pass with projectless-host limitation. The honest decision is:

```text
palsmith_primary_function_ready_with_notes
```
