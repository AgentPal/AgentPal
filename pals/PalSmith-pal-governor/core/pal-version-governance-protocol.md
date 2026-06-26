# Pal Version Governance Protocol

Status: PalSmith v0.2 no-code protocol.

Version governance helps move a Pal through draft, testing, stable, deprecated, and archived states without unsafe automatic edits.

## Version States

- draft
- testing
- stable
- deprecated
- archived

## Change Proposal

Important changes should produce:

- change purpose
- affected files
- risk level
- breaking change: yes/no
- eval required: yes/no
- snapshot required: yes/no
- rollback plan required: yes/no
- user confirmation questions

## Upgrade Rule

PalSmith does not automatically change version numbers or status. It proposes a version update and waits for user confirmation.

## Rollback Rule

Rollback requires explicit overwrite confirmation and a current-state backup or snapshot reference.
