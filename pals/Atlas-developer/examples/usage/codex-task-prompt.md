# Codex Task Prompt Example

```text
你现在负责一个明确范围的开发任务。

## 目标
修复用户报告的导入索引显示错误。

## 必读资料
- README.md
- AGENTS.md
- core/verification-protocol.md

## 修改范围
- src/imports/
- tests/imports/

## 禁止事项
- 不要改 UI 布局。
- 不要修改认证、权限或发布脚本。
- 不要顺手重构无关模块。

## 验收标准
- 相关测试通过。
- 新增或更新失败场景测试。
- 完成报告列出 affected paths、测试结果和剩余风险。

## 建议模型
中等或强模型。

## 推理强度
medium。

## 任务长度
中。

## 完成汇报格式
完成内容、修改文件、验证结果、未完成或风险。
```

