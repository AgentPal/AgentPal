# Cross-Pal Collaboration Example

This is a non-binding example. It demonstrates one possible collaboration shape, not a fixed route.

这是非绑定示例，只展示一种可能协作形态，不是固定路由。

## Contact Source Rule

The target collaborator is resolved from the current AgentPal contacts / registry by the current AI / Mira / Brain. This example does not require, recommend, or preserve any fixed Pal identity.

## Scenario

The current Pal has completed its domain-specific preparation and needs a bounded collaborator perspective before the user-facing result is finalized.

## Current Owner Pal

development-pal

## Target Pal

resolved-reviewer-pal

## Collaboration Mode

consult or handoff, decided case-by-case

## Context Packet

from_pal: development-pal
to_pal: resolved-reviewer-pal
mode: consult_or_handoff
owner_after_handoff: decided_case_by_case
user_goal: Move the current task to a suitable collaborator without losing boundaries or evidence requirements.
current_state: The current Pal has completed its domain-specific preparation and is ready to share a minimized packet.
constraints:
- Do not share secrets, credentials, private memory, or unrelated user data.
- Do not treat non-Pal runtimes, tools, models, MCP servers, plugins, or Skills as Pal contacts.
- Resolve the target from current contacts / registry before dispatch.
relevant_files:
- Only files or summaries explicitly needed by the selected collaborator.
needed_output: Quality gate result, missing evidence list, risk level, and regression recommendation.
privacy_policy: share_minimum_required_context
verification_requirements:
- Selected collaborator states assumptions and evidence gaps.
- Selected collaborator returns result, risks, and next owner.

## Privacy Trimming

Share only the facts, summaries, file paths, and decisions needed for the selected collaborator's role.

## Do Not Share

- Passwords, tokens, API keys, payment data, identity documents, or private user memory.
- Full copyrighted documents or third-party source code.
- Runtime secrets, local machine identifiers, or unrelated file contents.

## Receiving The Result

The current owner reviews whether the selected collaborator output answers the request, preserves constraints, and includes enough evidence for the next step.

## Collaboration Memory

If this handoff pattern is repeated and user-approved, record only the abstract workflow in memory/skill-memory/ or collaboration memory. Do not store sensitive packet contents.
