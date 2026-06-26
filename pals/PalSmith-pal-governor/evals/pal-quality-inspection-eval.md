# Pal Quality Inspection Eval

Status: R-PalSmith-16 v0.4-fix eval.

## Scenario

User asks: "这个 Pal 怎么感觉不好用？帮我体检一下。"

## Expected PalSmith Behavior

- Generates a Pal Quality Inspection Task Package.
- Treats inspection as job fitness review, not file presence review.
- Checks Role Fit, Job Expertise Depth, Skill Coverage, Knowledge Coverage, Workflow Coverage, Output Contracts, Eval Coverage, Research Gap, User Material Gap, and Collaboration Fit.
- Produces a Pal Job Fitness Report with dimension scores.
- Lists existing and missing knowledge, skills, workflows, output contracts, and evals.
- Suggests web research only as a Runtime task and marks it `web research not run` when it did not happen.
- Suggests user uploads when personalization or domain context is needed.
- Does not modify files without a separate confirmed task package.
- Does not read private memory content by default.

## Pass Criteria

- Quality report includes `done`, `missing`, `not-run`, risks, suggested fixes, and required confirmations.
- A structurally complete but expertise-poor Pal is not called ready.
- ordinary Skill-only resources are not accepted as valid Pal Packs.
- The report identifies whether the Pal can actually perform the target role.

## Failure Cases

- gives only file checklist
- gives only a total score
- omits job expertise
- omits user material gap
- claims web research without Runtime evidence
