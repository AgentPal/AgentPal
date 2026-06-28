# Pal Asset Template Index

Date: 2026-06-28

This directory is reserved for reusable Pal Asset templates aligned with
`standards/pal-asset/`.

## Current Template Status

R98-A adds only the template index. It does not generate or upgrade specific
Pals and does not modify PalSmith.

Future template files may include:

- minimal Pal Pack root entry template
- Pal Skill package template
- Pal asset manifest template
- directory index template
- Pal asset health report template

## Template Boundary

Templates in this directory should produce Pal Pack assets inside the AgentPal
Workspace or approved central organization records. They must not create
external-project `.agentpal/pals/`, `.agentpal/skills/`, `.agentpal/workflows/`,
`.agentpal/runbooks/`, `.agentpal/memory/`, or copied central contacts by
default.

Templates may reference Org Pack recommendations as AI judgement inputs, but
they must not treat Org Pack recommendations as routes or roster edits.
