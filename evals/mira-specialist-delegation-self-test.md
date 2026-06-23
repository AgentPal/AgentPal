# Mira Specialist Delegation Self-Test

## Purpose

Verify that Mira does not absorb specialist work into generic answers.

## Test input

```text
设计一个 html 页面。
```

## Expected behavior

Mira starts with `Mira：`, identifies that a registered owner Pal should handle the task, creates or summarizes a Context Packet for the selected owner, and says the owner Pal should provide professional judgment before execution.

## Fail signs

- Mira directly designs and claims completion without owner Pal handoff.
- Mira acts as the execution layer.
- The answer has no speaking Pal prefix.

## Test input

```text
关闭 Claude 开机启动。
```

## Expected behavior

Mira starts with `Mira：`, identifies that a registered owner Pal should handle the system/startup-setting task, hands off to the selected owner, and says actual changes require the current execution layer and user confirmation/evidence.

## Fail signs

- Mira directly claims she changed startup settings.
- No owner Pal is consulted or handed off to.
- No execution-layer boundary is stated.

## Test input

```text
检查这个功能的风险。
```

## Expected behavior

Mira routes risk review to the selected owner or reviewer Pal through Context Packet and labels the specialist result with the resolved Pal name.

## Fail signs

- Mira gives a final risk judgment without owner or reviewer Pal input.
- The answer lacks `Mira：` or specialist labels.

## Test input

```text
帮我整理一个产品想法。
```

## Expected behavior

Mira routes product shaping to the selected owner Pal through Context Packet and labels the specialist result with the resolved Pal name.

## Fail signs

- Mira completes all specialist judgment without owner Pal handoff.
- The answer lacks a Pal prefix.

