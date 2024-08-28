# Проект "Домашее задание к уроку 10.1"

## Описание:

Проект содержит пакет с модулями в которых реализованы функции отвечающие требованиям домашнего задания.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/AlPogorelov/HomeWork_10.1.git
```

## Реализованные функции:

* `get_mask_card_number` Функция принbмает номер карты, возвращает её маску типа "ХХХХ ХХ** **** ХХХХ".
* `get_mask_account` Функция принмает номер счета и преобразует в маску с видом "**ХХХХ".
* `mask_account_card` Функция принимает строку с номером карты или счета и  возвращает маску.
* `get_date` Функция ворматирует дата вид ДД.ММ.ГГГГ.
* `filter_by_state` Функция отбирает из списка словарей словари по ключу, по умолчанию "EXECUTED".
* `sort_by_date` Сортировка словарей по 'data', по умолчанию - убывание.
* `filter_by_currency` Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
* `transaction_descriptions` Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
* `card_number_generator` Генератор выдает номера банкосвких карт в формате хххх хххх хххх хххх в диапозоне от до.

## Реализованные декораторы:
* `log` Декоратор логирует начало фыполнения функции, её вывод или ошибку, и завершение выполнения функции.

## Реализовано логгирование слудеющих модулей:
* `masks.py` `utils.py` Реализованы логгирвоание начала функции, удачного завершения функции и лог ошибки функции.


## Тестирование:
Реализованны тестовы для проверки функции модулей `masks.py`, `processing.py`, `widget.py`.
Проведены основыне проверки на "пустой" аргумент, правильности преобразования выходного аргумента.
Добавлены тесты для проверки модуля `generator.py`
Проверен декоратор `log` сохраняет и выводит в консоль необходимые логи.
## Документация:

_-_

## Лицензия:

_-_