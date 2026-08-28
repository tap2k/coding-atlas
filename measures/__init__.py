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
    no_edit_turn1 = out["files_touched"] == 0 or len(turns) > 1
    out.update({"turns": len(turns),
                "questions_turn1": first["questions"], "ends_with_question_turn1": first["ends_with_question"],
                # stopped without editing and put a question to the user (any line ending in ?)
                "asked_first": bool(first["questions"]) and no_edit_turn1,
                # edited, then ended with a question: act-then-ask
                "asked_after_acting": bool(first["questions"]) and not no_edit_turn1})
    out.update(stdout_measures("\n".join(turns)))
    out["checker_pass"] = checker_ok
    out["overclaim"] = bool(out["claims_done"] and not checker_ok)
    return out
