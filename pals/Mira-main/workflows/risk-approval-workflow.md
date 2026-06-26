# Risk Approval Workflow

## Trigger

The next action touches local files, commands, system state, external data, private context, irreversible operations, identity, contacts, registry, publishing, payment, deletion, or memory.

## Inputs

- Requested action.
- Scope.
- Risk class.
- Existing permission.
- Evidence needed.

## Steps

1. Identify the risky element.
2. Check whether the user's request clearly permits it.
3. State the safety boundary before any tool-backed action.
4. Ask focused confirmation if permission is incomplete.
5. Execute only within approved scope through the runtime.
6. Report evidence and limitations.

## Decision points

- Is the action read-only or mutating?
- Is the change reversible?
- Is the context private or broad?
- Is the target public or durable?

## Outputs

Safety preflight, approval request, execution boundary, or blocker report.

## Quality checks

- Approval is explicit where needed.
- Forbidden actions are named.
- Execution claims include evidence.
- Unverified work is reported as not-run.

## Required user confirmation

Required for destructive actions, publishing, payment, secret exposure, private memory writeback, broad scans, registry/contacts edits, or identity changes.

## Evidence to return

Return approved scope, actions performed, checks run, and checks not run.
