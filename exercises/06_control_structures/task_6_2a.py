# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

address=input("Введите ip адрес: ")
octets = address.split('.')
correct_ip = True

if len(octets) < 4:
    correct_ip = False

else:
    for i in octets:
        if not (i.isdigit()and int(i) in range(0,256)):
            #print(i+" это не число")
            correct_ip = False
            break

if not correct_ip:
    print('Неправильный IP-адрес')

else:

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
