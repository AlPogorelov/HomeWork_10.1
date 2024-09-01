import json
import logging
import os

from src.external_api import convert

current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

utils_logger = logging.getLogger("utils.py")
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def open_json(name_file_json):
    """Десериализация полученного json файла в Python файл"""
    utils_logger.info("Функция начала работу")
    try:
        with open(name_file_json, encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                utils_logger.error("Невозможно декодировать json-данные")
                data = []
            except ValueError:
                utils_logger.error("Значение json-данных не корректно")
                data = []
            except TypeError:
                utils_logger.error("JSON-данные не поддерживается операцией сериализации")
                data = []
        utils_logger.info("Функция успешно завершена")
        return data
    except FileNotFoundError:
        utils_logger.error("Данного json-файла не существует")
        data = []
    return data


def sum_convert_amount(data):
    """Сумма транзакций в рублях, запрашивая по API курс валют"""
    utils_logger.info("Функция начала работу")
    usd = convert("RUB", "USD")
    eur = convert("RUB", "EUR")
    sum_amount = 0

    for i in data:
        if i == {}:
            utils_logger.warning("В списке есть пустой словарь")
            continue
        else:
            if i["operationAmount"]["currency"]["code"] == "RUB":
                sum_amount += float(i["operationAmount"]["amount"])
            elif i["operationAmount"]["currency"]["code"] == "USD":
                sum_amount += float(i["operationAmount"]["amount"]) * usd
            elif i["operationAmount"]["currency"]["code"] == "EUR":
                sum_amount += float(i["operationAmount"]["amount"]) * eur
    utils_logger.info("Функция успешно завершена")
    return sum_amount
