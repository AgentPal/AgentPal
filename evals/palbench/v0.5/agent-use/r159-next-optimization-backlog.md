# R159 Next Optimization Backlog

Status: open
Date: 2026-06-29

## R160 Candidates

| backlog_id | priority | item | rationale |
| --- | --- | --- | --- |
| R160-01 | P1 | Add two tiny public Delivery Pack fixtures for child-review tests | R159 proved child/background mechanics but pack content was missing |
| R160-02 | P1 | Add optional operator evidence format for Codex Plan Mode / Goal Mode UI switches | R159 can only mark these as recommendation-only |
| R160-03 | P2 | Add external-agent support wording table | Claude and CodeWhale have minimal evidence; DeepSeek is version/help-only; OpenCode/Gemini unavailable |
| R160-04 | P2 | Add a machine-readable Agent-use evidence rollup JSON | Current R159 records are Markdown plus fixture JSON; a rollup would simplify future validation |
| R160-05 | P3 | Add a small direct-use privacy fixture for customer-private rejection | Current R159 privacy tests are decision evidence, not a real customer-data file fixture |

## Keep Out Of Scope

- Do not add a daemon, scanner, connector, database, marketplace, external installer, or runtime client.
- Do not auto-copy Pal Packs into external `.agentpal`.
- Do not claim full non-Codex host support without a real host conversation.

