# PDF Export Task Package Runbook

## Trigger

A Runtime must export, review, or prepare a PDF artifact.

## Inputs

Source document, target PDF purpose, accessibility needs, reading-order needs, metadata, and output path.

## Steps

1. Identify PDF workflow type.
2. Define export, tags, reading order, links, images, tables, and metadata expectations.
3. Mark OCR, privacy, and publication risks.
4. Request page samples or structural evidence.
5. Record not-run checks.

## Decision points

Is OCR required? Is accessibility review required? Are redaction or publication involved?

## Outputs

PDF export or review Runtime Task Package.

## Quality checks

Do not accept a PDF path alone as complete evidence.

## Required user confirmation

Required for OCR of private scans, redaction, external sharing, or publication.

## Evidence to return

PDF path, page samples, reading-order notes, metadata, accessibility output if run, and failures.

