# Deep Conductor Protocol

Deep Conductor is AgentPal's no-code coordination methodology for complex work and project-level goals.

It is not an executor. It does not run commands, call external Agents, launch parallel workers, modify files, publish artifacts, operate as an AgentPal runtime, or manage background project tasks.

## Master Loop

Deep Conductor uses 12 operational steps:

1. Goal Intake.
2. Project / Pal Memory Loading.
3. Deliverable and Stage Judgement.
4. Capability Inventory Read.
5. Runtime Skill / Plugin / MCP Awareness.
6. Workflow Topology Selection.
7. Context Access Planning.
8. Prompt Shaping and Token Budgeting.
9. Runtime Task Package Generation.
10. Verification Planning.
11. Synthesis and User-facing Explanation.
12. Routing Memory Writeback Candidate.

Each step produces no-code artifacts that a host Runtime may read, execute, or verify only within its own permissions and evidence rules.

## Step 1: Goal Intake

Purpose: capture the user's goal and decide whether it is an ordinary task, a composite task, or a project-level continuing task.

Read:

- user goal;
- explicit constraints;
- current Pal entry context;
- `core/first-pal-gate.md`;
- `core/deliverable-aware-task-judgement-gate.md`.

Output:

- goal summary;
- task kind;
- project-or-single-task decision;
- initial risk and verification needs.

Do not:

- execute before owner judgement;
- ask broad clarification before naming provisional stage owners for composite work;
- treat wording as a keyword route.

Templates:

- `templates/orchestration/deep-conductor-plan.md`
- `templates/orchestration/project-conductor-task-map.md`

Eval:

- `evals/orchestration/deep-conductor-master-loop-self-test.md`

## Step 2: Project / Pal Memory Loading

Purpose: reuse bounded memory without leaking private content or assuming stale Runtime state is current.

Read:

- Pal-owned memory summaries when relevant;
- project memory or project state summaries when available and approved;
- `memory/runtime/cross-runtime-pal-memory-protocol.md`;
- `orchestration/routing-memory-writeback-protocol.md`.

Output:

- `memory_used`;
- memory sources;
- freshness and privacy notes;
- candidate lessons, not rules.

Do not:

- copy private memory into public packages;
- treat memory as proof of current Runtime capability;
- make Routing Memory a database or route map.

Templates:

- `templates/orchestration/conductor-decision-record.md`
- `templates/orchestration/context-budget-plan.md`

Eval:

- `evals/orchestration/conductor-memory-writeback-self-test.md`

## Step 3: Deliverable and Stage Judgement

Purpose: identify material work stages, deliverables, owner Pal candidates, and verification needs.

Read:

- `contacts/pals.json`;
- `registry/pal.index.json`;
- relevant Pal capability profiles or selected Pal `PAL.md` files when needed.

Output:

- domain focus;
- deliverables;
- stages;
- owner Pal candidates;
- verifier candidates;
- owner gaps.

Do not:

- make `HTML -> Atlas`, `research -> Vega`, or any task-to-Pal fixed route;
- let Runtime own a Pal-layer stage;
- collapse a multi-stage goal into one topic owner.

Templates:

- `templates/orchestration/project-conductor-task-map.md`
- `templates/orchestration/context-packet-template.md`

Eval:

- `evals/orchestration/project-conductor-task-map-self-test.md`

## Step 4: Capability Inventory Read

Purpose: identify candidate Runtime, model, reasoning, Runtime Skill, plugin, MCP, and Pal capabilities.

Read:

- `docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md`;
- `orchestration/capability-inventory-protocol.md`;
- smallest relevant Capability Inventory profile indexes or profiles.

Output:

- `capabilities_read`;
- candidate resources;
- evidence required before use.

Do not:

- scan the user's machine;
- read the full inventory by default;
- treat illustrative profiles as proof of availability.

Templates:

- `templates/orchestration/context-budget-plan.md`
- `templates/orchestration/conductor-decision-record.md`

Eval:

- `evals/orchestration/runtime-skill-aware-conductor-self-test.md`

## Step 5: Runtime Skill / Plugin / MCP Awareness

Purpose: separate Pal-owned Skills from host Runtime-installed Skill, plugin, and MCP candidates.

Read:

- `orchestration/pal-skill-vs-runtime-skill-protocol.md`;
- `templates/orchestration/runtime-skill-aware-task-package.md`;
- relevant Skill / Plugin / MCP profiles if needed.

Output:

- `runtime_skill_candidates`;
- `pal_owned_skills_used`;
- evidence required before Runtime Skill use.

Do not:

- claim a Pal executes a host Skill;
- claim a Runtime Skill is available without current evidence;
- mix Pal methods and Runtime tools.

Templates:

- `templates/orchestration/runtime-skill-aware-task-package.md`

Eval:

- `evals/orchestration/runtime-skill-aware-conductor-self-test.md`

## Step 6: Workflow Topology Selection

Purpose: choose the simplest topology that can satisfy the goal and evidence needs.

Read:

- `orchestration/workflow-topology-protocol.md`;
- `orchestration/owner-verifier-workflow-protocol.md`;
- `orchestration/parallel-independent-review-protocol.md`;
- `orchestration/plan-execute-verify-protocol.md`;
- `orchestration/project-conductor-workflow.md` for project-level goals.

Output:

- selected topology;
- alternatives rejected;
- topology reason;
- owner/verifier/reviewer candidate boundaries.

Do not:

- use Deep Conductor for simple single-owner tasks;
- start group chat;
- claim automatic parallel or external Agent execution.

Templates:

- `templates/orchestration/deep-conductor-plan.md`
- `templates/orchestration/conductor-decision-record.md`

Eval:

- `evals/orchestration/deep-conductor-no-auto-execution-self-test.md`

## Step 7: Context Access Planning

Purpose: define what each Pal, verifier, reviewer, or Runtime package can read and cannot read.

Read:

- `orchestration/context-access-list-protocol.md`;
- `orchestration/context-packet-protocol.md`;
- `templates/orchestration/context-packet-template.md`.

Output:

- Context Packets;
- Context Access Lists;
- `allowed_files`;
- `cannot_read`;
- context isolation rules.

Do not:

- copy full chat history;
- share reviewer drafts before synthesis;
- include private memory, secrets, or unrelated Pal assets.

Templates:

- `templates/orchestration/context-packet-template.md`
- `templates/orchestration/project-conductor-task-map.md`

Eval:

- `evals/orchestration/token-budget-in-conductor-self-test.md`

## Step 8: Prompt Shaping and Token Budgeting

Purpose: adapt the package to the candidate Runtime / model / reasoning / Skill profile while protecting verification quality.

Read:

- `orchestration/token-cost-aware-conductor-policy.md`;
- `templates/orchestration/context-budget-plan.md`;
- relevant model and reasoning profiles if needed.

Output:

- context budget plan;
- profile read count;
- reasoning candidate;
- prompt shaping notes.

Do not:

- skip required evidence to save tokens;
- use memory as proof of current state;
- forward unnecessary files.

Templates:

- `templates/orchestration/context-budget-plan.md`
- `templates/orchestration/deep-conductor-plan.md`

Eval:

- `evals/orchestration/token-budget-in-conductor-self-test.md`

## Step 9: Runtime Task Package Generation

Purpose: turn the plan into one or more host Runtime-readable task packages.

Read:

- `orchestration/task-package-output-contract.md`;
- `templates/orchestration/runtime-skill-aware-task-package.md`;
- `templates/orchestration/next-round-runtime-task-package.md`.

Output:

- Runtime Skill-aware task package;
- next-round runtime task package;
- required context;
- forbidden context;
- acceptance criteria.

Do not:

- make the host Runtime the Pal-layer owner;
- claim execution happened;
- make target Runtime a fixed route.

Templates:

- `templates/orchestration/runtime-skill-aware-task-package.md`
- `templates/orchestration/next-round-runtime-task-package.md`

Eval:

- `evals/orchestration/runtime-skill-aware-conductor-self-test.md`

## Step 10: Verification Planning

Purpose: define how completion will be checked before the Runtime executes.

Read:

- `orchestration/owner-verifier-workflow-protocol.md`;
- `templates/orchestration/verifier-context-packet.md`;
- `templates/orchestration/verification-result-record.md`;
- selected verifier Pal profile or `PAL.md` when needed.

Output:

- verification plan;
- evidence requirements;
- verifier candidate;
- pass / fail / blocked criteria.

Do not:

- accept a completion report as evidence by itself;
- hide `not-run`;
- hardcode Quinn or any Pal as verifier.

Templates:

- `templates/orchestration/verifier-context-packet.md`
- `templates/orchestration/verification-result-record.md`

Eval:

- `evals/orchestration/deep-conductor-no-auto-execution-self-test.md`

## Step 11: Synthesis and User-facing Explanation

Purpose: explain the plan, candidates, evidence needs, and next step to the user.

Read:

- owner / reviewer / verifier final reports when they exist;
- `pals/Mira-main/core/output-contract.md`;
- synthesis templates relevant to the selected topology.

Output:

- user-facing explanation;
- selected topology and reason;
- candidate resources and boundaries;
- next-round package summary;
- user decisions needed.

Do not:

- add specialist conclusions not present in reports;
- smooth away conflict;
- imply execution has happened.

Templates:

- `templates/orchestration/deep-conductor-plan.md`
- `templates/orchestration/parallel-review-synthesis-summary.md`

Eval:

- `evals/orchestration/deep-conductor-master-loop-self-test.md`

## Step 12: Routing Memory Writeback Candidate

Purpose: preserve useful lessons for future judgement without creating fixed routes.

Read:

- returned evidence;
- verification result;
- `orchestration/routing-memory-writeback-protocol.md`;
- `templates/orchestration/routing-decision-record.md`;
- `templates/orchestration/routing-result-record.md`.

Output:

- routing memory writeback candidate;
- Runtime Skill usage result candidate;
- next-time recommendation as evidence, not a rule.

Do not:

- write private facts into public memory;
- auto-write a database;
- say future tasks must use the same Pal, Runtime, Skill, model, or topology.

Templates:

- `templates/orchestration/routing-decision-record.md`
- `templates/orchestration/routing-result-record.md`
- `templates/orchestration/conductor-decision-record.md`

Eval:

- `evals/orchestration/conductor-memory-writeback-self-test.md`

## Boundary

Deep Conductor artifacts are no-code coordination artifacts. They may guide Codex, Claude Code, OpenCode, OpenHands, Gemini CLI, or another host Runtime. They do not prove that those Runtimes, Skills, plugins, MCP tools, files, commands, or external services are available.
