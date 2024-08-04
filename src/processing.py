from typing import Iterable, Optional


def filter_by_state(list_of_dicts: Iterable[dict], state: Optional[str] = "EXECUTED") -> Iterable[dict]:
    """Функция отбирает из списка словарей словари по ключу, по умолчанию "EXECUTED" """
    list_of_dicts_state = []
    for i in list_of_dicts:
        if i["state"] == state:
            list_of_dicts_state.append(i)
    return list_of_dicts_state