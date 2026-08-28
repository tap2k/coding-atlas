from .loaders import loader_for


def load(source: str) -> dict:
    return loader_for(source).load(source)


__all__ = ["load", "loader_for"]
