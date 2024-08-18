from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_dict, state):
    assert filter_by_state(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(list_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    assert filter_by_state(list_dict, state) == []


def test_sort_by_date(list_date):
    assert sort_by_date(list_date) == [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-10-14T08:21:33.419441"},
        {"date": "2018-09-12T21:27:25.241689"},
        {"date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(list_date, True) == [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-10-14T08:21:33.419441"},
        {"date": "2018-09-12T21:27:25.241689"},
        {"date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(list_date, False) == [
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2018-09-12T21:27:25.241689"},
        {"date": "2018-10-14T08:21:33.419441"},
        {"date": "2019-07-03T18:35:29.512364"},
    ]
