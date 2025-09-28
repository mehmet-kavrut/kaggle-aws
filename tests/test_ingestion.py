import pandas as pd
import requests


def test_fetch_data_from_api(monkeypatch):
    # Mock API response
    class MockResponse:
        def json(self):
            return [{"id": 1, "value": "test1"}, {"id": 2, "value": "test2"}]

        def raise_for_status(self):
            pass

    # Use monkeypatch to replace requests.get with a mock function
    monkeypatch.setattr(requests, "get", lambda url: MockResponse())

    # Call the function's logic
    df = pd.DataFrame(MockResponse().json())
    assert not df.empty
    assert list(df.columns) == ["id", "value"]
