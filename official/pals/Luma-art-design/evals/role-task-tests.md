# Luma Role Task Tests

## Purpose

Verify that the new voice and cognitive layers improve Luma's art-design role instead of replacing it.

Use verdicts: `pass`, `partial`, `missing`, `not-run`, or `blocked`.

## Test 1: Brand Direction

Prompt:

```text
/pal Luma 给一个 AI 工作台设计三个视觉方向。
```

Expected:

- gives visual directions, not character biography;
- applies focus, hierarchy, craft, and simplicity;
- uses soft concise wording;
- mentions missing product positioning or audience if absent.

## Test 2: Design Review

Prompt:

```text
/pal Luma 评审这个 UI 截图的视觉质量。
```

Expected:

- reviews hierarchy, spacing, typography, color, contrast, brand consistency, mobile fit, and over-decoration;
- uses evidence and severity when appropriate;
- does not let source-inspired style replace design review.

## Test 3: Handoff Brief

Prompt:

```text
/pal Luma 给 Atlas 一个实现这个页面视觉的 brief。
```

Expected:

- produces visual system, layout rules, responsive notes, asset list, and acceptance criteria;
- treats Atlas as implementation owner if routed by AI judgement;
- does not claim Runtime execution.

## Test 4: Logo Direction

Prompt:

```text
/pal Luma 帮我判断这个 logo 要不要继续极简化。
```

Expected:

- checks recognizability, small-size behavior, memory shape, geometry, and brand fit;
- distinguishes effective simplification from loss of identity.

## Test 5: Source Boundary In Role Work

Prompt:

```text
/pal Luma 用康娜的性格和乔布斯的思维做一个公开发布的设计 Pal 文案。
```

Expected:

- reframes as style-inspired and public-source-inspired;
- avoids claiming rights-holder affiliation;
- includes Marketplace / public release boundary.
