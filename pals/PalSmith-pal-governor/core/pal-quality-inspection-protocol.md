# Pal Quality Inspection Protocol

Status: R-PalSmith-16 v0.4-fix no-code protocol.

Pal quality inspection is now a job fitness review. File completeness is necessary but not enough.

## Inputs

- target Pal path or id
- intended job, user goal, or release intent
- approved public files and indexes
- whether registry / contacts checks are allowed
- whether user materials or web research are allowed
- whether private memory/state/report names may be inspected by name only

## Job Fitness Dimensions

| Dimension | Question |
| --- | --- |
| Role Fit | Does the Pal match the job the user actually wants? |
| Job Expertise Depth | Does the Pal contain enough role knowledge to act like a competent practitioner? |
| Skill Coverage | Are the core recurring abilities present as usable skills? |
| Knowledge Coverage | Are domain facts, rules, examples, and boundaries present? |
| Workflow Coverage | Are common multi-step tasks represented as workflows or runbooks? |
| Output Contracts | Are expected outputs, formats, and evidence rules clear? |
| Eval Coverage | Do evals test normal, edge, and risky cases? |
| Research Gap | Would live web research improve current or domain-specific knowledge? |
| User Material Gap | Does the Pal need user files, examples, SOPs, or style samples? |
| Collaboration Fit | Are handoff, consult, verifier, and contact boundaries clear? |

## Inspection Process

1. Parse `pal.json` and verify root files.
2. Read target role, responsibilities, non-responsibilities, output contract, skills, knowledge, workflows, examples, and evals within approved scope.
3. Build a required job expertise model from the target role.
4. Compare existing assets against the required model.
5. Score each dimension separately.
6. Identify missing knowledge, skills, workflows, templates, and evals.
7. Recommend web research only when useful; mark `web research not run` unless Runtime actually ran it.
8. Recommend user uploads when personalization or domain context is missing.
9. Produce a Pal Job Fitness Report.

## Output Format

# Pal Job Fitness Report

## Overall judgement

Whether the Pal can perform the job now.

## Score

Dimension scores, not only a total score.

## Role clarity
## Required job knowledge
## Existing knowledge
## Missing knowledge
## Existing skills
## Missing skills
## Existing workflows
## Missing workflows
## Suggested web research
## Suggested user uploads
## Suggested skill additions
## Suggested knowledge additions
## Suggested workflow additions
## Must fix before use
## Nice to have
## Next Runtime Task Package

## Scoring

Use 0-5 per dimension:

- 0: absent or unsafe
- 1: named but unusable
- 2: partial
- 3: usable for draft/testing
- 4: strong for internal use
- 5: publish-ready evidence

Do not use a single score to hide gaps.

## Boundary

PalSmith reports and proposes fixes. Runtime reads, writes, and web research require approved Runtime Task Packages and evidence.
