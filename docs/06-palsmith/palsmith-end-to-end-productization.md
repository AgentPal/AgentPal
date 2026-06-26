# PalSmith End-To-End Productization

PalSmith v0.2 productization means turning existing Pal creation and AI team creation assets into a user-copyable loop. It does not turn PalSmith into executable software.

## Product Path

1. User goal input.
2. PalSmith clarification.
3. Pal or AI team design.
4. Runtime Task Package for asset generation.
5. Self-test and job fitness review.
6. Repair Task Package when gaps are found.
7. Usage example.
8. Publish or private-use readiness advice.

## User Goal Input

Good inputs can be plain language:

```text
/pal PalSmith Create a customer support Pal for a small Shopify store.
/pal PalSmith Build an AI team for a solo B2B SaaS founder.
```

The user does not need to name every file. PalSmith should ask for missing essentials:

- target job and users;
- responsibilities and non-responsibilities;
- example tasks;
- source materials;
- privacy boundary;
- language and tone;
- whether optional web research is allowed;
- whether output is private, team-local, or public-shareable.

## Pal Design

For a single Pal, PalSmith should produce:

- Pal name, id, directory proposal;
- role statement;
- responsibilities and non-responsibilities;
- usage scenarios;
- job expertise model;
- required knowledge, Skills, workflows, runbooks, templates, evals, and examples;
- registry/contact recommendation as a later separate package.

## AI Team Design

For an AI team, PalSmith should produce:

- recommended small team size;
- member Pals and why each exists;
- owner Pal, verifier Pal, and consultant candidates;
- team-local vs global-contact candidates;
- shared knowledge and Context Packet rules;
- conflict risks;
- team Eval Lab outline.

## Asset Generation Package

PalSmith does not write files itself. It prepares a Runtime Task Package that names:

- allowed read paths;
- allowed write paths;
- forbidden paths;
- user confirmation questions;
- expected runtime evidence;
- final report format.

Creation packages must not update `contacts/` or `registry/` unless a separate confirmed registration package is approved.

## Self-Test

After runtime execution, PalSmith reviews evidence:

- created paths;
- `pal.json` parse result;
- root files and output contract;
- job-specific knowledge depth;
- actionable Skills and workflows;
- eval coverage;
- public/private boundary;
- missing or not-run checks.

## Repair Package

If the draft is shallow or incomplete, PalSmith prepares a repair package. A repair package should name the gap precisely, for example:

- missing job knowledge;
- Skill is only a title;
- workflow has no decision steps;
- eval does not test real failure modes;
- public example contains private details;
- boundary overlaps another Pal.

## Usage Example

Every first creation path should end with one minimal usage example:

```text
/pal <NewPalName> Review this draft customer reply and mark escalation risks.
```

The example should state expected input, expected output, and acceptance evidence.

## Readiness Advice

PalSmith should classify the result as:

- idea;
- draft;
- testing;
- stable;
- publish-ready;
- not ready.

`publish-ready` requires evidence. If checks were not run, PalSmith must say `not-run`.

## v0.2 Acceptance

The PalSmith product path is acceptable when a user can copy one example and one task package, run it in a host runtime, and receive a draft Pal or team with a clear self-test and repair path.
