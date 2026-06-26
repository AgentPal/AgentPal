# Harper Writing Capability Eval

## Purpose

Check whether Harper can classify a writing task, frame audience and goal, select the right skill, and return useful content with boundaries.

## Prompt

User asks for a launch announcement based on supplied notes, with a warm but concise tone.

## Expected Behavior

- Identify create or revise task.
- Confirm audience, channel, and publication if missing.
- Preserve supplied facts.
- Avoid adding unsupported claims.
- Return announcement draft and confirmation notes.

## Pass Criteria

Harper produces clear writing, marks assumptions, and keeps publication with the user.

## Fail Criteria

Harper adds facts, ignores audience, omits confirmation needs, or claims verification that did not happen.

## Assets Covered

writing-role, writing-intake, audience-and-goal-framing, content-quality-self-review, AI judgement, no_runtime_code.
