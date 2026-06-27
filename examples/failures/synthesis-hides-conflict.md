# Failure Example: Synthesis Hides Conflict

## Wrong Scenario

Nova says the feature is promising. Quinn says readiness is blocked because no acceptance criteria exist. Mira summarizes:

```text
The team generally agrees this is worth doing.
```

## Why It Is Wrong

Synthesis must preserve disagreement and minority opinions. A positive product signal does not erase a blocked quality or evidence result.

## Correct Behavior

The synthesis should keep conflict visible:

```yaml
agreement:
  - "More definition is needed."
disagreement:
  - "Nova sees potential product value; Quinn blocks readiness."
conflicts:
  - "Product interest conflicts with missing acceptance criteria."
recommended_next_step: "Define acceptance criteria before build or release."
```

## Corresponding Eval

- `evals/orchestration/parallel-review-synthesis-self-test.md`
