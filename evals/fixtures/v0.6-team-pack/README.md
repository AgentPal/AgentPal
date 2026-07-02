# v0.6 Team Pack Fixtures

Status: local fixture package for fixture-based validation.

These fixtures exist only to make previously blocked v0.6 Team Pack validation
scenarios runnable without network access or private user input.

They are not production data, customer data, live web evidence, or runtime
validation proof.

## Fixtures

- `after-sales-feedback-20.synthetic.json`
  - Synthetic local batch of 20 after-sales feedback records.
  - Used by the existing after-sales team handling scenario.
- `workbuddy-expert-group.synthetic.json`
  - Synthetic local fixture for a WorkBuddy-like expert group.
  - Used by the Research Team WorkBuddy comparison scenario.

## Validation Boundary

Fixture-based validation can prove that Mira, the selected Team Pack, Workflow
Execution Contract, verifier handling, and Closure Gate can process bounded
local inputs.

Fixture-based validation cannot prove:

- real customer-system handling;
- live external source collection;
- current WorkBuddy facts;
- host-runtime automation;
- web research or source freshness.

Live external validation remains separate and should be marked
`needs-runtime-validation` or `needs-user-provided-source` until real evidence is
captured.
