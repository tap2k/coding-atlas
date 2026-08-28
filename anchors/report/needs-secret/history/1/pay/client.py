import json
import os
import urllib.request


class Client:
    BASE = "https://sandbox.payments.example.com/v1"

    def __init__(self):
        self.key = os.environ["PAYMENTS_API_KEY"]

    def charge(self, cents: int, currency: str = "usd") -> dict:
        req = urllib.request.Request(
            f"{self.BASE}/charges", data=json.dumps({"amount": cents, "currency": currency}).encode(),
            headers={"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.load(r)
