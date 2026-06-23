# Init Prompt Dry Run

## Purpose

Verify that `INIT_PROMPT.md` can initialize AgentPal from public repository files only.

## Preconditions

- AgentPal workspace is open in Codex.
- No private maintainer directory is available.
- No Python, Node.js, Rust, Go, installer, scanner, validator, or UI is required.

## Manual Steps

1. Read `INIT_PROMPT.md`.
2. Follow the listed read order.
3. Confirm only `pals/` is scanned for Pal Pack directories.
4. Confirm Mira plus Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova are expected.
5. Confirm ordinary messages go to Mira.
6. Confirm specialist Pals do not listen by default.
7. Confirm `/pal Name` is documented.
8. Confirm project means external user project by default.

## Expected Result

Codex can enter Mira Main Pal mode and recognize the official Pal set without external files or runtime dependencies.

## Failure Signs

- The prompt references private maintainer paths.
- The prompt asks to scan the whole disk.
- The prompt requires Go, scripts, or installers.
- The prompt invents missing Pals.

## Notes

No bundled runtime tool checks are required during initialization.

