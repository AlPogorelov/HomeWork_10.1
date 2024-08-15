def filter_by_currency(transactions, currency):
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    result = list([x for x in transactions if x["operationAmount"]["currency"]["code"] == currency])
    for j in result:
        yield j


def transaction_descriptions(transactions):
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for x in transactions:
        yield x["description"]


def card_number_generator(start, stop):
    """Генератор выдает номера банкосвких карт в формате хххх хххх хххх хххх в диапозоне от до."""
    for i in range(start, stop + 1):
        vid_account = 10000000000000000
        delv = str(vid_account + i)[1:]
        delv_ = " ".join([(delv[z : z + 4]) for z in range(0, len(delv), 4)])
        yield delv_
