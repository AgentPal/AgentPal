# Compatibility Notes

The v0.4/v0.5 foundation pass keeps compatibility conservative.

- Official Pal Pack directories moved to `official/pals/`.
- `pals/README.md` remains so older readers can discover the new path.
- Legacy `contacts/` and `registry/` directories remain as compatibility pointers or historical records; the active roster is `workspace/organization/contacts/`.
- Root release files remain in place while `release/current/` provides current pointers.
- External project bindings should use new thin templates, but older bound projects can be upgraded in place.
- `projects/project-workgroup-template/agentpal/` is now a compatibility pointer. Its old thick prompt files moved to `archive/migration-from-v0.3/legacy-project-workgroup-template/`.
- Historical official Pal reports/state moved to `archive/migration-from-v0.3/official-pal-history/` so public Pal assets remain clean in fresh clones.

R69 classifies remaining old references instead of treating every archived example as active runtime guidance.
