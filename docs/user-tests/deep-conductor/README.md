# DeepConductor User Manual Test

## What This Test Checks

This test checks whether DeepConductor can turn a normal user request into a complete no-code coordination flow:

```text
task understanding -> Team First Discovery -> routing correction -> Work Plan -> Asset Preflight -> Execution Trace -> Owner Assignment Integrity -> Closure Gate -> Quinn verification -> deliverable
```

The test is not only checking whether the assistant writes a useful plan. It checks whether the plan is traceable, assigned correctly, asset-aware, closed, and verified.

## Where To Test

Run this in a project that has AgentPal enabled through a thin binding.

The project should contain:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- an AgentPal protected block in `AGENTS.md` for Codex, or in `CLAUDE.md` for Claude Code

If you are testing the R241 fresh project package, open this project in Codex:

```text
J:\开发\AgentPal_dcos\测试记录\r241-fresh-project-user-walkthrough\fresh-project
```

## Before You Start

Confirm:

- AgentPal is connected to the current project.
- The current project is the external test project, not the AgentPal workspace.
- You are not expecting AgentPal to run a backend, CLI, daemon, scanner, Marketplace backend, or live GitHub release.

## How To Start

Copy the main request from `deep-conductor-test-script.md` into the AgentPal-enabled project.

Then copy the boundary pressure request from the same file.

## What You Should See

The answer should visibly include:

- Task Intake
- Team First Discovery
- Routing Decision
- Rejected Assignment Reasons
- Execution Graph
- Pal Work Plans
- Asset Preflight
- Execution Trace
- Owner Assignment Integrity Gate
- Closure Gate
- Quinn Final Verification
- Final Deliverable

## How To Judge Pass / Fail

Use `deep-conductor-manual-test-checklist.md` and `deep-conductor-pass-fail-rubric.md`.

Pass means the answer shows the full coordination chain and corrects wrong assignments. It does not mean live external user validation, Marketplace release, backend completion, or full certification.

## If Project-Bound Mode Is Limited

If the host cannot prove it loaded the external project as a separate project-bound thread, record:

```text
project_bound_host_surface: not-run
result: pass_with_notes
```

Do not convert this into a full project-bound pass. The user can still inspect whether the DeepConductor content chain is correct, but one more host-level manual replay is needed.

## Results That Cannot Count As Pass

Do not count as pass if:

- the answer only writes a plan but shows no Team First Discovery;
- it creates a new team without checking existing Team Packs first;
- it names Pals but some selected Pals have no work plan, asset preflight, or output;
- it says Quinn verified but Quinn has no verification output;
- it lets Faye do routine promotion execution;
- it lets Quinn write ordinary copy;
- it lets PalSmith do routine execution when an existing team fits;
- it omits Closure Gate or Owner Assignment Integrity.
