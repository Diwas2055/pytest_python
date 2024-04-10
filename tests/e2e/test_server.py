# test_server.py

from hypothesis import given, strategies as st
from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


@given(st.integers())
def test_home(s):
    res = client.get(f"/api/{s}")

    assert res.status_code == 200
    assert res.json() == {"message": s * s}
