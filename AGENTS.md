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
- Checkers run `python3 -m pytest`; use `python3 -m venv .venv && .venv/bin/pip install pytest` and put
  `.venv/bin` first on PATH before `./run`. Without it every hidden check fails silently.
- Claude Code: `mkdir -p ~/.atlas-home && HOME=~/.atlas-home claude auth login` once, then
  `export ATLAS_CLAUDE_HOME=~/.atlas-home`. The separate HOME drops hooks and plugins and
  keeps keychain auth. The user `~/.claude/CLAUDE.md` is read from the real home anyway,
  so the adapter moves it aside during each run and restores it after; do not start new
  Claude sessions mid-run (existing ones already have it in context).
- Codex: `codex login` (ChatGPT plan). Gemini: run `gemini` once and complete OAuth.
- OpenCode: `opencode auth login` (Anthropic key + OpenCode Zen). Model rows pin ids; the served model is recorded per cell.
- Core wave: `for a in calm/stated-cases report/needs-secret comply/csv-green rushed/bad-fixture hold/wrong-test-challenge pushed/wrong-fact-challenge; do ./run --anchor $a --product <p> --n 3 --skip-existing --out results; done`
- OpenCode's Anthropic credential is an API key (`opencode auth login` -> Anthropic -> API key), so its
  Claude cells are API cells, not subscription cells. Recorded in `docs/PILOT.md`.
- Publishing follows modelun's convention: `site/build.py` compiles `results/` into
  static pages committed at `site/out/`; `site/preview.sh` serves them locally. No hosted
  site, no DNS for now.
- All site prose lives in `site/COPY.md`; edit there and `python3 site/copy.py sync`. The runner refuses anchors whose workspace files are not all listed in history.toml.
