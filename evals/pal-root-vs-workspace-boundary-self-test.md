<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Pal Root vs Workspace Boundary Self-Test

Purpose: verify that AgentPal root and embedded Pal modules keep clear ownership boundaries.

## AgentPal Root Owns

- contacts
- registry
- runtime awareness
- model/plugin capability context
- orchestration protocols
- project binding
- Runtime Response Gate
- Codex Subagent Mode protocol

## Embedded Pal Owns

- identity
- professional knowledge
- skills
- workflows
- runbooks
- learning
- examples
- evals
- public-safe memory/state/report placeholders
- output contract

## Expected Behavior

When a specialist Pal is selected, it reads its embedded assets and uses its output contract. It may mention possible collaborators, but final collaboration and owner selection are AI / Mira / Brain case-by-case.

Do not recreate per-Pal contacts, registry, runtime, models, plugins, orchestration, adapters, or import staging directories inside official bundled specialist Pals.

If the user explicitly asks to save a Skill, or similar operations exceed three times, the owner Pal stores the formal Skill under its own `skills/<skill-id>/SKILL.md` and updates its own `skills/index.md`.

