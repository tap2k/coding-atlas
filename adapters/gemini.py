import json

NAME = "gemini"
PERMISSION_MODE = "yolo"
_FLAGS = ["--yolo", "--skip-trust", "-o", "json"]


def _model(model):
    return ["-m", model] if model else []


def argv(instruction, model, out_file, cwd, mode=None):
    return ["gemini", "-p", instruction, *_FLAGS, *_model(model)]


def continue_argv(reply, model, out_file, cwd, mode=None):
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
    tk = [m.get("tokens", {}) for m in models.values()]
    meter = {"input_tokens": sum(x.get("prompt", 0) for x in tk), "output_tokens": sum(x.get("candidates", 0) for x in tk),
             "cache_read_tokens": sum(x.get("cached", 0) for x in tk), "thinking_tokens": sum(x.get("thoughts", 0) for x in tk),
             "api_turns": sum(m.get("api", {}).get("totalRequests", 0) for m in models.values())}
    return d.get("response", ""), main, meter
