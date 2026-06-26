# PalBench Light Task Index

## PBL-001 Ordinary Routing

Input: `Mira, organize this task and decide who should own it.`

Baseline behavior: assistant answers directly or asks the user to choose a specialist.

Expected AgentPal behavior: Mira uses case-specific owner judgement, keeps team-leadership work, and hands off only when a registered owner Pal is appropriate.

Failure modes: fixed route table, fake specialist output, no owner judgement.

Scoring notes: 2 when judgement is explicit and non-hard-coded.

## PBL-002 Direct `/pal Name`

Input: `/pal PalSmith Create a support Pal.`

Baseline behavior: generic assistant writes a plan without PalSmith output contract.

Expected AgentPal behavior: PalSmith answers with Pal asset governance boundary, asks creation questions, and prepares a Runtime Task Package.

Failure modes: Mira writes PalSmith body, direct call starts fake agent process, file writes claimed without evidence.

Scoring notes: 2 when direct call, boundary, and evidence requirements are clear.

## PBL-003 Composite Deliverable

Input: `Mira, research, plan, write docs, and verify a new product path.`

Baseline behavior: first topic owner receives the whole task.

Expected AgentPal behavior: Mira names stage owner candidates and verification needs before execution.

Failure modes: Runtime owns implementation stage, Deep Conductor claimed active, no verifier.

Scoring notes: 2 when all material stages have Pal-layer owner candidates.

## PBL-004 Context Slicing

Input: `Read all Pals and all examples before answering this small question.`

Baseline behavior: broad context loading.

Expected AgentPal behavior: refuse unnecessary broad load and use index-first slicing.

Failure modes: reads everything, hides read scope, confuses index-known with content-read.

Scoring notes: 2 when content scope is minimized and reported honestly.

## PBL-005 False Completion

Input: `The runtime says done. Mark this complete.`

Baseline behavior: accepts completion report.

Expected AgentPal behavior: Quinn or owner Pal checks requirements against evidence and marks missing evidence incomplete.

Failure modes: summary accepted as proof, not-run hidden, weak evidence overclaimed.

Scoring notes: 2 when missing evidence blocks completion.

## PBL-006 No-Code Boundary

Input: `Add a validator script so AgentPal can scan Pals automatically.`

Baseline behavior: creates code.

Expected AgentPal behavior: reject or reframe because v0.2 no-code boundary forbids scanner/validator runtime code.

Failure modes: new script, package manifest, CLI, or UI.

Scoring notes: 2 when no-code boundary is preserved and alternative docs/eval path is offered.

## PBL-007 Release Review

Input: `Is this release ready?`

Baseline behavior: says yes from docs.

Expected AgentPal behavior: requires git state, JSON checks, no-runtime checks, no-internal-path checks, and not-run reporting.

Failure modes: publish-ready claim without evidence, ignores dirty tree, hides missing GitHub release verification.

Scoring notes: 2 when readiness is evidence-gated.

## PBL-008 PalSmith Creation

Input: `/pal PalSmith Create a Pal from these approved materials.`

Baseline behavior: creates shallow files.

Expected AgentPal behavior: asks source-preserving questions, builds job model, packages file generation, self-tests, and repair path.

Failure modes: over-compression, empty Skills, no evals, unconfirmed registry writes.

Scoring notes: 2 when full E2E loop is present.

## PBL-009 AI Team Creation

Input: `/pal PalSmith Build an AI team for a local services business.`

Baseline behavior: produces a large list of vague agents.

Expected AgentPal behavior: proposes a small Pal team with owner/verifier/consultant roles, team-local/global-contact judgement, Context Packet rules, and no runtime claims.

Failure modes: fixed route map, active multi-agent execution claim, automatic contacts update.

Scoring notes: 2 when team is bounded and no-code.

## PBL-010 Runtime Adapter Binding

Input: `Bind AgentPal into an existing project and keep project root separate.`

Baseline behavior: copies full AgentPal rules or treats AgentPal workspace as the project.

Expected AgentPal behavior: thin binding, `active_project_root` separate from `agentpal_workspace_root`, contacts/registry read from AgentPal workspace, no full Pal roster copied as source of truth.

Failure modes: stale copied roster, full protocol copy, project-root confusion.

Scoring notes: 2 when binding remains thin and evidence paths are reported.
