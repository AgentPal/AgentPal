# First Pal Gate

The First Pal Gate runs before a Pal-mode answer performs work, asks broad clarification questions, hands off ownership, or lets the Runtime execute.

The first Pal is not always Mira. It can be:

- Mira, when the user sends an ordinary message
- a directly called Pal, such as `/pal Vega` or `/pal Atlas`
- the current owner Pal in an ongoing task

## Required Judgement

The first Pal must decide:

- Is this ordinary conversation?
- Is this a task?
- Is this a single-owner task?
- Is this a composite deliverable task?
- Does it need a staged Task Package?
- Does any stage need a specialist Pal candidate?
- Does any stage need a Runtime / Skill executor candidate?
- Does it need verification before completion can be claimed?

## Specialist Ownership Before Execution

Single-owner does not mean Mira-owned.

Before any Runtime command, shell command, MCP call, file write, or system inspection, the first Pal must decide whether a registered owner Pal should receive the task.

This judgement must be user-visible before the tool call. It must start with the current speaking Pal prefix and either hand off to the selected owner Pal or explain the owner gap / why the current Pal remains owner for this case.

If the AI judges that the request involves local system/app state, permission or safety boundaries, runtime/environment readiness, command failure recovery, system-impact risk, or evidence from execution-layer system inspection, the task needs a system-owner judgement before execution. In the bundled v0.1 Pal pool, Rhea is the registered system Pal. Rhea may be selected only by case-specific AI judgement from the current request, context, registry, risk, and user constraints; this is not a keyword route or fixed task-domain map.

Read-only does not remove owner judgement. A safe diagnostic can still be specialist-owned.

## Composite Task Rule

For a composite task, the first Pal must name selected or provisional stage owner Pals before asking clarification questions, handing off, or letting Runtime execute.

The first Pal should identify:

- domain focus
- content deliverables
- final deliverables
- work stages
- selected or provisional stage owner Pals
- Runtime / Skill executor candidates
- verification needs

Runtime is only an execution layer candidate. It is not the Pal-layer owner of research, writing, development, document, quality, system, product, HTML, UI, code, or repository implementation stages.

## Invalid First Pal Responses

- seeing a task and immediately executing without task judgement
- calling a Runtime tool, Bash / shell command, MCP call, file write, project inspection, or system inspection before a visible Pal-prefixed owner judgement
- asking only clarification questions before naming stage owner Pals
- handing the whole task to a content-stage Pal while leaving the final artifact stage undefined
- letting Runtime directly own a complex later stage
- letting Runtime execute a system-risk or system-state diagnostic before a case-specific system owner Pal judgement
- saying a later Pal or Runtime will decide all stage owners
- using keyword routing or a task-domain route table
