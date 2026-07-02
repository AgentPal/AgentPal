# Video Tool, Skill, Plugin, MCP, And Open-Source Candidate Index

Status: dated research seed
Last checked: 2026-06-30
Refresh rule: update before relying on availability, pricing, API support, platform specs, license, or integration claims.

This file is a candidate index, not a permanent fact table and not a route map.

## HTML / Programmatic Video

- HyperFrames: local Codex plugin candidate for HTML video compositions, captions, TTS, audio-reactive visuals, transitions, validation, preview, and render workflows. Availability must be checked in the current host runtime.
- Remotion: React-based programmatic video framework useful for component-driven video templates and rendering. Source: https://www.remotion.dev/

## Command-Line Video And Audio

- FFmpeg: core open-source multimedia tool for transcoding, trimming, filtering, audio/video processing, and technical checks. Source: https://ffmpeg.org/
- ffprobe: FFmpeg companion tool for inspecting streams, duration, codecs, and metadata.

## Agentic Video Pipelines

- OpenMontage: open-source AI video pipeline candidate with research, proposal, script, scene plan, assets, edit, and compose stages. Review license and runtime fit before integration. Source: https://github.com/calesthio/OpenMontage

## Subtitles, Transcription, And TTS

- HyperFrames transcribe and tts commands: local workflow candidate for transcription and voiceover when available.
- WhisperX: word-level timestamp transcription candidate for subtitle sync. Source: https://github.com/m-bain/whisperX
- Piper: local neural TTS candidate. Source: https://github.com/rhasspy/piper
- Subtitle Edit: subtitle editing and conversion candidate. Source: https://github.com/SubtitleEdit/subtitleedit

## External AI Video Tools

Runway, Kling, Veo, Pika, Luma, HeyGen, Synthesia, Descript, CapCut, DaVinci Resolve, Premiere Pro, and similar tools may be useful candidates, but Reel must refresh current capabilities, pricing, access, and privacy terms before relying on them.

## Workflow Rule

For any current task, Reel should record:

- tool candidate;
- why it fits;
- capability source;
- current availability evidence;
- privacy, rights, or external write risk;
- cost/API/key requirement;
- fallback if unavailable;
- invocation status: `real_call`, `dry_run`, `prompt_inspection`, `not_invoked`, or `blocked`.
