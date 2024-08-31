import csv


def open_csv(file_name):
    '''Функция открывает csv файл и преобразует его в список словарей'''
    dict_csv = []
    with open(file_name, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            dict_csv.append(row)
        return dict_csv
