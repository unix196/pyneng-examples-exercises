# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
address=input("Введите ip адрес: ")

if int(address.split('.')[0]) in range(1,223):
    type_octet="unicast"
elif int(address.split('.')[0]) in range(224,239):
    type_octet="multicast"
elif address == "255.255.255.255":
    type_octet="local broadcast"
elif address == "0.0.0.0":
    type_octet="unassigned"
else:
    type_octet="unused"

print(type_octet)
