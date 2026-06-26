# Pal Capability Map Protocol

Status: PalSmith v0.2 no-code protocol.

A Pal capability map helps users and Mira see what Pals exist, what they can do, and where capability gaps remain.

## Inputs

- selected Pal paths or full current contacts / registry
- optional team path
- whether output is for user explanation, team design, or release review

## Map Columns

| Pal | Role | Skills | Knowledge | Workflows | Runtime Task Packages | Can consult | Can delegate | Can handoff | Owner / verifier / consultant | Release safety | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Use Cases

- user asks what Pals can help with a goal
- PalSmith designs a team from a user goal
- Mira needs a readable capability summary
- release review checks coverage and gaps

## Output

- Markdown capability table
- capability gaps
- duplicate or overlapping coverage
- suggested team-local vs global-contact boundaries

## Boundary

No UI, dashboard, automatic metric collector, or runtime scanner is introduced.
