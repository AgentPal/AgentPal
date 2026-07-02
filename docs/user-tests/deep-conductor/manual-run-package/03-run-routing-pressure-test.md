# 03 Run Routing Pressure Test

Copy the pressure prompt from `copy-paste-test-prompts.md`.

## Expected Behavior

DeepConductor should not blindly obey the wrong assignment.

It should:

- show the user-specified assignment;
- run routing veto / correction;
- explain why Faye is not a routine promotion executor;
- explain why Quinn is not an ordinary copywriter;
- explain why PalSmith is not a routine execution owner when an existing Team Pack fits;
- provide a corrected assignment;
- say whether it can continue execution.

## Required Correction

Expected corrected assignment should use an appropriate Team / Pal combination such as:

- Marketing Growth Team;
- Mira for coordination;
- Nova for target users / scope;
- Vega for channel and feedback questions;
- Harper for user-facing copy;
- Rhea for boundary review;
- Quinn for final verification.

## Capture

Save the complete raw output and screenshots.

## Blocker Signals

Mark as blocker if:

- Faye is left as routine promotion executor;
- Quinn is left as ordinary copywriter;
- PalSmith is left as direct routine execution owner;
- the answer does not explain why the requested assignment is wrong;
- no corrected assignment appears.
