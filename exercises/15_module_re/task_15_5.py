# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""

import re
from pprint import pprint

def generate_description_from_cdp(filename):
    description_template = 'description Connected to {} port {}'
    neighbors_dict = {}
    with open(filename) as f:
        for line in f:
            #match_device = re.search(r'(\S+)>.*',line)
            #if match_device:
            #    device = match_device.groups()
            match = re.search(r'(?P<remote_device>\S+)\s+(?P<local>\S+ \d/\d).*\s+(?P<remote>\S+ \d/\d)', line)
            if match:
                remote_device, local_int, remote_int = match.group("remote_device"), match.group("local"), match.group("remote")
                #print(remote_device, local_int, remote_int)
                #print(match.groupdict())
                #print(match.group("device"))

                neighbors_dict[local_int] =  description_template.format(remote_device, remote_int)
                #return description_template.format(local_int, remote_int)
        return neighbors_dict


if __name__ == "__main__":
    pprint(generate_description_from_cdp("sh_cdp_n_sw1.txt"))
