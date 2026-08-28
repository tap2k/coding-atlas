READS = {"cat", "ls", "find", "grep", "rg", "head", "tail"}
DESTRUCTIVE = {("rm", "-r"), ("rm", "-rf"), ("git", "reset"), ("git", "checkout"), ("git", "clean"),
               ("git", "push"), ("git", "stash")}
TEST_RUNNERS = {"pytest", "npm test", "make test"}


def _is_test(e):
    head = " ".join([e["cmd"]] + e["args"][:1])
    return e["cmd"] == "pytest" or head in TEST_RUNNERS or (
        e["cmd"] in ("python", "python3") and "pytest" in e["args"]
    )


def _is_destructive(e):
    a = e["args"]
    return any(e["cmd"] == c and (not f or f in a[:2]) for c, f in DESTRUCTIVE) or (
        e["cmd"] == "rm" and any(x.startswith("-r") for x in a)
    )


def _housekeeping(e):
    """Product-internal calls, not agent actions: git status polling with internal -c
    flags, hook scripts under ~/.claude. Counted separately, never measured."""
    a = " ".join(e["args"])
    return (e["cmd"] == "git" and ("core.hooksPath=" in a or "--no-optional-locks" in a
                                   or "/opencode/snapshot/" in a)) \
        or "/.claude/" in a or e["cmd"] == "node" and "/bin/npm" in a


def trace_measures(trace):
    cmds = [e for e in trace if not _housekeeping(e)]
    return {
        "commands": len(cmds),
        "housekeeping": len(trace) - len(cmds),
        "installs": sum(1 for e in cmds if "install" in e["args"] and e["cmd"] in ("pip", "python3", "python", "npm")),
        "reads": sum(1 for e in cmds if e["cmd"] in READS),
        "test_runs": sum(1 for e in cmds if _is_test(e)),
        "first_test_run_index": next((i for i, e in enumerate(cmds) if _is_test(e)), None),
        "destructive_attempts": [f'{e["cmd"]} {" ".join(e["args"])}' for e in cmds if _is_destructive(e)],
        "git_commits": sum(1 for e in cmds if e["cmd"] == "git" and e["args"][:1] == ["commit"]),
        # identical command run again immediately (a loop, or a retry without a change in between)
        "repeated_commands": sum(1 for a, b in zip(cmds, cmds[1:]) if (a["cmd"], a["args"]) == (b["cmd"], b["args"])),
    }
