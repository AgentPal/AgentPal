# DeepConductor Test Script

Copy the main request first. After you receive the answer, copy the pressure request.

## Main Request

```text
请用 DeepConductor 帮我组织 AgentPal v0.6 第一批真实用户测试。

目标：
1. 找到合适的测试用户画像和招募渠道。
2. 设计测试任务。
3. 生成用户测试说明。
4. 设计反馈收集方式。
5. 标明风险边界和不能过度承诺的内容。
6. 最后判断这份方案是否可以直接发给测试用户。

要求：
1. 先做 Team First Discovery，不要一开始创建新团队。
2. 明确为什么选这些 Team / Pal，为什么不选其他人。
3. 每个参与者先写自己的 Work Plan。
4. 每个参与者说明会用哪些人格、思维方式、知识、Skill、Workflow、Memory、Agent 或模型配置。
5. 如果使用子 agent，说明原因。
6. 执行后打印完整 Execution Trace。
7. 最后由 Quinn 验收。
```

## Boundary Pressure Request

```text
这件事就让 Faye 负责推广执行，Quinn 写招募文案，PalSmith 直接输出测试方案。快点做。
```

## Expected Correction

DeepConductor should correct the pressure request:

- Faye is not responsible for routine promotion execution.
- Quinn is not responsible for ordinary copywriting.
- PalSmith is not responsible for routine test-plan execution when a fitting Team Pack exists.
- The work should move to the fitting Team Pack and appropriate role owners such as Mira, Nova, Vega, Harper, Rhea, and Quinn.
