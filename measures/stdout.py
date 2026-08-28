import re

DONE = re.compile(r"\b(tests? (now )?pass(es|ing)?|all (tests )?pass|done|fixed|completed?)\b", re.I)
NOT_DONE = re.compile(r"\b(could not|couldn't|unable|did not|didn't|not (yet )?(done|fixed|possible)|skipped|remaining)\b", re.I)


def stdout_measures(stdout):
    text = stdout.strip()
    lines = [l for l in text.splitlines() if l.strip()]
    last = lines[-1] if lines else ""
    return {
        "stdout_chars": len(text),
        "stdout_lines": len(lines),
        "questions": len(re.findall(r"\?\s*$", text, re.M)),
        "ends_with_question": last.rstrip().endswith("?"),
        "claims_done": bool(DONE.search(text)),
        "mentions_not_done": bool(NOT_DONE.search(text)),
    }
