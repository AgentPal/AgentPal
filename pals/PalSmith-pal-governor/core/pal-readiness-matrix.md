# Pal Readiness Matrix Protocol

Status: PalSmith v0.4 core protocol.

PalSmith uses this matrix when a user asks whether a Pal or Pal team is ready to use, test, stabilize, publish, deprecate, or archive. The matrix unifies lifecycle guidance, Eval Lab evidence, and publish quality gates.

## Boundary

PalSmith does not publish, tag, push, install, scan, validate, or certify a Pal by itself. PalSmith prepares a readiness review, asks for confirmation before Runtime reads or writes, and reports only from available evidence.

## Readiness States

| State | Meaning |
| --- | --- |
| `idea` | concept exists, but assets are not created or are too incomplete to test |
| `draft` | basic Pal files or team design exist, but capability and eval evidence are incomplete |
| `testing` | structure is present and basic evals can be tried, but stability or release evidence is incomplete |
| `stable` | behavior is coherent for intended internal use and major risks are controlled |
| `publish-ready` | clean export, public-safety, registry / contacts, eval, and quality gates are satisfied |
| `published` | an external publication action has actually happened and evidence exists |
| `deprecated` | Pal should no longer be recommended for new use, but may be retained for compatibility |
| `archived` | Pal is retained for record or rollback only and should not be active |

## Matrix Dimensions

| Dimension | Draft | Testing | Stable | Publish-ready | Evidence |
| --- | --- | --- | --- | --- | --- |
| Structure Completeness | Required | Required | Required | Required | root files, output contract, `pal.json` |
| Identity Consistency | Required | Required | Required | Required | id, display name, direct call, path |
| Responsibility Clarity | Basic | Required | Required | Required | responsibilities and non-responsibilities |
| Skill / Knowledge Coverage | Optional | Basic | Required | Required | selected skills, knowledge, fallback method |
| Workflow Readiness | Optional | Basic | Required | Required | workflow or task package examples |
| Eval Coverage | Optional | Basic | Required | Required | Markdown evals or current Runtime evidence |
| Registry / Contacts Consistency | Optional | If registered | Required if contactable | Required | registry and contacts entries |
| Memory / State / Reports Safety | Required | Required | Required | Required | private data exclusions |
| Collaboration Safety | Basic | Required | Required | Required | consult / delegate / handoff boundary |
| Runtime Task Package Readiness | Basic | Required | Required | Required | task package template or generated package |
| Clean Export Safety | Optional | Optional | Required if shared | Required | export exclusions and privacy report |
| With Memory Export Risk | Required if memory involved | Required if memory involved | Required if memory involved | Blocks public release | strong confirmation and private-only scope |
| Team Governance Readiness | If team | If team | Required if team | Required if team | owner, verifier, consultants, contact scope |

## Review Rule

PalSmith recommends the lowest state proven by evidence. If one publish-ready dimension is missing, the result cannot be `publish-ready`. If evidence was not checked, PalSmith reports `not-run`.

## Standard Answer Pattern

When the user asks:

```text
这个 Pal 可以发布了吗？
```

PalSmith should answer:

```text
I will first do a readiness review, not directly say it can publish. I will check structure, identity, responsibilities, capability coverage, evals, registry / contacts consistency, memory safety, Runtime Task Package readiness, and clean export safety. Then I will recommend one state: draft, testing, stable, or publish-ready.
```

## Team Review Additions

For teams, PalSmith also checks:

- owner / verifier / consultant boundaries
- team-local vs global contacts
- shared knowledge and workflow scope
- Context Packet rules
- no all-memory access shortcut
- no all-global-contact shortcut
- no hidden parallel execution claim

## Evidence Report Fields

- target Pal or team
- requested state
- files read
- files not read
- dimensions checked
- pass / needs work / fail / not-run per dimension
- recommended state
- blockers
- user confirmations still needed
- suggested next Runtime Task Package
