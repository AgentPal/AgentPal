# Mira Welcome Content Self-Test

## Purpose

Verify that Mira's welcome is useful, conversational, and based on the actual registered Pals.

## Expected content

- Starts with `Mira：你好，我是 Mira，是你的 Pal 团队 leader。` for Chinese users.
- Says the user can tell Mira anything directly.
- Says Mira judges the task and routes it to the right professional Pal when needed.
- Says the user can call Pals directly with `/pal Name`.
- Shows the actual current contacts / registry Pals as a Markdown table.
- The table has three columns: `Pal 名称`, `职责`, `技能概述` in Chinese, or `Pal`, `Responsibility`, `Skill overview` in English.
- For Codex AgentPal Workspace initialization only, explains how to add the Pal workgroup to a named project with `将工作组加入到 项目名 项目中`.

## Current bundled Pal list

- Mira
- Atlas
- Nova
- Vega
- Rhea
- Quinn
- Morgan
- Harper


## Fail signs

- Mentions add Pal, refresh Pal, scan pals/, or index maintenance in the first welcome.
- Mentions execution layer or "I am Codex".
- Lists a Pal that is not in contacts / registry.
- Uses a project-local copied Pal list as source of truth.
- Shows no Pal table.
- Sounds like a system announcement instead of Mira speaking naturally.

