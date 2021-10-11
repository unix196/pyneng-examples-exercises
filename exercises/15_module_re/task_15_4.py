# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re
from pprint import pprint

def get_ints_without_description(filename):
    #list_int_without_desc = []
    #with open(filename) as f:
    # first varian
    #    line = f.readline()
    #    while line:
    #        line = f.readline()
    #        if line.startswith("interface"):
    #            line_tmp = f.readline() # читаем следующую строчку, если нашли совпадение
    #            if not line_tmp.startswith(" description"):
    #                interface = line.split()[1]
    #                list_int_without_desc.append(interface)
    #return list_int_without_desc



if __name__ == "__main__":
    pprint(get_ints_without_description("config_r1.txt"))
