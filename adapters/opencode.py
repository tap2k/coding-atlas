import json

"""OpenCode: the open harness row of the grid. --model is provider/model, and it must be
a dated snapshot, never an alias; the runner enforces that for every adapter."""
NAME = "opencode"
PERMISSION_MODE = "default-autoapprove"  # opencode run is non-interactive; tools auto-run
_FLAGS = ["--pure", "--format", "json"]


def _model(model):
    return ["-m", model] if model else []


def argv(instruction, model, out_file, cwd):
    # --dir is explicit: without it OpenCode has resolved the project from a stale session.
    return ["opencode", "run", "--dir", cwd, *_FLAGS, *_model(model), instruction]


def continue_argv(reply, model, out_file, cwd):
    return ["opencode", "run", "--dir", cwd, "--continue", *_FLAGS, *_model(model), reply]


def env(iso_dir):
    return {}


def version():
    return ["opencode", "--version"]


def parse_output(stdout, stderr, out_file_text):
    texts, model = [], None
    for line in stdout.splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        part = e.get("part", {})
        if e.get("type") == "text":
            texts.append(part.get("text", ""))
        model = model or part.get("modelID") or e.get("modelID")
    return "\n".join(texts), model
