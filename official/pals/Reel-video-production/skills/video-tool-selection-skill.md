# Video Tool Selection Skill

## Purpose

Choose the right runtime, model, reasoning strength, Skill, plugin, MCP, or external tool combination for a video task.

## Method

1. Classify the deliverable.
2. Identify tool needs: HTML video, command-line processing, React video, agentic pipeline, subtitles, TTS, audio, or external generation.
3. Check current host capability evidence or mark `unknown`.
4. Choose candidate tools and fallback.
5. State model/reasoning needs.
6. Preserve tool references as candidates, not routes.

## Output

Compact Agent-use style decision:

- owner Pal;
- verifier Pal;
- runtime/tool candidates;
- capability source;
- selected mode;
- evidence required;
- authorization needed;
- fallback.
