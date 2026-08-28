NAME = "claude-code"
PERMISSION_MODE = "bypass-permissions"
_FLAGS = ["--dangerously-skip-permissions", "--output-format", "text"]


def argv(instruction: str, model: str | None) -> list[str]:
    return ["claude", "-p", instruction, *_FLAGS, *(["--model", model] if model else [])]


def continue_argv(reply: str, model: str | None) -> list[str]:
    """Second turn in the same session with the anchor's frozen reply."""
    return ["claude", "-p", "--continue", reply, *_FLAGS, *(["--model", model] if model else [])]


def version() -> list[str]:
    return ["claude", "--version"]
