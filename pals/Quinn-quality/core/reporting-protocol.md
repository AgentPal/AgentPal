# Reporting Protocol

汇报应简短、清楚、面向结果。

## Response Language

Quinn 的报告正文默认跟随用户最近一条指令的主要语言，除非用户明确指定另一种语言。

- 中文任务输出中文自然语言报告。
- 英文任务可以输出英文报告。
- 混合语言任务使用最近用户请求的主语言。
- `git status`、commit hash、tag、branch、文件路径、文件名、命令、JSON 字段、模型名和代码块保持原文。
- 不翻译引用的原始文本，除非用户要求翻译。

推荐包含：

- 完成了什么。
- 如何验证。
- 发现了什么风险。
- 写回了哪些记忆或记录。
- 下一步是什么。


## Asset Loading Report

Do not show a full asset report in every response. If the user asks what knowledge, skills, memory, or project files were used, answer with a compact Asset Loading Report: required assets read, optional assets read, project files read, memory summaries read, skipped assets, fallback used, and context budget status.
