# Protected Block Standard

AgentPal host-runtime instruction blocks must use stable begin and end markers.

Required markers:

```md
<!-- BEGIN AGENTPAL WORKGROUP -->
<!-- END AGENTPAL WORKGROUP -->
```

Install and update operations may replace only the content inside those markers. They must preserve all user-authored content outside the protected block.

The block should point to `.agentpal/project.json` and `.agentpal/AGENTPAL.md` rather than copying the full AgentPal workspace rules.
