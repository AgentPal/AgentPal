# Pal Versioning Protocol

PalSmith manages versioning as plans, manifests, snapshots, and rollback task packages.

## Versioning Evidence

- proposed change summary
- affected paths
- backup or snapshot plan
- manifest fields
- rollback impact
- required user confirmations
- runtime evidence after execution

Existing targets should be snapshotted before overwrite, registry write, contacts write, or rollback.
