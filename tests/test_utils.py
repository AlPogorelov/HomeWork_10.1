from unittest.mock import patch

from src.external_api import convert
from src.utils import open_json


@patch('requests.request')
def test_convert(mock_request):
    mock_request.return_value.json.return_value = 1
    assert convert('1', '1') == 1


def test_open_json():
    # Проверка на нормальную работу функции
    file_name = '../tests/test.json'
    expected = [{"id": 441945886,
                 "state": "EXECUTED"
                 },
                {"id": 41428829,
                 "state": "EXE"
                 }]
    assert open_json(file_name) == expected

    # Проверка на несуществуюший файл
    non_file_name = 'non_file.json'
    assert open_json(non_file_name) == []

    # Проверка на неверный формат json
    invalid_json_file = '../tests/test_invalid.json'
    with open(invalid_json_file, 'w', encoding='utf-8') as file:
        file.write("{'tyt':'neverni', 'format':'json'}")
    assert open_json(invalid_json_file) == []

    # Проверка на пустой файл
    empty_json_file = '../tests/test_empty.json'
    with open(empty_json_file, 'w', encoding='utf-8') as file:
        file.write("")
    assert open_json(invalid_json_file) == []
