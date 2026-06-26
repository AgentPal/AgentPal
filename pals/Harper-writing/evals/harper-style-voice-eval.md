# Harper Style Voice Eval

## Purpose

Check whether Harper can extract and apply voice without close imitation or fact drift.

## Prompt

User provides two approved brand samples and asks for a support message in the same voice.

## Expected Behavior

- Extract stable voice traits and situational tone.
- Produce support copy that fits the reader's state.
- Preserve facts and avoid unsupported details.
- Ask confirmation if samples are not approved.

## Pass Criteria

Voice guidance is specific, output is clear, and sensitive tone is handled with care.

## Fail Criteria

Harper copies a third-party style too closely, overuses personality, or changes the facts.

## Assets Covered

style-and-voice-control, brand-voice-consistency, plain-language-clarity, consult / delegate / handoff.
