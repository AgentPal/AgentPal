# Skill Card: testdino-hq/playwright-skill

## Name

TestDino Playwright Skill

## Source

GitHub: https://github.com/testdino-hq/playwright-skill

## License

MIT. GitHub API checked on 2026-06-22.

## Handling Status

convert-to-runbook

## Main Purpose

Provides Playwright-oriented testing guidance and browser verification practices.

## Useful For Atlas

- Turning UI acceptance criteria into executable browser verification tasks.
- Asking Runtime or non-Pal runtime to return screenshots, steps, failures, and logs.
- Distinguishing "page loads" from "user workflow works".

## Not Suitable For Direct Use

- Atlas must not run Playwright, open browsers, handle login cookies, or inspect private sessions.
- Browser automation can expose sensitive data and should be scoped to local or approved test environments.
- The upstream Skill should not be copied into this repository.

## Safety Boundary

Browser verification must state target URL, environment, test account status, sensitive data restrictions, allowed actions, screenshots required, and evidence format. Real production actions need explicit user approval.

## Third-Party Source Included

No. This card contains only source metadata and Atlas's own assessment.

## Pal Contacts

No. This is a Skill/resource candidate, not a standard Pal Pack.

## Recommended Trigger Scenarios

- A feature has UI acceptance criteria.
- A frontend fix needs screenshot evidence.
- A regression requires browser-level confirmation.

## How Atlas Uses It

Atlas uses it as a reference for `runbooks/testing/browser-verification-with-playwright.md`, an AgentPal/Atlas-native browser verification runbook.

## Attribution

Original project: `testdino-hq/playwright-skill` by TestDino HQ and contributors. See the source repository and its MIT License for original terms.


