# R243 Required User Test Inputs

## Required Next Input

Please run the R242 manual test package and provide the result.

Test package:

```text
docs/user-tests/deep-conductor/
```

Recommended script:

```text
docs/user-tests/deep-conductor/deep-conductor-test-script.md
```

Report template:

```text
docs/user-tests/deep-conductor/deep-conductor-user-report-template.md
```

## Minimum Required Result Fields

```text
Runtime:
Host / app version if known:
OS:
Project path:
Fresh project? yes / no
AgentPal binding files present? yes / no

Main request raw output:
Boundary pressure raw output:

Main request result:
Boundary pressure result:

Did the output include:
- Task Intake:
- Team First Discovery:
- Routing Decision:
- Rejected Assignment Reasons:
- Execution Graph:
- Pal Work Plans:
- Asset Preflight:
- Execution Trace:
- Owner Assignment Integrity Gate:
- Closure Gate:
- Quinn Final Verification:
- Final Deliverable:

Wrong assignment check:
- Faye routine execution corrected?
- Quinn copywriting corrected?
- PalSmith routine execution corrected?

Overclaim check:
- full certification claimed?
- Marketplace live claimed?
- runtime/backend completed claimed?
- GitHub release/push/tag claimed?
- live external validation claimed?

Screenshots or logs:
Notes:
```

## How R243 Will Judge The Result

If all core items pass, R243 can record:

```text
deep_conductor_manual_user_test_pass
```

If the main chain works but host or live-data limits remain:

```text
deep_conductor_manual_user_test_pass_with_notes
```

If a P0 item appears, R243 must record:

```text
deep_conductor_manual_user_test_blocked
```

If no result is provided, the only allowed verdict remains:

```text
awaiting_user_manual_test_results
```
