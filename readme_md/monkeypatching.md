# Monkeypatching

Monkeypatching is a term for mocking or patching a piece of code (class, function, module, variable or object) as part of a Unit Test.

It is a technique used to replace a piece of code with a mock, so that the code under test interacts with the mock instead of the real code.

In this tutorial, we will learn how to use monkeypatching in Pytest to replace a function with a mock, and then test the code under test to see if it interacts with the mock correctly.

## Example

Let's say we have a simple function that fetches data from a URL and returns the response:

```python
import requests

def fetch_data(url):
    response = requests.get(url)
    return response
```

We want to test this function, but we don't want to make an actual HTTP request in our test. Instead, we can use monkeypatching to replace the `requests.get` function with a mock that returns a fake response.

Here's how we can do that using Pytest:

```python

import requests

def fetch_data(url):
    response = requests.get(url)
    return response

def test_fetch_data(monkeypatch):

    def mock_get(url):
        class MockResponse:
            def __init__(self, text):
                self.text = text

        return MockResponse("Mocked Response")

    monkeypatch.setattr(requests, "get", mock_get)

    response = fetch_data("http://example.com")

    assert response.text == "Mocked Response"
```

In this example, we are using the `monkeypatch` fixture provided by Pytest to replace the `requests.get` function with a mock function called `mock_get`. The `mock_get` function returns a fake response object with a `text` attribute that contains the text "Mocked Response".

## References

- <https://pytest-with-eric.com/mocking/pytest-monkeypatch/>
- <https://docs.pytest.org/en/latest/monkeypatch.html>
