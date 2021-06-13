# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

temp = """
Prefix {prefix:>26}
AD/Metric {ad:>17}
Next-Hop {next:>21}
Last update {last:>14}
Outbound Interface {int:>17}
"""

with open("ospf.txt") as f:
    for  line in f:
        l=line.split()
        prefix =l[1]
        ad = l[2][1:-1]
        next = l[4][:-1]
        last = l[5][:-1]
        int = l[6]

        print(temp.format(prefix=prefix, ad=ad, next=next, last=last, int=int))
