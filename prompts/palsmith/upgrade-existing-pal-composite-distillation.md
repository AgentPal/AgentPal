# Upgrade An Existing Pal With Composite Distillation

Copy this prompt into AgentPal when you want PalSmith to plan a safe upgrade for
an existing Pal.

```text
/pal PalSmith 请帮我升级一个已有 Pal。

目标 Pal：

我想改变或增强的内容：
- 语气 / 说话风格：
- 性格：
- 思维方式 / 判断逻辑：
- 岗位职责：
- 岗位知识：
- Skill / 插件 / 外部软件 / Agent 使用：
- 工作流：
- 记忆 / 复盘：
- 协作 / discovery / Marketplace 边界：

资料来源或灵感来源：

发布目标：
- 私有
- 团队内部
- 公开示例
- official candidate
- Marketplace candidate

请先用 AI 语义判断这是不是 simple edit、existing Pal composite upgrade、
authorization flow，还是其他模式。不要用关键词路由，不要因为出现或没
出现某个词就直接决定路线。

如果是 existing Pal composite upgrade，请先输出升级计划，至少包括：
- upgrade mode judgement 和判断理由
- current Pal inventory
- source boundary
- cognitive distillation plan
- voice / personality distillation plan
- role-duty installation plan
- domain knowledge installation plan
- Skill / plugin / Agent capability map
- workflow impact plan
- memory impact plan
- collaboration / discovery / Marketplace boundary impact plan
- target file map
- eval plan
- allowed write paths
- blocked write paths
- 最多 3 个确认问题

不要直接写文件。
不要直接改 PAL.md / persona.md / voice.md / knowledge / workflow。
不要复制原作台词或未授权内容。
不要冒充真人、角色、品牌或权利方。
不要修改 central contacts。
不要把私有资料写入公开示例或 Marketplace。
等我确认后，再准备 Runtime Task Package。
```

Example:

```text
/pal PalSmith 给 Luma 增加康娜卡姆依那种说话、语气、性格；再加上乔布斯的思维逻辑、设计的极致、简约追求。
```

Expected first move:

- semantically classify the request as an existing Pal composite upgrade;
- explain that this is not a simple file edit;
- state source boundaries for character-inspired voice and public-person
  thinking inspiration;
- produce an upgrade plan and target file map;
- ask for confirmation before any write.
