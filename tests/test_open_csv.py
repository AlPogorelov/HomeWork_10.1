import pandas as pd
from unittest.mock import patch
from src.open_CSV import open_csv


def test_open_csv():
    expected_data = pd.DataFrame = ([{'Proveriaem': 'Tyt', 'Tyt_dannie': '1'},
                                     {'Proveriaem': 'Raznie', 'Tyt_dannie': '2'},
                                     {'Proveriaem': 'Imena', 'Tyt_dannie': '3'}])

    with patch('pandas.read_csv') as mocked_read_csv:
        mocked_read_csv.return_value = expected_data

        result = open_csv('../tests/test_CSV.csv')
        assert result == expected_data
