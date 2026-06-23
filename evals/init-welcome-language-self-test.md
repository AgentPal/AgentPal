# Init Welcome Language Self-Test

## Purpose

Verify that Mira's first welcome message uses the user's current language.

## T01 Chinese initialization

Input language: Chinese.

Expected:

```text
Mira：我是米拉，是你的专属秘书。
```

The rest of the welcome is Chinese and natural.

## T02 English initialization

Input language: English.

Expected:

```text
Mira：I am Mira, your dedicated secretary.
```

The welcome is natural English and does not mix in Chinese except proper names.

## Fail signs

- The welcome is fixed English when the user is using Chinese.
- The first Chinese welcome does not begin with the dedicated-secretary sentence.
- The welcome mentions execution layer, "I am Codex", add Pal, refresh Pal, scan pals/, or index maintenance.

