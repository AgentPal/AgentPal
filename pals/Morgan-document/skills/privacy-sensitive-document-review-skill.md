# Privacy Sensitive Document Review Skill

## Purpose

Identify privacy and sensitivity risks before document reading, transformation, sharing, export, or storage.

## When to use

Use for contracts, IDs, medical, financial, customer, employee, credentials, legal-ish, proprietary, confidential, or external-share documents.

## Inputs

Document type, source scope, requested action, recipient, storage location, output format, and user approvals.

## Required context

Privacy boundary, allowed disclosure level, retention rule, redaction needs, and evidence requirements.

## Process

1. Classify sensitivity and exposure path.
2. Apply minimization: use only the content needed for the task.
3. Identify redaction, anonymization, or withholding needs.
4. Ask for approval before sharing or storing sensitive material.
5. Record not-run items and residual risk.

## Output

Privacy-sensitive review with risk level, allowed content, withheld content, approval points, and safe task package.

## Quality bar

The plan must reduce unnecessary exposure and make user approvals explicit.

## User confirmation points

Confirm private file reads, external sharing, retention, redaction, publication, and sensitive handoff.

## No-code boundary

This skill does not inspect private files unless the Runtime has approval and evidence; it adds no privacy scanner.

## Common mistakes

Quoting sensitive details unnecessarily, assuming public-safe status, or storing raw private content in Pal assets.

## Example

Morgan asks to redact customer IDs before handing a support report to another Pal for writing polish.

