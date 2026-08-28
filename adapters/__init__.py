"""Adapters do invocation only: how to run a product headless in a directory with an
instruction and a model. Contract:

  NAME, PERMISSION_MODE
  argv(instruction, model, out_file, cwd) -> list[str]
  continue_argv(reply, model, out_file, cwd) -> list[str]   # second turn, same session
  env(iso_dir) -> dict                                       # extra env for the run
  parse_output(stdout, stderr, out_file_text) -> (message, served_model)
      # message: the agent's final text to the user; served_model: what the product says
      # it used, or None. Both from the product's machine-readable output; nothing else
      # is read from it.
  hide_user_files() -> restore_fn                            # optional
  version() -> list[str]
"""
import importlib


def load(name: str):
    return importlib.import_module(f"adapters.{name.replace('-', '_')}")
