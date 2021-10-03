# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""

import re
from pprint import pprint

def parse_sh_ip_int_br(filename):
    interface_list = []
    with open(filename) as f:
        for line in f:
            match = re.search(r'(?P<intf>\S+)\s+(?P<ip>\S+)\s+\S+\s+\S+\s+(?P<status>\S+|\S+\s+\S+)\s+(?P<protocol>up$|down$)', line)
            if match:
                interface_list.append(match.groups())
    return interface_list

if __name__ == "__main__":
    pprint(parse_sh_ip_int_br("sh_ip_int_br.txt"))
