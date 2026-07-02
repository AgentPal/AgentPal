# 08 Test Closure Gate

## Goal

Verify that Closure Gate catches missing work before the final answer.

## Prompt

```text
请检查刚才的团队任务是否真的完成。用 Closure Gate 检查 required steps、verifier、child step 回流、asset use、routing correction 和 memory/writeback decision。
```

## Expected Result

The output should include:

```text
closure_gate_status:
required_steps_closed:
verifier_handled:
child_steps_returned:
asset_use_recorded:
routing_correction_recorded:
memory_writeback_decision:
skipped_or_blocked_reason:
final_status:
```

## Required Behavior

- If a required step is missing, status cannot be complete.
- If verifier was required but absent, status must be blocked or partial.
- If a child task was created, it must return to the parent.
- If a Pal was selected but did not participate, the gate must flag it.
- If a tool was used without Pal asset judgement, the gate must flag it.

## Fail Signals

- Closure Gate is missing.
- Closure Gate says pass while required steps are missing.
- Verifier is missing but the task is still marked complete.
- Child steps do not return.
- Fake handoff is not detected.
