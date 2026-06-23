# Official Pals Index Consistency Check

## Purpose

Verify that contacts, registry, mention aliases, and Mira's default Pal map agree.

## Preconditions

- AgentPal repository files are present.
- No external Pal directories are needed.

## Manual Steps

1. Compare `contacts/pals.json` with `registry/pal.index.json`.
2. Confirm both contain Mira plus seven official specialist Pals.
3. Confirm each id, display name, directory name, path, and direct call match.
4. Confirm each path exists under `pals/`.
5. Confirm `contacts/mention-aliases.md` lists `/pal Name` calls.
6. Confirm `pals/Mira-main/knowledge/default-pals/default-pal-map.md` matches the same Pal set.

## Expected Result

All Pal records are consistent and point to existing Pal Pack directories.

## Failure Signs

- A Pal appears in contacts but not registry.
- A path is missing.
- Tools, models, plugins, MCP servers, or non-Pal runtimes appear as Pal contacts.
- A direct call uses a directory name instead of display name.

## Notes

Display-name calls such as `/pal Atlas` are preferred. Directory-name calls such as `/pal Atlas-developer` are not the user-facing protocol.


