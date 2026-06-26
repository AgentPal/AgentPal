# Quinn Quality / Verification Source Inventory

Access date: 2026-06-26.

Runtime evidence: live web research was run by the current Codex execution layer using web search.

## Sources

| Source ID | Title | URL | Publisher | Source type | Trust level | Key points | Relevance to Quinn | Should become | Actual file path | Coverage status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QV-S01 | What is the Definition of Done? | https://www.atlassian.com/agile/project-management/definition-of-done | Atlassian | Industry guide | High | DoD is a shared completion standard for product increments; it distinguishes done from ready and supports release readiness. | Supports Definition of Done and completion gate design. | Knowledge, skill, workflow, eval | `knowledge/definition-of-done-knowledge.md` | covered |
| QV-S02 | What is Acceptance Criteria? | https://www.atlassian.com/work-management/project-management/acceptance-criteria | Atlassian | Industry guide | High | Acceptance criteria are predefined conditions a task must satisfy before acceptance; they reduce ambiguity. | Supports acceptance criteria design and review. | Knowledge, skill, workflow, eval | `knowledge/acceptance-criteria-knowledge.md` | covered |
| QV-S03 | Just Say No to More End-to-End Tests | https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html | Google Testing Blog | Engineering practice | High | Test strategy should avoid overreliance on E2E tests; a pyramid shape with many small tests is a useful heuristic. | Supports test strategy planning and regression gate design. | Knowledge, skill, workflow | `knowledge/test-strategy-knowledge.md` | covered |
| QV-S04 | The Practical Test Pyramid | https://martinfowler.com/articles/practical-test-pyramid.html | Martin Fowler | Engineering article | High | Test pyramid groups tests by granularity and helps choose economical coverage. | Supports risk-prioritized test strategy. | Knowledge, skill | `knowledge/test-strategy-knowledge.md` | covered |
| QV-S05 | Risk-based testing | https://glossary.istqb.org/en_US/term/risk-based-testing | ISTQB Glossary | Standards glossary | High | Risk-based testing manages, selects, prioritizes, and uses test activities based on risk types and levels. | Supports risk severity and regression prioritization. | Knowledge, skill, workflow | `knowledge/risk-severity-knowledge.md` | covered |
| QV-S06 | Releases | https://docs.gitlab.com/user/project/releases/ | GitLab Docs | Product documentation | High | Releases package code, binaries, documentation, and release notes into an auditable snapshot. | Supports release quality gate evidence requirements. | Knowledge, workflow, runbook | `knowledge/release-quality-gate-knowledge.md` | covered |
| QV-S07 | Release evidence | https://docs.gitlab.com/user/project/releases/release_evidence/ | GitLab Docs | Product documentation | High | Release evidence snapshots data related to a release and can include artifacts for audits. | Supports evidence completeness and release gate reports. | Knowledge, skill, runbook | `knowledge/evidence-review-knowledge.md` | covered |
| QV-S08 | Deployment gates concepts | https://learn.microsoft.com/en-us/azure/devops/pipelines/release/approvals/gates | Microsoft Learn | Product documentation | High | Deployment gates enforce criteria before deployment proceeds. | Supports release quality gates and required approvals. | Knowledge, workflow | `knowledge/release-quality-gate-knowledge.md` | covered |
| QV-S09 | Google Engineering Practices: Code Review | https://google.github.io/eng-practices/review/ | Google | Engineering practice | High | Independent review helps maintain code and product quality. | Supports cross-Pal review, evidence review, and independent quality judgement. | Knowledge, workflow, eval | `knowledge/cross-pal-review-knowledge.md` | covered |
| QV-S10 | Evaluation best practices | https://developers.openai.com/api/docs/guides/evaluation-best-practices | OpenAI | Official AI evaluation docs | High | Evaluation should define tasks and judge model performance with clear criteria; documentation notes platform transition/deprecation timeline. | Supports Quinn eval design and agent-quality verification. | Knowledge, eval | `evals/quinn-quality-capability-eval.md` | covered |
| QV-S11 | How evals drive the next chapter in AI | https://openai.com/index/evals-drive-next-chapter-of-ai/ | OpenAI | Official article | High | Evals specify what great means, measure performance under real conditions, and improve from errors. | Supports evidence-backed quality loops for AI/Pals. | Knowledge, workflow, eval | `knowledge/quality-reporting-knowledge.md` | covered |
| QV-S12 | Demystifying evals for AI agents | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | Anthropic | Engineering article | High | Evals reveal agent issues before users see them and compound over the lifecycle. | Supports false completion detection and agent-quality evals. | Knowledge, eval | `knowledge/false-completion-knowledge.md` | covered |
| QV-S13 | Building Effective AI Agents | https://www.anthropic.com/research/building-effective-agents | Anthropic | Research / engineering article | High | Agentic systems benefit from clear success criteria, feedback loops, and human oversight. | Supports cross-Pal review and quality gates for agentic work. | Knowledge, workflow | `knowledge/cross-pal-review-knowledge.md` | covered |

## Credibility Notes

The strongest sources are official product/platform docs and recognized engineering practice sources. Google Testing Blog and Google Engineering Practices are used for test strategy and review discipline. Atlassian is used for agile DoD and acceptance criteria framing. ISTQB is used for risk-based testing vocabulary. GitLab and Microsoft are used for release evidence and quality gate concepts. OpenAI and Anthropic are used for AI/agent eval framing.

## Uncertainty

Quinn is a no-code Pal asset, not a CI product. Release evidence and deployment gate examples are adapted as judgement concepts, not copied as tool requirements.
