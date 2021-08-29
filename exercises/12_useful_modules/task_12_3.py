# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate

def print_ip_table(avail_ips,not_avail_ips):
    #columns = ['Reachable', 'Unreachable']
    #summary_list = []
    #выровнять кол-во элементов в списке
    #diff_elements = len(avail_ips) - len(not_avail_ips)
    #if diff_elements > 0:
    #    for i in range(diff_elements):
    #        not_avail_ips.append("")
    #elif diff_elements < 0:
    #    for i in range(abs(diff_elements)):
    #        avail_ips.append("")

    #for ip_avail,ip_not_avail in zip(avail_ips,not_avail_ips):
    #    summary_list.append([ip_avail,ip_not_avail])
    #print(summary_list)
    #summary_table = tabulate(summary_list, headers=columns)
    #return tmp_list
    #return summary_table
    table = {'Reachable': avail_ips, 'Unreachable': not_avail_ips}
    return tabulate(table, headers='keys')

if __name__ == "__main__":
    print(print_ip_table(['8.8.8.8','8.8.4.4', '1.1.1.1'],['192.168.100.100','192.168.3.30','10.0.0.1','10.0.0.2']))
