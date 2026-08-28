NAME = "gemini"
PERMISSION_MODE = "yolo"
_FLAGS = ["--yolo", "--skip-trust", "-o", "text"]


def _model(model):
    return ["-m", model] if model else []


def argv(instruction, model, out_file, cwd):
    return ["gemini", "-p", instruction, *_FLAGS, *_model(model)]


def continue_argv(reply, model, out_file, cwd):
    return ["gemini", "-p", reply, "--resume", "latest", *_FLAGS, *_model(model)]


def env(iso_dir):
    return {}


def version():
    return ["gemini", "--version"]
