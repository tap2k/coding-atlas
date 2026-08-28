import json


class JsonLoader:
    def load(self, source: str) -> dict:
        with open(source) as f:
            return json.load(f)
