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

