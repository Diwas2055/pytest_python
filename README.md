# Use Hypothesis,Schemathesis,Mock,MonkeyPatching and Pytest for Robust Property-Based Testing in Python

## Introducton

`Pytest` is a Python testing framework. It was designed to make testing more efficient, reliable, and enjoyable. Pytest is built on top of the popular unittest testing module and adds many features and enhancements. With Pytest, you can run tests for individual files or directories, use plugins to customize your testing experience, and generate detailed . For more details on Pytest, check out the [Pytest Readme](readme_md/pytest_intro.md).

`Hypothesis` is a property-based testing library for Python. It lets you write tests that check the correctness of your code by specifying properties that your code should satisfy. Hypothesis then generates test data to check if those properties hold true. This can help you catch a wide range of edge cases and unexpected behaviour that may not be covered by example-based testing.

`Schemathesis` is a modern API testing tool based on the `OpenAPI` and `GraphQL` specifications. It uses Hypothesis under the hood to apply property-based testing to API schemas. In other words, given a schema, Schemathesis can automatically generate test cases for you. Since `FastAPI` is based on `OpenAPI` standards, Schemathesis works well with it.

In unit testing, a code block that you want to test may depend on other code. When we unit test, we test only a code block without those dependencies. To isolate the behavior of the code you need to test, you need to replace the other code with mocks that simulate the behavior of the real code. So, `mocking` is using mocks that simulate real code behavior.

`pytest-mock` is a plugin for Pytest that provides a simple way to create and use mocks in your tests. It allows you to replace dependencies with mocks, and then check if the code under test interacts with those dependencies correctly.

`Monkeypatching` is a term for mocking or patching a piece of code (class, function, module, variable or object) as part of a Unit Test. It is a technique used to replace a piece of code with a mock, so that the code under test interacts with the mock instead of the real code

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

## Note

> Is MonkeyPatch The Same As Mocking or Patching? Yes and No ;)

    The two are very similar and have subtle differences.

    `Monkeypatching` is the act of replacing a function, method, class or variable at runtime.

    `Mock` actually uses Monkeypatch under the hood to mock or change certain objects being evaluated at run time as part of your test.

    The exact differences are not really important, what’s more important is that you understand that it’s possible to override functions, classes, libraries and variables in Unit Tests.

## References

- <https://stackoverflow.com/questions/41701226/what-is-the-difference-between-mocking-and-monkey-patching>
