# Example: Source Based Article

## 用户请求

“根据我贴的调研资料，写一篇介绍 AgentPal Pal Pack 的文章。”

## Harper 的判断

这是基于资料写作任务。需要确认目标读者、发布渠道、资料来源和是否允许引用。不能补写资料中没有的当前事实。

## 执行策略

使用 `source-grounded-writing`、`outline-writer`、`draft-writer`、`communication-risk-review`。

## 任务包 / 报告 / handoff

如果资料缺来源或更新时间，由当前 AI 逐案考虑是否需要研究视角补证据表。Harper 收到 evidence 后写文章草稿，并列出使用资料和待确认事实。

## 模型和推理强度建议

强模型用于资料边界判断和最终复验；中等模型可写初稿。推理强度：medium。

## Evidence 要求

资料清单、来源时间、关键断言对应来源、未覆盖问题。

## 验收标准

文章读者清楚，关键事实可追溯，没有伪造引用。

