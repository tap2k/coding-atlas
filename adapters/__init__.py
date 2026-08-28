"""Adapters do invocation only: how to run a product headless in a directory with an
instruction and a model. Contract (all optional except argv/version):

  NAME, PERMISSION_MODE
  argv(instruction, model, out_file, cwd) -> list[str]    # out_file: where to write the final
                                                     # message if the product cannot use stdout
  continue_argv(reply, model, out_file, cwd) -> list[str] # second turn, same session
  env(iso_dir) -> dict                               # extra env; iso_dir is a clean per-run
                                                     # config dir for products that honor one
  version() -> list[str]
"""
import importlib


def load(name: str):
    return importlib.import_module(f"adapters.{name.replace('-', '_')}")
