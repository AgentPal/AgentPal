# Example Pal Readiness Review Task Package

This is an example only. It is not an execution record and does not prove that a real Pal was reviewed.

## User Goal

```text
/pal PalSmith 这个内容运营 Pal 可以发布了吗？
```

## PalSmith Initial Answer

```text
PalSmith：I will first do a readiness review, not directly mark it publish-ready. I will check structure, identity, responsibilities, capability coverage, evals, registry / contacts consistency, memory safety, Runtime Task Package readiness, and clean export safety. I need confirmation for a read-only review of the target Pal files.
```

## Confirmation

```text
Confirmed: read only `pals/ContentOps-pal/`, `registry/pal.index.json`, and `contacts/pals.json`. Do not write files and do not publish.
```

## Runtime Task Package

- `task_id`: `palsmith-readiness-review-contentops`
- `task_name`: `Pal Readiness Review Task Package`
- `owner_pal`: `PalSmith`
- `allowed_read_paths`:
  - `pals/ContentOps-pal/`
  - `registry/pal.index.json`
  - `contacts/pals.json`
- `forbidden_read_paths`:
  - `pals/ContentOps-pal/memory/user/`
  - `pals/ContentOps-pal/memory/project/`
  - credentials, logs, unrelated Pals
- `allowed_write_paths`: none
- `verification_requirements`:
  - required root files
  - `pal.json` parse
  - registry / contacts consistency
  - eval coverage
  - clean export safety evidence
  - `not-run` for unchecked items

## Example Matrix Result

| Dimension | Draft | Testing | Stable | Publish-ready | Current Result |
| --- | --- | --- | --- | --- | --- |
| Structure Completeness | Required | Required | Required | Required | Pass |
| Identity Consistency | Required | Required | Required | Required | Pass |
| Responsibility Clarity | Basic | Required | Required | Required | Pass |
| Skill / Knowledge Coverage | Optional | Basic | Required | Required | Needs work |
| Workflow Readiness | Optional | Basic | Required | Required | Pass |
| Eval Coverage | Optional | Basic | Required | Required | Needs work |
| Registry / Contacts Consistency | Optional | If registered | Required if contactable | Required | Pass |
| Memory / State / Reports Safety | Required | Required | Required | Required | Pass |
| Collaboration Safety | Basic | Required | Required | Required | Pass |
| Runtime Task Package Readiness | Basic | Required | Required | Required | Pass |
| Clean Export Safety | Optional | Optional | Required if shared | Required | Not-run |
| With Memory Export Risk | Required if memory involved | Required if memory involved | Required if memory involved | Blocks public release | Pass |
| Team Governance Readiness | If team | If team | Required if team | Required if team | Not applicable |

## Recommendation

Recommended state: `testing`.

Reason: structure and identity are present, but eval coverage is incomplete and clean export safety was not run. PalSmith must not call this `publish-ready`.

## Next Task Package

- `Pal Eval Lab Task Package`
- `Clean Pal Export Task Package`
- optional follow-up `Pal Publish Quality Gate Task Package`
