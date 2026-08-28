# AGENTS.md

Read `docs/BRIEF.md` first; it is the design brief (architecture, measures, user-side
rule, verbs, rules for growth, open design items). This repo is public: design only.
Strategy, prior-art assessment, sequencing, and go-to-market live outside it and must not
be committed here.

Rules that bind:
- Anchors are frozen once tagged. Append, never edit. Bump `spec_version` per anchor.
- No LLM anywhere in `measures/`. Every measure is a count or boolean from the tree diff,
  the process trace, stdout, or the meter.
- Adapters do invocation only. If a measure needs a product's native transcript, the
  measure is wrong.
- No aggregate score exists in any schema. Profiles, not ranks.
- No hosted runner, no CI service. The runner stays small.
- Cheap: small repos, short tasks, subscriptions over API keys where allowed.

Local pilot setup (until the container exists):
- Claude Code: `cp -R ~/.claude ~/.atlas-claude && rm -rf ~/.atlas-claude/{CLAUDE.md,plugins,hooks}`,
  strip `hooks` from `~/.atlas-claude/settings.json`, then `export ATLAS_CLAUDE_CONFIG_DIR=~/.atlas-claude`.
  Verify: `CLAUDE_CONFIG_DIR=~/.atlas-claude claude -p "do you see a CLAUDE.md? yes/no"` says no.
- Codex: `codex login` (ChatGPT plan). Gemini: run `gemini` once and complete OAuth.
- OpenCode: `opencode auth login` for Anthropic. Pilot runs every product on its default model (`pinned: false`); the served model is recorded where the product reports it.
- Pilot: `for a in comply/csv-green ask/rename-which; do for p in claude-code codex gemini opencode; do ./run --anchor $a --product $p --n 3 --out results; done; done`
