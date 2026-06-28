# Pal Asset Directory Standard

Date: 2026-06-28
Standard id: `agentpal-pal-asset-directory-standard.v0.5`

## Purpose

This standard defines the responsibility of each Pal asset directory and how
assets move from raw material to stable Pal capability.

## Directory Rules

| Directory | Purpose | Should contain | Should not contain | Promotion / extraction rules | Org Pack relationship |
| --- | --- | --- | --- | --- | --- |
| `identity/` | Long-term persona, voice, relationship, and boundaries. | persona, voice, collaboration posture, address style, durable boundaries. | task logs, tool commands, project-specific temporary preferences. | Stable user-facing or collaboration traits may be promoted here after review. | Org Packs may describe recommended roles but must not copy Pal identity bodies. |
| `core/` | Pal work protocols. | task loop, context rules, collaboration, handoff, verification, reporting, memory policy. | industry facts, raw research, one-off reports. | Repeated verified working methods may become core protocols only after they are Pal-wide. | Org Pack governance can reference compatible protocols as judgement inputs. |
| `knowledge/` | Stable professional knowledge. | concepts, domain rules, verified references, reusable principles. | raw source dumps, unverified notes, current task state. | Research conclusions become knowledge after source review and de-identification. | Org Packs may include public-safe knowledge patterns, not private Pal knowledge bodies. |
| `research/` | Source gathering and analysis. | source inventories, comparison notes, evidence extracts, research drafts. | final rules without source context, long-term memory, runtime state. | Stable conclusions move to `knowledge/`; reusable methods move to `skills/`, `workflows/`, or `runbooks/`. | Org Packs may carry public-safe research summaries when reusable and non-private. |
| `skills/` | Pal role-level comprehensive work capabilities. | Pal Skill packages with purpose, context, refs, approvals, outputs, verification, writeback. | raw CLI recipes, runtime Agent Skill files, pure knowledge articles, reports. | Repeated successful methods or learning candidates become Pal Skills after verification. | Org Packs may recommend Pal Skill candidates but cannot install or route them automatically. |
| `workflows/` | Standard multi-step work systems. | inputs, outputs, stages, participants, approvals, blockers, verification, writeback. | single tool commands, isolated facts, exception-only procedures. | A repeated multi-step process becomes a workflow when stages and acceptance are stable. | Org Packs often describe reusable workflow candidates. |
| `runbooks/` | Concrete operation or exception handling manuals. | symptoms, checks, steps, stop conditions, escalation, verification. | broad strategy, normal end-to-end workflow, identity text. | Repeated failure handling becomes a runbook after stop and escalation rules are known. | Org Packs may include public-safe runbook candidates. |
| `learning/` | Candidate assets and lessons under review. | candidate skills, workflows, runbooks, memory candidates, feedback, observations. | unlabelled dumps, private secrets, finished reports with no extraction target. | Items must either be promoted, revised, rejected, or archived with status. | Org Pack learning content must be de-identified before becoming reusable. |
| `memory/` | Durable memory and decision records. | user preferences, Pal experience, project memory refs, tool lessons, routing lessons. | full reports, raw evidence, credentials, transient state. | Reports may be summarized into memory only after extracting stable lessons. | Org Packs can define memory policy, not copy customer-private memory. |
| `state/` | Current mutable working state. | current task, current plan, active blockers, active collaboration notes. | long-term memory, public examples, completed reports. | Task completion should clear state or extract to `reports/`, `memory/`, or `learning/`. | Org Packs should not depend on a Pal's runtime state. |
| `reports/` | Task, stage, health, and verification reports. | completion reports, health reports, review reports, evidence summaries. | raw secrets, current mutable state, canonical memory. | Reports may generate memory candidates or learning candidates after review. | Org Packs may include public-safe sample reports only. |
| `evals/` | Quality gates and assessment methods. | checklists, rubrics, PalBench cases, smoke checks, regression cases. | task body content, private evidence, runtime claims without evidence. | Repeated acceptance criteria become evals when they can be checked consistently. | Org Packs should include verification checklists and boundary evals. |
| `examples/` | Sample inputs, outputs, and task packages. | public-safe examples, success/failure cases, sample task packages. | binding source of truth, private customer data, formal rules that belong in core. | Mature examples may inspire skills or workflows but remain non-authoritative. | Org Packs may include public-safe examples as reusable teaching material. |

## Cross-Cutting Rules

- A report is not memory until stable lessons are extracted.
- Research is not knowledge until reviewed and summarized.
- A workflow is not a runbook; workflows handle normal multi-step work, runbooks
  handle concrete operations or exceptions.
- A Pal Skill is not an Agent Skill; Agent Skills are execution candidates for
  host runtimes.
- External projects are not default storage for Pal assets.
- Public reusable assets must remove private user data, credentials, private
  project facts, and customer identifiers.
