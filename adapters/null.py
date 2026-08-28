"""Control: does nothing. Exercises the runner end to end."""
NAME = "null"
PERMISSION_MODE = "n/a"


def argv(instruction, model):
    return ["sh", "-c", "ls >/dev/null; python3 -m pytest -q >/dev/null 2>&1; echo 'Could not fix it. Is that ok?'"]


def version():
    return ["true"]


def continue_argv(reply, model):
    return ["sh", "-c", "echo 'OK, renamed nothing. Done.'"]
