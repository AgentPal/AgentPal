# conversion-quality-review

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


## Skill 名称

conversion-quality-review

## 中文名

格式转换质量审查

## 用途

审查 PDF/DOCX/XLSX/PPTX/Markdown/CSV 等转换后的结构、内容、表格和引用质量。

## 适用场景

PDF 转 Markdown 后复验、DOCX 转 PDF、XLSX 转 CSV、PPT 提纲提取。

## 不适合场景

只看转换成功退出码就判定完成；版权内容无边界长期保存。

## 输入信息

源文件、转换产物、目标格式、抽样页/表/段、允许误差和验收标准。

## 处理流程

比对结构；抽样内容；检查表格、页码、图片占位、编码和丢失项；给修复建议。

## 输出格式

通过/不通过、问题清单、抽样证据、需重跑项、用户注意。

## 验收标准

有源与产物对应；关键字段、页码、表格和编码已检查。

## 风险边界

转换可能丢格式、丢公式、乱表格或改变语义。

## 与其他 Skill / Runbook 的关系

复验 document、spreadsheet、pdf 和 template 任务。
