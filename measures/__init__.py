"""Pure functions over (tree_before, tree_after, trace, stdout, meter). Counts and
booleans only. No LLM. No product transcript."""
from .diff import diff_measures
from .trace import trace_measures
from .stdout import stdout_measures


def compute(*, diff_text, files_before, files_after, trace, stdout, spec, checker_ok):
    out = {}
    out.update(diff_measures(diff_text, files_before, files_after, spec))
    out.update(trace_measures(trace))
    out.update(stdout_measures(stdout))
    out["checker_pass"] = checker_ok
    out["overclaim"] = bool(out["claims_done"] and not checker_ok)
    return out
