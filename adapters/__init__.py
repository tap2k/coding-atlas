"""Adapters do invocation only: how to run a product headless in a directory with an
instruction and a model. They return argv. Nothing else."""
import importlib


def load(name: str):
    return importlib.import_module(f"adapters.{name.replace('-', '_')}")
