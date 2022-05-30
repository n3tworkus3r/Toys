import os
import time
import json
import random
import shodan
import censys
import socket
import requests
import datetime
import argparse
import threading
from queue import Queue
#import censys.ipv4
#from censys import ipv4
from multiprocessing import Pool, freeze_support, Manager


shodan_api_key = "P5wbfMoNGt883QS40OXVarK4cZ8xU8vm"
censys_api_key = "0b14dc2b-a27e-4cfd-9fbf-445d628ffbdf"
censys_api_secret = "9bzSTUar1gBYNwDt22Sv4lX1RV5cFf2U"

# Аргументы запуска скрипта.
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="Режимы работы", choices=[1, 2, 3, 4, 5, 6], type=int, required=True)
parser.add_argument("-p", "--proxy", help="Использование прокси", action='store_true')
args = parser.parse_args()

# Список портов, которые мы будем сканировать в найденых айпи.
ports = [21, 22, 23, 80, 443, 2222, 8080, 8000, 8888]

m = Manager()
ip_list = m.list()
brute_data = m.list()
proxy_list = m.list()
asic_miners = m.list()
password_list = m.list()

# Список юзер-агентов.
ua = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 6.0)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)']

# Список стандартных имён, который мы будем использовать для брута юзеров.
standard_users = ["admin", "Admin", "web", "root", "innominer", "innot1t2", "miner", "inno", "administrator", "user"]


# Shodan
def shodan_scanner(dork, start=1, stop=2):
    # Подключаемся к shodan используя shodan_api_key
    api = shodan.Shodan(shodan_api_key)
    # Загружаем результаты и сохраняем их в ip_list
    for page in range(start, stop):
        try:
            time.sleep(0.5)
            results = api.search(dork, page=page)
            for result in results['matches']:
                if not result['ip_str'] in ip_list:
                    # Выводим список айпи и сохраняем в ip_list
                    ip_list.append(result['ip_str'])
                    print(result['ip_str'])
        except shodan.exception.APIError as error:
            print('[!] Error: ' + str(error))
            continue

# Censys
def censys_scanner(dork, records=25):
    # Подключаемся к censys используя censys_api_key и censys_api_secret
    c = ipv4.CensysIPv4(api_id=censys_api_key, api_secret=censys_api_secret)
    # Поиск айпи
    try:
        for result in c.search(dork, max_records=records):
            res = json.dumps(result, indent=4)
            r = json.loads(res)
            if r["ip"] not in ip_list:
                # Выводим список айпи и сохраняем в ip_list
                ip_list.append(r["ip"])
                print(r["ip"])
    except censys.exceptions as error:
        print('[!] Error: ' + str(error))


###############################################

results_file = r'logs/' + date + '.txt'
print("\nCensys:")
# records=47 — количество айпи
censys_scanner("AsicMiner", records=47)
print("\nShodan:")
# stop=3 — последняя страница для поиска (3 страницы ~ 47 уникальных айпи)
shodan_scanner("title:AsicMiner", stop=3)

###################################
###        WRITE TO FILE        ###
###################################
f = open(results_file, "a")
for ip in ip_list:
 f.write(str(ip) + "\n")
 print(ip)
f.close()
###################################