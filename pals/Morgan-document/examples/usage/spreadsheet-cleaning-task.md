# 示例：清洗表格并生成报告

## 用户请求

把这些销售 CSV 清洗一下，按月份和客户汇总成报告。

## Morgan 的判断

这是表格清洗与汇总任务。先读取表头和样例行，不覆盖原始 CSV。金额、日期和客户字段需要复核。

## 执行策略

使用 `spreadsheet-task-plan`、`conversion-quality-review` 和 `file-privacy-risk-check`。生成字段映射、异常行规则和输出文件计划。

## 任务包 / Handoff

- Allowed Paths: 用户指定 CSV 目录
- Operations: inspect headers, sample rows, produce cleaned copy and summary report
- Constraints: do not overwrite source files
- Output: cleaned CSV/XLSX, summary report, data quality notes

## 模型与推理强度

规划 medium；字段歧义多时用强模型；明确清洗可交给中等模型执行。

## Evidence 要求

输入文件清单、输出文件路径、字段映射、异常行数量、抽样验证、未覆盖原表声明。

## 验收标准

汇总维度正确；金额和日期抽样通过；原始文件保留。
