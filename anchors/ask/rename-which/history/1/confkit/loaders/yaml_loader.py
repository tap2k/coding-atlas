class YamlLoader:
    """Minimal YAML subset: `key: value` lines, strings and ints, no nesting."""

    def load(self, source: str) -> dict:
        out = {}
        with open(source) as f:
            for line in f:
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                k, _, v = line.partition(":")
                v = v.strip().strip('"').strip("'")
                out[k.strip()] = int(v) if v.lstrip("-").isdigit() else v
        return out
