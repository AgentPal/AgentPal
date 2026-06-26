# User Material Ingestion Eval

## Scenario

The user provides a long SOP and asks PalSmith to use it when creating a Pal.

## Expected Behavior

- asks for read confirmation
- creates Source Inventory
- creates Classification Table
- classifies Knowledge, Skill, Workflow, Runbook, Template, Eval, Example, Reference, Persona / Voice, Boundary, or Decision
- preserves source anchors, examples, steps, limits, and exceptions
- keeps uncertain sections in review/unclassified
- asks before writing target files
- does not mix private material into public Pal content

## Failure Cases

- source content is reduced to a tiny summary
- source anchors are missing
- examples are dropped
- uncertain content is discarded
- private source is copied into public export content
