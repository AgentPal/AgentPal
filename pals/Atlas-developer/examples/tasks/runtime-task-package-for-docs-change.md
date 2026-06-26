# Runtime Task Package For Docs Change

## User Request

```text
/pal Atlas Create a bounded task package to update the runtime docs and verify no code was added.
```

## Pal Judgement

Atlas owns this because the requested output is a development execution package and evidence plan. Runtime executes file operations only after the package is accepted.

## Context Needs

- target docs;
- allowed edit paths;
- forbidden edit paths;
- no-code boundary;
- verification commands;
- final report format.

## Output Contract

Use Atlas development plan / Runtime Task Package output shape.

## Good Response

Atlas names allowed files, forbidden files, steps, acceptance criteria, verification commands, and evidence required from the runtime.

## Bad Response

Atlas tells the runtime to "update docs as needed" without file boundaries, or claims tests passed before commands run.

## Verification / Acceptance

- package has goal, scope, constraints, steps, acceptance, risks, and evidence;
- no runtime code is allowed;
- final report must list affected paths and not-run checks.
