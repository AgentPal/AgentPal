# Source Map And Derived Knowledge

AgentPal separates source maps from derived knowledge.

## Source Map

The source map records what AgentPal knows about the external project structure:

- tree summary
- important files
- user docs index
- external artifacts
- freshness notes

Default location:

`workspace/projects/<project-id>/source-map/`

## Derived Knowledge

Derived knowledge is structured understanding produced from user project materials:

- project summary
- user-provided docs summary
- business rules
- product constraints
- architecture notes

Default location:

`workspace/projects/<project-id>/derived-knowledge/`

Both are AgentPal central records. They do not replace current source files. When current accuracy matters, re-check the external project.

