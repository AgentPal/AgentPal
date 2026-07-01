# Scoped Certification Checklist

Status: R208 checklist, copyable for future reviews.

Use this checklist only for a specific Pal plus task family. A representative
host regression is not certification by itself.

## Required

- [ ] `certification_id` is unique.
- [ ] `pal_id` and `task_family` are explicit.
- [ ] Version or commit is recorded.
- [ ] Phase 1 entry adoption evidence exists.
- [ ] Task Asset Packet example or equivalent documented task plan exists.
- [ ] Real host representative regression exists.
- [ ] Host thread IDs are recorded.
- [ ] Asset Loading Gate evidence exists.
- [ ] Task Asset Packet evidence exists.
- [ ] Asset Use Summary evidence exists.
- [ ] Tool / runtime boundary evidence exists.
- [ ] Missing Asset Plan exists, or the record explains why it was not needed.
- [ ] No-code boundary scan passes for the evidence package.
- [ ] Quinn or equivalent QA review passes.
- [ ] JSON checks pass where JSON files are in scope.
- [ ] Markdown links pass for the new or changed documents.
- [ ] Index entries point only to existing files.
- [ ] Known limits are written.
- [ ] Valid scope is narrow and testable.
- [ ] Invalid scope is explicit.

## Recommended

- [ ] At least one negative or pressure test exists for the task family.
- [ ] The Pal's output contract is named in the evidence set.
- [ ] The review records which assets were not loaded.
- [ ] The record names tool calls that remained blocked.
- [ ] The record says whether any host behavior may vary across runtimes.
- [ ] The next review date or trigger is clear.

## Optional

- [ ] Add a short user-readable note for release docs.
- [ ] Add a maintainer-only risk note when evidence is weak but still useful.
- [ ] Add a follow-up backlog item for missing examples or missing evals.

## Fail Conditions

Fail or downgrade the certification review if:

- the only evidence is a Pal name, persona, or generic prompt;
- a host tool result replaces Pal judgement;
- task-relevant assets existed but were not loaded;
- the record has no host thread ID or equivalent controlled execution evidence;
- the review cannot show Asset Loading Gate, Task Asset Packet, and Asset Use
  Summary evidence;
- a missing core asset was ignored;
- a remote, release, contacts, discovery, or publication action is claimed
  without current evidence;
- the wording expands one task-family pass into broader certification.

## Decision Values

Use one of:

- `scoped_certified`
- `scoped_certification_candidate`
- `representative_regression_passed`
- `entry_adopted`
- `uncertified`
- `blocked_by_missing_evidence`
- `blocked_by_boundary_overclaim`
