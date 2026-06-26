# runtime-capability-knowledge

## Concept Explanation

Runtime capability is the set of actions the current execution layer can perform under current permissions, tools, sandbox, network, and workspace state.

## Judgement Standards

- Capability must be observed or declared by the current Runtime.
- Capability does not imply permission to use it.
- Available tools do not guarantee success.
- Unknown capability must be marked unknown until inspected.
- Unsupported actions must be not-run or blocked.

## Examples

- A Runtime can read files but not browse the web.
- A Runtime can run shell commands but may not have admin rights.

## Counterexamples

- Assuming a different runtime's plugin exists here.
- Claiming tests passed without test output.

## Scope

Use before commands, file writes, browsing, release checks, or external tool use.

## How This Becomes Skill, Workflow, Or Eval

Skill: runtime-capability-assessment. Runbook: runtime-capability-check. Eval: system runtime capability.

## Common Mistakes

Mixing capability with approval, skipping not-run labels, and failing to name working directory.

## Source Refs Or Local Notes

Based on local AgentPal runtime boundary plus SRC-09 and SRC-11.

