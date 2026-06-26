# Vega Skills Index

Each internal skill must use skills/<skill-id>/SKILL.md as the runtime entry. README.md remains human-readable notes.

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| [citation-summary](citation-summary/SKILL.md) | skills/citation-summary/SKILL.md | [README](citation-summary/README.md) | Use this skill when you need to 把多个来源的关键事实整理成可引用摘要，保留来源、时间、支持程度和局限。 |
| [competitor-analysis](competitor-analysis/SKILL.md) | skills/competitor-analysis/SKILL.md | [README](competitor-analysis/README.md) | Use this skill when you need to 帮助用户比较同类产品、项目、工具或方案的定位、能力、差异、可学习点和不应照搬点。 |
| [contradiction-and-uncertainty-check](contradiction-and-uncertainty-check/SKILL.md) | skills/contradiction-and-uncertainty-check/SKILL.md | [README](contradiction-and-uncertainty-check/README.md) | Use this skill when you need to 防止 Vega 只找支持自己结论的来源，检查反证、来源冲突、时间冲突和过度推断。 |
| [copyright-and-source-boundary](copyright-and-source-boundary/SKILL.md) | skills/copyright-and-source-boundary/SKILL.md | [README](copyright-and-source-boundary/README.md) | Use this skill when you need to 防止 Vega 把外部资料全文、付费内容、未授权材料或敏感资料直接写入公开包或长期知识库。 |
| [deep-research-plan](deep-research-plan/SKILL.md) | skills/deep-research-plan/SKILL.md | [README](deep-research-plan/README.md) | Use this skill when you need to 把复杂研究任务拆成可执行的研究问题、子问题、来源计划、搜索计划和验证计划。 |
| [evidence-table-builder](evidence-table-builder/SKILL.md) | skills/evidence-table-builder/SKILL.md | [README](evidence-table-builder/README.md) | Use this skill when you need to 把研究材料整理成证据表，避免只给用户堆摘要或链接。 |
| [github-project-comparison](github-project-comparison/SKILL.md) | skills/github-project-comparison/SKILL.md | [README](github-project-comparison/README.md) | Use this skill when you need to 比较多个 GitHub 项目的适用性、活跃度、集成难度、License、风险和推荐用途。 |
| [knowledge-card-curator](knowledge-card-curator/SKILL.md) | skills/knowledge-card-curator/SKILL.md | [README](knowledge-card-curator/README.md) | Use this skill when you need to 把研究结果转成可写入系统层、Pal 层或项目层的知识卡候选。 |
| [outdated-info-warning](outdated-info-warning/SKILL.md) | skills/outdated-info-warning/SKILL.md | [README](outdated-info-warning/README.md) | Use this skill when you need to 判断某条信息是否可能已经过期，并提醒用户重新验证。 |
| [research-brief-writer](research-brief-writer/SKILL.md) | skills/research-brief-writer/SKILL.md | [README](research-brief-writer/README.md) | Use this skill when you need to 把调研结果压缩成结论先行、证据清楚、能支持下一步行动的研究简报。 |
| [search-query-design](search-query-design/SKILL.md) | skills/search-query-design/SKILL.md | [README](search-query-design/README.md) | Use this skill when you need to 帮助 Vega 为 Runtime 或外部 Runtime 设计高质量搜索查询，而不是只搜索一个泛词。 |
| [source-quality-check](source-quality-check/SKILL.md) | skills/source-quality-check/SKILL.md | [README](source-quality-check/README.md) | Use this skill when you need to 判断资料来源是否可信、是否新鲜、是否有偏见、是否适合引用。 |
| [technical-option-comparison](technical-option-comparison/SKILL.md) | skills/technical-option-comparison/SKILL.md | [README](technical-option-comparison/README.md) | Use this skill when you need to 比较多个技术方案或工具的适用场景、证据、风险和推荐方向。 |
| [vega-research-intake](vega-research-intake/SKILL.md) | skills/vega-research-intake/SKILL.md | [README](vega-research-intake/README.md) | Use this skill when you need to 判断用户请求属于哪类研究任务，明确研究深度、来源需求、输出形式和是否需要其他 Pal 协作。 |

## R03 Research / Intelligence Lead Skill Cards

- `research-intake-skill.md`
- `research-question-framing-skill.md`
- `search-strategy-design-skill.md`
- `source-discovery-skill.md`
- `source-credibility-evaluation-skill.md`
- `source-inventory-building-skill.md`
- `evidence-matrix-skill.md`
- `claim-evidence-alignment-skill.md`
- `research-synthesis-skill.md`
- `comparative-analysis-skill.md`
- `uncertainty-and-confidence-reporting-skill.md`
- `knowledge-distillation-skill.md`
- `research-handoff-skill.md`

## Skill Memory Default

When the user explicitly asks to save a Skill, or similar operations happen more than 3 times, create the formal Skill under this Pal's own skills/<skill-id>/SKILL.md and update skills/index.md. Use memory/skill-memory/ only for runtime notes before either formal trigger is met; use learning/ only as an exception when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.


## Context Loading Rule

Read this index only after this Pal is selected as owner, consultant, reviewer, or direct /pal Name target.

Use this index to choose the smallest relevant asset slice. Do not load every file in this directory by default.

Read assets here when:

- the current task requires this Pal's professional method;
- the output contract needs a specific skill, knowledge card, runbook, or workflow;
- the user asks which assets were used;
- an eval or release check is inspecting this Pal.

Do not read assets here when:

- Mira is only doing initial routing;
- another Pal owns the task and no consultation was requested;
- the task is ordinary chat, Codex generic, or Mira-owned team-leadership work;
- examples, evals, reports, memory, or future design material would be enough only by curiosity rather than task need.

## Formal Skill Asset Map

R13 formal skill mapping lives in `skill-asset-map.md`. It maps every `pal.json` formal skill to either a Flat Skill Card or a Directory Skill Package and records missing assets as release-readiness issues.
