from gdou_dianfei import EBClient


def test_public_api_exports_client():
    assert EBClient.__name__ == "EBClient"
