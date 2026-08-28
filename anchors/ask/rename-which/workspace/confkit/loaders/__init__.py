from .yaml_loader import YamlLoader
from .json_loader import JsonLoader
from .tomlcfg import TomlLoader
from .env_loader import EnvironmentConfig

_BY_EXT = {".yaml": YamlLoader, ".yml": YamlLoader, ".json": JsonLoader, ".toml": TomlLoader}


def loader_for(source: str):
    if source.startswith("env:"):
        return EnvironmentConfig()
    for ext, cls in _BY_EXT.items():
        if source.endswith(ext):
            return cls()
    raise ValueError(f"no loader for {source!r}")


__all__ = ["YamlLoader", "JsonLoader", "TomlLoader", "EnvironmentConfig", "loader_for"]
