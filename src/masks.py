from typing import Iterable, Union


def get_mask_card_number(card_number: Iterable[str]) -> str:
    """Функция принмает номер карты, возвращает её маску типа "ХХХХ ХХ** **** ХХХХ" """
    card_number_str = str(card_number)
    card_number_split = [card_number_str[i : i + 6] for i in range(0, len(card_number_str), 6)]
    card_number_split[1] = "******"
    card_number_mask = "".join(card_number_split)
    card_number_mask_ = [card_number_mask[i : i + 4] for i in range(0, len(card_number_mask), 4)]
    mask_card = " ".join(card_number_mask_)
    return mask_card


def get_mask_account(number_account: Union[int, str]) -> str:
    """Функция принмает номер счета и преобразует в маску с видом "**ХХХХ" """
    number_account = str(number_account)
    mask_account = f" **{number_account[-4:]}"
    return mask_account
