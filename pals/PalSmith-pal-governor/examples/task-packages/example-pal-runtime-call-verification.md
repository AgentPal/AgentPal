# Example Pal Runtime Call Verification

Direct call: `/pal TestXiaohongshu`

## Result

verification level reached: Level 2 Runtime Simulation

| Evidence | Path |
| --- | --- |
| contacts entry | `contacts/pals.json` |
| registry entry | `registry/pal.index.json` |
| Pal identity | `pals/_test/test-xiaohongshu-operator-pal/PAL.md` |

Level 3 Native Runtime Call: not-run.

Reason: current Codex session did not expose an independent AgentPal `/pal` runtime API.

Release blocker: no for Pal Pack structure; yes only if the release claims native runtime call support.
