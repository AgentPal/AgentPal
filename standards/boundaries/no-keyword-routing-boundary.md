# No Keyword Routing Boundary

AgentPal routing is AI judgement only.

Do not add or rely on:

- `keyword_map`
- `domain_map`
- `role_map`
- fixed natural-language dispatch tables
- direct rules such as "development means Atlas" or "testing means Quinn"

Capability notes are allowed only as non-binding judgement inputs. The current AI must decide the owner from the specific user goal, expected deliverable, risk, context, available Pal assets, and host runtime capability.

Explicit `/pal Name` and `@Name` mentions are direct Pal calls. They are resolved by contact aliases, not by semantic keywords.
