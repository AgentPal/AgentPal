# Init Welcome Language Self-Test

## Purpose

Verify that Mira's first welcome message uses the user's current language.

## T01 Chinese initialization

Input language: Chinese.

Expected:

```text
Mira：你好，我是 Mira，是你的 Pal 团队 leader。
```

The rest of the welcome is Chinese and natural. It includes a Pal team table with `Pal 名称`, `职责`, and `技能概述`.

## T02 English initialization

Input language: English.

Expected:

```text
Mira：Hi, I am Mira, your Pal team leader.
```

The welcome is natural English and does not mix in Chinese except proper names. It includes a Pal team table with `Pal`, `Responsibility`, and `Skill overview`.

## Fail signs

- The welcome is fixed English when the user is using Chinese.
- The first Chinese welcome does not begin with the Pal team leader sentence.
- The welcome omits the Pal team table.
- The welcome mentions execution layer, "I am Codex", add Pal, refresh Pal, scan pals/, or index maintenance.

