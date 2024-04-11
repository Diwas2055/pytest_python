# Mocking

Mocking is a technique used to isolate a piece of code being tested from its dependencies so that the test can focus on the code under test in isolation.

This is achieved by replacing the dependencies with mock objects that simulate the behaviour of the real objects.

Mock objects are typically pre-programmed with specific responses to method calls that the code under test is expected to make.

This allows the test to verify that the code under the test behaves correctly under different circumstances.

Mocking is a valuable technique in unit testing because it helps to isolate bugs, and improve test coverage.

It also allows you to test code that is not yet fully implemented or that depends on components that are not yet available.

Some popular mocking frameworks include Mockito for Java, unittest.mock and pytest-mockfor Python, and Moq for .NET.

## References

- <https://pytest-mock.readthedocs.io/en/latest/>
- <https://docs.python.org/3/library/unittest.mock.html>
- <https://pytest-with-eric.com/mocking/pytest-mocking/>
