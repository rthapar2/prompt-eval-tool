# Day 6 — Reading the anthropic SDK's messages.py

Read through `create()` in
`.venv/lib/python3.9/site-packages/anthropic/resources/messages/messages.py`.

## What I recognized
- `max_tokens: int` — the parameter I already pass as `1024` in `hello_claude.py`;
  it's a hard ceiling on response length, not a target.
- `model` — same string I already set (and saw the SDK checks for deprecated
  model names here).
- `temperature` — not something I set yet, but I now understand it controls
  randomness: low for consistent answers, high for variety/creativity.

## What confused me
- The `thinking: ThinkingConfigParam | Omit = omit` parameter — the SDK uses a
  special `Omit` sentinel instead of `None` as the default, specifically so it
  can tell "the user didn't pass this" apart from "the user explicitly passed
  nothing." Took a second explanation to click.
