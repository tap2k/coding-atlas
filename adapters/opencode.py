import json

"""OpenCode: the open harness row of the grid. --model is provider/model, and it must be
a dated snapshot, never an alias; the runner enforces that for every adapter."""
NAME = "opencode"
PERMISSION_MODE = "default-autoapprove"  # opencode run is non-interactive; tools auto-run
_FLAGS = ["--pure", "--format", "json"]


def _model(model):
    return ["-m", model] if model else []


def argv(instruction, model, out_file, cwd, mode=None):
    # --dir is explicit: without it OpenCode has resolved the project from a stale session.
    return ["opencode", "run", "--dir", cwd, *_FLAGS, *_model(model), instruction]


def continue_argv(reply, model, out_file, cwd, mode=None):
    return ["opencode", "run", "--dir", cwd, "--continue", *_FLAGS, *_model(model), reply]


def env(iso_dir):
    return {}


def version():
    return ["opencode", "--version"]


def parse_output(stdout, stderr, out_file_text):
    texts, model, meter = [], None, {"input_tokens": 0, "output_tokens": 0, "cache_read_tokens": 0, "cost_usd": 0.0, "api_turns": 0, "tool_errors": 0}
    for line in stdout.splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        part = e.get("part", {})
        if e.get("type") == "text":
            texts.append(part.get("text", ""))
        if e.get("type") == "step_finish":
            tk = part.get("tokens", {})
            meter["input_tokens"] += tk.get("input", 0); meter["output_tokens"] += tk.get("output", 0)
            meter["cache_read_tokens"] += tk.get("cache", {}).get("read", 0); meter["cost_usd"] += part.get("cost", 0) or 0
            meter["api_turns"] += 1
        if e.get("type") == "tool_use" and part.get("state", {}).get("status") == "error":
            meter["tool_errors"] += 1
        model = model or part.get("modelID") or e.get("modelID")
    return "\n".join(texts), model, meter
