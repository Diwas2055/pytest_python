# Use Hypothesis,Schemathesis and Pytest for Robust Property-Based Testing in Python

## Introducton

`Pytest` is a Python testing framework. It was designed to make testing more efficient, reliable, and enjoyable. Pytest is built on top of the popular unittest testing module and adds many features and enhancements. With Pytest, you can run tests for individual files or directories, use plugins to customize your testing experience, and generate detailed . For more details on Pytest, check out the [Pytest Readme](readme_md/pytest_intro.md).

`Hypothesis` is a property-based testing library for Python. It lets you write tests that check the correctness of your code by specifying properties that your code should satisfy. Hypothesis then generates test data to check if those properties hold true. This can help you catch a wide range of edge cases and unexpected behaviour that may not be covered by example-based testing.

`Schemathesis` is a modern API testing tool based on the `OpenAPI` and `GraphQL` specifications. It uses Hypothesis under the hood to apply property-based testing to API schemas. In other words, given a schema, Schemathesis can automatically generate test cases for you. Since `FastAPI` is based on `OpenAPI` standards, Schemathesis works well with it.

## Objectives

By the end of this tutorial you should be able to:

- Understand the key differences between example-based, property-based and model-based testing
- Use the Hypothesis library with Pytest to test your code and ensure coverage for a wide range of test data
- Apply property-based testing to your Python apps
- Build a Shopping App and test it using property-based testing

## Example-Based Testing vs Property-Based Testing

`Example-based testing` and `property-based testing` are two common approaches to software testing along with model-based testing.

`Example-based testing` involves writing test cases that provide specific inputs and expected outputs for functions or methods.

- These tests are easy to write and understand, and they can catch many common errors.

`Property-based testing` involves testing properties or invariants that code should satisfy, and then automatically generating test data to check if those properties hold true.

- This approach can catch a much broader range of edge cases and unexpected behaviour that may not be covered by example-based testing.
