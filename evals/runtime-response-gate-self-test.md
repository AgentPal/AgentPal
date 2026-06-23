<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Runtime Response Gate Self-Test

## Purpose

Verify that Runtime Response Gate runs before every answer and does not contain hard-coded semantic routing.

## Required Gates

- Codex generic gate
- explicit Pal command gate
- project context gate
- Mira owner-routing gate
- AI routing judgement gate
- Owner Pal immediate answer gate
- output contract gate
- safety and availability guardrails
- repeated task candidate gate

## Pass Criteria

- User asks for Codex generic -> answer starts with `Codex generic answer:`.
- Explicit `/pal Name` commands are deterministic.
- User asks owned work -> Mira does not provide the owned work body after handoff.
- Mira handoff -> owner Pal answers immediately.
- Owner Pal answer -> uses Output Contract.
- Semantic owner selection -> AI routing judgement is case-by-case.
- Pal capability reference is not a route map.
- Safety and availability guardrails are deterministic.
- Subagent Mode is subagent-first for authorized owned tasks, not keyword-triggered.
- User asks fixed workflow / Skill / Runbook -> candidate is triggered.

## Fail Criteria

- Mira gives development plan body after handoff.
- Mira gives professional advice body after handoff.
- Mira routes but owner Pal does not answer.
- Codex generic request lacks `Codex generic answer:`.
- Explicit fixed-flow request does not trigger candidate.
- Specialist Pal only changes name and ignores Output Contract.
- A response uses keyword or task-domain mapping as the reason for choosing a Pal.
- A fixed Pal set is required by semantic wording alone.


