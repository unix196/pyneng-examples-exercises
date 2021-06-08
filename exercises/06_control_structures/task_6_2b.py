# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



while True:
    address=input("Введите ip адрес: ")
    octets = address.split('.')
    correct_ip = True
    if len(octets) < 4:
        correct_ip = False
        print('Неправильный IP-адрес')
    else:
        for i in octets:
            if not (i.isdigit() and int(i) in range(0,256)):
                #print(i+" это не число")
                correct_ip = False
                print('Неправильный IP-адрес')
                break

    if correct_ip: break

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
