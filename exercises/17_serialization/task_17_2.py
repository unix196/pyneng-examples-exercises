# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import re
import csv

sh_version_files = glob.glob("sh_vers*")

headers = ["hostname", "ios", "image", "uptime"]

def parse_sh_version(sh_ver):
    #regex = (
    #    'Cisco IOS Software, \S+ \S+ \S+ Version (?P<ios>\S+),'
    #    'System image file is "(?P<image>\S+)"'
    #     'uptime is (?P<uptime>.*)')
    #match = re.search(regex, sh_ver, re.DOTALL,)
    #if match:
    #    return match.group()
    match_ios = re.search(r'Cisco IOS Software, \S+ \S+ \S+ Version (\S+),', sh_ver)
    match_image = re.search(r'System image file is "(\S+)"', sh_ver)
    match_uptime = re.search(r'uptime is (.*)', sh_ver)
    if match_uptime:
        uptime = match_uptime.group(1)
    if match_image:
        image = match_image.group(1)
    if match_ios:
        ios = match_ios.group(1)
    return ios, image,uptime

def write_inventory_to_csv(sh_version_files,output_file):
    list_inventory = []
    for file in sh_version_files:
        hostname = file.split("_")[2].split(".")[0]
        with open(file) as f:
            text = f.read()
            row = list(parse_sh_version(text))
            row.insert(0,hostname)
            list_inventory.append(row)

    with open(output_file, 'w') as f_output:
        writer = csv.writer(f_output)
        writer.writerow(["hostname","ios","image","uptime"])
        for row in list_inventory:
            writer.writerow(row)

if __name__ == "__main__":
    write_inventory_to_csv(sh_version_files, "routers_inventory.csv")

