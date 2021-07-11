# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    intf_vlan_mapping - ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
    trunk_template - список команд для порта в режиме trunk

    Возвращает список всех портов в режиме trunk с конфигурацией на основе шаблона
    """
    trunk_dict_config = {}
    trunk_mode_list = []
    for intf, vlans in intf_vlan_mapping.items():
        #trunk_mode_list.append(f"interface {intf}")
        for i in trunk_template:
            if i.startswith("switchport trunk allowed"):
                vlans=[str(vlan) for vlan in vlans] # int to str in vlans list
                vlans_str = ",".join(vlans)
                trunk_mode_list.append(f"{i} {vlans_str}")
            else:
                trunk_mode_list.append(i)
        trunk_dict_config[intf] = trunk_mode_list
    print(trunk_dict_config)

generate_trunk_config(trunk_config,trunk_mode_template)
