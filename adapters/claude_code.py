import json
import os

NAME = "claude-code"
PERMISSION_MODE = "bypass-permissions"
_FLAGS = ["--dangerously-skip-permissions", "--output-format", "json"]


def _model(model):
    return ["--model", model] if model else []


def argv(instruction, model, out_file, cwd):
    return ["claude", "-p", instruction, *_FLAGS, *_model(model)]


def continue_argv(reply, model, out_file, cwd):
    return ["claude", "-p", "--continue", reply, *_FLAGS, *_model(model)]


def hide_user_files():
    """Claude Code reads ~/.claude/CLAUDE.md from the real home regardless of HOME or
    CLAUDE_CONFIG_DIR, and --bare (which skips it) refuses OAuth. So move it aside for the
    duration of a run. Returns a restore function. Sessions already running keep their copy."""
    real = os.path.join(os.path.expanduser(f"~{os.environ.get('USER','')}"), ".claude", "CLAUDE.md")
    hidden = real + ".atlas-hidden"
    if not os.path.exists(real):
        return lambda: None
    os.rename(real, hidden)
    return lambda: os.path.exists(hidden) and os.rename(hidden, real)


def env(iso_dir):
    # User CLAUDE.md, hooks, plugins, and keychain auth all hang off $HOME, so isolation
    # is a separate HOME that has been logged in once: `HOME=~/.atlas-home claude login`.
    h = os.environ.get("ATLAS_CLAUDE_HOME")
    return {"HOME": h} if h else {}


def version():
    return ["claude", "--version"]


def parse_output(stdout, stderr, out_file_text):
    try:
        d = json.loads(stdout)
    except json.JSONDecodeError:
        return stdout, None
    models = [m for m in d.get("modelUsage", {}) if "haiku" not in m] or list(d.get("modelUsage", {}))
    return d.get("result", ""), (models[0] if models else None)
