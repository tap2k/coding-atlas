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
