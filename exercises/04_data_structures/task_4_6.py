# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix {prefix:>24}
AD/Metric {ad:>15}
Next-Hop  {hop:>18}
Last update {last:>12}
Outbound Interface {interface}
"""

#template = """
#Prefix {prefix:~>24}
#AD/Metric {ad:~>15}
#Next-Hop  {hop:~>18}
#Last update {last:~>12}
#Outbound Interface {interface}
#"""

#print(template.format(prefix=ospf_route.split()[0], hop=ospf_route.split()[3], ad=ospf_route.split()[1], last=ospf_route.split()[-2], interface=ospf_route.split()[-1]))
prefix=ospf_route.split()[0]
ad=ospf_route.split()[1][1:-1]
hop=ospf_route.split()[3][0:-1]
update=ospf_route.split()[-2][0:-1]
int=ospf_route.split()[-1]
print(template.format(prefix=prefix, ad=ad, hop=hop,last=update, interface=int))
