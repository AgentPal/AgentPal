# Write pal.json

## Status

Current for AgentPal `v0.1.0-rc.1`.

`pal.json` is the machine-readable metadata file for one Pal Pack.

## Minimal Shape

```json
{
  "schema": "agentpal.pal-pack.v0.1",
  "id": "example-role",
  "name": "Example",
  "display_name": "Example / Role Pal",
  "directory_name": "Example-role",
  "path": "official/pals/Example-role",
  "role": "role",
  "type": "pal-pack",
  "direct_call": "/pal Example",
  "aliases": ["Example", "example"],
  "version": "0.1.0",
  "license": "MIT",
  "collaboration": {
    "discoverable": true,
    "contactable": true,
    "allowed_modes": ["consult", "delegate", "handoff", "review"]
  }
}
```

## Required Meaning

- `id` should be stable and lowercase.
- `directory_name` should match the folder name.
- `type` must be `pal-pack`.
- `direct_call` should use the display name, such as `/pal Example`.
- aliases should not collide with existing registered Pals.

## Do Not Add

Do not add Skills, plugins, models, MCP servers, runtimes, or raw repositories as Pal entries in `pal.json`.
