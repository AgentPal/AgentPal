# Development Lifecycle Example

用户请求：

```text
帮我给项目加一个导入预检功能。
```

Atlas 应先转成开发生命周期任务，而不是直接让执行层改代码。

```text
## 判断
这是开发任务，但还需要明确范围和验收。

## 本轮目标
为导入流程增加预检：在真正写入前检查文件结构、License 字段和明显风险，并返回可读错误。

## 必读资料
- README.md
- AGENTS.md
- src/imports/
- tests/imports/

## 修改范围
- src/imports/preflight*
- src/imports/*
- tests/imports/*

## 禁止事项
- 不要改 UI。
- 不要新增外部依赖。
- 不要修改真实数据目录。
- 不要改发布脚本。

## 执行计划
1. 强模型 high：确认接口边界和测试方案。
2. 中等模型 medium：实现预检逻辑和测试。
3. Atlas：审查 evidence 和边界。

## 验收标准
- 无效导入会返回结构化错误。
- 合法导入不受影响。
- 相关测试通过。
- 完成报告列出 changed files、测试结果和剩余风险。

## 完成汇报格式
- 完成内容
- 修改文件
- 验证结果
- 未完成或风险
- 需要人工确认
```

