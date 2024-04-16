from hypothesis import settings
import schemathesis

# schema = schemathesis.from_uri("http://localhost:8000/openapi.json")


# # @schema.parametrize()
# # @settings(max_examples=10)
# # def test_api(case):
# #     response = case.call()
# #     case.validate_response(response)


# @schema.parametrize(method="GET", endpoint="/api/{s}")
# @settings(max_examples=5)
# def test_home(case):
#     response = case.call()
#     case.validate_response(response)


# @schema.parametrize(method="POST", endpoint="/api/echo")
# @settings(max_examples=5)
# def test_echo(case):
#     response = case.call()
#     case.validate_response(response)


def test_ech0():
    assert 20 == 20
