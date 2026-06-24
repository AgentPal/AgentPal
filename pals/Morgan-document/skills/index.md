# Morgan Skills Index

Each internal skill must use skills/<skill-id>/SKILL.md as the runtime entry. README.md remains human-readable notes.

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| [batch-file-organization](batch-file-organization/SKILL.md) | skills/batch-file-organization/SKILL.md | [README](batch-file-organization/README.md) | Use this skill when you need to 为批量分类、复制、移动、归档和目录整理生成低风险计划。 |
| [conversion-quality-review](conversion-quality-review/SKILL.md) | skills/conversion-quality-review/SKILL.md | [README](conversion-quality-review/README.md) | Use this skill when you need to 审查 PDF/DOCX/XLSX/PPTX/Markdown/CSV 等转换后的结构、内容、表格和引用质量。 |
| [document-processing-plan](document-processing-plan/SKILL.md) | skills/document-processing-plan/SKILL.md | [README](document-processing-plan/README.md) | Use this skill when you need to 为 DOCX、Markdown、TXT、PPTX 或混合文档生成摘要、清理、合并、拆分、转换任务计划。 |
| [duplicate-cleanup-plan](duplicate-cleanup-plan/SKILL.md) | skills/duplicate-cleanup-plan/SKILL.md | [README](duplicate-cleanup-plan/README.md) | Use this skill when you need to 生成重复文件候选和审查流程，不直接删除。 |
| [file-privacy-risk-check](file-privacy-risk-check/SKILL.md) | skills/file-privacy-risk-check/SKILL.md | [README](file-privacy-risk-check/README.md) | Use this skill when you need to 判断文件任务是否涉及证件、合同、财税、医疗、客户资料、凭据、私钥、账号和外发风险。 |
| [file-search-handoff](file-search-handoff/SKILL.md) | skills/file-search-handoff/SKILL.md | [README](file-search-handoff/README.md) | Use this skill when you need to 生成元数据优先的文件搜索任务包，先找候选路径，不默认读取文件内容。 |
| [file-task-intake](file-task-intake/SKILL.md) | skills/file-task-intake/SKILL.md | [README](file-task-intake/README.md) | Use this skill when you need to 判断文件、文档、表格、PDF、归档或办公自动化请求属于哪类任务，并决定澄清、规划、转交或风险提醒。 |
| [metadata-indexing-plan](metadata-indexing-plan/SKILL.md) | skills/metadata-indexing-plan/SKILL.md | [README](metadata-indexing-plan/README.md) | Use this skill when you need to 规划用文件名、路径、扩展名、大小、时间、hash 和摘要字段建立可重建索引。 |
| [naming-taxonomy-builder](naming-taxonomy-builder/SKILL.md) | skills/naming-taxonomy-builder/SKILL.md | [README](naming-taxonomy-builder/README.md) | Use this skill when you need to 设计文件命名模板、分类法、版本规则、状态规则和冲突处理。 |
| [office-template-fill](office-template-fill/SKILL.md) | skills/office-template-fill/SKILL.md | [README](office-template-fill/README.md) | Use this skill when you need to 把用户数据和办公模板填充需求整理成可执行、可验收的任务包。 |
| [pdf-task-plan](pdf-task-plan/SKILL.md) | skills/pdf-task-plan/SKILL.md | [README](pdf-task-plan/README.md) | Use this skill when you need to 区分文本型、扫描型、混合型、表格密集型和表单 PDF，规划提取、OCR、转 Markdown 和复验。 |
| [spreadsheet-task-plan](spreadsheet-task-plan/SKILL.md) | skills/spreadsheet-task-plan/SKILL.md | [README](spreadsheet-task-plan/README.md) | Use this skill when you need to 为 XLSX、CSV、TSV 的清洗、汇总、合并、校验和报告生成任务包。 |

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
