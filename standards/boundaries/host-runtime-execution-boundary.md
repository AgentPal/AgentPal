# Host Runtime Execution Boundary

AgentPal does not execute work by itself.

If files are edited, commands are run, repositories are pushed, releases are published, browser checks are performed, or external systems are contacted, that evidence comes from the current host runtime.

AgentPal files may instruct the host runtime to:

- load bounded Pal context
- judge owner Pals case by case
- create a Task Package
- report command evidence
- mark missing, not-run, blocked, or unverified states honestly

AgentPal files must not claim that a task was executed unless the host runtime provides current evidence.
