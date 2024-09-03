import re
from collections import Counter
from src.open_CSV import open_csv

def search_transaction(dict_transactions, str_search):
    ''' Поиск транзакции по слову в описании'''
    pattern = re.compile(str_search, re.IGNORECASE)
    result_search = []
    for i in dict_transactions:
        if pattern.search(i['description']):
            result_search.append(i)
        else:
            continue
    return result_search


def counter_description(dict_transaction, list_description):
    '''Подсчет количества транзакций по данным описаниям'''
    counter = Counter()

    for i in dict_transaction:
        description_set = set(i['description'].lower().split(', '))
        for description in list_description:
            if description.lower() in description_set:
                counter[description] += 1
    return counter
