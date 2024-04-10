# Schemathesis

Schemathesis is a modern API testing tool based on the OpenAPI and GraphQL specifications. It uses Hypothesis under the hood to apply property-based testing to API schemas. In other words, given a schema, Schemathesis can automatically generate test cases for you. Since FastAPI is based on OpenAPI standards, Schemathesis works well with it.

Schemathesis is a tool that automates API testing by leveraging API specs as a blueprints for generating test cases. It focuses on testing for general properties — such as ensuring no input leads to server errors and all responses adhere to the API spec — rather than just checking specific input-output combinations.

This approach broadens your testing suite’s capability to detect a wide range of potential issues, from trivial bugs to critical vulnerabilities.

The simplest way to run tests is via the `schemathesis command`. With Uvicorn running in one terminal window, open a new window and run:

```bash
schemathesis run http://localhost:8000/openapi.json
```

You should see:

```bash
========================= Schemathesis test session starts ========================
Schema location: http://localhost:8000/openapi.json
Base URL: http://localhost:8000/
Specification version: Open API 3.0.2
Workers: 1
Collected API operations: 1

GET /api/{s} .                                                               [100%]

===================================== SUMMARY =====================================

Performed checks:
    not_a_server_error                    100 / 100 passed          PASSED

================================ 1 passed in 0.61s ================================
```

Notice how this only checked for `not_a_server_error`. Schemathesis has five built-in checks:

- `not_a_server_error`: response has 5xx HTTP status
- `status_code_conformance`: response status is not defined in the API schema
- `content_type_conformance`: response content type is not defined in the API schema
- `response_schema_conformance`: response content does not conform to the schema defined for this specific response
- `response_headers_conformance`: response headers does not contain all defined headers.

You can perform all built-in checks with the --checks all option:

```bash
schemathesis run --checks all http://localhost:8000/openapi.json

## or 

st run --checks all http://localhost:8000/openapi.json

```

```bash
========================= Schemathesis test session starts ========================
Schema location: http://localhost:8000/openapi.json
Base URL: http://localhost:8000/
Specification version: Open API 3.0.2
Workers: 1
Collected API operations: 1

GET /api/{s} .                                                               [100%]

===================================== SUMMARY =====================================

Performed checks:
    not_a_server_error                              100 / 100 passed          PASSED
    status_code_conformance                         100 / 100 passed          PASSED
    content_type_conformance                        100 / 100 passed          PASSED
    response_headers_conformance                    100 / 100 passed          PASSED
    response_schema_conformance                     100 / 100 passed          PASSED

================================ 1 passed in 0.87s ================================
```

## Additional Options

You can test a `specific endpoint` or `HTTP method` rather than the whole application:

```bash
schemathesis run --endpoint /api/. <http://localhost:8000/openapi.json>

schemathesis run --method GET <http://localhost:8000/openapi.json>
```

A `max response` time can be used to help flesh out edge cases that may slow down the endpoints. The time is in milliseconds.

```bash
schemathesis run --max-response-time=50 <HTTP://localhost:8000/openapi.json>
```

## Do some of your endpoints require authorization?

```bash
schemathesis run -H "Authorization: Bearer TOKEN" <http://localhost:8000/openapi.json>

schemathesis run -H "Authorization: ..." -H "X-API-Key: ..." <HTTP://localhost:8000/openapi.json>
```

## You can use multiple workers to speed up the tests

```bash
schemathesis run --workers 8 http://localhost:8000/openapi.json
```

Normally, Schemathesis generates random data for each endpoint. Stateful tests make sure that the data comes from previous tests/responses:

```bash
schemathesis run --stateful=links http://localhost:8000/openapi.json
```

Finally, replaying tests is simple since each test case is associated with a seed value. When a test case fails, it'll provide the seed so that the you can reproduce the failed case:

```bash
schemathesis run <http://localhost:8000/openapi.json>
```

```bash
============================ Schemathesis test session starts ============================
platform Darwin -- Python 3.10.6, schemathesis-3.17.2, hypothesis-6.54.4,
    hypothesis_jsonschema-0.22.0, jsonschema-4.15.0
rootdir: /hypothesis-examples
hypothesis profile 'default' ->
    database=DirectoryBasedExampleDatabase('/hypothesis-examples/.hypothesis/examples')
Schema location: <http://localhost:8000/openapi.json>
Base URL: <http://localhost:8000/>
Specification version: Open API 3.0.2
Workers: 1
collected endpoints: 1

GET /api/{s} F                                                                      [100%]

======================================== FAILURES ========================================
_____________________________________ GET: /api/{s} ______________________________________

1. Received a response with 5xx status code: 500

Path parameters : {'s': 0}

Run this Python code to reproduce this failure:
  requests.get('<http://localhost:8000/api/0>', headers={'User-Agent': 'schemathesis/2.6.0'})

Or add this option to your command line parameters:
    --hypothesis-seed=135947773389980684299156880789978283847
======================================== SUMMARY =========================================

Performed checks:
    not_a_server_error                    0 / 3 passed          FAILED

=================================== 1 passed in 0.10s ====================================
```

Then, to reproduce, run:

```bash
schemathesis run <http://localhost:8000/openapi.json> --hypothesis-seed=135947773389980684299156880789978283847
```

## Python Tests

You can use Schemathesis inside your tests as well:

```python
import schemathesis

schema = schemathesis.from_uri("http://localhost:8000/openapi.json")


@schema.parametrize()
def test_api(case):
    case.call_and_validate()
```

Schemathesis also supports making calls directly to `ASGI` (i.e.,Uvicorn and Daphne) and `WSGI` (i.e., Gunicorn and uWSGI) applications instead of over the network:

```python
import schemathesis
from schemathesis.specs.openapi.loaders import from_asgi

from server import app

schema = from_asgi("/openapi.json", app)

@schema.parametrize()
def test_api(case):
    response = case.call_asgi()
    case.validate_response(response)
```

## References

- [Schemathesis Documentation](https://schemathesis.readthedocs.io/en/stable/getting-started.html)
- [Writing Python tests](https://schemathesis.readthedocs.io/en/stable/python.html)
- [Schemathesis GitHub](https://github.com/schemathesis/schemathesis)
- [Command Line Interface](https://schemathesis.readthedocs.io/en/stable/cli.html)
