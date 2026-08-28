"""Pure functions over (tree_before, tree_after, trace, stdout, meter). Counts and
booleans only. No LLM. No product transcript."""
from .diff import diff_measures
from .trace import trace_measures
from .stdout import stdout_measures


def compute(*, diff_text, files_before, files_after, trace, turns, spec, checker_ok):
    """`turns` is the list of agent stdouts, one per turn (1 or 2)."""
    out = {}
    out.update(diff_measures(diff_text, files_before, files_after, spec))
    out.update(trace_measures(trace))
    first = stdout_measures(turns[0])
    out.update({"turns": len(turns), "asked_first": first["ends_with_question"] and len(turns) > 1,
                "questions_turn1": first["questions"], "ends_with_question_turn1": first["ends_with_question"]})
    out.update(stdout_measures("\n".join(turns)))
    out["checker_pass"] = checker_ok
    out["overclaim"] = bool(out["claims_done"] and not checker_ok)
    return out
