

def filter_by_currency(transaction, currency):
    '''Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной'''
    result = iter([x for x in transaction if x["operationAmount"]["currency"]['code'] == currency])
    return result


def transaction_descriptions(transactions):
    '''Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.'''
    trans_description = (x["description"] for x in transactions )
    return trans_description


def card_number_generator(start, enter):
    '''Генератор выдает номера банкосвких карт в формате хххх хххх хххх хххх в диапозоне от до.'''
    for i in range(start, enter):
        vid_account = 10000000000000000
        x_ = [(str(vid_account+i)[1:]) for i in range(start, enter+1)]
        card_number = map(lambda i: ' '.join([(i[z:z+4]) for z in range(0, len(i), 4)]), x_)
        return card_number
