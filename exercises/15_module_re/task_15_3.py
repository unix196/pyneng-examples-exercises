# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re
from pprint import pprint

asa_template = """
object network LOCAL_{}
 host {}
 nat (inside,outside) static interface service {} {} {}"""


def convert_ios_nat_to_asa(src_filename,dst_filename):
    open(dst_filename, 'w').close()
    with open(src_filename) as f_src:
        for line in f_src:
            match = re.search(r'ip nat inside source static (?P<proto>\S+) (?P<ip>\S+) (?P<src_port>\S+) interface (\S+) (?P<dst_port>\d+)', line)
            proto,ip,src_port,dst_port = match.group("proto"), match.group("ip"), match.group("src_port"), match.group("dst_port")
            #asa_line = asa_template.format(match.group("ip"),match.group("ip"),match.group("proto"),match.group("src_port"),match.group("dst_port"))
            asa_line = asa_template.format(ip,ip,proto,src_port,dst_port)
            f_dst = open(dst_filename, 'a')
            f_dst.write(asa_line)
            f_dst.close()

if __name__ == "__main__":
    pprint(convert_ios_nat_to_asa("cisco_nat_config.txt","asa_nat_config.txt"))
