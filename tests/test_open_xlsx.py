import pandas as pd
from unittest.mock import patch

from src.open_xlsx import open_xlsx

expected_data =[{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z'},
                {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z'}]

def test_open_xlsx():
    assert open_xlsx('../tests/test_xlsx.xlsx') == expected_data
    