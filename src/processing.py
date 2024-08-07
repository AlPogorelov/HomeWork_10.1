from typing import Iterable, Optional


def filter_by_state(list_of_dicts: Iterable[dict], state: Optional[str] = "EXECUTED") -> Iterable[dict]:
    """Функция отбирает из списка словарей словари по ключу, по умолчанию "EXECUTED" """
    list_of_dicts_state = list()
    for i in list_of_dicts:
        if i.get("state") == state:
            list_of_dicts_state.append(i)
    return list_of_dicts_state


def sort_by_date(list_of_dicts: Iterable[dict], date: Optional[bool] = True) -> Iterable[dict]:
    """Сортировка словарей по 'data', по умолчанию - убывание"""
    if date:
        sorted_list_of_dicts = sorted(list_of_dicts, key=lambda data: data["date"], reverse=True)
    else:
        sorted_list_of_dicts = sorted(list_of_dicts, key=lambda data: data["date"])
    return sorted_list_of_dicts


if __name__ == '__main__':
    print(sort_by_date([
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2018-09-12T21:27:25.241689"},
        {"date": "2018-10-14T08:21:33.419441"},
    ], False))