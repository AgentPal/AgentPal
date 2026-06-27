# Project Artifact Boundary Standard

AgentPal separates user project artifacts from AgentPal internal project records.

## User Project Artifacts

The external project may contain its own docs, design files, requirements, assets, data, source code, and business reports. AgentPal may read these when the task requires them and the runtime has access.

## AgentPal Central Records

AgentPal internal summaries, source maps, derived knowledge, task packages, reports, governance records, routing memory, and runtime memory belong under:

`workspace/projects/<project-id>/`

## Explicit User Request Exception

If the user explicitly asks AgentPal to create or edit a business document inside the external project, that document may be written to the external project. This exception does not make `.agentpal/` a memory store or Pal asset store.

