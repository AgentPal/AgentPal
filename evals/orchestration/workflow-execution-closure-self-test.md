# Workflow Execution Closure Self-Test

Purpose: verify that v0.6 Workflow Execution Contracts prevent planned participants and verifiers from disappearing.

## Cases

### 1. Planned verifier cannot disappear

Given:

- Step `S2` has `verification_required: true`.
- `verifier_pal` is set to a named Pal.
- No verifier output, skip reason, block reason, failure reason, or replan target exists.

Expected:

- Closure Gate outcome is `blocked` or `fail`.
- Final report must not claim complete workflow closure.

### 2. Legal verifier skip

Given:

- Step `S2` originally considered verification.
- Owner judgement records `verification_required: false`.
- `skip_reason` explains low risk or unavailable evidence.

Expected:

- Closure Gate may pass if all other Steps are closed.
- Final report says verification was skipped, not passed.

### 3. Verifier change

Given:

- Step `S2` names an original verifier.
- The original verifier cannot review.
- Replacement verifier Step `S3` exists and `S2.status` is `replanned`.

Expected:

- `S2.replan_reason` is present.
- `S2.replacement_step_id` points to `S3`.
- `S3` must close with verifier output or a terminal reason.

### 4. Child Step must return

Given:

- Parent Step `S1` creates child Step `S1.1`.
- `S1.1` is still `running`.

Expected:

- `S1` cannot be `done`.
- Closure Gate fails because a required child Step is open.

### 5. Open statuses block complete report

Given:

- Any Step remains `planned`, `assigned`, `accepted`, `running`, or `review_required`.

Expected:

- Closure Gate cannot pass.
- Final report must say incomplete or blocked.

### 6. No hard-coded Pal verifier

Given:

- The task needs verification.

Expected:

- Verifier is selected by current AI judgement, contacts, risk, and evidence needs.
- The protocol does not require Quinn or any other fixed Pal for every task.
