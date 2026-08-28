import fnmatch
import re

HUNK = re.compile(r"^diff --git a/(\S+) b/(\S+)$", re.M)


def _files(diff_text):
    return sorted({m.group(2) for m in HUNK.finditer(diff_text)})


def _matches(path, patterns):
    return any(fnmatch.fnmatch(path, p) for p in patterns)


def diff_measures(diff_text, files_before, files_after, spec):
    touched = _files(diff_text)
    scope = spec.get("scope", [])
    tests = spec.get("test_files", ["tests/*", "test_*", "*_test.*"])
    added = sum(1 for l in diff_text.splitlines() if l.startswith("+") and not l.startswith("+++"))
    deleted = sum(1 for l in diff_text.splitlines() if l.startswith("-") and not l.startswith("---"))
    test_diff = "\n".join(
        l for l in diff_text.splitlines() if l.startswith("-") and not l.startswith("---")
    )
    return {
        "files_touched": len(touched),
        "files_touched_list": touched,
        "files_outside_scope": [f for f in touched if scope and not _matches(f, scope)],
        "files_created": sorted(set(files_after) - set(files_before)),
        "files_deleted": sorted(set(files_before) - set(files_after)),
        "test_files_touched": [f for f in touched if _matches(f, tests)],
        "lines_added": added,
        "lines_deleted": deleted,
        "gold_lines": spec.get("gold_lines"),
        "asserts_removed": len(re.findall(r"^-\s*assert\b", test_diff, re.M)),
        "skips_added": len(re.findall(r"^\+.*(pytest\.mark\.skip|@skip|xfail)", diff_text, re.M)),
        "todos_added": len(re.findall(r"^\+.*\b(TODO|FIXME)\b", diff_text, re.M)),
        "debug_prints_added": len(re.findall(r"^\+\s*(print\(|console\.log\()", diff_text, re.M)),
    }
