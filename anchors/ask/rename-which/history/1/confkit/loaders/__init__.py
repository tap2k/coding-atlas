from .yaml_loader import YamlLoader
from .json_loader import JsonLoader

_BY_EXT = {".yaml": YamlLoader, ".yml": YamlLoader, ".json": JsonLoader}


def loader_for(source: str):
    for ext, cls in _BY_EXT.items():
        if source.endswith(ext):
            return cls()
    raise ValueError(f"no loader for {source!r}")


__all__ = ["YamlLoader", "JsonLoader", "loader_for"]
