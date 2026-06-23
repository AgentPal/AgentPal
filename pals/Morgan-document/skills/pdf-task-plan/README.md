# pdf-task-plan

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


## Skill 名称

pdf-task-plan

## 中文名

PDF 任务计划

## 用途

区分文本型、扫描型、混合型、表格密集型和表单 PDF，规划提取、OCR、转 Markdown 和复验。

## 适用场景

PDF 转 Markdown、报告摘要、表格提取、扫描件 OCR、知识候选生成。

## 不适合场景

把 OCR 结果当最终事实；未经授权读取证件、合同或财税 PDF。

## 输入信息

PDF 路径、目标输出、是否允许 OCR、是否需要表格、页码范围、敏感等级。

## 处理流程

判断 PDF 类型；选择提取策略；保留页码和结构；标记低置信字段；输出候选而非正式知识。

## 输出格式

PDF 类型判断、提取策略、输出结构、复验点、evidence 要求。

## 验收标准

页码可追溯；扫描件标记 OCR 风险；敏感内容不长期保存。

## 风险边界

表格错位、OCR 误识别、页序错误和版权内容保存风险。

## 与其他 Skill / Runbook 的关系

接 documents、conversion-quality-review、file-privacy-risk-check。
