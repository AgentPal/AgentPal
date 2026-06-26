# PalSmith Demo Script

Status: PalSmith v0.4 demo aid.

This 10-minute script helps users, maintainers, and demo hosts show the PalSmith path from one sentence to a Pal or AI team plan. It is not a fixed script, not keyword routing, and not proof that any Runtime action has already happened.

## Demo Boundary

- PalSmith owns Pal asset governance judgement.
- The current Agent Runtime executes only approved Runtime Task Packages.
- No hidden app, CLI, scanner, validator, importer, exporter, or UI is involved.
- Examples are few-shot demonstrations. The current Pal and current Brain / AI still judge whether to consult, delegate, or hand off to PalSmith.

## 10-Minute Flow

| Minute | Action | Expected Result |
| --- | --- | --- |
| 0-1 | Open AgentPal and call PalSmith | user sees direct Pal entry |
| 1-3 | Demo 1: personal work Pal | PalSmith proposes one Pal and asks confirmation |
| 3-6 | Demo 2: cross-border commerce AI team | PalSmith proposes 3-5 Pals and team boundaries |
| 6-9 | Demo 3: publish readiness | PalSmith runs readiness review path in report form |
| 9-10 | Recap no-code boundary | user understands Runtime evidence and confirmation |

## Demo 1: Create A Personal Work Pal

### 用户输入

```text
/pal PalSmith 帮我创建一个个人工作 Pal，负责整理我的会议记录和行动项。
```

### PalSmith 应该怎么回答

PalSmith should first explain:

- inferred goal
- proposed Pal name and role
- responsibilities
- non-responsibilities
- privacy boundary
- whether it is private, team-local, or global-contact candidate
- confirmation questions

### 用户确认

```text
确认先只创建私有草稿，不加入 contacts，不读取私人 memory。
```

### Runtime Task Package

PalSmith prepares `Pal Creation Task Package`.

### 预期创建内容

Only after confirmation, the current Agent Runtime may create a draft Pal directory with root files, output contract, and placeholders.

### PalSmith 质量体检

PalSmith checks:

- required root files
- responsibility clarity
- no private memory copied
- registry / contacts not changed unless separately confirmed

### 最终状态

Recommended state: `draft`.

## Demo 2: Create A Cross-Border Commerce AI Team

### 用户输入

```text
/pal PalSmith 帮我搭建一个跨境电商 AI 团队，先覆盖选品、Listing、广告和客服。
```

### PalSmith 应该怎么回答

PalSmith should propose a 3-5 Pal team:

| Pal | Purpose |
| --- | --- |
| Market Scout | product and competitor research |
| Listing Writer | listing copy and FAQ drafts |
| Ad Planner | campaign hypotheses and test plans |
| Support Drafter | customer reply drafts |
| Commerce Verifier | risk, consistency, and publish review |

PalSmith should also explain owner, verifier, consultants, shared knowledge, shared workflows, Context Packet rules, and team-local vs global contacts.

### 用户确认

```text
确认这个 5 Pal 方案，但先只生成团队设计和 task package，不实际创建文件。
```

### Runtime Task Package

PalSmith prepares `AI Team Builder Task Package`. If the user later confirms creation, PalSmith prepares `Pal Team Creation Task Package`.

### 预期创建内容

In this demo, no files are created because the user requested design only. The final report should say `not-run` for file creation.

### PalSmith 质量体检

PalSmith checks whether the design has:

- clear owner/verifier/consultants
- no all-global-contact shortcut
- no all-memory access
- 3-5 Pal size control
- follow-up creation boundary

### 最终状态

Recommended state: `idea` or `draft`, depending on whether files were created.

## Demo 3: Publish Readiness Check

### 用户输入

```text
/pal PalSmith 这个 Pal 可以发布了吗？
```

### PalSmith 应该怎么回答

PalSmith should not answer "yes" immediately. It should say:

```text
I will first do a readiness review. I will check structure, identity, responsibilities, capability coverage, evals, export safety, registry / contacts consistency, and runtime evidence before recommending draft / testing / stable / publish-ready.
```

### 用户确认

```text
确认只读检查，不写文件，不发布。
```

### Runtime Task Package

PalSmith prepares `Pal Readiness Review Task Package`.

### 预期创建内容

No created files unless the user asks for a report file. The Runtime may read approved public Pal files and return evidence.

### PalSmith 质量体检

PalSmith uses:

- readiness matrix
- Eval Lab result
- publish quality gate
- clean export safety
- no-code boundary

### 最终状态

Recommended state is one of:

- `draft`
- `testing`
- `stable`
- `publish-ready`

If evidence is missing, PalSmith reports `missing` or `not-run` instead of smoothing the result into a pass.

## Closing Line

```text
PalSmith does not create magic automation. It gives the current Runtime a bounded task package, checks the evidence, and helps the user understand the next state.
```
