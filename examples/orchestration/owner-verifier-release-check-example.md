# Owner + Verifier Release Check Example

This synthetic example shows a no-code staged release check. Candidates are selected for this case only.

## User Input

```text
Check whether this release candidate is ready to publish, and ask a quality Pal to independently re-check the evidence.
```

## Owner Candidate

Mira is the owner candidate because the request needs release coordination, evidence inventory, and final synthesis.

## Verifier Candidate

Quinn is the verifier candidate because this case is a quality and release evidence review. Quinn is a candidate, not the default verifier for all tasks.

## Owner Output

```yaml
owner_pal_candidate: Mira
owner_claim: "Release readiness can be judged after docs, version, checks, and release blockers are reviewed."
expected_deliverables:
  - release readiness decision
  - evidence inventory
  - release blockers
acceptance_criteria:
  - version references are consistent
  - required release notes exist
  - checks are either passed or explicitly marked not-run
  - no push, tag, or release happens inside this review
evidence_required_for_verification:
  - changed files list
  - release notes path
  - command outputs or not-run labels
  - blocker list
```

## Verifier Context Packet

```yaml
schema: agentpal.verifier-context-packet.v0.3
packet_id: vcp-release-check-001
from_pal: Mira
to_verifier_candidate: Quinn
verification_mode: release_gate
user_goal: "Check whether this release candidate is ready to publish."
owner_pal: Mira
owner_claim: "Readiness depends on version consistency, release notes, checks, and blockers."
expected_deliverables:
  - release readiness decision
  - blocker list
acceptance_criteria:
  - "Version claims map to files."
  - "Checks have evidence or not-run labels."
  - "No publishing action is taken."
evidence_to_check:
  - type: file
    source: "release notes path"
    expected_signal: "candidate notes exist"
  - type: command_output
    source: "git status and test output"
    expected_signal: "clean or honestly reported"
allowed_files:
  - "release/"
  - "evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/"
cannot_read:
  - private_user_memory
  - secrets
  - full_chat_history_by_default
known_risks:
  - "completion claim without command output"
false_completion_patterns:
  - completion_report_treated_as_evidence
  - hidden_not_run_check
needed_output:
  - verdict
  - missing_evidence
  - risks
  - repair_required
  - confidence
return_to: Mira
```

## Verification Result Record

```yaml
schema: agentpal.verification-result-record.v0.3
verification_id: vrr-release-check-001
verifier_candidate: Quinn
mode: release_gate
verdict: blocked
confidence: medium
checked_evidence:
  - evidence: "release notes path"
    source: "file listing"
    result: "present"
missing_evidence:
  - "test command output"
  - "exact tag/version consistency evidence"
risks:
  - "release could be claimed ready without executed checks"
false_completion_caught:
  caught: true
  pattern: hidden_not_run_check
required_repairs:
  - "Provide test outputs or mark checks not-run."
recommended_next_step: "Return to owner for evidence completion."
return_to: Mira
notes: "Blocked is correct until evidence exists."
```

## Mira / Owner Synthesis

Mira reports that the verifier result is blocked, names the missing evidence, and prepares a repair package for release evidence collection.

## Good Behavior

- Verifier checks evidence, not only the owner summary.
- Missing checks become `blocked`, not pass.
- Quinn is described as a candidate for this case.

## Bad Behavior

- Treating a release completion report as proof.
- Publishing, tagging, or pushing during the review.
- Presenting Quinn as the universal verifier.

## Acceptance Criteria

- The workflow includes owner output, verifier packet, result record, and synthesis.
- Verdict is one of `pass`, `fail`, or `blocked`.
- Missing evidence stays visible.

## No-Code Boundary Note

This is a no-code staged workflow. It does not create a release robot, background worker, or automatic multi-runtime check.
