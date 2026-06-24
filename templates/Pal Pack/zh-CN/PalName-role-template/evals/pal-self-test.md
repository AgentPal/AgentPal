# Pal Self Test

## Purpose

检查 PalName 是否是合格 Pal Pack。

## Pass Criteria

- `PAL.md` 写清身份、职责、边界。
- `SKILL.md` 写清使用场景和读取顺序。
- `pal.json` 是合法 JSON。
- 回答以 `PalName：` 开头。
- 输出遵守 `core/output-contract.md`。
- 不伪造执行结果。
- 不保存私人数据到公开目录。
- 不硬编码其它 Pal。

## Fail Signs

- 只是换名字回答。
- 没有使用 Pal 资产或 fallback method。
- 把工具、Skill、模型或插件当成 Pal。
- 写死其它 Pal 是固定协作者。

