# claim-evidence-alignment

## Purpose

Check whether each claim is supported by the cited evidence and whether its wording overstates what the source proves.

## When to use

Use before final reports, recommendations, knowledge cards, or Pal handoffs.

## Inputs

Draft claims, source inventory, evidence matrix, confidence notes, and user decision criteria.

## Required context

Claim-evidence knowledge, research synthesis knowledge, and copyright boundary.

## Process

1. Label each sentence as fact, inference, recommendation, uncertainty, or user decision.
2. Link each factual claim to source IDs.
3. Check whether the cited source directly supports the wording.
4. Downgrade or qualify claims that rely on weak, old, indirect, or biased sources.
5. Separate recommendation from evidence.
6. Mark unverified claims as open questions.

## Output

Alignment review with approved claims, revised claims, unsupported claims, and confidence changes.

## Quality bar

No major factual claim should survive without traceable evidence or an explicit "not verified" label.

## User confirmation points

Ask when the user wants a stronger recommendation than the evidence supports.

## No-code boundary

This skill reviews text and evidence. It does not run automated fact checking tools inside AgentPal.

## Common mistakes

- Citing a source for a claim it does not make.
- Turning correlation into causation.
- Removing uncertainty to sound decisive.
- Reusing citations from memory without live verification.

## Example

Change "Framework B is secure" to "Framework B documents a security model and recent advisories were not found in the checked sources; this is not a security audit."

