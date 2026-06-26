# Pal Knowledge Ingestion Skill

## Purpose

Turn approved material into durable Pal knowledge without losing substantive content.

## When To Use

Use when a Pal needs domain knowledge, user notes, research summaries, SOPs, examples, decision records, or reference material.

## Inputs

- source files or text approved by the user
- target Pal and role
- intended use of the material
- privacy/publication boundary

## Required Context

Read `pal-user-material-ingestion-knowledge.md`, `pal-content-preservation-principles.md`, `pal-skill-vs-knowledge-vs-workflow.md`, and material ingestion protocol/template.

## Process

1. Inventory sources with filenames, sections, dates, and scope.
2. Classify content into knowledge, skill, workflow, runbook, template, eval, example, reference, persona/voice, boundary, or decision.
3. Preserve source anchors and important examples.
4. Split long material into multiple knowledge files when needed.
5. Produce a knowledge file plan and unclassified review queue.
6. Ask confirmation before Runtime writes any target files.
7. After writing, verify that summaries do not replace full knowledge.

## Output

- Material Ingestion Plan
- Source Inventory
- Classification Table
- Knowledge Files Plan
- preservation checklist
- Runtime Task Package

## Quality Bar

Useful detail must survive the transformation. Navigation summaries can exist, but they do not replace complete knowledge.

## User Confirmation Points

- read scope
- private/public boundary
- target files
- handling of uncertain or sensitive material

## No-Code Boundary

Runtime reads and writes approved files. PalSmith plans, reviews, and reports.

## Common Mistakes

- compressing long material into a short card
- dropping examples, exceptions, and limits
- failing to preserve source location
- mixing private user memory into public Pal content

## Example

A 20-page customer support SOP should become several knowledge/runbook/template files with source sections, decision rules, escalation steps, examples, and excluded private details.
