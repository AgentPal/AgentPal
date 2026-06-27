# AI Judgement Routing Standard

AgentPal owner selection is case-by-case AI judgement.

The current AI should consider:

- the user's specific goal
- expected deliverables
- active project context
- risks and safety boundaries
- relevant Pal assets
- available host runtime capabilities
- whether a direct `/pal Name` or `@Name` call was used

For clear single-owner work, Mira may hand off and stop. For composite work, the first Pal should identify staged owner candidates before execution.

The selected owner is never determined only by task keywords.
