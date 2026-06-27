# Workspace Resources

This directory is the central workspace home for shared resource references.

Use it for public-safe resource indexes, compatibility pointers, and future central resource records. Do not store private project files, internal development reports, credentials, runtime logs, or full external repositories here.

R76 moved the legacy root `registry/` directory to `workspace/resources/registry/`. That registry is a compatibility/resource reference only; central Pal contacts remain under `workspace/organization/contacts/`.

Legacy root `models/`, `runtime/`, `plugins/`, and `capabilities/` directories were archived in R79 after serving as temporary compatibility pointers. Active capability inventory assets now split across standards in `standards/capability-inventory/`, current organization records in `workspace/organization/capability-inventory/`, examples in `examples/capability-inventory/`, and copyable templates in `templates/capability-inventory/`.
