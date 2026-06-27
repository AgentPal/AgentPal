# Pal Pack Structure

## Status

Current for AgentPal `v0.1.0-rc.1`.

A Pal Pack is one directory under `official/pals/<Pal-Directory>/`. The AgentPal root is the workspace; it is not itself a single Pal Pack.

## Minimal Usable Structure

```text
official/pals/<Pal-Directory>/
├─ AGENTS.md
├─ PAL.md
├─ README.md
├─ SKILL.md
├─ pal.json
├─ core/
│  ├─ output-contract.md
│  └─ task-loop.md
├─ identity/
│  ├─ persona.md
│  ├─ boundaries.md
│  └─ voice.md
├─ knowledge/
│  └─ index.md
├─ skills/
│  └─ index.md
├─ runbooks/
│  └─ index.md
├─ workflows/
│  └─ index.md
├─ memory/
│  └─ README.md
├─ state/
│  └─ README.md
├─ reports/
│  └─ README.md
└─ evals/
   └─ definition-of-done.md
```

`memory/user/README.md` is also acceptable when the Pal separates user memory from other memory types.

## Standard Additions

- `examples/` with synthetic examples.
- `learning/` with knowledge gaps and candidates.
- `skills/<skill-id>/SKILL.md` for formal Pal-owned Skills.
- `runbooks/<topic>/<runbook>.md` for repeatable procedures.
- `workflows/<workflow-id>/README.md` for multi-step lifecycle flows.

## Official Pattern

Official Pals such as `official/pals/Mira-main`, `official/pals/Atlas-developer`, and `official/pals/Nova-product` are richer than the minimum. Treat them as examples, not as a requirement to fill every directory immediately.

## Validity Rule

A valid Pal answer cannot be only a renamed assistant response. It must use the Pal identity, `core/output-contract.md`, and a relevant asset or an honest fallback method.
