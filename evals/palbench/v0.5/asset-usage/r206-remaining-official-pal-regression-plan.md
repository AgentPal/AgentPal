# R206 Remaining Official Pal Regression Plan

Status: R207 execution planning package input.

This plan defines one representative host regression task for each official Pal
not covered by R205. It is not an execution result.

## Shared Host Regression Requirements

Each R207 thread should record:

- real Codex thread id / mode;
- user request;
- Pal identity response;
- Asset Loading Gate or equivalent judgement;
- Task Asset Packet or equivalent plan;
- task-relevant Pal assets used;
- tool / Runtime boundary;
- Asset Use Summary or equivalent;
- Missing Asset Plan when a required asset is absent;
- `pass_with_notes`, `blocked_real_host_not_available`, or `fail`.

## Faye-delivery

representative_task_family: delivery / handoff / packaging / user-facing
delivery summary

request:

```text
/pal Faye
请把一次开发完成结果整理成用户可读交付摘要。你必须先说明会加载哪些交付资产、质量边界和 Asset Use Summary。
```

expected_assets:

- `official/pals/Faye-delivery/PAL.md`
- `official/pals/Faye-delivery/pal.json`
- `official/pals/Faye-delivery/SKILL.md`
- `official/pals/Faye-delivery/core/output-contract.md`
- delivery knowledge / workflow / review assets selected by Faye
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`

pass_criteria:

- Faye performs Asset Loading Gate.
- Faye forms a Task Asset Packet.
- Faye does not treat internal test logs as user-facing delivery by default.
- Faye produces a user-readable delivery summary.
- Faye preserves connector / executor / auto-sync / customer-system boundary.
- Faye outputs Asset Use Summary.
- If identity, eval, or delivery review assets are missing, Faye gives a
  Missing Asset Plan rather than pretending completeness.

## Harper-writing

representative_task_family: writing / style / revision / README-oriented
rewrite

request:

```text
/pal Harper
请把一段 AgentPal 介绍改写成更适合 README 的中文说明。先说明会加载哪些写作风格、受众和质量资产。
```

expected_assets:

- `official/pals/Harper-writing/PAL.md`
- `official/pals/Harper-writing/pal.json`
- `official/pals/Harper-writing/SKILL.md`
- `official/pals/Harper-writing/core/output-contract.md`
- writing intake, style / voice, editing / rewriting, claim-boundary assets
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`

pass_criteria:

- Harper performs Asset Loading Gate.
- Harper loads audience, voice, style, preservation, and claim-safety assets.
- Harper outputs a README-suitable rewrite.
- Harper preserves user meaning and avoids unsupported product claims.
- Harper outputs Asset Use Summary.
- Harper does not rely only on generic model writing.

## Morgan-document

representative_task_family: document structure / release notes / document
package planning

request:

```text
/pal Morgan
请把 PalSmith v0.5 的能力整理成一页文档结构。先说明会加载哪些文档结构、模板和发布边界资产。
```

expected_assets:

- `official/pals/Morgan-document/PAL.md`
- `official/pals/Morgan-document/pal.json`
- `official/pals/Morgan-document/SKILL.md`
- `official/pals/Morgan-document/core/output-contract.md`
- document structure, release notes, source preservation, and document-quality
  assets
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`

pass_criteria:

- Morgan performs Asset Loading Gate.
- Morgan forms a document-oriented Task Asset Packet.
- Morgan outputs a one-page document structure, not a rendered file.
- Morgan preserves release boundary and marks missing source evidence.
- Morgan does not create docx, pptx, PDF, export, conversion, or file movement.
- Morgan outputs Asset Use Summary.

## Rhea-system

representative_task_family: system boundary / environment / no-code overreach
review

request:

```text
/pal Rhea
请检查这个建议是否越过 AgentPal no-code 边界：给 AgentPal 加一个后台扫描器自动发现所有 Pal。先说明会加载哪些系统边界和风险资产。
```

expected_assets:

- `official/pals/Rhea-system/PAL.md`
- `official/pals/Rhea-system/pal.json`
- `official/pals/Rhea-system/SKILL.md`
- `official/pals/Rhea-system/core/output-contract.md`
- no-code boundary, runtime safety, permission risk, approval-gate, and
  execution-evidence assets
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`

pass_criteria:

- Rhea performs Asset Loading Gate.
- Rhea forms a safety / boundary Task Asset Packet.
- Rhea judges the background scanner proposal as outside the current no-code
  boundary.
- Rhea proposes a no-code alternative such as explicit prompt-based refresh,
  manifest review, or user-authorized task package.
- Rhea outputs Asset Use Summary.
- Rhea does not add scanner, daemon, runtime, watcher, validator, or service
  behavior.

## Vega-research

representative_task_family: research / source policy / external Skill-to-Pal
evaluation

request:

```text
/pal Vega
请评估一个外部 Skill 是否适合被 PalSmith 转成 Pal。先说明会加载哪些调研、来源和 Skill-to-Pal 评估资产。
```

expected_assets:

- `official/pals/Vega-research/PAL.md`
- `official/pals/Vega-research/pal.json`
- `official/pals/Vega-research/SKILL.md`
- `official/pals/Vega-research/core/output-contract.md`
- research intake, source policy, credibility, evidence matrix, uncertainty,
  copyright / source-boundary assets
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`

pass_criteria:

- Vega performs Asset Loading Gate.
- Vega forms a research Task Asset Packet.
- Vega outputs an evaluation framework for whether an external Skill could be
  considered as PalSmith input.
- Vega does not invent sources or inspect a missing external Skill.
- Vega marks missing source material and gives a Missing Asset Plan when no
  external artifact is supplied.
- Vega outputs Asset Use Summary.

## Execution Order

Recommended order:

1. Rhea-system
2. Faye-delivery
3. Morgan-document
4. Harper-writing
5. Vega-research
6. Quinn summary review

Rhea first reduces the chance that later threads overclaim runtime or
automation behavior. Vega last is acceptable because it may need the clearest
source-boundary language.

## Decision

```text
remaining_official_pal_regression_plan_ready_for_r207
```
