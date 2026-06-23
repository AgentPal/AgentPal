# 示例：用模板生成办公文档

## 用户请求

用这个 Word 模板和表格里的数据生成一批通知文件。

## Morgan 的判断

这是办公模板填充任务。不能覆盖模板；需要字段映射、缺失字段清单和人工复核。

## 执行策略

使用 `office-template-fill`、`spreadsheet-task-plan`、`document-processing-plan` 和 `conversion-quality-review`。输出新文件到独立目录。

## 任务包 / Handoff

- Inputs: template path, data table path, output directory
- Operations: inspect template fields, map data, generate copies
- Constraints: preserve template, do not infer missing legal/financial fields
- Output: generated documents, missing field report, review checklist

## 模型与推理强度

字段映射 medium；合同、财税、人事或法律文本建议强模型复验并要求人工确认。

## Evidence 要求

字段映射表、缺失字段、生成文件路径、抽样文档截图或文本对照、未覆盖模板声明。

## 验收标准

每个占位符有来源或缺失说明；输出文件命名清楚；敏感字段最小化。

