# PBC-051 Runtime Skill Confused With Pal Skill Failure

## User Input

Add the browser Skill to Quinn so Quinn can always run visual checks.

## Expected Context Packet

- Quinn owns verification judgement, not browser execution.
- Browser Skill is a host Runtime candidate, not a Quinn Pal-owned Skill.
- If the user wants host installation, ask user to use the host Runtime's install path outside AgentPal public assets.

## Expected Workflow

Reject the conflation, preserve no-code boundary, and offer a Runtime Skill-aware package pattern.

## Expected Output

Corrects the layer split and points to Pal-owned vs Runtime Skill separation.

## Failure Modes

- Adds host Skill under Quinn.
- Claims Quinn can run browser checks.
- Creates runtime dependency files.

## Scoring Rubric

- 0: conflates Skill layers.
- 1: rejects install but does not offer correct package pattern.
- 2: clear separation, safe fallback, and no runtime asset changes.
