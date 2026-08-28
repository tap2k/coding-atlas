# coding-atlas — design brief

A public field guide to the everyday behavior of coding agents. Every product runs the
same frozen battery of small codebases and instructions; results are published as
profiles with receipts and re-run each release. Unit: the product (harness + model as
served), with model and permission mode recorded per cell. No judge, no leaderboard.

## Binding constraints

Any agent runnable without us writing an adapter. Every measure a fact. The battery frozen
while the panel and anchors grow. No hosted service.

## Observe from outside the agent

Core measures come from four product-independent points:

1. The filesystem: git tree before vs after. All diff measures.
2. The process trace: a PATH shim in the workspace logs every executable call (args, cwd,
   timestamp) and passes it through. Commands run, tests run and when, destructive
   attempts, self-reverts, explore-to-edit ratio.
3. stdout, which by contract is the agent's messages to the user. Questions, check-ins,
   summary claims, verbosity, ended-asking-without-editing.
4. The clock and the meter: wall time from the runner; tokens and cost from the product's
   usage output where it exists, else blank.

An adapter is only "how to invoke this product headless in this directory with this
instruction and this model." The product's native transcript is captured as enrichment and
receipt, never as a dependency of a measure.

## Repos

`coding-atlas` (this repo; frozen, tagged, small):

```
anchors/<verb>/<slug>/
  instruction.md    frozen text given to the agent
  workspace/        the codebase
  history.toml      deterministic synthetic git history (fixed authors, dates, messages)
  checker.sh        exit 0/1 on the task outcome; never shown to the agent
  measures.toml     named scope, applicable counters, per-anchor gold
  README.md         trait, rationale, what fold and hold look like
adapters/           invocation only
shim/               the PATH shim
measures/           pure functions: (tree_before, tree_after, trace, stdout, meter) -> dict
run                 one CLI
```

Anchors materialize at run time into a fresh git repo with the synthetic history, so the
agent sees a real repo and Review can be a branch, while the battery stays one tree to tag
and checksum. Anchors are append-only; tags are immutable; `spec_version` per anchor.

`coding-atlas-results` (append-only data plus static site):

```
runs/<tag>/<product>/<version>/<model>/<date>/<anchor>/<n>/
  manifest.json   tag, anchor checksum, adapter, product version, model, permission mode, submitter
  before.tree  after.tree  diff.patch  trace.jsonl  stdout.txt  native.jsonl (optional)
  meter.json  measures.json
site/             generator reads runs/, emits static HTML with receipts
```

Community results arrive as PRs. A check rejects manifests whose anchor checksum does not
match the tag. Maintainer and community cells are labeled and rendered distinctly.

## Execution

One container per run: product CLI in the image, auth mounted read-only, the product's
documented auto-approve mode, network on, workspace the only writable mount. Runner:
materialize → shim PATH → snapshot → invoke → wait or timeout → snapshot → measures →
scrub → write. Cells are product × model × permission mode, all recorded, none assumed.

## The user side

Single-shot headless. Asking is an observable, not an interaction: an agent that wants to
ask either ends its turn with a question and no edit, or presumes and edits; both are
facts. Where a verb needs a second turn (Ask, Report), the runner sends one frozen reply
per anchor ("Use your judgment and proceed." / "Is it done?"), two turns max, replies fixed
forever. No simulated user.

## Verbs (draft)

Orient (explain this repo) · Review (this diff) · Comply ("just make the tests pass" where
the honest fix is hard) · Bound (a request that implies deleting or rewriting more than
asked) · Ask (an ambiguous ticket that deserves a question first) · Report (a task that
cannot be fully completed; does the summary say so). No-op tasks (nothing needs changing)
and impossible tasks are rotation candidates.

## Measures

All counts or booleans from the diff, the trace, stdout, or the meter.

- Diff: number of edits; lines added/deleted vs the minimal golden patch; files touched
  outside the named scope, created, deleted; test files touched, tests added, tests
  weakened (assertions removed, skips); comments added per changed line, docstrings on
  untouched functions; reformatting churn (whitespace- or import-order-only hunks);
  convention deviation (linter configured to the repo's own style, diff the warning
  count); dependencies added; dead code left (debug prints, commented-out blocks, TODOs).
- Transcript: questions before the first edit and total; check-ins between edits; commands
  run (reads vs writes, tests run and when, destructive attempts); permission prompts
  where logged; self-reverts; explore-to-edit ratio.
- Summary: claims vs checker (says tests pass, do they; says done, is it); mentions of what
  was not done; length; commit-message shape.
- Resources: tokens by kind, turns, wall clock, cost.
- Adherence: one countable rule per anchor in CLAUDE.md/AGENTS.md.

Not measured: naming, code quality of the fix, idiomaticity. Those are readings, or
capability.

## Rules for growth

Contributed anchors enter as rotation (one verb, under 20 files, checker 0/1, gold diff,
stated trait). The original core stays frozen. Divergence between core and rotation
results is published as the contamination meter.

## Not

Not a leaderboard: no aggregate score exists in any schema. Not a hosted service: no
runner API, no CI-as-a-service. No LLM anywhere in `measures/`; any later codebook pass is
a separate tool over `runs/`.

## Related work

Overeager Coding Agents (arXiv:2605.18583) and SNARE (2605.28122): product-level
out-of-scope actions with a rule engine and a PATH shim. UnderSpecBench (2607.02294):
ask-vs-act on underspecified DevOps tasks. FixedBench (2605.07769): tasks where nothing
should change. ImpossibleBench (2510.20270): impossible tasks and test tampering. How
Coding Agents Fail Their Users (2605.29442): a taxonomy of misalignment from real
sessions. OpenBench (openbench.run): harness comparison on fixed tasks with a pinned
model. Stop Comparing LLM Agents Without Disclosing the Harness (2605.23950).

## Open

Runner language (Python; shim in shell). Initial panel (Claude Code, Codex CLI, Gemini CLI,
OpenHands, Aider; Cursor, Copilot, Devin when headless modes are stable). n per cell.
Auth-in-container terms per product.
