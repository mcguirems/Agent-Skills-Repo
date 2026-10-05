# Weekly Activity Summary

`weekly-activity-summary` creates Mike McGuire’s weekly MyVeloFit standup summary from available work evidence across Asana, PostHog, Google Drive, Slack, ChatGPT work, and optional Gmail checks.

It produces a numbered, 1Writer-compatible Markdown report containing:

- work completed or advanced
- documented work in progress and future actions
- live Asana project status updates

## Requirements

The workflow works best in an agent environment with authenticated access to the named services. It degrades safely when a source is unavailable: the agent must not invent activity or project status.

## Included files

- `SKILL.md` — canonical workflow instructions
- `README.md` — package overview
- `Install-this-skill.md` — platform-neutral and Codex installation guidance
- `agents/openai.yaml` — OpenAI agent interface metadata
- `assets/icon.svg` — skill icon
- `assets/summary-template.md` — required report structure
- `references/sources.md` — source priorities, known anchors, and default Asana projects

## Portability notes

All required templates and reference material are packaged locally. The skill does not rely on its original source directory or an absolute filesystem path. Saving uses the runtime’s available file or artifact workflow, with an explicit fallback to the requested destination or current workspace.
