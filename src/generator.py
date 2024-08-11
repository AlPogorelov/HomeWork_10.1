def filter_by_currency(transactions, currency):
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    result = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    return result


def transaction_descriptions(transactions):
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for x in transactions:
        yield x["description"]



def card_number_generator(start, stop):
    """Генератор выдает номера банкосвких карт в формате хххх хххх хххх хххх в диапозоне от до."""
    for i in range(start, stop):
        vid_account = 10000000000000000
        x_ = [(str(vid_account + i)[1:]) for i in range(start, stop + 1) if start != 0 and stop != 0]
        card_number = map(lambda i: " ".join([(i[z : z + 4]) for z in range(0, len(i), 4)]), x_)
        return card_number
