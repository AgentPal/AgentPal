# Video Quality Checks

## Must Check

- Aspect ratio.
- Safe areas.
- Visual overflow.
- Text/caption clipping.
- Subtitle sync.
- Audio loudness and clipping risk.
- Black frames.
- Blank frames.
- Frozen or unintended static sections.
- Transition abruptness.
- Pacing.
- Platform target.
- Brand consistency.
- Export codec and file size when relevant.

## Evidence

Acceptable evidence may include:

- rendered preview;
- frame samples;
- HyperFrames inspect output;
- ffprobe/ffmpeg checks;
- transcript timing;
- audio waveform or loudness check;
- human review notes.

Use `not-run` where evidence is absent.
