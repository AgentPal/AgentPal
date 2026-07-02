# AgentPal v0.6 User Test Pass / Fail Rubric

## Overall Pass

Use `pass` only when all selected feature tests pass in a project-bound host and no required note remains.

## Pass With Notes

Use `pass_with_notes` when the content chain works but any of these remain:

- project-bound host surface not proven;
- slash command surface not verified;
- screenshots missing but raw output complete;
- live external validation not run;
- tester is Codex acting as manual tester;
- fresh project is false.

## P0 Blockers

Any P0 means the feature result is `blocked` or `fail`:

- AgentPal cannot be triggered in the test project.
- Team First Discovery does not execute.
- DeepConductor selects wrong owners and does not correct them.
- A selected Pal has no participation record.
- Pal Work Plan is missing.
- Asset Preflight is missing.
- Workflow Execution Contract step owner is missing.
- Quinn / verifier disappears.
- Closure Gate is missing.
- PalSmith create-Pal flow uses legacy route instead of current main route.
- User custom Pal is public or discoverable by default without authorization.
- Output claims unfinished capabilities are complete.

## P1 Notes

P1 does not always block, but the result must be `pass_with_notes`:

- Project-bound mode not verified.
- Codex slash-command surface not verified.
- Screenshots unavailable but raw output complete.
- Live external validation not completed.
- Fresh project not used.

## P2 Usability Notes

P2 does not block:

- Prompt wording can be clearer.
- Form fields can be easier to fill.
- Output tables can be better formatted.

## Overclaim Failures

Mark as fail if the output claims any of these without evidence:

- strict project-bound pass;
- live external user validation;
- Marketplace live status;
- one-command public installation;
- runtime/backend completed;
- GitHub push / tag / Release;
- full certification of all Pal task families.
