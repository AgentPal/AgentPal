# HyperFrames Boundary And Workflow

Source: local HyperFrames plugin skill inspected during Reel creation.

## What HyperFrames Is Good For

- HTML-based video compositions.
- Title cards.
- Overlays.
- Captions and subtitles synced to audio.
- TTS narration.
- Audio-reactive visuals.
- Animated text emphasis.
- Scene transitions.
- Product explainers and launch videos.

## Core Workflow

1. Define visual identity before composition HTML.
2. Scaffold or prepare project.
3. Write composition HTML with timing attributes.
4. Use GSAP for deterministic motion.
5. Run lint and validation.
6. Inspect visual layout.
7. Preview in Studio.
8. Render only when authorized and ready.

## Critical Rules

- HTML is the source of truth.
- Visual identity is required before composition authoring.
- Use `data-composition-id`, `data-start`, `data-duration`, and `data-track-index`.
- Timelines must be registered in `window.__timelines`.
- Multi-scene compositions need transitions and entrance animations.
- Validate, inspect, and preview before claiming completion.

## Reel Use

Reel may prepare HyperFrames task packages or execute through the host runtime when authorized and available. Reel must not claim render success without current evidence.
