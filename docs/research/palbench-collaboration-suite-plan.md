# PalBench Collaboration Suite Plan

PalBench Collaboration is the v0.3 qualitative regression suite for AgentPal multi-Pal collaboration behavior.

It evaluates no-code orchestration quality, not foundation-model capability. It does not claim statistical significance and does not require active Deep Conductor execution.

## What It Verifies

The suite checks whether AgentPal-mode behavior preserves:

- direct `/pal Name` calls;
- `@Pal` consult defaults;
- Context Packet fields and privacy boundaries;
- Owner + Verifier evidence separation;
- Plan -> Execute -> Verify staging;
- Parallel Independent Review isolation;
- Routing Memory as judgement input, not fixed routing;
- Mira or owner Pal conflict summary;
- no hard-coded task/domain routing;
- no future design written as current runtime behavior.

## Case Format

Each case includes:

- user input;
- expected Context Packet;
- expected workflow;
- expected output;
- failure modes;
- scoring rubric.

## Scoring

Use 0 / 1 / 2 qualitative scoring:

- 0: contradicted, absent, unsafe, or boundary-breaking;
- 1: partially present with important gaps;
- 2: clear, usable, and aligned with v0.3 no-code protocol.

Scores are regression signals. They are not benchmark claims.

## Initial Coverage

The first suite includes at least 10 cases:

1. `/pal Atlas` direct call.
2. `@Quinn` consult.
3. Owner + Verifier release check.
4. Parallel independent product / dev / QA review.
5. Plan -> Execute -> Verify docs task.
6. Context Packet privacy boundary.
7. Routing Memory reuse.
8. Mira Conductor conflict summary.
9. Direct owner Pal suggests another Pal candidate.
10. Bad group chat collapse.
11. Mention consult does not transfer owner.
12. Explicit handoff transfers owner candidate.
13. Context Packet missing required fields.
14. Full chat history copied as failure.
15. Owner + Verifier dev task.
16. PalSmith generated Pal health check.
17. Completion report missing evidence.
18. Verifier only reads owner claim.
19. Hardcoded verifier failure.
20. Blocked verification due to missing evidence.
21. Repair package after failed verification.
22. Release risk parallel review.
23. Research conclusion parallel review.
24. PalSmith AI team parallel review.
25. Reviewer reads peer draft failure.
26. Synthesis hides conflict failure.
27. Minority opinion preserved.

## Boundary

PalBench Collaboration must not require:

- automatic Deep Conductor;
- active Subagent Mode;
- external Agent calls;
- automatic routing memory writeback;
- automatic capability probing;
- CLI, UI, scanner, validator, installer, daemon, or service.
