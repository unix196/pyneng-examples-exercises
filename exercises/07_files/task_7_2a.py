# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys
file = sys.argv[1]
with open(file) as f:
    for line in f:
        #if not line.startswith("!") and not ignore[0] in line and not ignore[1] in line and not ignore[2] in line:
        if not line.startswith("!"):
            words = line.split()
            if not set(words).intersection(set(ignore)):
                print(line.rstrip())
