# Example: Snapshot And Rollback

This is an example only. It does not create or restore real snapshots.

## User Says

`/pal PalSmith 修改前先做快照`

## PalSmith Questions

- Which paths should be snapshotted?
- Should this be a private backup or clean snapshot?
- Where should the snapshot be written?
- If rollback is later needed, what restore target should be used?

## Plan

- Create snapshot before controlled writes.
- Generate snapshot manifest with source paths, destination, timestamp, and restore notes.
- For rollback, create a pre-rollback backup before restore.

## Runtime Task Package

- `task_name`: snapshot task package, optionally rollback task package
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `allowed_read_paths`: approved target paths and approved snapshot
- `allowed_write_paths`: approved snapshot or restore paths
- `forbidden_write_paths`: unrelated Pals, unconfirmed overwrite targets
- `required_exclusions`: forced overwrite without confirmation
- `user_confirmation_required`: yes

## Handoff To Runtime

The current Agent Runtime creates the snapshot and manifest. Rollback runs only after explicit overwrite confirmation.

## PalSmith Acceptance

Accept only if snapshot evidence, manifest, restore instructions, and pre-rollback backup evidence are present.
