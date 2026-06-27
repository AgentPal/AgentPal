# Central Project Record

A central project record is AgentPal's workspace-side record for one external user project.

Default location:

`workspace/projects/<project-id>/`

The external project remains clean. It keeps only the thin binding entrypoints needed by the host runtime. AgentPal project-level assets stay in the central record:

- binding record
- source map
- derived knowledge
- project memory
- task ledger
- decisions
- routing memory
- runtime memory
- task packages
- context packets
- verification records
- reports
- governance records
- capability inventory

Real project records are workspace-private by default and should not be committed to the public AgentPal repository.

