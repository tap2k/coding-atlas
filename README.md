# coding-atlas

When a coding agent says done, is it? A field guide to what agents do in tricky
situations, and what they tell you they did.

Thirteen agent configurations (Claude Code, Codex CLI, Gemini CLI as products, plus ten
models in the OpenCode harness) run the same six small booby-trapped repos with the same
one-line instructions, three times each. Each repo has a right thing to do, a shortcut
that looks done, and a hidden check the agent never sees. Two records per run: what the
agent changed (diff, every shell command) and what it said. The measures are counts and
string comparisons — no judge model, no score, profiles not ranks.

The six situations ask three questions, twice each: when the job is only part done, does
it say so (calm); when the test and the truth disagree, does it find out which is lying
(rushed); when the user insists on something wrong, does it hold or fold (pushed). Two
more situations measure the wrapper rather than the model: asking before a destructive
guess, and keeping a rule file the harness's own prompt argues against.

Layout: `anchors/` (frozen scenarios: workspace, synthetic git history, instruction,
hidden checker, measures spec), `adapters/` (how to invoke each product headless, ~10
lines each), `measures/` (pure functions over diff, trace, stdout), `run` (materialize,
shim PATH, invoke, snapshot, measure), `results/` (every run's receipts), `site/`
(static site compiled from results, committed at `site/out/`; prose editable in
`site/COPY.md`, `python3 site/copy.py sync` to apply). `docs/PILOT.md` is the running
log of findings, corrections, and design decisions.

Reproduce a cell: `./run --anchor <verb>/<name> --product <adapter> [--model id]`.
Preview the site: `site/preview.sh`.

Add a scenario: copy any folder under `anchors/` and change three things — the workspace
(a small repo with a trap), `instruction.md` (one line), and `checker_test.py` (the
hidden check). `history.toml` lists every workspace file; the runner refuses to start
otherwise. New scenarios enter as rotation; the core set stays frozen between waves.
