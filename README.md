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
* `mask_account_card` СФункция принимает строку с номером карты или счета и  возвращает маску.
* `get_date` Функция ворматирует дата вид ДД.ММ.ГГГГ.
* `filter_by_state` Функция отбирает из списка словарей словари по ключу, по умолчанию "EXECUTED".
* `sort_by_date` Сортировка словарей по 'data', по умолчанию - убывание.

## Тестирование:
Реализованны тестовы для проверки функции модулей `masks.py`, `processing.py`, `widget.py`.
Проведены основыне проверки на "пустой" аргумент, правильности преобразования выходного аргумента.
## Документация:

_-_

## Лицензия:

_-_