# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess
import sys

ips = sys.argv[1][1:-1].split(",") #убираем кв. скобки из переданного аргумента, разделяем строку по запятой
def ping_ip_addresses(list_ips):
    #print(list_ips)
    ips_tuple = ()
    valid_ip = []
    bad_ip = []
    for ip in list_ips:
        result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            valid_ip.append(ip)
        else:
            bad_ip.append(ip)
    ips_tuple = (valid_ip, bad_ip)
    return ips_tuple

if __name__ == "__main__":
    print(ping_ip_addresses(ips))
