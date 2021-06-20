# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan = input("Введите номер влана: ")


tmp_list = []
with open("CAM_table.txt") as f:
    for line in f:
        if line.strip() and line.strip()[0].isdigit():
            words = line.strip().split()
            words[0] = int(words[0]) # теперь первым эл-им идет число
            if int(vlan) == words[0]:
                tmp_list.append(words)

mac_template = "{:7} {:<17} {:<12} {}"

for upper_list in sorted(tmp_list):  #Python automatically sorts lists of lists by the first element
    upper_list[0] = str(upper_list[0])
    print(mac_template.format(upper_list[0],upper_list[1],upper_list[2],upper_list[3]))
