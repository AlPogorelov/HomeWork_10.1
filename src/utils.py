import json

from src.external_api import convert


def open_json(name_file_json):
    """Десериализация полученного json файла в Python файл"""
    with open(name_file_json, encoding="utf-8") as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            data = {}
        except ValueError:
            data = {}
        except data == {}:
            data = {}
    return data


def sum_convert_amount(data):
    """Сумма транзакций в рублях, запрашивая по API курс валют"""
    usd = convert("RUB", "USD")
    eur = convert("RUB", "EUR")
    sum_amount = 0

    for i in data:
        if i == {}:
            continue
        else:
            if i["operationAmount"]["currency"]["code"] == "RUB":
                sum_amount += float(i["operationAmount"]["amount"])
            elif i["operationAmount"]["currency"]["code"] == "USD":
                sum_amount += float(i["operationAmount"]["amount"]) * usd
            elif i["operationAmount"]["currency"]["code"] == "EUR":
                sum_amount += float(i["operationAmount"]["amount"]) * eur
    return sum_amount
