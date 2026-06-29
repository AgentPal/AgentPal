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
52. Context budget project release.
53. Context budget research to HTML.
54. Memory reuse reduces context read.
55. Runtime Skill reduces rework.
56. Weak model needs detailed task package.
57. Cheapest-first quality loss failure.
58. Context overload failure.
59. Skipped verification to save token failure.
60. Exact token meter claim failure.
61. Context usage report missing failure.
62. E2E project release conductor.
63. E2E research to HTML deliverable.
64. E2E PalSmith AI team creation.
65. E2E cross-runtime continuation.
66. E2E document task with runtime skill.
67. E2E missing memory failure.
68. E2E skipped Capability Inventory failure.
69. E2E no Context Budget failure.
70. E2E no verification failure.
71. E2E no Routing Memory failure.
72. E2E live project release replay.
73. E2E live research-to-HTML replay.
74. Runtime Skill availability replay.
75. Owner + Verifier fake completion replay.
76. Parallel review live replay.
77. Cross-runtime continuation replay.
78. Subagent / external Agent availability replay.
79. Synthesis readability audit.
80. E2E package feasibility status.
81. Runtime availability evidence required.
82. Partial capability not overstated.
83. Subagent unavailable is not failure.
84. External Agent unavailable fallback.
85. E2E synthesis short summary required.
86. Routing Memory records unavailable capability.
87. Runtime task package availability-first.

## Boundary

PalBench Collaboration must not require:

- automatic Deep Conductor;
- active Subagent Mode;
- external Agent calls;
- automatic routing memory writeback;
- automatic capability probing;
- CLI, UI, scanner, validator, installer, daemon, or service.

Runtime Skill cases verify no-code Task Package quality only. They do not require AgentPal to call, install, scan, or execute host Runtime Skills.

Context Budget cases verify qualitative context planning, read tiers, prompt shaping, Runtime Skill cost notes, verification preservation, and Context Usage Reports. They do not require exact token metering or automatic cost calculation.

Deep Conductor E2E cases verify the full no-code loop from user goal through memory, Capability Inventory, Context Budget, topology, Context Packets, Runtime Skill-aware packages, verification, synthesis, Routing Memory candidate, and next-round recommendation. They do not require AgentPal to execute packages, probe host capabilities automatically, or run background workflows.

Real host replay cases verify whether a current Runtime can manually follow the no-code packages and return evidence. They must preserve unavailable, unknown, blocked, and not-run outcomes instead of smoothing them into pass.
