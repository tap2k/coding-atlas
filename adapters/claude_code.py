NAME = "claude-code"
PERMISSION_MODE = "bypass-permissions"


def argv(instruction: str, model: str | None) -> list[str]:
    cmd = ["claude", "-p", instruction, "--dangerously-skip-permissions", "--output-format", "text"]
    if model:
        cmd += ["--model", model]
    return cmd


def version() -> list[str]:
    return ["claude", "--version"]
