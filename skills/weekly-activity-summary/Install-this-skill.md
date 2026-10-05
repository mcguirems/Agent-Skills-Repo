# Install This Skill

## Platform-neutral installation

Download `weekly-activity-summary.zip`, extract it, and place the top-level `weekly-activity-summary/` folder in the directory your agent uses for local skills. Keep the internal structure unchanged so `SKILL.md` can resolve its templates and references.

```text
weekly-activity-summary/
  SKILL.md
  README.md
  Install-this-skill.md
  agents/
  assets/
  references/
```

Restart or reload the agent’s skill registry if the runtime does not discover new skills automatically.

## Codex installation

For Codex, the typical user-level destination is:

- `~/.codex/skills/weekly-activity-summary/`

Copy the extracted top-level folder there, then start a new session or reload skills. Invoke it with `$weekly-activity-summary` or ask for Mike’s weekly activity or standup summary.

## Connected services

For full coverage, authenticate the agent to the relevant Asana, PostHog, Google Drive, Slack, and ChatGPT work sources. Gmail is optional and intentionally low priority. Missing access must result in narrower coverage, never invented evidence.
