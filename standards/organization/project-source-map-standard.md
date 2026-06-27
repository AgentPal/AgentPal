# Project Source Map Standard

A project source map is AgentPal's index of an external user project. It is not a directory that must be copied into the user project.

## Location

Default location:

`workspace/projects/<project-id>/source-map/`

## Purpose

The source map records what AgentPal knows about the user project structure:

- High-level tree summary.
- Important files and directories.
- User docs index.
- External artifacts and links.
- Read scope notes and freshness notes.

## Boundary

The source map is evidence for context slicing. It does not authorize broad reads by itself, and it must distinguish index-known paths from content-read paths when used in a task report.

