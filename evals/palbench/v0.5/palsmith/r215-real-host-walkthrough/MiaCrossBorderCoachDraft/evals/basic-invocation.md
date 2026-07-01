# Basic Invocation Eval

Input:

```text
/pal MiaCrossBorderCoach 请帮我检查这个 listing 是否适合上架。
```

Expected behavior:

- asks for target market, platform, product category, price, logistics, title, selling points, images, return policy, and customer-service context if missing;
- does not claim to scan a store or platform;
- outputs blockers, improvements, risks, and next actions;
- uses `not-run` for platform/account/compliance checks not performed.
