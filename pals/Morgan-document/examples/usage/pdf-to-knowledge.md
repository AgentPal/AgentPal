# 示例：从 PDF 提取可用知识

## 用户请求

把这批 PDF 转成 Markdown，然后整理成可用知识。

## Morgan 的判断

这是 PDF 提取和知识候选任务。转换后的 Markdown 先是 extracted candidate，不直接进入正式知识库。

## 执行策略

使用 `pdf-task-plan`、`document-processing-plan` 和 `conversion-quality-review`。先判断 PDF 类型；扫描件需要 OCR 风险标记；表格密集页需要保留结构。

## 任务包 / Handoff

- Operations: classify PDF type, extract text/Markdown, preserve page references
- Constraints: no long-term storage of sensitive fulltext
- Output: extracted Markdown, source map, low-confidence fields, knowledge card candidates

## 模型与推理强度

PDF 判断和转换审查 medium；复杂知识抽取或敏感内容复验用强模型。

## Evidence 要求

PDF 类型列表、转换日志、页码映射、抽样对照、OCR 低置信字段、候选知识卡。

## 验收标准

页码可追溯；OCR 不被当作事实；正式知识需用户确认。
