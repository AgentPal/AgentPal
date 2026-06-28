# Context Access List For Delivery Pack

Date: 2026-06-29
Status: local v0.5 no-code protocol

## Purpose

A Context Access List controls what each Pal, Runtime, Skill reference, or
reviewer may read and receive during a Faye Delivery Pack task.

It protects privacy, limits context drift, and prevents a first participant's
work from biasing independent reviews.

## Required Fields

Every Delivery Pack CAL entry must include:

- `participant_id`
- `participant_type`
- `task_stage`
- `can_read_paths`
- `cannot_read`
- `can_receive_outputs_from`
- `private_data_boundary`
- `content_read_budget`
- `output_contract`
- `verification_required`

## Field Rules

### `can_read_paths`

List only specific files, directories, summaries, or placeholders required for
the stage. Directory access must be narrow and justified.

### `cannot_read`

Must include forbidden or irrelevant context such as:

- real customer private data unless explicitly approved;
- unrelated Pal memory;
- unrelated project records;
- full AgentPal workspace by default;
- external project `.agentpal/` thick asset directories;
- credentials, tokens, cookies, passwords, API keys, private keys, and secrets;
- other independent reviewer drafts before synthesis.

### `can_receive_outputs_from`

List which earlier outputs may be read. Parallel independent review entries
should usually receive only the user brief and approved context, not other
reviewer drafts.

### `private_data_boundary`

State whether the stage may use:

- public reusable assets only;
- de-identified placeholders;
- approved private project records;
- no customer-private evidence.

### `content_read_budget`

State the intended read budget as either a count, a small named set, or a reason
for expansion. Index-known paths are not content reads until opened.

### `output_contract`

State the expected output shape and forbidden claims.

### `verification_required`

State what evidence must prove the output and which items may remain `not-run`,
`missing`, `blocked`, or `requires-human-review`.

## Runtime / Skill References

Runtime and Skill references are candidates only. A CAL may name a candidate
Runtime or Skill, but it must not automatically call it or treat availability as
confirmed without current evidence.

## Completion Bar

A Delivery Pack CAL is acceptable when it:

- lists allowed and forbidden context per participant;
- protects customer-private data;
- preserves independent review isolation;
- includes read budgets;
- defines output contracts;
- states verification requirements;
- keeps candidate Pals and Skills as AI judgement inputs.
