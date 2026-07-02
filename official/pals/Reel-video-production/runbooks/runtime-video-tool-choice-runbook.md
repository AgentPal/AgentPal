# Runtime Video Tool Choice Runbook

## Use When

The user asks what video tool, plugin, Skill, MCP, model, or external service should be used.

## Steps

1. Identify the deliverable and platform.
2. Identify whether the task is motion graphics, screen demo, talking-head, edit/trim, subtitles, TTS, audio cleanup, or full AI generation.
3. Check current host capability evidence or mark `unknown`.
4. Choose likely candidates:
   - HyperFrames for HTML/motion/caption/TTS composition.
   - FFmpeg for technical video/audio processing.
   - Remotion for React component video.
   - OpenMontage for agentic video pipelines.
   - Subtitle/TTS/audio tools for specialized timing and sound tasks.
5. State evidence required before claiming execution.
6. State fallback if unavailable.

## Stop Conditions

- Tool access requires credentials, payment, or external account changes.
- Publication is requested without authorization.
- Rights for footage, music, voice, or generated media are unclear.
