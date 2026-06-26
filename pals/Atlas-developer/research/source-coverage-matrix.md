# Atlas Developer Research Source Coverage Matrix

## Coverage summary

| Importance | Total | Covered | Partial | Missing | Coverage |
| --- | ---: | ---: | ---: | ---: | ---: |
| critical | 14 | 14 | 0 | 0 | 100% |
| important | 12 | 12 | 0 | 0 | 100% |
| optional | 6 | 4 | 2 | 0 | 66.7% |

## Matrix

| Source ID | Extracted point | Importance | Should become | Actual file path | Actual section | Coverage status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | Coding-agent tasks need clear prompts, validation, and capability awareness. | critical | skill / workflow | `skills/runtime-task-package-writing-skill.md` | Process | covered | Became task package fields and evidence requirements. |
| A01 | Skills and MCP/tool availability should be considered before execution. | important | knowledge | `knowledge/runtime-task-package-knowledge.md` | Judgement standards | covered | Adapted to AgentPal runtime boundary. |
| A02 | Coding agents execute in runtime sandboxes; Atlas is not that runtime. | critical | boundary knowledge | `knowledge/no-code-agentpal-boundary-knowledge.md` | Concept explanation | covered | Protects no-code AgentPal package. |
| A03 | Context is finite and must be curated. | critical | skill / knowledge | `skills/file-boundary-control-skill.md` | Quality bar | covered | Supports bounded file and context sharing. |
| A04 | Use agentic complexity only when it fits the task. | important | workflow / eval | `workflows/multi-agent-development-workflow.md` | Decision points | covered | Prevents unnecessary multi-Pal/process expansion. |
| A05 | Repository instructions and task clarity improve coding-agent work. | critical | skill | `skills/developer-handoff-skill.md` | Process | covered | Strengthens handoff packet. |
| A06 | AI code review still depends on repository context and instructions. | important | knowledge | `knowledge/code-review-knowledge.md` | Judgement standards | covered | Review is evidence, not completion proof. |
| A07 | Code review protects code health and requires independent consent. | critical | workflow | `workflows/code-review-workflow.md` | Quality checks | covered | Review findings should lead. |
| A08 | Reviewers balance progress with code health. | important | skill | `skills/code-review-skill.md` | Quality bar | covered | Adds risk-prioritized review. |
| A09 | Testing includes methods, bugs, management, and automation. | critical | knowledge / workflow | `knowledge/test-strategy-knowledge.md` | Judgement standards | covered | Test strategy is broader than one command. |
| A10 | Unit tests support regression and design when resilient. | important | runbook | `runbooks/failed-test-triage-runbook.md` | Quality checks | covered | Avoids brittle test-only acceptance. |
| A11 | Releases package code, docs, notes, and evidence snapshots. | critical | workflow / runbook | `workflows/release-readiness-workflow.md` | Evidence to return | covered | Release readiness needs traceability. |
| A12 | Release engineering needs consistent repeatable methods. | important | knowledge | `knowledge/release-engineering-knowledge.md` | Judgement standards | covered | Atlas must require repeatable evidence. |
| A13 | Code reviews catch logic errors and support team learning. | important | knowledge | `knowledge/code-review-knowledge.md` | Examples | covered | Adds review value beyond style. |
| A14 | Definition of Done defines completion across work items. | critical | knowledge / eval | `knowledge/definition-of-done-knowledge.md` | Concept explanation | covered | "Done" needs explicit evidence. |
| A15 | Small problem scopes improve review of AI-generated changes. | critical | knowledge / eval | `knowledge/file-boundary-knowledge.md` | Counterexamples | covered | Controls "while here" refactors. |
| A16 | Avoid complacency with AI-generated code. | critical | knowledge / eval | `knowledge/evidence-based-verification-knowledge.md` | Common mistakes | covered | Completion report is not proof. |
| A04 | Agents can trade cost and latency for performance. | optional | knowledge | `knowledge/multi-agent-development-knowledge.md` | Scope | partial | AgentPal v0.1 remains Simple Pal Mode only. |
| A11 | GitLab releases can generate audit-ready evidence. | optional | workflow | `workflows/release-readiness-workflow.md` | Evidence to return | covered | Concept only, not GitLab-specific dependency. |
| A12 | Large-scale release engineering methods inform smaller teams. | optional | knowledge | `knowledge/release-engineering-knowledge.md` | Scope | partial | Kept as repeatability principle. |
| A15 | AI-friendly codebases are structured and tested. | optional | runbook | `runbooks/refactor-safety-runbook.md` | Quality checks | covered | Used for refactor guardrails. |

## Result

The source set supports the R02 Atlas Developer deepening scope. Missing items are not source gaps; they are future empirical testing gaps after all default Pals are deepened.
