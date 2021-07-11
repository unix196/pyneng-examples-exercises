# -*- coding: utf-8 -*-
import os
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
                elif line.strip().startswith("switchport mode access"):
                    access_vlan = 1
                    access_dict[intf] = access_vlan
                elif line.strip().startswith("switchport access"):
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

print(get_int_vlan_map("config_sw2.txt"))
