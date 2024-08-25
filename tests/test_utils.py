from unittest.mock import patch
import requests

from src.external_api import convert


@patch('requests.request')
def test_convert(mock_request):
    mock_request.return_value.json.return_value = 1
    assert convert('1','1') == 1

