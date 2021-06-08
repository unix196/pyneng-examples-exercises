# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network=input("Введите ip сеть: ")
net,mask = network.split('/')

net_octet = net.split('.')
oct1, oct2, oct3, oct4 = [int(net_octet[0]), int(net_octet[1]), int(net_octet[2]), int(net_octet[3])]

network_template="""
Network:
{:<10}{:<10}{:<10}{:<10}
{:08b}  {:08b}  {:08b}  {:08b}
"""

mask_template="""
Mask:
/{}
{:<10}{:<10}{:<10}{:<10}
{}  {}  {}  {}
"""


print(network_template.format(oct1,oct2,oct3,oct4,oct1,oct2,oct3,oct4))

bin_mask="1" * int(mask) + "0" * (32 - int(mask))
mask1=bin_mask[0:8]
mask2=bin_mask[8:16]
mask3=bin_mask[16:24]
mask4=bin_mask[24:32]

print(mask_template.format(mask,int("0b"+mask1,2),int("0b"+mask2,2),int("0b"+mask3,2),int("0b"+mask4,2),mask1,mask2,mask3,mask4))
