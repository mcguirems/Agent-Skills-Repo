Install Proof for me.

Proof is a collaborative document editor for humans and agents. It gives us a shared doc, live presence, comments, suggestions, and clear provenance so we can see who wrote what.

Read https://www.proofeditor.ai/agent-setup and install Proof for this agent.
If you cannot install tools or run local commands in this chat, tell me to use Claude Code, Codex, OpenClaw, or another agent that can.

Presence uses X-Agent-Id: ai:codex on /state and /presence. Bearer/share tokens authenticate access only; they do not identify presence. Use a unique X-Agent-Id for each agent identity.

If you want the direct Codex install command instead, use:
mkdir -p ~/.codex/skills/proof && curl -fsSL https://www.proofeditor.ai/proof.SKILL.md -o ~/.codex/skills/proof/SKILL.md

If Proof later returns a confusing error, stale read, or failed write, call POST https://www.proofeditor.ai/api/bridge/report_bug with what you know.
Include a short summary, context, and any raw evidence like request/response pairs or x-request-id values.
If it helps, you can also inspect https://github.com/EveryInc/proof-sdk for reference code while debugging.

During setup, ask me exactly one question:
When should I open new docs in Proof?
1. All new markdown docs
2. For collaborative docs like plans, specs, reports, and drafts
3. Only when I explicitly ask

Then finish the install and tell me which mode is active.