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
28. Deep Conductor project release planning.
29. Deep Conductor research to HTML report.
30. Deep Conductor PalSmith AI team creation.
31. Deep Conductor cross-runtime continuation.
32. Deep Conductor token budget failure.
33. Deep Conductor skips Capability Inventory failure.
34. Deep Conductor missing verification failure.
35. Deep Conductor no memory writeback failure.
36. Cross-runtime Codex to Claude continuation.
37. Pal memory snapshot used in next task.
38. Routing memory guides but does not force selection.
39. Runtime Skill usage memory reuse.
40. Runtime switch loses Pal memory failure.
41. Routing Memory fixed route failure.
42. Private project memory leak failure.
43. Cross-runtime continuation without verification failure.
44. Runtime Skill office document candidate.
45. Runtime Skill browser check candidate.
46. Runtime Skill repo analysis candidate.
47. Runtime Skill availability unknown.
48. Runtime Skill unavailable fallback.
49. Runtime Skill output requires verification.
50. Runtime Skill usage memory reuse.
51. Runtime Skill confused with Pal Skill failure.

## Boundary

PalBench Collaboration must not require:

- automatic Deep Conductor;
- active Subagent Mode;
- external Agent calls;
- automatic routing memory writeback;
- automatic capability probing;
- CLI, UI, scanner, validator, installer, daemon, or service.

Runtime Skill cases verify no-code Task Package quality only. They do not require AgentPal to call, install, scan, or execute host Runtime Skills.
