# Failure: Runtime Skill Treated As Pal-owned Skill

## Wrong Behavior

Morgan records an office-document Runtime Skill under `pals/Morgan-document/skills/` and then claims Morgan can convert `.docx` files.

## Why It Is Wrong

Runtime Skills belong to the host Runtime. Pal-owned Skills are no-code Pal methods. Mixing them makes AgentPal look like an execution layer and creates false capability claims.

## Correct Behavior

Morgan may use a Pal-owned document planning method and name an office-document Runtime Skill as a candidate in a Runtime Skill-aware Task Package. The host Runtime must confirm availability and execute it.

## Corresponding Eval

`evals/orchestration/pal-owned-skill-vs-runtime-skill-self-test.md`
