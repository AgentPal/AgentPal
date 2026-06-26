# Content Preservation Eval

## Scenario

PalSmith receives a long user source and produces Pal knowledge files.

## Expected Behavior

- output includes source inventory
- summaries are navigation, not replacements
- long material is split into multiple files when useful
- examples, exceptions, boundaries, and steps are preserved
- unread sections are marked `not-run`
- uncertain classification is retained for review

## Failure Cases

- over-compression removes useful details
- target files lack source location
- output tells the user to rely on the original source instead of preserving key content
- no content preservation checklist
