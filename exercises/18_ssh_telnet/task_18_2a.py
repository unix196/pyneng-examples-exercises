# -*- coding: utf-8 -*-
"""
Задание 18.2a

Скопировать функцию send_config_commands из задания 18.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода информация о том
к какому устройству выполняется подключение.
По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства
из файла devices.yaml с помощью функции send_config_commands.
"""

import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]

def send_config_commands(dev, cli_commands,log=True):
    if log:
        print("Подключаюсь к {}...".format(dev["host"]))
    try:
        ssh = ConnectHandler(**dev)
        ssh.enable()
        result = ssh.send_config_set(cli_commands)
        return result
    except (AuthenticationException, NetmikoTimeoutException) as e:
        print(str(e))

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_config_commands(dev, commands))