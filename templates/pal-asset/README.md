# Pal Asset Template Index

Date: 2026-06-28

This directory is reserved for reusable Pal Asset templates aligned with
`standards/pal-asset/`.

## Current Templates

- `pal-json-template.json`: v0.5 / v0.6-compatible `pal.json` starter with
  stable identity, human display name, role title, contact label, aliases, and
  no-code runtime boundaries.
- `asset-manifest-template.json`: optional Pal asset manifest starter.
- `index-templates/`: reusable index templates for knowledge, Skills,
  workflows, runbooks, memory, learning, evals, examples, and research.

## Template Boundary

Templates in this directory should produce Pal Pack assets inside the AgentPal
Workspace or approved central organization records. They must not create
external-project `.agentpal/pals/`, `.agentpal/skills/`, `.agentpal/workflows/`,
`.agentpal/runbooks/`, `.agentpal/memory/`, or copied central contacts by
default.

Templates may reference Org Pack recommendations as AI judgement inputs, but
they must not treat Org Pack recommendations as routes or roster edits.
