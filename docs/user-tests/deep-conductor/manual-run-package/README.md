# DeepConductor Manual Run Package

## Purpose

This package is for a real user or tester to run the DeepConductor manual test and bring results back for R245.

This package does not automatically decide pass or fail. It tells you exactly what to run, what to capture, and what to return.

## What You Must Return

Return all of these:

- filled `manual-test-result-form.md`;
- raw output from the main test prompt;
- raw output from the routing pressure prompt;
- screenshots when possible;
- completed checklist from `expected-artifacts-checklist.md`;
- blocker notes if any required section is missing;
- host runtime and project mode.

## When To Screenshot

Take screenshots when:

- AgentPal cannot load in the project;
- DeepConductor does not trigger;
- Team First Discovery is missing;
- selected Pals are named but do not participate;
- Quinn verification is missing;
- Closure Gate is missing;
- the answer overclaims release, backend, runtime, Marketplace, full certification, or live external validation.

## What Counts As A Blocker

Treat these as blockers:

- no Team First Discovery;
- new team creation before checking existing teams;
- wrong assignment not corrected;
- selected Pal has no work plan or output;
- Asset Preflight missing;
- Owner Assignment Integrity missing;
- Closure Gate missing;
- Quinn final verification missing;
- final deliverable cannot be used.

## Important Boundary

This R244 package does not mean DeepConductor passed user testing. R245 will intake your returned materials and make the pass / fail / blocked judgement.
