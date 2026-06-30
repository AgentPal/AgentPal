# Existing Pal Composite Upgrade Plan Template

Use this template when PalSmith judges that an existing Pal change may affect
Pal-defining behavior. The judgement must be semantic and evidence-based, not a
keyword route.

## upgrade_mode_judgement

- request classification:
- judgement reason:
- not keyword routing statement:
- uncertainty:
- simple edit excluded: yes / no / unclear
- authorization flow involved: yes / no / unclear

## target_pal

- display name:
- id:
- path:
- status: official / user custom / draft / unknown
- current direct call:
- current owner boundary:

## current_pal_inventory

- files inspected:
- identity assets:
- voice/personality assets:
- thinking/knowledge assets:
- workflows:
- skills / capability maps:
- runtime / Agent usage policy:
- memory / learning assets:
- collaboration / discovery assets:
- evals:
- missing or stale assets:

## user_request

- raw request:
- interpreted intent:
- requested sources:
- requested target behavior:
- requested publication or discovery change:
- assumptions:

## source_type

- public figure:
- literary / character style:
- expert practice:
- brand style:
- book / public source:
- user private material:
- organization material:
- other:

## source_boundary

- non-representation boundary:
- no copied source text boundary:
- public-source-inspired / style-inspired wording:
- private material boundary:
- copyright / rights-holder notes:
- confidence and uncertainty:

## distillation_dimensions

### cognitive_model

- mental models:
- decision heuristics:
- value floor:
- anti-patterns:
- judgement boundaries:
- uncertainty notes:

### voice_style

- speech rhythm:
- sentence length:
- common transitions:
- common address forms:
- forbidden expressions:
- scenario tone shifts:

### personality

- personality base:
- emotional expression:
- caution level:
- risk preference:
- behavior boundaries:

### role_duties

- affected responsibilities:
- non-responsibilities:
- deliverables:
- acceptance criteria:

### domain_knowledge

- knowledge to add:
- source scope:
- confidence:
- update needs:

### workflow

- affected workflows:
- new workflows:
- workflow evals:

### skill_agent_usage

- Pal-owned Skill changes:
- host Skill / plugin candidates:
- Agent Runtime candidates:
- evidence required before capability claims:

### memory

- memory templates:
- privacy boundary:
- writeback confirmation:

### collaboration

- consult / delegate / handoff impact:
- allowed shared information:
- blocked shared information:
- discovery impact:

### marketplace

- metadata impact:
- public listing allowed: yes / no / requires review
- source disclosure:

## target_file_map

| Purpose | Target file | Action | Required evidence |
| --- | --- | --- | --- |
| identity summary |  | add / update / no change |  |
| voice rules |  | add / update / no change |  |
| thinking model |  | add / update / no change |  |
| knowledge |  | add / update / no change |  |
| workflow |  | add / update / no change |  |
| skill / Agent usage |  | add / update / no change |  |
| memory |  | add / update / no change |  |
| collaboration |  | add / update / no change |  |
| eval |  | add / update / no change |  |
| report |  | add / update / no change |  |

## write_order

1. source boundary
2. identity / role impact
3. voice / personality assets
4. thinking / knowledge assets
5. workflow and skill / Agent maps
6. memory and collaboration boundaries
7. evals
8. README / PAL summary only after supporting assets exist
9. report

## eval_plan

- semantic classification test:
- voice consistency test:
- cognitive consistency test:
- role task test:
- workflow test:
- Skill / Agent claim boundary test:
- memory privacy test:
- collaboration / discovery / contacts boundary test:
- Marketplace claim test:

## risk_boundary

- no direct core identity rewrite before plan:
- no character impersonation:
- no copied lines:
- no real-person replication:
- no unauthorized private material:
- no automatic contacts or registry write:
- no Marketplace publication:
- no runtime/backend implementation:

## confirmation_questions

Ask no more than three focused questions before writing. Required confirmation:

```text
Please confirm whether PalSmith may prepare a Runtime Task Package for the
listed allowed write paths. I will not write files, change contacts, enable
discovery, or publish Marketplace metadata until you approve the exact scope.
```

## allowed_write_paths

- 

## blocked_write_paths

- `workspace/organization/contacts/` unless separately authorized
- `official/pals/` for new official Pal creation unless separately authorized
- user private materials into public assets
- Marketplace public listing files unless separately reviewed
- runtime code, CLI, scanner, daemon, connector, backend service
