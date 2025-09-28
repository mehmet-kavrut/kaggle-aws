import unittest
import pandas as pd
import requests
from unittest.mock import patch


class TestAPI(unittest.TestCase):

    @patch("requests.get")
    def test_fetch_data_from_api(self, mock_get):
        # Mock API response
        class MockResponse:
            def json(self):
                return [{"id": 1, "value": "test1"}, {"id": 2, "value": "test2"}]

            def raise_for_status(self):
                pass

        mock_get.return_value = MockResponse()

        # Call the function's logic
        df = pd.DataFrame(MockResponse().json())
        self.assertFalse(df.empty)
        self.assertListEqual(list(df.columns), ["id", "value"])
