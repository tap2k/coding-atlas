# confkit

Load application config from YAML, JSON, TOML, or environment variables.

    from confkit import load
    cfg = load("settings.toml")     # picks a loader by extension
    cfg = load("env:APP_")          # environment variables with a prefix

Loaders live in `confkit/loaders/`, one module per format, each exposing a `*Loader`
class with a `load(source) -> dict` method.
