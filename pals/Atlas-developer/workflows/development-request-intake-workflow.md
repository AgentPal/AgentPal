# Development Request Intake Workflow

## Trigger

A user, Mira, or another Pal asks for a feature, bug fix, refactor, technical task, code review, release check, or implementation-shaped deliverable.

## Inputs

- User goal.
- Current project or repository path.
- Known files or modules.
- Acceptance criteria.
- Constraints, forbidden actions, and risk notes.
- Contacts / registry when collaboration may matter.

## Steps

1. Classify the request type.
2. Check whether goal, file scope, constraints, and acceptance criteria are complete.
3. Identify whether Atlas owns the development planning stage.
4. Identify candidate collaborators by case-specific AI judgement.
5. Ask focused clarification only when needed.
6. Decide whether to proceed to implementation planning, handoff, consultation, or approval stop.

## Decision points

- Is this actually a development task?
- Does product scope need Nova?
- Does Pal asset work need PalSmith?
- Does environment risk need Rhea?
- Does quality gate need Quinn?
- Is user approval needed before runtime action?

## Outputs

Development intake judgement, missing-input list, owner/collaboration decision, and next action.

## Quality checks

- No keyword routing.
- No runtime-only ownership.
- No broad file reading before scope is clear.
- Risk gates are visible.

## Required user confirmation

Required for destructive edits, dependency installs, publishing, deployment, credentials, system changes, broad refactors, registry/contact edits, or private data use.

## Evidence to return

Return classification, scope state, owner judgement, required inputs, and any not-run inspection.
