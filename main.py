from src.generator import filter_by_currency
from src.masks import get_mask_card_number
from src.open_CSV import open_csv
from src.open_xlsx import open_xlsx
from src.processing import filter_by_state, sort_by_date
from src.search import search_transaction
from src.utils import open_json
import os

from src.widget import mask_account_card, get_date

#Привесткие
print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')

#Выбор рабочего файла
print('''Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')

user_input = input()

def select_file(user_input):
    if user_input == '1':
        print('Для обработки выбран JSON-файл')
        file_name = 'data/operations.json'
        dict_oper = open_json(file_name)

        return dict_oper
    elif user_input == '2':
        print('Для обработки выбран CSV-файл')
        file_name = 'data/transaction.csv'
        dict_oper = open_csv(file_name)

        return dict_oper
    elif user_input == '3':
        print('Для обработки выбран XLSX-файл')
        file_name = 'data/transactions_excel.xlsx'
        dict_oper = open_xlsx(file_name)

        return dict_oper
    else:
        print('Вы указали неверный пункт меню')

dict_operations = select_file(user_input)


status_filter = input('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
''')
if status_filter.upper() in ['EXECUTED', 'CANCELED', 'PENDING']:
    status_filter = status_filter.upper()
    transaction_sort = filter_by_state(dict_operations, status_filter)

else:
    print(f'Статус операции "{status_filter}" недоступен.')
    status_filter = input('''Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    ''')

print('Отсорировать операции по дате? Да/Нет')
if input().lower() == 'да':
    if input('Отсортировать по возрастанию или по убыванию?').lower() == 'по возрастанию':
        data = False
        transaction_sort = sort_by_date(transaction_sort, data)
    else:
        data = True
        transaction_sort = sort_by_date(transaction_sort, data)


print("Выводить только рублевые транзакции? Да/Нет")
if input().lower() == 'да':
    transaction_sort = list(filter_by_currency(transaction_sort, 'RUB'))[:-1]

print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
if input().lower() == 'да':
    word_sort = input('Слово для сортировки')
    transaction_sort = search_transaction(transaction_sort, word_sort)

if len(transaction_sort) == 0:
    print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
else:
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковский операций в выборке:{len(transaction_sort)}')
    for i in transaction_sort:
        date = get_date(i['date'])
        if i['description'] == 'Открытие вклада':
            from_to = mask_account_card(i['to'])
        else:
            from_to = mask_account_card(i['from']) + '->' + mask_account_card(i['to'])

        print(f' {date} {i['description']} \n {from_to} \n '
              f'Сумма: {round(float(i['operationAmount']['amount']))} {i['operationAmount']['currency']['code']}')
