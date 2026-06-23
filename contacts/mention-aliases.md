# Mention Aliases

Use display names for direct Pal calls.

## Direct Calls

| Mention | Pal | Mode |
|---|---|---|
| `/pal Mira` | Mira | consult by default |
| `/pal Atlas` | Atlas | consult by default |
| `/pal Vega` | Vega | consult by default |
| `/pal Rhea` | Rhea | consult by default |
| `/pal Quinn` | Quinn | consult by default |
| `/pal Morgan` | Morgan | consult by default |
| `/pal Harper` | Harper | consult by default |
| `/pal Nova` | Nova | consult by default |

## `@Name` Aliases

| Alias | Pal |
|---|---|
| `@Mira` | Mira |
| `@mira` | Mira |
| `@米拉` | Mira |
| `@Atlas` | Atlas |
| `@atlas` | Atlas |
| `@阿特拉斯` | Atlas |
| `@Vega` | Vega |
| `@vega` | Vega |
| `@维加` | Vega |
| `@Rhea` | Rhea |
| `@rhea` | Rhea |
| `@瑞亚` | Rhea |
| `@Quinn` | Quinn |
| `@quinn` | Quinn |
| `@昆恩` | Quinn |
| `@Morgan` | Morgan |
| `@morgan` | Morgan |
| `@摩根` | Morgan |
| `@Harper` | Harper |
| `@harper` | Harper |
| `@哈珀` | Harper |
| `@Nova` | Nova |
| `@nova` | Nova |
| `@诺瓦` | Nova |

Pattern:

```text
/pal {display_name}
```

Unknown names should be checked against `registry/pal.index.json` and `contacts/pals.json`.

If a name is not found, report an Unknown Pal. Do not invent or impersonate the missing Pal.

Users call Pals by display name, not directory name:

```text
/pal Atlas
```

not:

```text
/pal Atlas-developer
```

