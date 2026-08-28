import os


class EnvironmentConfig:
    """Reads `PREFIX*` variables; `env:APP_` gives {"port": "8080"} for APP_PORT=8080."""

    def load(self, source: str) -> dict:
        prefix = source.removeprefix("env:")
        return {k.removeprefix(prefix).lower(): v for k, v in os.environ.items() if k.startswith(prefix)}
