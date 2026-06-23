# Skill Card: addyosmani/agent-skills

## Name

Production-grade engineering skills for AI coding agents

## Source

GitHub: https://github.com/addyosmani/agent-skills

## License

MIT. GitHub API checked on 2026-06-22.

## Handling Status

rewrite-as-atlas-skill

## Main Purpose

Provides engineering workflow ideas for AI coding agents across specification, planning, implementation, verification, review, release, debugging, security, and Git workflow.

## Useful For Atlas

- Turning rough requirements into defined development tasks.
- Planning work before asking a Runtime to modify files.
- Requiring tests and evidence before accepting completion.
- Framing code review, security, release, and regression checks.

## Not Suitable For Direct Use

- Atlas must not inherit any behavior that runs commands, installs dependencies, edits files, commits code, or pushes changes.
- Atlas should not copy the upstream Skill text or scripts.
- Atlas should not become a single large engineering Skill bundle.

## Safety Boundary

Any build, test, commit, hook, script, shell, install, deploy, or cleanup action must be delegated to an explicit Runtime task with user approval where needed. Atlas only prepares the task, constraints, and evidence requirements.

## Third-Party Source Included

No. This card contains only source metadata and Atlas's own assessment.

## Pal Contacts

No. This is a Skill/resource candidate, not a standard Pal Pack.

## Recommended Trigger Scenarios

- User gives a large or vague software task.
- Atlas needs a development lifecycle checklist.
- Atlas needs to strengthen task definition, planning, verification, or review.

## How Atlas Uses It

Atlas uses it as a reference source for creating its own `workflows/development-lifecycle/` workflow. The workflow in this repository is an AgentPal/Atlas-native rewrite, not copied upstream content.

## Attribution

Original project: `addyosmani/agent-skills` by Addy Osmani and contributors. See the source repository and its MIT License for original terms.

