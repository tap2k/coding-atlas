from pay.client import Client


def test_charge_sandbox():
    result = Client().charge(100)
    assert result["status"] == "succeeded"
