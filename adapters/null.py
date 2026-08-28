"""Control: does nothing. Exercises the runner end to end, including the second turn."""
NAME = "null"
PERMISSION_MODE = "n/a"


def argv(instruction, model, out_file):
    return ["sh", "-c", "ls >/dev/null; python3 -m pytest -q >/dev/null 2>&1; echo 'Could not fix it. Is that ok?'"]


def continue_argv(reply, model, out_file):
    return ["sh", "-c", "echo 'OK, renamed nothing. Done.'"]


def env(iso_dir):
    return {}


def version():
    return ["true"]
