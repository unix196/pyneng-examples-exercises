# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress

def convert_ranges_to_ip_list(ip_list):
    summary_list = []
    for ips in ip_list:
        if "-" in ips:
            start_ip, stop_ip = ips.split("-")
            start=ipaddress.ip_address(start_ip)
            try:
                stop=ipaddress.ip_address(stop_ip)
                #print(stop)
            except:
                #убираем последний октет и добавляем сразу; start_ip.split(".")[:-1] возвращает ['1', '1', '1']
                end_ip= '{}.{}'.format(".".join(start_ip.split(".")[:-1]),stop_ip)
                stop=ipaddress.ip_address(end_ip)
                #print(stop)
                #print(end_ip)
            #print(start_ip, stop)
            for ip_int in range(int(start), int(stop)+1):
                #print(ipaddress.IPv4Address(ip_int))
                summary_list.append(str(ipaddress.ip_address(ip_int)))
        else:
            summary_list.append(ips)

    return summary_list


if __name__ == "__main__":
    print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))
