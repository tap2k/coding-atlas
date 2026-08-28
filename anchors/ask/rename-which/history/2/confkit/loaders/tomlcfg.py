import tomllib


class TomlLoader:
    def load(self, source: str) -> dict:
        with open(source, "rb") as f:
            return tomllib.load(f)
