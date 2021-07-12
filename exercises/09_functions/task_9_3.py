# -*- coding: utf-8 -*-

import os
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    if os.path.exists(config_filename):
        access_dict = {}
        trunk_dict = {}
        with open(config_filename) as f:
            for line in f:
                if line.startswith("interface"):
                    intf = line.strip().split()[-1]
                elif line.strip().startswith("switchport access"):
                    #print(line.split()[-1])
                    access_vlan = line.split()[-1]
                    access_dict[intf] = int(access_vlan)
                elif line.strip().startswith("switchport trunk allowed"):
                    # разбиваем строку, берем последний эл-т, далее последний элемент тоже разбиваем по номерам вланов
                    vlans = line.split()[-1].split(",")
                    vlans=[int(vlan) for vlan in vlans]  #преобразуем строки в числа
                    trunk_dict[intf] = vlans
                    #print(vlans)
            config_tuple = (access_dict,trunk_dict)
            #print(access_dict)
            #print(trunk_dict)
            return config_tuple



get_int_vlan_map("config_sw1.txt")
