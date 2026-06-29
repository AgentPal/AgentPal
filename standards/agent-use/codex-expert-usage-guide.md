# Codex Expert Usage Guide For Pals

Status: v0.5 no-code protocol

## Purpose

Every Pal should help the user use Codex like an expert in that Pal's domain.
This guide gives Pals a shared decision surface for Codex modes, Skills,
plugins, child threads, external Agent handoff, and evidence records.

It does not make AgentPal a runtime, subagent system, scanner, connector, or
execution layer. Codex remains the host execution layer when it actually runs
tools, commands, file edits, or background threads.

## Shared Questions

Before recommending Codex execution, a Pal asks:

1. Is the user asking for a short answer, a plan, or execution?
2. Is the work low-risk enough for `normal_chat`?
3. Does the work need design, approval, risk review, or a task package first?
4. Has the user already approved a bounded execution package?
5. Would owner + verifier improve evidence quality?
6. Can parallel review add value without leaking private context?
7. Are the stages dependent and therefore sequential?
8. Did the user, Pal Skill, workflow, project memory, or capability profile
   explicitly specify a tool or external Agent?
9. Which installed Skill/plugin is actually available in this host?
10. What evidence will prove completion?

## Mode Guidance

- Use `normal_chat` for short answers, simple rewrites, and explanation.
- Use `plan_mode` when the user needs options, risk review, task packaging, or
  approval before execution.
- Use `goal_mode` when a clear, bounded, approved task should be executed with
  verification.
- Use `owner_verifier` when one Pal can prepare/execute and Quinn or another
  verifier should independently review evidence.
- Use `parallel_review` when independent reviews add value and privacy can be
  bounded by Context Access Lists.
- Use `sequential_chain` when stages depend on previous outputs.
- Use `external_agent_handoff` when Claude Code, CodeWhale, Gemini CLI, or
  another runtime is explicitly requested or better suited and current evidence
  shows it can at least be handed off safely.
- Use `fallback` when capability, authorization, privacy, or ownership is
  unknown or blocked.

## Child Threads

Use `standards/agent-use/child-thread-decision-card.md` before creating or
recommending child/background threads. `codex_mode` remains one of the R157
enum values; child-thread state goes in `child_thread_type` and
`subthread_subagent_decision`.

## Explicit Tool Directives

Use `standards/agent-use/explicit-tool-directive-rule.md` when the user or a
Pal workflow names a tool, Skill, plugin, runtime, or external Agent. Do not
re-argue tool choice after an explicit directive passes the safety gate. Record
the directive source and invocation record.

## Pal-specific Focus

- Mira: coordinate mode choice, child-thread packaging, and merge-back.
- Rhea: verify Host Capability Snapshot, authorization, privacy, and external
  Agent minimal evidence.
- Atlas: produce Codex Plan/Goal task packages for code, repo, and execution
  work; prepare Claude Code handoffs when appropriate.
- Quinn: verify Decision Cards, Child-thread Decision Cards, Explicit Tool
  Directive Records, invocation evidence, not-run claims, and enum compliance.
- PalSmith: keep Pal-owned Skills, host Skills, plugins, and external Agents
  distinct; design Pal teams without modifying contacts by default.
- Faye: translate business delivery workflows into Task Packages and direct-use
  records when a business process names a tool.
- Morgan: use document/PDF/spreadsheet/presentation runtime Skills through
  direct-use records when files and safety gates are satisfied.
- Nova: enforce Product Design get-context, audit, and image-to-code gates.
- Vega: use research/browser/source evidence Skills when current facts or
  evidence are required; keep facts, inference, and uncertainty separate.
- Harper: use writing/content pipelines and HyperFrames candidates only when
  style, source, media, and install/safety prerequisites are satisfied.

## Evidence

Pals must not claim that Codex Plan Mode, Goal Mode, child threads, subagents,
plugins, external Agents, or Skills ran unless the current host returned
evidence. Recommendation-only stays recommendation-only.

