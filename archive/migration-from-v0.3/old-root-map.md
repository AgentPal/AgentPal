# Old Root Map From v0.3

This map records the first governance pass from the v0.3 root layout toward the v0.4/v0.5 central organization layout.

| Old Area | New / Preferred Area | Status |
| --- | --- | --- |
| `pals/` | `official/pals/` | Official Pal Pack directories moved. `pals/README.md` remains as compatibility pointer. |
| `contacts/` | `workspace/organization/contacts/` | New central source of truth created. Legacy files remain for compatibility until later cleanup. |
| `registry/` | `workspace/organization/contacts/` plus future indexes | Legacy registry remains for compatibility. |
| `projects/project-workgroup-template/agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` | `archive/migration-from-v0.3/legacy-project-workgroup-template/agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` | Legacy thick workgroup prompt archived in R69. |
| `projects/project-workgroup-template/agentpal/PAL_GROUP.md` | `archive/migration-from-v0.3/legacy-project-workgroup-template/agentpal/PAL_GROUP.md` | Legacy thick workgroup file archived in R69. |
| official Pal runtime reports and state | `archive/migration-from-v0.3/official-pal-history/` | Historical reports, state, and private-adjacent memory moved out of `official/pals/` in R69. |
| root release files | `release/current/` pointers | Root release files remain; current pointers added. |
| external project `.agentpal/` thick state folders | central `workspace/projects/` records | Default project binding forbids thick state folders. |

This pass does not remove all historical references. Current install/runtime docs should use central roster and thin binding paths; old references in archive or regression cases are retained only with classification.
