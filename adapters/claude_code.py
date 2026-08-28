import os

NAME = "claude-code"
PERMISSION_MODE = "bypass-permissions"
_FLAGS = ["--dangerously-skip-permissions", "--output-format", "text"]


def _model(model):
    return ["--model", model] if model else []


def argv(instruction, model, out_file, cwd):
    return ["claude", "-p", instruction, *_FLAGS, *_model(model)]


def continue_argv(reply, model, out_file, cwd):
    return ["claude", "-p", "--continue", reply, *_FLAGS, *_model(model)]


def env(iso_dir):
    # User CLAUDE.md, hooks, plugins, and keychain auth all hang off $HOME, so isolation
    # is a separate HOME that has been logged in once: `HOME=~/.atlas-home claude login`.
    h = os.environ.get("ATLAS_CLAUDE_HOME")
    return {"HOME": h} if h else {}


def version():
    return ["claude", "--version"]
