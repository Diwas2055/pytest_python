import requests
from src.monkeypatching import get_cat_fact


def test_cat_fact_no_monkeypatch():
    code, response = get_cat_fact()
    assert code == 200


def test_cat_fact_w_monkeypatch(monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = "www.testurl.com"

        def json(self):
            return {
                "data": ["Mother cats teach their " "kittens to use the litter box."]
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    assert get_cat_fact() == (
        200,
        {"data": ["Mother cats " "teach their kittens " "to use the litter box."]},
    )


# In this case, we define a class `MockResponse` and force it to return a JSON response, essentially simulating the Requests.GET method.
# We then define a function mock_get that returns an instance of `MockResponse`.
