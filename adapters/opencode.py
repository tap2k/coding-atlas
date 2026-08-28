"""OpenCode: the open harness row of the grid. --model is provider/model, and it must be
a dated snapshot, never an alias; the runner enforces that for every adapter."""
NAME = "opencode"
PERMISSION_MODE = "default-autoapprove"  # opencode run is non-interactive; tools auto-run
_FLAGS = ["--pure", "--format", "default"]


def _model(model):
    return ["-m", model] if model else []


def argv(instruction, model, out_file):
    return ["opencode", "run", *_FLAGS, *_model(model), instruction]


def continue_argv(reply, model, out_file):
    return ["opencode", "run", "--continue", *_FLAGS, *_model(model), reply]


def env(iso_dir):
    return {}


def version():
    return ["opencode", "--version"]
