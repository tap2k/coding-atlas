"""Run your own agent against the battery. Set ATLAS_CMD to the command that invokes
your agent in the current directory; {instruction} is replaced with the anchor's
instruction. Optionally set ATLAS_CONTINUE_CMD for the second turn ({reply}).

  ATLAS_CMD='my-agent run "{instruction}"' ./run --anchor comply/csv-green --product custom
"""
import os
import shlex

NAME = "custom"
PERMISSION_MODE = os.environ.get("ATLAS_CUSTOM_MODE", "unspecified")


def argv(instruction, model, out_file, cwd, mode=None):
    return shlex.split(os.environ["ATLAS_CMD"].replace("{instruction}", instruction))


def continue_argv(reply, model, out_file, cwd, mode=None):
    cmd = os.environ.get("ATLAS_CONTINUE_CMD", os.environ["ATLAS_CMD"])
    return shlex.split(cmd.replace("{instruction}", reply).replace("{reply}", reply))


def env(iso_dir):
    return {}


def parse_output(stdout, stderr, out_file_text):
    return (out_file_text if out_file_text is not None else stdout), os.environ.get("ATLAS_CUSTOM_MODEL"), {}


def version():
    return ["sh", "-c", "echo ${ATLAS_CUSTOM_VERSION:-unversioned}"]
