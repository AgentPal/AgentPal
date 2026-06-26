# environment-troubleshooting-knowledge

## Concept Explanation

Environment troubleshooting converts errors into safe diagnosis steps before repair. It separates symptom, likely cause, read-only checks, repair gates, and evidence.

## Judgement Standards

- Start with goal and observed error.
- Prefer read-only checks.
- Verify working directory and tool version.
- Avoid installs or path edits until evidence supports them.
- Require rerun evidence after repair.

## Examples

- Missing command: check availability, PATH, project manager hints, and installation status.
- Version mismatch: check project config and actual version.

## Counterexamples

- Reinstalling first.
- Running random commands from internet snippets.

## Scope

Use for local development, runtime setup, command failures, package manager problems, and tool availability.

## How This Becomes Skill, Workflow, Or Eval

Skill: environment-troubleshooting. Workflow: environment-troubleshooting. Runbook: runtime-capability-check.

## Common Mistakes

Skipping exact error text, confusing shell state with project config, and not retesting.

## Source Refs Or Local Notes

Based on Rhea local environment assets plus SRC-02 and SRC-09.

