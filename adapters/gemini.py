import json

NAME = "gemini"
PERMISSION_MODE = "yolo"
_FLAGS = ["--yolo", "--skip-trust", "-o", "json"]


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


def parse_output(stdout, stderr, out_file_text):
    try:
        d = json.loads(stdout)
    except json.JSONDecodeError:
        return stdout, None
    models = d.get("stats", {}).get("models", {})
    # the main model is the one that did the work; lite models act as routers
    main = max(models, key=lambda k: models[k].get("api", {}).get("totalRequests", 0)) if models else None
    return d.get("response", ""), main
