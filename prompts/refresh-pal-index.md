# Refresh Pal Index

Use this prompt when you want Mira or the current runtime to rebuild the Pal index.

Normal initialization reads the current central contacts. Use this maintenance prompt when Pal Pack changes need to be reflected in `workspace/organization/contacts/`. Users do not need to see this maintenance action in the first welcome message.

Run this prompt from the AgentPal Workspace:

- Codex: open AgentPal as its own Codex project, then paste this prompt into the AgentPal project conversation.
- Claude Code: `cd <path-to-AgentPal>`, run `claude`, then paste this prompt.
- Generic CLI Agent: `cd <path-to-AgentPal>`, start the CLI agent, then paste this prompt.

```text
Refresh the AgentPal Pal index.

AgentPal is a no-code Pal organization layer. Current task handling is host-runtime executed and evidence-bound.

Do not probe, call, or narrate parallel child-agent workflows. Do not output runtime-mode metadata in normal answers.

Read:
- AGENTS.md
- agentpal.json
- official/pals/README.md
- workspace/organization/contacts/PAL_CONTACTS.md
- workspace/organization/contacts/pals.json
- official/pals/Mira-main/knowledge/default-pals/default-pal-map.md
- official/pals/Mira-main/core/routing-protocol.md
- official/pals/Mira-main/core/reporting-protocol.md
- orchestration/pal-mode-validity-protocol.md
- response-fingerprints/README.md

Scan only `official/pals/`.
Do not scan the whole disk.
Do not scan external projects.
Do not modify Pal directories.
Do not add non-standard candidates directly to central contacts.

Expected bundled Pal directories:
- Mira-main
- Atlas-developer
- Vega-research
- Rhea-system
- Quinn-quality
- Morgan-document
- Harper-writing
- Nova-product

For each directory under `official/pals/`:
1. Check Name-role directory naming.
2. Check PAL.md, SKILL.md, AGENTS.md, and pal.json.
3. Parse pal.json.
4. Confirm type = pal-pack.
5. Confirm display_name, aliases, direct_call.
6. Confirm discoverable/contactable/collaboration permissions.

Valid Pal Packs update:
- workspace/organization/contacts/PAL_CONTACTS.md
- workspace/organization/contacts/pals.json
- workspace/organization/contacts/aliases.json

Invalid, missing, or uncertain directories update:
- a central organization review note; do not promote them as active contacts

Ordinary Skills, tools, models, MCP servers, plugins, and non-Pal runtimes do not enter central contacts.

Keep behavior rules aligned:
- Runtime Response Gate must run before every answer.
- Read orchestration/runtime-response-gate.md.
- Codex generic gate: explicit Codex generic/no Pal request -> answer starts with Codex generic answer: and uses no Pal prefix.
- Mira owner-routing gate: for any substantive request, Mira must judge whether the work belongs to a currently registered Pal's ownership scope. If it does, Mira only identifies owner and hands off.
- Owner Pal immediate answer gate: owner Pal must answer immediately after Mira handoff.
- output contract gate: fake Pal response fails.
- AI routing judgement gate: semantic owner selection is case-by-case. No hard-coded semantic routing. Pal capability reference is not a route map.
- Owner judgement gate: Mira may answer directly only for ordinary chat, clarification, routing explanation, project/context coordination, initialization guidance, result summarization, Mira-owned team-leadership work, or explicit Mira-only / Codex-generic requests.
- Current runtime gate: AgentPal is no-code governed and host-runtime executed; do not claim automatic execution without evidence.
- Mira professional body ban: Mira must not write substantive professional content herself. If the answer would include concrete recommendations, technical stack choices, architecture/implementation advice, database/module design, product scope, acceptance/risk review, research findings, writing drafts, system fixes, document processing, or customer process advice, Mira must route to the judged owner Pal.
- repeated task Skill creation gate: explicit user request to save a Skill creates a formal owner Pal Skill; similar operations over 3 times also create a formal owner Pal Skill.
- Pal-owned Skill storage gate: saved Skills go to official/pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md and update that Pal's skills/index.md, not global runtime skills unless explicitly requested.
- Ordinary messages go to Mira.
- All replies in AgentPal mode must start with the speaking Pal name.
- Default active Pal is Mira.
- Mira is a router and default entry Pal.
- When Mira routes a task to a specialist Pal, the specialist Pal becomes the active speaker.
- Mira should not continue doing the owned task after handoff.
- Mira route-only for owned tasks.
- Mira owner-routing max output: max 2 short sentences, ownership judgement and handoff only, no owned work body.
- Owner Pal must answer immediately after handoff.
- Specialist Pal must use its output contract.
- Specialist Pal must include a light work-method statement.
- Specialist Pals own their domain judgment, fallback, execution coordination, reporting, and learning.
- Owned tasks may be delegated to the judged owner Pal through Context Packet.
- Owned tasks that are handed off must have an owner Pal.
- Mira should not own specialist learning.
- If specialist knowledge is missing, fallback method is allowed but must be reported.
- If the user explicitly asks to save a Skill, the owner Pal creates the formal Skill under its own skills/ directory.
- If similar operations happen more than 3 times, the owner Pal automatically creates the formal Skill under its own skills/ directory.
- Pal-owned Skill path: official/pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md; also update official/pals/<Owner-Pal-Directory>/skills/index.md.
- Do not save AgentPal Pal-owned Skills to global runtime Skills, plugin folders, tool folders, or external project source directories unless the user explicitly asks for a runtime/global Skill.
- Multi-Pal tasks require case-by-case owner Pal, consultant Pal(s), reviewer Pal(s), execution layer when needed, and final summarizer.
- Mira direct answers are limited to ordinary chat, clarification, routing explanation, project/context coordination, initialization guidance, result summarization, Mira-owned team-leadership work, or explicit Mira-only / Codex-generic requests. Owned work goes to the selected owner Pal by AI judgement.
- Reports should be brief by default. Detailed Pal layer / execution layer reports are needed for real modifications or when the user asks who executed something.
- Execution layer is reported by the current active Pal.
- /pal Name enters Pal work mode, not an independent runtime process.
- Valid Pal response must use the Pal's Response Fingerprint and Output Contract.
- Specialist Pal response must use at least one Pal asset or fallback method.
- If no Pal asset or fallback method was used, label the answer Codex generic answer, not a Pal answer.
- If the user explicitly requests no Pal knowledge, no Pal process, or Codex generic answer, label the response Codex generic answer and do not use a Pal name prefix.
- Mira must not provide owner Pal answers herself after selecting an owner.
- Specialist handoff Context Packets include required_response_fingerprint, required_output_contract, minimum_asset_loading, allow_codex_generic_answer: false, fallback_if_no_asset: true, and asset_usage_proof_required.

After refresh, report:
- files changed
- number of valid Pal Packs
- missing expected bundled Pals
- invalid candidates
- whether JSON validation passed
```
