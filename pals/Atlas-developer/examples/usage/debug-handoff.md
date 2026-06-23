# Debug Handoff Example

用户请求：

```text
测试失败了，让 Claude Code 帮我看一下。
```

Atlas 生成外部 Runtime Debug 交接：

```text
## Debug 目标
定位并修复 imports 预检测试失败。

## 失败现象
`tests/imports/preflight.test.ts` 中 invalid-license-case 失败。

## 必读资料
- AGENTS.md
- src/imports/preflight.ts
- tests/imports/preflight.test.ts

## 允许修改范围
- src/imports/preflight.ts
- tests/imports/preflight.test.ts

## 禁止事项
- 不要修改 UI。
- 不要安装依赖。
- 不要修改真实 imports 数据。
- 不要删除测试绕过失败。

## 定位要求
先复现或说明无法复现。提出最多 3 个假设，优先找最小根因。

## 最小修复要求
只修复导致该测试失败的逻辑或测试断言，不做无关重构。

## 建议模型与推理强度
Claude Code，medium；如果根因涉及跨模块边界，升为 high。

## 完成汇报格式
- 根因
- 修改文件
- 测试结果
- 剩余风险
- 是否需要人工确认
```

Atlas 复验时只根据 evidence 判断，不接受“已经修好”的口头结论。

