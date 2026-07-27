# Prompt Eval Tool

A learning project for testing purposes only — built to practice working with the Claude API and Git/GitHub, and to eventually become a small tool for checking whether an LLM prompt's output still meets quality expectations after it's been edited (a "prompt regression tester").

## Current status

Early stage. Right now this repo contains a single smoke-test script (`hello_claude.py`) that confirms the environment, API connection, and request/response handling all work end to end. The actual evaluation logic (test cases, rubrics, pass/fail scoring) hasn't been built yet.

## Setup

```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

You'll also need an `ANTHROPIC_API_KEY` set in your environment with an active credit balance.

## Running it

```
.venv/bin/python hello_claude.py
```
