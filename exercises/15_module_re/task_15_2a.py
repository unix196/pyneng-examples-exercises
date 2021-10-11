# -*- coding: utf-8 -*-
"""
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей,
где ключи - взяты из первого списка, а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('R1', '12.4(24)T1', 'Cisco 3825'),
 ('R2', '15.2(2)T1', 'Cisco 2911')]

Функция должна вернуть такой список со словарями:
[{'hostname': 'R1', 'ios': '12.4(24)T1', 'platform': 'Cisco 3825'},
 {'hostname': 'R2', 'ios': '15.2(2)T1', 'platform': 'Cisco 2911'}]

Функция не должна быть привязана к конкретным данным или количеству
заголовков/данных в кортежах.

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - список data

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import re
from pprint import pprint

headers = ["hostname", "ios", "platform"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]


def convert_to_dict(list_fields,list_tuple):
    hardware = []
    for data in list_tuple:
        list_dicts = {}
        for i in range(len(headers)):
            list_dicts[list_fields[i]] = data[i]
        hardware.append(list_dicts)
    return hardware




if __name__ == "__main__":
    pprint(convert_to_dict(headers,data))
