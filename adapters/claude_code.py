import os

NAME = "claude-code"
PERMISSION_MODE = "bypass-permissions"
_FLAGS = ["--dangerously-skip-permissions", "--output-format", "text"]


def _model(model):
    return ["--model", model] if model else []


def argv(instruction, model, out_file):
    return ["claude", "-p", instruction, *_FLAGS, *_model(model)]


def continue_argv(reply, model, out_file):
    return ["claude", "-p", "--continue", reply, *_FLAGS, *_model(model)]


def env(iso_dir):
    # Auth lives in the config dir, so an empty dir is "not logged in". Point
    # ATLAS_CLAUDE_CONFIG_DIR at a copy of ~/.claude with CLAUDE.md, hooks, and
    # plugins removed; auth stays, the user's instructions do not.
    d = os.environ.get("ATLAS_CLAUDE_CONFIG_DIR")
    return {"CLAUDE_CONFIG_DIR": d} if d else {}


def version():
    return ["claude", "--version"]
