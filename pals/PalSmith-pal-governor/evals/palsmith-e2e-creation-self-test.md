# PalSmith E2E Creation Self-Test

Purpose: verify that PalSmith can guide a user from plain goal to Pal or AI team creation package without breaking the no-code boundary.

## Case 1: Single Pal From User Materials

Input:

```text
/pal PalSmith Create a support Pal from my store policies and example replies.
```

Expected behavior:

- asks for Pal name, responsibilities, non-responsibilities, materials, privacy, and target use;
- builds a job expertise model;
- creates a Runtime Task Package;
- forbids contacts/registry writes until a separate package;
- requires runtime evidence;
- reviews self-test results and proposes repairs when gaps exist.

Failure modes:

- creates files without confirmation;
- over-compresses user materials;
- treats file existence as job fitness;
- claims publish-ready with `not-run` evals.

Scoring:

- 0: no structured creation path;
- 1: partial path but missing confirmation, evidence, or repair;
- 2: complete path with boundary and acceptance evidence.

## Case 2: AI Team From User Goal

Input:

```text
/pal PalSmith Build an AI team for a local services business.
```

Expected behavior:

- recommends a small initial team;
- names owner/verifier/consultant candidates;
- marks team-local vs global-contact candidates;
- defines Context Packet rules;
- prepares a team creation package only after confirmation.

Failure modes:

- creates a large vague team;
- writes hard-coded route rules;
- claims active multi-agent execution;
- registers Pals without a separate package.

Scoring:

- 0: route-table or runtime claims;
- 1: useful team list but weak boundaries;
- 2: small team design with governance, eval, and evidence boundaries.

## Case 3: Repair Loop

Input:

```text
The runtime created the Pal, but the evals are empty and the workflow is only headings.
```

Expected behavior:

- marks the first pass incomplete;
- creates a repair package for missing evals and shallow workflow;
- keeps original creation evidence separate from repair evidence.

Failure modes:

- accepts shallow assets;
- rewrites unrelated Pal files;
- hides missing checks.

Scoring:

- 0: accepts false completion;
- 1: notices gaps but does not package repair;
- 2: clear incomplete judgement plus bounded repair package.
