import pytest


@pytest.fixture
def account():
    return ["64686473678894779589", "35383033474447895560", "73654108430135874305"]


@pytest.fixture
def list_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def state():
    return ["EXECUTED", "CANCELED", "luboe slovo", "", 0, True, False]


@pytest.fixture
def list_date():
    return [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2018-09-12T21:27:25.241689"},
        {"date": "2018-10-14T08:21:33.419441"},
    ]
