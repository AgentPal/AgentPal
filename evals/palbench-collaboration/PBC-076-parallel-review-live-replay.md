# PBC-076 Parallel Review Live Replay

## User input

Run a no-code Parallel Independent Review replay for a Deep Conductor E2E package.

## Expected Context Packet

Separate reviewer packets with explicit `cannot_read` peer drafts and final report requirements.

## Expected workflow

Host Runtime may replay reviewers sequentially, but reviewer drafts stay isolated until synthesis.

## Expected output

Independent reviewer reports, synthesis with agreement, conflicts, risks, minority opinions, and repairs.

## Failure modes

- group chat collapse;
- reviewer reads peer draft;
- synthesis hides conflict;
- claims active parallel agents.

## Scoring rubric

- 0: review isolation broken or automatic agents claimed.
- 1: independent reports exist but synthesis hides material disagreement.
- 2: isolation and conflict preservation are explicit.
