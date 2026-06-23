# Rhea Workflows Index

Rhea v0.1 内置一个正式 Workflow：

| id | path | purpose |
|---|---|---|
| system-maintenance-lifecycle | `workflows/system-maintenance-lifecycle/` | 从问题接入、范围划定、只读检测、风险审查、审批、执行层交接、evidence 审查、报告和记忆候选的系统维护闭环 |

Workflow 不直接执行命令、安装、卸载、删除或系统写入。真实执行交给 Runtime 或外部 Runtime，Rhea 负责计划、边界、审批和复验。

