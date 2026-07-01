# PalSmith Task Package Templates

These templates are no-code Runtime Task Packages. PalSmith prepares the plan and acceptance criteria; the current Agent Runtime executes only approved reads/writes and returns evidence.

| Template | Example / AI judgement cue | Current Pal / PalSmith collaboration | Runtime executor | User confirmation | Memory involved | Registry / contacts | Public release fit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pal-health-inspection-task-package.md` | Example: "体检所有 Pal", "检查这个 Pal" | current Pal may hand off health/consistency review to PalSmith after AI judgement | current Agent Runtime | only if writing a report | private memory excluded by default | may read registry/contacts | yes, report must avoid private data |
| `clean-pal-export-task-package.md` | "导出 Pal，不含记忆" | PalSmith owns clean public export planning | current Agent Runtime | yes | excludes `memory/user/` and `memory/project/` | no writes | yes |
| `with-memory-export-task-package.md` | "导出 Pal，包含记忆" | PalSmith owns high-risk private export planning | current Agent Runtime | strong confirmation | explicit memory scope only | no writes | no, unless converted to clean export |
| `pal-import-staging-task-package.md` | "从 GitHub / 本地导入 Pal" | PalSmith owns untrusted import staging | current Agent Runtime | yes | memory read denied unless approved | no writes | staging report only |
| `pal-install-task-package.md` | "安装 staged Pal" | PalSmith may recommend after staging review | current Agent Runtime | yes | private memory excluded unless approved | no writes | yes if clean |
| `pal-creation-task-package.md` | "创建一个 Pal" | PalSmith owns Pal Pack creation planning | current Agent Runtime | yes | no private memory | suggestions only | yes |
| `pal-team-creation-task-package.md` | "创建一个 Pal 团队" | PalSmith owns team/package planning | current Agent Runtime | yes | no private memory | suggestions only | yes |
| `create-first-professional-pal.md` | Auxiliary / legacy single-Pal package. Use only as supporting reference after the current `create-composite-pal.md` chain has set asset execution inheritance. | PalSmith owns bounded single Pal creation planning | current Agent Runtime | yes before writes | explicit source scope only | suggestions only | depends on source rights |
| `create-ai-team-from-goal.md` | User wants a bounded AI team from a broad goal | PalSmith owns end-to-end team design and creation planning | current Agent Runtime | yes before writes | explicit source scope only | suggestions only | depends on source rights |
| `registry-update-task-package.md` | "生成 / 写入 registry 更新" | PalSmith checks standard Pal eligibility | current Agent Runtime | exact diff confirmation | excluded | writes registry only | yes |
| `contacts-update-task-package.md` | "加入通讯录 / contacts" | PalSmith checks contactability and rejects ordinary Skills | current Agent Runtime | exact diff confirmation | excluded | writes contacts only | yes |
| `snapshot-task-package.md` | "修改前做快照" | PalSmith owns snapshot planning | current Agent Runtime | yes | depends on approved target | no writes unless target includes JSON | private by default |
| `rollback-task-package.md` | "回滚这个修改" | PalSmith owns rollback risk planning | current Agent Runtime | explicit overwrite confirmation | depends on approved target | only if confirmed target | private by default |
| `official-pal-registration-task-package.md` | "登记为官方 Pal / 加入官方清单" | PalSmith checks official Pal consistency | current Agent Runtime | exact JSON confirmation | excluded | writes agentpal/registry/contacts | yes |
| `pal-quality-inspection-task-package.md` | "这个 Pal 怎么感觉不好用" | PalSmith owns quality inspection | current Agent Runtime | only if writing a report or fixes | private memory excluded by default | may read registry/contacts | yes |
| `user-material-ingestion-task-package.md` | "我有资料要喂给这个 Pal" | PalSmith owns content-preserving material ingestion planning | current Agent Runtime | yes before reading private material or writing assets | explicit material scope only | no automatic writes | depends on material rights |
| `content-preservation-review-task-package.md` | "检查材料有没有被压缩坏" | PalSmith owns source inventory and preservation review | current Agent Runtime | only if writing a report | explicit source set only | read-only unless confirmed | depends on material rights |
| `web-research-to-knowledge-task-package.md` | "帮这个 Pal 补行业知识" | PalSmith owns research-to-knowledge planning and citation boundaries | current Agent Runtime | yes before network access or writing assets | private memory excluded by default | no automatic writes | yes if sources permit |
| `palsmith-self-health-review-task-package.md` | "检查 PalSmith 自己是不是空心" | PalSmith owns self-health review for skill/knowledge depth | current Agent Runtime | only if writing reports/fixes | private memory excluded by default | may read registry/contacts | yes |
| `pal-conflict-detection-task-package.md` | "这些 Pal 职责是不是重复" | PalSmith owns conflict detection | current Agent Runtime | only if writing a report | excluded | read-only unless later confirmed | yes |
| `pal-capability-map-task-package.md` | "我有哪些 Pal 能做这个" | PalSmith owns capability map generation | current Agent Runtime | only if writing a report | excluded | may read registry/contacts | yes |
| `pal-team-design-task-package.md` | "我想搭建一个 AI 团队" | PalSmith owns team design before creation | current Agent Runtime | creation requires later confirmation | no private memory | suggestions only | yes |
| `pal-version-upgrade-task-package.md` | "把这个 Pal 升到 stable" | PalSmith owns version governance | current Agent Runtime | yes | depends on target | no contacts write by default | yes |
| `pal-version-rollback-task-package.md` | "回滚这个 Pal 版本" | PalSmith owns rollback governance | current Agent Runtime | explicit overwrite confirmation | depends on target | no contacts write by default | private by default |
| `pal-eval-lab-task-package.md` | "这个新 Pal 可以用了么" | PalSmith owns Eval Lab planning | current Agent Runtime | only if writing evals/reports | private memory excluded by default | may read registry/contacts | yes |
| `ai-team-builder-task-package.md` | AI judgement says the user wants an AI team design | PalSmith owns team-building design | current Agent Runtime | creation requires later confirmation | private memory excluded by default | suggestions only | yes |
| `pal-team-governance-task-package.md` | AI judgement says a team needs governance review | PalSmith owns team governance | current Agent Runtime | only if writing reports/files | private memory excluded by default | may read registry/contacts | yes |
| `cross-pal-review-task-package.md` | AI judgement says independent Pal review is needed | PalSmith owns review boundary and quality gate | current Agent Runtime | only if writing reports | context packets only | read-only unless later confirmed | yes |
| `pal-publish-quality-gate-task-package.md` | AI judgement says a Pal or team needs publish readiness | PalSmith owns publish gate | current Agent Runtime | status writes require confirmation | private memory excluded by default | may read registry/contacts | yes |
| `pal-readiness-review-task-package.md` | AI judgement says lifecycle / Eval Lab / publish readiness should be unified | PalSmith owns readiness matrix review | current Agent Runtime | writes or private reads require confirmation | private memory excluded by default | may read registry/contacts | yes |
| `pal-runtime-call-verification-task-package.md` | AI judgement says direct-call verification is needed | PalSmith owns call verification levels | current Agent Runtime | only if writing reports | excluded | may read registry/contacts | yes |
| `github-import-verification-task-package.md` | AI judgement says GitHub import should be verified | PalSmith owns import verification plan | current Agent Runtime | network/fetch/install require confirmation | memory denied unless approved | no automatic writes | yes |

## Selection Rule

AgentPal does not route by keyword. The current Pal and current Brain / AI judge task ownership from user goal, expected deliverable, risk, contacts/registry, and available Pal assets. Mira is the default entry Pal, but any Pal may consult, delegate, or hand off to PalSmith when AI judgement says the task belongs to Pal asset governance. PalSmith then chooses the smallest matching template and asks focused confirmation questions before any Runtime write.

## Runtime Evidence

Every template expects concrete evidence: files read, files changed, generated reports, JSON parse results, included/excluded files, and `not-run` checks.
