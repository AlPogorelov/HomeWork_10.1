import os
from typing import Iterable, Union

import logging

current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

masks_logger = logging.getLogger('masks.py')
file_handler = logging.FileHandler(abs_file_path,'w', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s : %(message)s')
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)

def get_mask_card_number(card_number: Iterable[str]) -> str:
    """Функция принмает номер карты, возвращает её маску типа "ХХХХ ХХ** **** ХХХХ" """
    masks_logger.info(f'Начало работы функции.')
    card_number_str_ = str(card_number)
    card_number_str_set = card_number_str_.split()
    card_number_str = "".join(card_number_str_set)
    if card_number_str.isdigit() and len(card_number_str) == 16:
        card_number_split = [card_number_str[i : i + 6] for i in range(0, len(card_number_str), 6)]
        card_number_split[1] = "******"
        card_number_mask = "".join(card_number_split)
        card_number_mask_ = [card_number_mask[i : i + 4] for i in range(0, len(card_number_mask), 4)]
        mask_card = " ".join(card_number_mask_)
        masks_logger.info(f'Функция успешно завершена')
        return mask_card
    else:
        masks_logger.warning(f'Вводные данные не номер карты.')
        return ""


def get_mask_account(number_account: Union[int, str]) -> str:
    """Функция принмает номер счета и преобразует в маску с видом "**ХХХХ" """
    masks_logger.info(f'Начало работы функции.')
    number_account = str(number_account)
    if number_account.isdigit() and len(number_account) == 20:
        mask_account = f"**{number_account[-4:]}"
        masks_logger.info(f'Функция успешно завершена')
        return mask_account
    else:
        masks_logger.warning(f'Вводные данные не номер счета.')
        return ""


# if __name__ == '__main__':
#     get_mask_card_number('1596837868705199')
#     get_mask_account('1596837868705199')