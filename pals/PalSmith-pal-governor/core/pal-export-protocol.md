# Pal Export Protocol

PalSmith prepares export task packages. It does not package files itself.

## Clean Pal Export Task Package

Clean exports are for public sharing. The task package must include public-safe source paths, required manifest/report outputs, and private-data exclusions.

Exclude `memory/user/`, `memory/project/`, `state/`, `reports/`, credentials, tokens, logs, cache, temporary files, and executable scripts.

## With Memory Export Task Package

With-memory exports may include private runtime data and require strong confirmation. The task package must request a privacy report and restore instructions.

## Runtime Evidence

The current Agent Runtime must report included files, excluded files, generated manifest/report paths, and any not-run checks.
