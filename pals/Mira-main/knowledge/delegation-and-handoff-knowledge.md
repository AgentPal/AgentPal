# Delegation And Handoff Knowledge

## 概念解释

Consult, delegate, and handoff are different collaboration modes. Consult keeps Mira as owner and asks for advice. Delegate assigns a stage to another Pal. Handoff transfers active ownership to another Pal.

## 判断标准

- Consult when Mira owns the final output but needs a bounded expert view.
- Delegate when a stage needs specialist work and Mira will later synthesize.
- Handoff when a single owner Pal should take over the task.
- Provide a Context Packet for delegation or handoff.

## 示例

- Consult: Mira asks PalSmith whether a proposed Pal asset edit is governance-safe.
- Delegate: Vega researches sources for a larger report while Mira tracks stages.
- Handoff: PalSmith owns a Pal quality inspection.

## 反例

- Bad: Mira keeps writing the specialist answer after a handoff.
- Bad: Handoff without stating the owner reason.
- Bad: Delegation with no scope or evidence boundary.

## 适用范围

Applies to Pal-layer collaboration only. It does not create active parallel child-agent execution in v0.1.

## 如何转为 skill / workflow / eval

Use with `pal-consult-delegate-handoff-skill.md`, `pal-delegation-workflow.md`, and `mira-delegation-eval.md`.

## 常见错误

- Treating every specialist mention as a handoff.
- Forgetting same-response owner answer when the runtime supports it.
- Allowing Core files to behave like a hidden semantic router.

## 来源引用或本地知识说明

Local references: root AGENTS, Mira AGENTS, PalSmith routing knowledge. External references: `research/source-inventory.md` M09, M10, M12, and M13.
