# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys
file = sys.argv[1]
with open(file) as f, open("config_sw1_summary.txt","w") as f_write:
    for line in f:
        if not line.startswith("!"):
            words = line.split()
            if not set(words).intersection(set(ignore)):
                f_write.write(line)
                #print(line.rstrip())
