NAME = "codex"
PERMISSION_MODE = "bypass-approvals-and-sandbox"
_FLAGS = ["--dangerously-bypass-approvals-and-sandbox", "--skip-git-repo-check", "--ignore-user-config", "--ignore-rules"]


def _model(model):
    return ["-m", model] if model else []


def argv(instruction, model, out_file, cwd):
    # stdout is the event log; the final assistant message goes to out_file.
    return ["codex", "exec", *_FLAGS, *_model(model), "-o", out_file, instruction]


def continue_argv(reply, model, out_file, cwd):
    return ["codex", "exec", "resume", "--last", *_FLAGS, *_model(model), "-o", out_file, reply]


def env(iso_dir):
    return {}


def version():
    return ["codex", "--version"]
