# Runtime Skill Candidate Decision Protocol

This protocol decides whether a Task Package should name host Runtime Skill, plugin, or MCP candidates.

It is a no-code decision protocol. It does not call, install, scan, validate, or invoke host Runtime capabilities.

## Decision Steps

1. Identify deliverable and stage.
   - Name the user goal, final deliverable, and current stage.
   - Keep stage ownership at the Pal layer before naming execution candidates.

2. Identify execution capability need.
   - Decide whether the stage needs browsing, document rendering, repository analysis, external lookup, file conversion, test execution, or another host capability.
   - If no specialized capability is needed, use an ordinary Task Package.

3. Read minimal Runtime / Skill / Plugin / MCP profiles.
   - Use the smallest relevant profile slice.
   - Profiles are judgement inputs only.

4. Check current host Runtime assumptions.
   - State the current Runtime if known.
   - Mark unknown availability as unknown.
   - Do not infer installation from a profile or a past task.

5. Decide `runtime_skill_candidates`.
   - Name only candidates that fit the stage.
   - Include reason, required inputs, and evidence required.
   - Candidate does not mean forced call.
   - Preserve `not_a_fixed_route: true` in the resulting package.

6. Decide fallback if Skill unavailable.
   - Choose ordinary Runtime Task Package, alternate candidate, user install/Runtime choice, or blocked/not-run.
   - Make fallback explicit before execution.

7. Generate Runtime Skill-aware Task Package.
   - Use `templates/orchestration/runtime-skill-aware-task-package.md`.
   - Include Pal-owned Skills separately from Runtime Skill candidates.
   - Set `availability_check_required: true` unless the current Runtime has already reported availability in this task.

8. Define verification criteria.
   - List required evidence from the host Runtime.
   - Identify owner/verifier Pal candidates when quality review is needed.
   - Do not accept tool output without checking it against the original goal.

9. Record usage result.
   - If the task runs, record success, failure, not-run, verification result, fallback used, and next-time candidate guidance.
   - Usage Memory is a learning hint, not a route.

## Availability Rule

If the Runtime cannot confirm an installed Skill, the package asks the Runtime to check. If the Skill is missing, unsupported, disabled, or unsafe, the package follows fallback.

## Boundary Rule

Runtime Skill candidates are host Runtime capabilities. They are not Pal-owned Skills and not AgentPal capabilities.

Every candidate result remains `not_a_fixed_route: true`.
