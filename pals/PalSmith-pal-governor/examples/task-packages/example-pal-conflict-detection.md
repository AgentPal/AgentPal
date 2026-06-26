# Example Pal Conflict Detection

User goal: "这几个 Pal 职责是不是重复？"

PalSmith prepares a read-only conflict detection task package.

| Conflict type | Pals | Severity | Evidence | Recommendation |
| --- | --- | --- | --- | --- |
| alias overlap | Growth Pal / Marketing Pal | P1 | both claim `/pal Growth` | rename one alias |
| responsibility overlap | Content Pal / Social Pal | P2 | both own social calendar | clarify boundary |
| owner missing | Launch Team | P1 | no verifier in `team.json` | assign verifier |

No files are changed. Contacts and registry edits require separate confirmation.
