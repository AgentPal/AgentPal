# PalSmith Pal Completeness Guide

PalSmith uses a completeness ladder to decide what a Pal can honestly claim.
This keeps a draft Pal from being treated as executable before it has the assets
needed for real work.

## Completeness Ladder

| Level | What It Has | What Is Missing | Can Do | Must Not Claim | How To Upgrade |
| --- | --- | --- | --- | --- | --- |
| `persona_seed_only` | A name, rough role, or style idea | stable role, knowledge, workflows, tool policy, evals | start discussion and gather requirements | executable Pal, verified Pal, real job capability | define role, boundaries, and source rules |
| `persona_plus_voice` | Persona plus tone or conversation style | job knowledge, workflows, Skill map, runtime policy, evals | keep a consistent voice in limited drafts | professional execution readiness | add role duties and domain knowledge |
| `role_knowledge_pal` | role, duties, boundaries, domain knowledge | repeatable workflow, tool policy, memory, evals | discuss the job and produce limited guidance | reliable task execution across cases | add workflows and quality gates |
| `workflow_capable_pal` | workflows, runbooks, and task path | tool/runtime boundaries, memory rules, regression proof | guide a task process and produce plans | tool-backed execution readiness | map tools, Skills, and host-runtime limits |
| `tool_aware_pal` | knows which host tools may help and when | asset usage regression and representative evidence | prepare tool-aware Task Packages | executable just because a tool exists | add Asset Use Summary and eval evidence |
| `executable_pal` | identity, voice, thinking, role, knowledge, Skill map, workflow, runtime policy, memory policy, collaboration boundary, eval assets | representative task regression | perform bounded Pal work with evidence | verified across untested task families | run asset usage regression |
| `verified_executable_pal` | executable assets plus representative asset usage regression | broader evidence outside tested scenarios | claim readiness for the tested task family | universal readiness for all tasks | expand real host tests case by case |

## Rules

- Persona-only cannot be called executable.
- Tool-aware does not equal executable.
- A host tool is not a Pal asset.
- Verified executable requires asset usage regression evidence.
- A controlled-write fixture is test evidence, not a real user Pal upgrade.

## How PalSmith Should Use This

Before creating or upgrading a Pal, PalSmith should:

1. judge the requested mode by AI judgement, not keyword routing;
2. read the target Pal's relevant assets;
3. assign the current completeness level;
4. name missing assets;
5. produce a Missing Asset Plan if needed;
6. ask for confirmation before writes;
7. record an Asset Use Summary after substantive work.

## Practical Examples

A video editing Pal with only persona and tone is `persona_plus_voice`. It can
sound consistent, but it cannot claim editing expertise until it has editing
knowledge, workflow, tool policy, memory boundary, collaboration rules, and
evals.

A design Pal that directly calls ImageGen without design assets is not
asset-grounded. ImageGen may execute an image request, but it does not replace
the Pal's design thinking, visual workflow, or quality gate.

A test fixture upgraded during R200 can prove the controlled write path. It
does not prove that the real user custom Pal was upgraded, and it does not
promote the fixture to official status.
