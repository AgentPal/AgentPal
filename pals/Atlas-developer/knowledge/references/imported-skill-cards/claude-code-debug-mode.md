# Skill Card: doraemonkeys/claude-code-debug-mode

## Name

Claude Code Debug Mode

## Source

GitHub: https://github.com/doraemonkeys/claude-code-debug-mode

## License

MIT. GitHub API checked on 2026-06-22.

## Handling Status

rewrite-as-atlas-skill

## Main Purpose

Provides a focused debugging workflow for coding agents, centered on hypotheses, runtime evidence, instrumentation, and human-in-the-loop verification.

## Useful For Atlas

- Structuring non-Pal runtime debugging handoff.
- Asking for reproduction, hypothesis, minimal fix, and regression evidence.
- Preventing vague prompts like "fix this" from reaching weak or low-context models.

## Not Suitable For Direct Use

- Atlas must not insert logs, run programs, clean debug code, or modify files itself.
- Any instrumentation must be scoped, reversible, and performed by the target Runtime.
- Atlas should not copy the upstream Skill text.

## Safety Boundary

Debug tasks may touch runtime code and logs. Atlas must require affected paths, rollback notes, test results, and a clear statement when the issue cannot be reproduced.

## Third-Party Source Included

No. This card contains only source metadata and Atlas's own assessment.

## Pal Contacts

No. This is a Skill/resource candidate, not a standard Pal Pack.

## Recommended Trigger Scenarios

- A build, test, UI, or runtime failure has logs or screenshots.
- An non-Pal runtime needs a narrow debugging task.
- A weak model needs a highly structured debug prompt.

## How Atlas Uses It

Atlas uses it as a reference for `runbooks/debugging/agent-debug-handoff.md`, an AgentPal/Atlas-native debug handoff runbook.

## Attribution

Original project: `doraemonkeys/claude-code-debug-mode` by doraemonkeys and contributors. See the source repository and its MIT License for original terms.


