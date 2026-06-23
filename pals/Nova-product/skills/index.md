# Nova Skills Index

Each internal skill must use skills/<skill-id>/SKILL.md as the runtime entry. README.md remains human-readable notes.

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| [acceptance-criteria-writer](acceptance-criteria-writer/SKILL.md) | skills/acceptance-criteria-writer/SKILL.md | [README](acceptance-criteria-writer/README.md) | Use this skill when you need to Create testable, observable acceptance criteria for product requirements, user stories, handoffs, and runtime tasks. |
| [decision-log-writer](decision-log-writer/SKILL.md) | skills/decision-log-writer/SKILL.md | [README](decision-log-writer/README.md) | Use this skill when you need to Record product decisions, alternatives, rationale, assumptions, tradeoffs, and follow-up review points. |
| [developer-handoff](developer-handoff/SKILL.md) | skills/developer-handoff/SKILL.md | [README](developer-handoff/README.md) | Use this skill when you need to Package product decisions into a clear handoff for suitable implementation collaborator, Codex, Claude Code, OpenHands, Gemini CLI, DeepSeek-TUI, or AgentPal runtime. |
| [feature-prioritization](feature-prioritization/SKILL.md) | skills/feature-prioritization/SKILL.md | [README](feature-prioritization/README.md) | Use this skill when you need to Rank candidate features by user value, product stage, development cost, risk, dependencies, and AgentPal boundary impact. |
| [idea-intake](idea-intake/SKILL.md) | skills/idea-intake/SKILL.md | [README](idea-intake/README.md) | Use this skill when you need to Classify an incoming user idea, feature request, product direction, project, automation request, Pal/Agent request, or development request before Nova chooses the next Skill. |
| [mvp-slicing](mvp-slicing/SKILL.md) | skills/mvp-slicing/SKILL.md | [README](mvp-slicing/README.md) | Use this skill when you need to Choose the right first release shape: validation version, lightweight complete working version, complete platform version, or long-term productized version. |
| [prd-writer](prd-writer/SKILL.md) | skills/prd-writer/SKILL.md | [README](prd-writer/README.md) | Use this skill when you need to Turn a defined product direction into a structured Product Requirements Document that can be reviewed, accepted, and handed off. |
| [problem-definition](problem-definition/SKILL.md) | skills/problem-definition/SKILL.md | [README](problem-definition/README.md) | Use this skill when you need to Turn "I want a feature" into a clear problem statement that explains who has the problem, when it happens, what they do now, and why it is worth solving. |
| [product-feedback-synthesis](product-feedback-synthesis/SKILL.md) | skills/product-feedback-synthesis/SKILL.md | [README](product-feedback-synthesis/README.md) | Use this skill when you need to Turn raw feedback, user comments, bug-like complaints, feature requests, and stakeholder opinions into themes, product signals, decisions, and next actions. |
| [risk-and-assumption-review](risk-and-assumption-review/SKILL.md) | skills/risk-and-assumption-review/SKILL.md | [README](risk-and-assumption-review/README.md) | Use this skill when you need to Identify unvalidated assumptions, product risks, privacy/compliance issues, overbuild signals, technical uncertainty, and evidence gaps before development or release. |
| [scope-and-boundary](scope-and-boundary/SKILL.md) | skills/scope-and-boundary/SKILL.md | [README](scope-and-boundary/README.md) | Use this skill when you need to Define what version one includes, what it excludes, what is deferred, and what would make the product overbuilt. |
| [user-scenario-mapping](user-scenario-mapping/SKILL.md) | skills/user-scenario-mapping/SKILL.md | [README](user-scenario-mapping/README.md) | Use this skill when you need to Map who will use the product, when they need it, what they are trying to accomplish, and what must be true for them to switch. |

## Skill Memory Default

When the user explicitly asks to save a Skill, or similar operations happen more than 3 times, create the formal Skill under this Pal's own skills/<skill-id>/SKILL.md and update skills/index.md. Use memory/skill-memory/ only for runtime notes before either formal trigger is met; use learning/ only as an exception when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.

